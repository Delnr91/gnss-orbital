"""Internationalization (i18n) subsystem for the orbital dynamics package.

This module provides locale management using the Registry pattern. It loads
translation keys from JSON files and supports fallback to default language ('en').
"""

import os
import json
from typing import Dict, Any, List, Optional


def _find_locales_dir() -> str:
    """Resolves the locales/ directory for both repo and installed layouts.

    Walks upward from this file looking for a sibling ``locales`` folder so it
    works whether the package lives in ``src/orbital`` (repo checkout) or
    ``site-packages/orbital`` (installed with data files alongside).
    """
    current = os.path.dirname(os.path.abspath(__file__))
    for _ in range(4):
        candidate = os.path.join(current, "locales")
        if os.path.isdir(candidate):
            return candidate
        current = os.path.dirname(current)
    # Last resort: keep the historical relative path even if missing
    return os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "locales"
    )


class Locale:
    """Translation registry for multilingual support.

    Loads translations from JSON files in the locales/ directory.
    Implements a fallback chain: requested_lang -> 'en' -> raw_key.
    """

    _instances: Dict[str, "Locale"] = {}
    _default_lang: str = "en"
    _locales_dir: str = _find_locales_dir()

    _lang: str
    _translations: Dict[str, Any]

    def __new__(cls, lang: Optional[str] = None) -> "Locale":
        if lang is None:
            lang = cls._default_lang
        # Normalize language code to lowercase (e.g. 'es', 'en', 'zh')
        lang = lang.lower().split("-")[0]
        if lang not in cls._instances:
            instance = super().__new__(cls)
            instance._lang = lang
            instance._translations = instance._load_translations(lang)
            cls._instances[lang] = instance
        return cls._instances[lang]

    @classmethod
    def set_default_language(cls, lang: str) -> None:
        """Sets the global default language for translations."""
        cls._default_lang = lang.lower().split("-")[0]

    def _load_translations(self, lang: str) -> Dict[str, Any]:
        """Loads translation file for the given language code."""
        file_path = os.path.join(self._locales_dir, f"{lang}.json")
        
        # If the file does not exist, try to fall back to 'en'
        if not os.path.exists(file_path):
            if lang == self._default_lang:
                return {}
            # Try to load default language
            default_path = os.path.join(self._locales_dir, f"{self._default_lang}.json")
            if not os.path.exists(default_path):
                return {}
            file_path = default_path
            
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    return data
                return {}
        except (json.JSONDecodeError, OSError):
            return {}

    def t(self, key: str, default: Optional[str] = None, **kwargs: Any) -> str:
        """Translates a key with optional string interpolation formatting.

        Keys can be nested using dot notation (e.g., 'orbit.period').

        Args:
            key: Dot-separated path to the translation string.
            default: Fallback string if the key is not found.
            **kwargs: Placeholder replacements for formatting the string.
        """
        parts = key.split(".")
        val: Any = self._translations
        
        # Traverse translations
        for part in parts:
            if isinstance(val, dict) and part in val:
                val = val[part]
            else:
                val = None
                break

        # Fallback to English if not found and we are not already in English
        if val is None and self._lang != self._default_lang:
            default_locale = Locale(self._default_lang)
            val = default_locale._get_raw_key(parts)

        if val is None:
            return default if default is not None else key

        if not isinstance(val, str):
            return str(val)

        try:
            return val.format(**kwargs)
        except KeyError:
            return val

    def _get_raw_key(self, parts: List[str]) -> Optional[str]:
        """Helper to get a key from this locale instance's translations dictionary."""
        val: Any = self._translations
        for part in parts:
            if isinstance(val, dict) and part in val:
                val = val[part]
            else:
                return None
        return val if isinstance(val, str) else None

    @classmethod
    def available_languages(cls) -> List[str]:
        """Scans the locales directory and returns supported language codes."""
        if not os.path.exists(cls._locales_dir):
            return ["en"]
        langs = []
        for file in os.listdir(cls._locales_dir):
            if file.endswith(".json"):
                langs.append(file[:-5])
        return sorted(langs)

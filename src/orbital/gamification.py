"""Gamification achievement system for orbital dynamics.

Implements the Observer design pattern to track actions, evaluate unlock
conditions, and persist progress locally in a JSON file.
"""

from __future__ import annotations

import os
import json
from typing import Dict, Any, List, Optional
from .i18n import Locale


class Achievement:
    """An unlockable milestone or badge in the study plan.

    Attributes:
        id: Unique identifier for the achievement.
        tier: Category tier (e.g., bronze, silver, gold, master).
        title_key: i18n key for the title.
        description_key: i18n key for the description.
        condition: Action identifier required to unlock it.
    """

    def __init__(
        self,
        id: str,
        tier: str,
        title_key: str,
        description_key: str,
        condition: str,
    ) -> None:
        self.id = id
        self.tier = tier
        self.title_key = title_key
        self.description_key = description_key
        self.condition = condition

    def to_dict(self) -> Dict[str, str]:
        return {
            "id": self.id,
            "tier": self.tier,
            "title_key": self.title_key,
            "description_key": self.description_key,
            "condition": self.condition,
        }


class ProgressTracker:
    """Tracks and persists user progress through notebook and example tasks.

    Stores unlocked achievements and completed actions to a local JSON file in
    the user's home directory under `.gnss-orbital/progress.json`.
    """

    def __init__(self) -> None:
        self.save_dir = os.path.join(os.path.expanduser("~"), ".gnss-orbital")
        self.save_path = os.path.join(self.save_dir, "progress.json")
        self.achievements: List[Achievement] = []
        self._load_achievements_config()
        self._load_user_progress()

    def _load_achievements_config(self) -> None:
        """Loads static achievements metadata from assets/badges/achievements.json."""
        config_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "assets",
            "badges",
            "achievements.json",
        )
        if not os.path.exists(config_path):
            # Fallback hardcoded defaults if JSON asset is missing
            self.achievements = [
                Achievement(
                    "leo_explorer",
                    "bronze",
                    "achievements.bronze.leo_explorer.title",
                    "achievements.bronze.leo_explorer.description",
                    "simulate_leo",
                ),
                Achievement(
                    "kepler_solver",
                    "bronze",
                    "achievements.bronze.kepler_solver.title",
                    "achievements.bronze.kepler_solver.description",
                    "solve_kepler",
                ),
                Achievement(
                    "navigator",
                    "silver",
                    "achievements.silver.navigator.title",
                    "achievements.silver.navigator.description",
                    "modify_six_elements",
                ),
                Achievement(
                    "comparison",
                    "silver",
                    "achievements.silver.comparison.title",
                    "achievements.silver.comparison.description",
                    "compare_four_orbits",
                ),
                Achievement(
                    "hohmann",
                    "gold",
                    "achievements.gold.hohmann.title",
                    "achievements.gold.hohmann.description",
                    "hohmann_transfer",
                ),
                Achievement(
                    "iris2_architect",
                    "master",
                    "achievements.master.iris2_architect.title",
                    "achievements.master.iris2_architect.description",
                    "model_iris2",
                ),
            ]
            return

        try:
            with open(config_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data.get("achievements", []):
                    self.achievements.append(
                        Achievement(
                            id=item["id"],
                            tier=item["tier"],
                            title_key=item["title_key"],
                            description_key=item["description_key"],
                            condition=item["condition"],
                        )
                    )
        except (json.JSONDecodeError, KeyError, OSError):
            pass

    def _load_user_progress(self) -> None:
        """Loads completed actions and unlocked achievements from disk."""
        self.completed_actions: List[str] = []
        self.unlocked_ids: List[str] = []

        if os.path.exists(self.save_path):
            try:
                with open(self.save_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.completed_actions = data.get("completed_actions", [])
                    self.unlocked_ids = data.get("unlocked_achievements", [])
            except (json.JSONDecodeError, OSError):
                pass

    def _save_user_progress(self) -> None:
        """Persists completed actions and unlocked achievements to disk."""
        os.makedirs(self.save_dir, exist_ok=True)
        try:
            with open(self.save_path, "w", encoding="utf-8") as f:
                json.dump(
                    {
                        "completed_actions": self.completed_actions,
                        "unlocked_achievements": self.unlocked_ids,
                    },
                    f,
                    indent=2,
                )
        except OSError:
            pass

    def record_action(self, action_id: str) -> List[Achievement]:
        """Records an action and returns any newly unlocked achievements.

        Args:
            action_id: The identifier of the action performed.
        """
        newly_unlocked: List[Achievement] = []

        if action_id not in self.completed_actions:
            self.completed_actions.append(action_id)

        # Evaluate conditions
        for ach in self.achievements:
            if ach.id not in self.unlocked_ids:
                if ach.condition in self.completed_actions:
                    self.unlocked_ids.append(ach.id)
                    newly_unlocked.append(ach)

        if newly_unlocked:
            self._save_user_progress()

        return newly_unlocked

    def get_progress(self) -> Dict[str, Any]:
        """Returns a dictionary summary of the user's progress."""
        return {
            "total_achievements": len(self.achievements),
            "unlocked_count": len(self.unlocked_ids),
            "unlocked_list": self.unlocked_ids,
            "completed_actions": self.completed_actions,
        }

    def display_progress(self, lang: Optional[str] = None) -> str:
        """Generates a text-based dashboard displaying unlocked badges."""
        locale = Locale(lang)
        lines = [
            "================================================",
            f"   {locale.t('achievements.unlocked_list').upper()}",
            "------------------------------------------------",
        ]
        
        for ach in self.achievements:
            status = "[X]" if ach.id in self.unlocked_ids else "[ ]"
            title = locale.t(ach.title_key)
            desc = locale.t(ach.description_key)
            lines.append(f" {status} {title}")
            lines.append(f"     -> {desc}")
            
        lines.append("================================================")
        return "\n".join(lines)

from orbital.i18n import Locale


def test_i18n_loading() -> None:
    loc_en = Locale("en")
    assert loc_en.t("orbit.semi_major_axis") == "Semi-major Axis"

    loc_es = Locale("es")
    assert loc_es.t("orbit.semi_major_axis") == "Semieje Mayor"


def test_i18n_fallback() -> None:
    # Querying a key that does not exist in Spanish should fallback to English
    # Or if it doesn't exist anywhere, return the key
    loc = Locale("es")
    res = loc.t("some.nonexistent.key")
    assert res == "some.nonexistent.key"


def test_available_languages() -> None:
    langs = Locale.available_languages()
    assert "en" in langs
    assert "es" in langs
    assert "zh" in langs

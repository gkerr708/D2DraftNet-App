#from d2draftnet.embedding_model import DraftPredictionNN
from pathlib import Path
from d2draftnet_app.config import HEROS, PROJECT_DIR


def test_heros_sorted():
    """Test that the heroes are sorted"""
    assert sorted(HEROS) == HEROS

def get_hero_icon_names():
    """Gets all of the names of the hero icons"""
    hero_icons_dir = PROJECT_DIR / "d2draftnet_app/static/hero_icons/"
    fullnames = [icon.name for icon in hero_icons_dir.iterdir()]
    return sorted([name.replace("_icon_dota2_gameasset.png", "") for name in fullnames])

def test_hero_icons():
    """Verify all of the HEROS and in the icon directory"""
    hero_icons = get_hero_icon_names()
    assert all([hero in hero_icons for hero in HEROS])


if __name__ == "__main__":
    test_hero_icons()

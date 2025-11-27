import json
import os
from typing import Dict, Any

MEMORY_FILE = "user_memory.json"


def _load_all() -> Dict[str, Any]:
    """
    Load all user profiles from JSON memory file.
    """
    if not os.path.exists(MEMORY_FILE):
        return {}
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        # If corrupted, just reset
        return {}


def _save_all(data: Dict[str, Any]) -> None:
    """
    Save all user profiles to JSON memory file.
    """
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def get_user_profile(user_id: str = "default") -> Dict[str, Any]:
    """
    Get a single user's profile. Returns {} if not found.
    """
    all_users = _load_all()
    return all_users.get(user_id, {})


def save_user_profile(user_id: str, profile: Dict[str, Any]) -> None:
    """
    Save/update a single user's profile.
    """
    all_users = _load_all()
    all_users[user_id] = profile
    _save_all(all_users)

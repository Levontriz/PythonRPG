"""
Configuration management system.
Handles loading and saving game configuration.
"""

import json
import os


class Config:
    def __init__(self):
        self.config = {}
        self.config_file = "config.json"
        self.load_config()

    def load_config(self):
        """Load configuration from file."""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    self.config = json.load(f)
            else:
                self._create_default_config()
        except Exception as e:
            print(f"Error loading config: {e}")
            self._create_default_config()

    def _create_default_config(self):
        """Create default configuration."""
        self.config = {
            "game_settings": {
                "difficulty": "normal",
                "enable_mods": True
            },
            "display": {
                "show_combat_details": True,
                "show_critical_messages": True
            }
        }
        self.save_config()

    def save_config(self):
        """Save configuration to file."""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=4)
        except Exception as e:
            print(f"Error saving config: {e}")

    def get(self, key, default=None):
        """Get a configuration value."""
        return self.config.get(key, default)

    def set(self, key, value):
        """Set a configuration value."""
        self.config[key] = value
        self.save_config()

"""
Tests for the configuration settings of the Kyber VPN backend.
"""
import pytest
from app.core.config import settings

class TestConfig:
    """Test cases for configuration settings."""
    
    def test_settings_loaded(self):
        """Test that settings are loaded correctly."""
        assert settings is not None
        assert hasattr(settings, "SECRET_KEY")
        assert hasattr(settings, "ACCESS_TOKEN_EXPIRE_MINUTES")
        assert settings.ACCESS_TOKEN_EXPIRE_MINUTES > 0
        assert hasattr(settings, "ALGORITHM")
        assert settings.ALGORITHM == "HS256"
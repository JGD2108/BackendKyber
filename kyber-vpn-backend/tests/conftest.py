"""
Pytest configuration and shared fixtures for the Kyber VPN backend tests.
"""
import pytest
import sys
import os

# Add the project root to the Python path to allow imports from app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture
def mock_kyber_keypair():
    """Return a mock Kyber keypair for testing."""
    return {
        "public_key": "mock_public_key_base64",
        "secret_key": "mock_secret_key_base64"
    }

@pytest.fixture
def mock_user_data():
    """Return mock user data for testing."""
    return {
        "username": "test_user",
        "display_name": "Test User",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW"  # "password"
    }
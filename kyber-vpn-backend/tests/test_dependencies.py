"""
Tests to check for required dependencies in the Kyber VPN backend.
"""
import pytest
import importlib

class TestDependencies:
    """Test that all required dependencies are available."""
    
    def test_bcrypt_dependency(self):
        """Test that bcrypt is installed and can be imported."""
        try:
            import bcrypt
            assert bcrypt.__version__  # Check it has a version attribute
        except ImportError:
            pytest.fail("bcrypt module is not installed. Run 'pip install bcrypt'")
    
    def test_cryptography_dependency(self):
        """Test that cryptography is installed and can be imported."""
        try:
            import cryptography
            assert cryptography.__version__  # Check it has a version attribute
        except ImportError:
            pytest.fail("cryptography module is not installed")
    
    def test_fastapi_dependency(self):
        """Test that FastAPI is installed and can be imported."""
        try:
            import fastapi
            assert fastapi.__version__  # Check it has a version attribute
        except ImportError:
            pytest.fail("fastapi module is not installed")
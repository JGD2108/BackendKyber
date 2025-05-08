"""
Tests for security-related functionality in the Kyber VPN backend.
"""
import pytest
from datetime import timedelta
from app.core.security import create_access_token, verify_token, verify_password, get_password_hash

class TestSecurity:
    """Test cases for security functions."""
    
    def test_password_hashing(self):
        """Test that password hashing and verification work correctly."""
        # Given a test password
        password = "test_password123"
        
        # When we hash it
        hashed = get_password_hash(password)
        
        # Then it should not equal the original password
        assert hashed != password
        
        # And verification should pass with the correct password
        assert verify_password(password, hashed)
        
        # And verification should fail with an incorrect password
        assert not verify_password("wrong_password", hashed)
    
    def test_token_creation_and_verification(self):
        """Test that JWT tokens can be created and verified."""
        # Given test data
        test_data = {"sub": "test_user", "role": "user"}
        
        # When we create a token with explicit expiry to avoid dependency on settings
        token = create_access_token(
            data=test_data,
            expires_delta=timedelta(minutes=15)  # Explicit expiry for testing
        )
        
        # Then we should get a string
        assert isinstance(token, str)
        
        # And verification should return the payload
        payload = verify_token(token)
        assert payload is not None
        assert payload.get("sub") == "test_user"
        assert payload.get("role") == "user"
        
        # And verification should fail for an invalid token
        assert verify_token("invalid.token.here") is None

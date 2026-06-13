import pytest
from unittest.mock import patch

@pytest.fixture
def mock_user_id():
    return "test-user-123"


@pytest.fixture
def mock_user_email():
    return "test@example.com"


@pytest.fixture
def mock_supabase():
    with patch('src.gerador.get_supabase') as mock:
        yield mock


@pytest.fixture
def test_token():
    from src.auth import create_access_token
    return create_access_token("test-user-123", "test@example.com")

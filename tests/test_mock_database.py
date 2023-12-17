from httpx import AsyncClient
import pytest

from models.user import User
from models.candidate import Candidate
from tests.conftest import mock_no_authentication


class TestMockAuthentication:
    @classmethod
    def setup_class(cls):
        mock_no_authentication()

    @pytest.mark.anyio
    async def test_mock_databases(self, client_test: AsyncClient):
        # generate data
        await User(
            uuid="55edadce-56c5-4a94-9b7f-3bd3fe273743",
            first_name="Haziq ",
            last_name="M",
            email="admin@gmail.com",
            password="admin123",
        ).create()

        await Candidate(
            first_name="Haziq",
            last_name="M",
            email="haziq@gmail.com",
            uuid="55edadce-56c5-4a94-9b7f-3bd3fe273713",
            career_level="Senior",
            job_major="Software Consultant",
            years_of_experience=7,
            degree_type="Computer Science",
            skills=["software", "coding"],
            nationality="Pakistan",
            city="Lahore",
            salary="60000",
            gender="Male"
        ).create()

        response = await client_test.get("candidate")

        assert response.status_code == 200

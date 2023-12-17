from httpx import AsyncClient
import pytest
from tests.conftest import mock_no_authentication


class TestMockAuthentication:
    @classmethod
    def setup_class(cls):
        mock_no_authentication()

    @pytest.mark.anyio
    async def test_api_processed_jobs(self, client_test: AsyncClient):
        response = await client_test.get("candidate")

        assert response.status_code == 200

from fastapi.testclient import TestClient
from ab_test_api import app


test_client = TestClient(app)
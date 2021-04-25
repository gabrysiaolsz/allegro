from fastapi.testclient import TestClient
from github.GithubException import UnknownObjectException

import main

client = TestClient(main.app)


class MockRepository:
    def __init__(self, name, stargazers_count):
        self.name = name
        self.stargazers_count = stargazers_count


class MockUser:
    def __init__(self, repos):
        self.repos = repos

    def get_repos(self):
        return self.repos


def test_github_api_user_does_not_exist(monkeypatch):
    def get_user_404(username):
        raise UnknownObjectException(404, "")

    monkeypatch.setattr(main.GITHUB_API, "get_user", get_user_404)

    response = client.get("/users/mockuser/stats")
    assert response.status_code == 404


def test_correct_listed_repos_name_and_stars_count(monkeypatch):
    def mock_get_user(username):
        return MockUser(
            [MockRepository("mock_repo_1", 1), MockRepository("mock_repo_2", 2)]
        )

    monkeypatch.setattr(main, "get_user", mock_get_user)

    response = client.get("/users/mockuser/repos")
    assert response.status_code == 200
    assert response.json() == [
        {"name": "mock_repo_1", "stars_count": 1},
        {"name": "mock_repo_2", "stars_count": 2},
    ]


def test_correct_stars_sum_from_public_repositories(monkeypatch):
    def mock_get_user(username):
        return MockUser(
            [MockRepository("mock_repo_1", 1), MockRepository("mock_repo_2", 2)]
        )

    monkeypatch.setattr(main, "get_user", mock_get_user)

    response = client.get("/users/mockuser/stats")
    assert response.status_code == 200
    assert response.json() == {"received_stars_sum": 3}

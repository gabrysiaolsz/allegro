from fastapi import FastAPI, HTTPException
from github import Github, NamedUser, GithubException

app = FastAPI()

GITHUB_API = Github()


def get_user(username: str) -> NamedUser:
    try:
        return GITHUB_API.get_user(username)
    except GithubException:
        raise HTTPException(status_code=404, detail="User not found")


@app.get("/users/{username}/repos", responses={404: {"description": "User not found"}})
async def get_repos_by_username(username: str):
    repos_info = []
    user = get_user(username)
    for repo in user.get_repos():
        repos_info.append({"name": repo.name, "stars_count": repo.stargazers_count})

    return repos_info


@app.get("/users/{username}/stats", responses={404: {"description": "User not found"}})
async def get_number_of_stars_by_username(username: str):
    stars_count = 0
    user = get_user(username)
    for repo in user.get_repos():
        stars_count += repo.stargazers_count

    return {"received_stars_sum": stars_count}

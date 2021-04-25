1. Installation and usage guide
    - First, create virtual environment, by running the following command:
      `$ python3 -m venv new-env`
    - After that, activate it with:
      `$ source new-env/bin/activate`
    - Then, download the requirements by running:
      `$ pip install -r requirements.txt`
    - Run the tests using:
      `$ pytest tests.py`
    - Run the app with:
      `$ uvicorn main:app --reload --port 8000`

      The output shows the URL where the app is being served in your local machine - it's the `localhost:8000`
    - To see the list of all public repositories (with name and stargazers count) of a given user, open your browser on:
      `localhost:8000/users/username/repos`, changing the `username` with the username of a user you want to see
      the information about.
    - To see the sum of received stars from every public repository of a given user, open the browser on:
   `localhost:8000/users/username/stats`, changing the `username` as explained above.
2. Development ideas
   - Adding more endpoints to show other statistics. 
   - Writing front-end to the application.
   - Adding authorisation to increase allowed number of queries. 
3. Comments on the draft
   - There's an automatically generated documentation, which you can see under the `localhost:8000/docs` address.
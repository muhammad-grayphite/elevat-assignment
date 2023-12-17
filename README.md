# Assignment Elevatus


1. reate a virtual environment in it:

```console
$ virtualenv .venv --python=python3
$ source .venv/bin/activate
```

2. Install the modules listed in the `requirements.txt` file:

```console
(venv)$ pip install -r requirements.txt
```
3. Update `.env.dev` with your params

4. Start the application:

```console
python main.py
```
Go to /docs for swagger.

## For Tests

```console
(venv)$ pytest
```

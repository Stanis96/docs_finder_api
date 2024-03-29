![Build Status](https://github.com/Stanis96/docs_finder_api/actions/workflows/linters.yml/badge.svg?branch=main)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
<h1 align="center">Docs finder - for working with documents.</h1>

### Description:
This is a FastAPI project with MongoDB that serves as a search engine for documents.
The application allows users to search for specific documents
by inputting relevant keywords or phrases.

### Installation:
* Clone the repository to a local directory:
  ```sh
  git clone https://github.com/Stanis96/docs_finder_api
  ```
* Set your own variable values in ```.env_template``` and rename to ```.env```
* Application launch:
```sh
  docker-compose -f docker-compose.yaml up --build
  ```
* Loading test data into the database:
```sh
  python launch_data.py
  ```

### API specification:
>Swagger UI:
> >http://localhost:8000/docs

>ReDoc UI:
> >http://localhost:8000/redoc
>
| Router                         | Description                             |
|:-------------------------------|:----------------------------------------|
| GET/api/v1/retrieve_all        | Retrieve all data                       |
| GET/api/v1/search_current_page | Returns a specific page with data limit |
| GET/api/v1/search_text         | Search for posts in text                |
| GET/api/v1/search_date         | Search posts by date                    |

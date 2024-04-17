## Overview

This project is a guide to quickly create a new project from it

<details>
<summary>Functional Requirements</summary>

## Functional Requirements

- TBD

</details>

<details>
<summary>Non-Functional Requirements</summary>

## Non-Functional Requirements

- TBD

</details>

<details>
<summary>Folders</summary>

## Contents of the template

- `api`: Basic FastAPI implementation
- `common`
    - `database`: DB functionality, sample row models and DAO
    - `models`: Sample business models
    - `constants`: What the name implies
    - `utilities`: shared utilities
- `data_upload`: Template to read from a CSV and insert to DB
- `resources`: Mostly DB file, other files as needed
- `tests`: Templates for both Unit and Feature testing
- `uploads`: empty folder, to be used to put files for the `data_upload`
- `requirements.txt`: Basic dependencies, un-versioned
- `Dockerfile` and `docker-compose.yaml` for basic implementation

</details> <!-- Folders -->

<details>
<summary>Usage</summary>

## Usage

### Necessary packages

```commandline
pip install -r ./requirements.txt
```

### How to run the API (Docker)

```commandline
docker-compose up api
```

### FastAPI Interface

```
http://localhost:8000/docs
```

</details>


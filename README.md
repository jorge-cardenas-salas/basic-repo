## Overview

This project is a guide to quickly create a new project from it

<details>

<summary>Problem Statement</summary>

## Problem Statement

Hi Jorge,
Question for today’s exercise :
Description (For backend candidates)
Your assignment is to create a microservice which serves the contents of photographers.json through a REST API.
The service should expose three REST endpoints:

- GET /api/photographers - returns the list of all photographers.
- GET /api/photographers/{photographerID} - returns a single photographer by ID.
- GET /api/photographers/event/{eventType} - returns a list of photographers for the specified event type.

  Examples of event_types:

- wedding
- birthdays
- wildlife
- sports

  The above APIs should only return high-level characteristics of the photographer data. For example - name, contact,
  avatar, event_types etc.
  Please create unit tests that cover the core logic.
  With time permitting, package the application for distribution. Some examples of this:
  Docker image (preferred)
  Tomcat WAR
  Static binary

Preparation Instructions to be Shared in Advance
You are free to choose whatever programming language you are comfortable with, SDKs, web frameworks, databases, and
online resources to complete this exercise.

</details>

<details>
<summary>Functional Requirements</summary>

## Functional Requirements

- DB is optional
- > GET /api/photographers/event/{eventType}
  - If event doesn't exist, then return empty data (no error)
- `username`
  - do NOT enforce format or uniqueness

</details>

<details>
<summary>Non-Functional Requirements</summary>

## Non-Functional Requirements

- Copy/pasting from Google is OK
- id and uid are PK (unique)
- > - GET /api/photographers - returns the list of all photographers
  - Only high-level data (no drill down of data)
    - No sensitive data
- Event types are Enums

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


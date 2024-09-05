# notes_api

## Project Overview

This project is a simple RESTful API for a note-taking application built using Django and Django REST Framework (DRF). It allows users to create, fetch, query, and update notes. This API does not include user management or a user interface.

## Features

- **Create Note:** Create a new note with a title and body.
- **Fetch Note by ID:** Retrieve a note using its primary key.
- **Query Notes by Title Substring:** Search for notes by a substring in the title.
- **Update Note:** Update an existing note's title and body.

## Models

### Note

- **title:** String, a brief title for the note.
- **body:** String, the main content of the note.
- **created_at:** DateTime, the date and time the note was created.
- **updated_at:** DateTime, the date and time the note was last updated.

## Endpoints

### POST api/notes/
Create a new note.

**Request Body:**
```json
{
  "title": "Note Title",
  "body": "Note body content."
}
```

### GET api/notes/int:pk/
Fetch a note by its primary key.

### GET api/notes/query/
Query notes by title substring.

Query Parameters:
title: The substring to search for in note titles.

### PUT api/notes/int:pk/update/
Update an existing note.
```json
{
  "title": "Updated Title",
  "body": "Updated body content."
}
```
## Installation
**1.Clone the repository:**
```
https://github.com/safvan001/notes_api.git
```
```
cd noteapi
```
**2.Set up a virtual environment:**
```
python -m venv env
env\Scripts\activate
```
**3.Install the dependencies:**
```
pip install -r requirements.txt
```
**4.Apply database migrations:**
```
python manage.py migrate
```
**5.Run the development server:**
```
python manage.py runserver
```
**6.Run tests:**
```
python manage.py test
```








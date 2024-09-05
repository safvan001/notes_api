# notes_api

# Note-Taking API

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

### POST /notes/
Create a new note.

**Request Body:**
```json
{
  "title": "Note Title",
  "body": "Note body content."
}
```

### GET /notes/int:pk/
Fetch a note by its primary key.

### GET /notes/query/
Query notes by title substring.

Query Parameters:
title: The substring to search for in note titles.

### PUT /notes/int:pk/update/
Update an existing note.
```json
{
  "title": "Updated Title",
  "body": "Updated body content."
}
```


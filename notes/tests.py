from rest_framework import status
from rest_framework.test import APITestCase
from notes.models import Note

from django.urls import reverse

class NoteTests(APITestCase):
    def test_create_note(self):
        url = reverse('create-notes')
        response = self.client.post(url, {'title': 'Test Note', 'body': 'Test Body'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_fetch_note_by_id(self):
        note = Note.objects.create(title='Test Note', body='Test Body')
        url = reverse('fetch-note', kwargs={'pk': note.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_query_notes_by_title(self):
        Note.objects.create(title='Test Note', body='Test Body')
        url = reverse('query-notes')
        response = self.client.get(url, {'title': 'Test'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_note(self):
        note = Note.objects.create(title='Test Note', body='Test Body')
        url = reverse('update-note', kwargs={'pk': note.id})
        response = self.client.put(url, {'title': 'Updated Note', 'body': 'Updated Body'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)



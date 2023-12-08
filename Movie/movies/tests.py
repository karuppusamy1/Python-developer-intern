# movies/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Comment

class MovieAppTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create test movie data if needed
        # ...

    def test_comment_creation(self):
        # Ensure a comment is created correctly
        movie_id = 1  # Replace with a valid movie ID
        comment_text = 'This is a test comment.'

        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Post a comment
        response = self.client.post(reverse('comments', args=[movie_id]), {'comment': comment_text})

        # Check if the comment is created
        self.assertEqual(response.status_code, 302)  # Expect a redirect after posting a comment

        # Check if the comment is in the database
        self.assertEqual(Comment.objects.count(), 1)
        comment = Comment.objects.get()
        self.assertEqual(comment.comment, comment_text)
        self.assertEqual(comment.user, self.user)
        self.assertEqual(comment.movie_id, movie_id)

    def test_search_view(self):
        # Test the search view
        response = self.client.get(reverse('search'), {'q': 'Avengers', 'type': 'movie'})
        self.assertEqual(response.status_code, 200)  # Expect a successful response

        # Add more specific assertions based on your search results template

    def test_index_view_pagination(self):
        # Test pagination on the index view
        # Create test movie data if needed
        # ...

        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)  # Expect a successful response

        # Add assertions to check if pagination links are present and functioning

    # Add more tests as needed

from unittest import TestCase

import requests


class ApiTestCase(TestCase):

    def setUp(self):
        self.api = f"https://jsonplaceholder.typicode.com"

    def test_get_users_returns_user_details_with_200(self):
        api = f"{self.api}/users/1"

        response = requests.get(api)

        expected_response = {
            "id": 1,
            "name": "Leanne Graham",
            "username": "Bret",
            "email": "Sincere@april.biz",
            "address": {
                "street": "Kulas Light",
                "suite": "Apt. 556",
                "city": "Gwenborough",
                "zipcode": "92998-3874",
                "geo": {
                    "lat": "-37.3159",
                    "lng": "81.1496"
                }
            },
            "phone": "1-770-736-8031 x56442",
            "website": "hildegard.org",
            "company": {
                "name": "Romaguera-Crona",
                "catchPhrase": "Multi-layered client-server neural-net",
                "bs": "harness real-time e-markets"
            }
        }

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_response)

    def test_get_users_returns_empty_object_when_user_not_found(self):
        api = f"{self.api}/users/999"

        response = requests.get(api)

        expected_response = {}

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), expected_response)

    def test_get_users_returns_list_of_object_when_no_specified_id(self):
        api = f"{self.api}/users"

        response = requests.get(api)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertEqual(len(response.json()), 10)

    def test_post_posts_returns_success(self):
        api = f"{self.api}/posts"

        example_request = {
            "id": 1,
            "title": "Example title",
            "body": 'Example body',
            "userId": 1
        }
        expected_response = {'id': 101, 'title': 'Example title', 'body': 'Example body', 'userId': '1'}

        response = requests.post(api, data=example_request)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), expected_response)

    def test_get_posts_returns_success_with_specific_id(self):
        api = f"{self.api}/posts/1"

        expected_response = {
            "userId": 1,
            "id": 1,
            "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
        }

        response = requests.get(api)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_response)

    def test_put_posts_returns_success(self):
        api = f"{self.api}/posts/1"

        expected_response = {
            "userId": "1",
            "id": 1,
            "title": "Changed title",
            "body": "Modified body"
        }

        response = requests.put(api, data=expected_response)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_response)

    def test_patch_posts_returns_success_for_partial_modification(self):
        api = f"{self.api}/posts/1"

        request_body = {
            "id": 1,
            "title": "Changed title",
        }
        expected_response = {'userId': 1, 'id': '1', 'title': 'Changed title', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}

        response = requests.patch(api, data=request_body)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_response)

    def test_delete_posts_returns_success(self):
        api = f"{self.api}/posts/1"

        response = requests.delete(api)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {})

    def test_delete_posts_returns_not_found(self):
        api = f"{self.api}/posts"

        request_body = {"id": 199999}

        response = requests.delete(api, data=request_body)

        self.assertEqual(response.status_code, 404)

import requests


class UserEndpoint:
    def __init__(self, base_url, header):
        self.base_url = base_url
        self.headers = header

    def get_user(self, user_id):
        url = f'{self.base_url}/public/v2/users/{user_id}'
        response = requests.get(url)
        return response

    def create_user(self, user_data):
        url = f'{self.base_url}/public/v2/users'
        response = requests.post(url, json=user_data, headers=self.headers)
        return response

    def update_user(self, user_id, user_data):
        url = f'{self.base_url}/public/v2/users/{user_id}'
        response = requests.patch(url, json=user_data, headers=self.headers)
        return response

    def delete_user(self, user_data):
        url = f'{self.base_url}/public/v2/users'
        response = requests.delete(url, json=user_data, headers=self.headers)
        return response

    def get_all_users(self):
        url = f'{self.base_url}/public/v2/users/'
        response = requests.get(url)
        return response


class PostEndpoint(UserEndpoint):

    def get_post(self, user_id):
        url = f'{self.base_url}/public/v2/users/{user_id}/posts'
        response = requests.get(url)
        return response

    def create_post(self, user_id, post_data):
        url = f'{self.base_url}/public/v2/users/{user_id}/posts'
        response = requests.post(url, json=post_data, headers=self.headers)
        return response


class CommentEndpoint(UserEndpoint):

    def get_comment(self, user_id):
        url = f'{self.base_url}/public/v2/posts/{user_id}/comments'
        response = requests.get(url)
        return response

    def post_comment(self, user_id, data):
        url = f'{self.base_url}/public/v2/posts/{user_id}/comments'
        response = requests.post(url, json=data, headers=self.headers)
        return response

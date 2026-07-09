import requests


class YougileApi:
    def __init__(self, base_url, login, password, company_id):
        self.base_url = base_url
        self.login = login
        self.password = password
        self.company_id = company_id
        self.token = self.get_token_from_api()
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

    def get_token_from_api(self):
        auth_data = {
            "login": self.login,
            "password": self.password,
            "companyId": self.company_id
        }
        resp = requests.post(f"{self.base_url}/auth/keys", json=auth_data)
        resp.raise_for_status()
        return resp.json()["key"]

    def create_project(self, title):
        payload = {"title": title}
        resp = requests.post(f"{self.base_url}/projects",
                             json=payload, headers=self.headers)
        return resp

    def get_project(self, project_id):
        resp = requests.get(f"{self.base_url}/projects/{project_id}",
                            headers=self.headers)
        return resp

    def update_project(self, project_id, new_title):
        payload = {"title": new_title}
        resp = requests.put(f"{self.base_url}/projects/{project_id}",
                            json=payload, headers=self.headers)
        return resp

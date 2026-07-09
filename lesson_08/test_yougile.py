import pytest
from YougileApi import YougileApi

BASE_URL = "https://ru.yougile.com/api-v2/"
LOGIN = ""
PASSWORD = ""
COMPANY_ID = ""

api = YougileApi(BASE_URL, LOGIN, PASSWORD, COMPANY_ID)


class TestYougileProjects:
    project_id = None

    def test_create_project_positive(self):
        project_title = "Yougile POST positive"
        response = api.create_project(project_title)
        assert response.status_code == 201

        TestYougileProjects.project_id = response.json()["id"]

    def test_create_project_negative(self):
        response = api.create_project("")
        assert response.status_code == 400

    def test_get_project_positive(self):
        # Используем сохраненный project_id через self
        response = api.get_project(self.project_id)
        assert response.status_code == 200

    def test_get_project_negative(self):
        invalid_id = "12345678-1234-1234-1234-123456789012"
        response = api.get_project(invalid_id)
        assert response.status_code == 404

    def test_update_project_positive(self):
        new_title = "Yougile PUT positive"

        update_resp = api.update_project(self.project_id, new_title)
        assert update_resp.status_code == 200

        get_resp = api.get_project(self.project_id)
        assert get_resp.json()["title"] == new_title

    def test_update_project_negative(self):
        invalid_id = "12345678-1234-1234-1234-123456789012"
        response = api.update_project(invalid_id, "Yougile PUT negative")
        assert response.status_code == 404

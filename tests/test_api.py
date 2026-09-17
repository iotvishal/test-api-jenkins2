from task_api.main import app


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_get_tasks():
    client = app.test_client()

    response = client.get("/tasks")

    assert response.status_code == 200

    data = response.get_json()

    assert len(data) == 2
    assert data[0]["title"] == "Learn Jenkins"


def test_get_existing_task():
    client = app.test_client()

    response = client.get("/tasks/1")

    assert response.status_code == 200

    data = response.get_json()

    assert data["id"] == 1
    assert data["title"] == "Learn Jenkins"


def test_get_missing_task():
    client = app.test_client()

    response = client.get("/tasks/999")

    assert response.status_code == 404


def test_create_task():
    client = app.test_client()

    response = client.post(
        "/tasks",
        json={
            "title": "Learn Docker"
        }
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["title"] == "Learn Docker"
    assert data["completed"] is False

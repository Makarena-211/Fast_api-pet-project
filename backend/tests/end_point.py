
from fastapi.testclient import TestClient
from conftest import test_client, painting_payload, painting_delete_payload, painting_update_payload
import pytest
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import app





def test_create_painting(test_client, painting_payload):
    response = test_client.post('/paintings/create', json=painting_payload)
    assert response.status_code == 201
    created_painting = response.json()
    assert created_painting["name"] == painting_payload["name"]
    assert created_painting["photo"] == painting_payload["photo"]
    assert created_painting["author"] == painting_payload["author"]
    assert created_painting["price"] == painting_payload["price"]
    assert created_painting["type"] == painting_payload["type"]

def test_get_paintings(test_client):
    response = test_client.get('/paintings/')
    assert response.status_code == 200
    data = response.json()
    print(data)

def test_delete_paintings(test_client, painting_payload, painting_delete_payload):
    # Создание картины
    response = test_client.post('/paintings/create', json=painting_payload)
    assert response.status_code == 201

    # Удаление картины
    response = test_client.delete_with_payload(url='/paintings/delete', json=painting_delete_payload)
    assert response.status_code == 204


# def test_create_update(test_client, painting_payload, painting_update_payload):
#     #response = test_client.post('/painting/create', json=painting_payload)
#     #assert response.status_code == 201
#     #created_painting_photo = painting_payload["photo"]
        
#     response = test_client.get('/paintings')
#     assert response.status_code == 200
#     data = response.json()
#     painting_id = data["id"]


#     paintings = response.json()
#     created_painting = next((p for p in paintings if p["photo"] == created_painting_photo), None)
#     assert created_painting is not None, "Созданная картина не найдена"

#     painting_id = created_painting["id"]
#     response = test_client.put(f'/paintings/update/{painting_id}', json=painting_update_payload)
#     assert response.status_code == 200

#     updated_painting = response.json()
#     assert updated_painting["name"] == painting_update_payload["name"]
#     assert updated_painting["photo"] == painting_update_payload["photo"]
#     assert updated_painting["author"] == painting_update_payload["author"]
#     assert updated_painting["price"] == painting_update_payload["price"]
#     assert updated_painting["type"] == painting_update_payload["type"]






import pytest


@pytest.mark.asyncio
async def test_tasks_flow(client):
    
    res = await client.get("/tasks/")
    assert res.status_code == 200
    assert res.json() == []

    
    res = await client.post("/tasks/", json={"title": "X", "description": "d", "is_complete": False})
    assert res.status_code == 201
    data = res.json()
    task_id = data["id"]
    assert data["title"] == "X"

    
    res = await client.get("/tasks/")
    assert res.status_code == 200
    assert len(res.json()) == 1

    
    res = await client.get(f"/tasks/{task_id}/")
    assert res.status_code == 200
    assert res.json()["id"] == task_id

  
    res = await client.patch(f"/tasks/{task_id}/", json={"title": "X2"})
    assert res.status_code == 200
    assert res.json()["title"] == "X2"

   
    res = await client.delete(f"/tasks/{task_id}/")
    assert res.status_code == 204

    
    res = await client.get(f"/tasks/{task_id}/")
    assert res.status_code == 404



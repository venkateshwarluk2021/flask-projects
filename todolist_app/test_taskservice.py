import task_service

def test_add_and_get_task(db_setup):
    task_service.add_task("Pytest Task", "desc", "2025-07-23", False)
    tasks= task_service.get_all_tasks()
    assert len(tasks) == 1
    assert tasks[0].title == "Pytest Task"


def test_update_task(db_setup):
    task_service.add_task("Old", "desc", "2025-07-23", False)
    task = task_service.get_all_tasks()[0]

    task_service.update_task(task.id, "New Title", "Updated", "2025-07-24", True)
    updated = task_service.get_task_by_id(task.id)

    assert updated.title == "New Title"
    assert updated.completed == True

def test_delete_task(db_setup):
    task_service.add_task("Temp", "desc", "2025-07-23",False)
    task = task_service.get_all_tasks()[0]
    task_service.delete_task(task.id)
    assert len(task_service.get_all_tasks()) == 0

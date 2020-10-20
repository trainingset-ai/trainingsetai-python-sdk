import pytest
from os import environ
from imp import load_source
TrainingsetModule = load_source("sdk", "sdk/__init__.py")

try:
    api_key = environ['TRAININGSET_API_KEY']
    client = TrainingsetModule.TrainingsetClient(api_key)
except KeyError:
    raise Exception(
        "TRAININGSET_API_KEY environment variable is not set")


@pytest.fixture
def task_template():
    return {
        "attachment_url": "http://placekitten.com/1920/1080",
        "instructions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    }


@pytest.fixture
def objects_to_annotate():
    return [{"label": "test", "color": "rgba(0, 0, 0, 0)"}]


def test_create_box_annotation_task(task_template, objects_to_annotate):
    task_template["min_height"] = 0
    task_template["min_width"] = 0
    task_template["objects_to_annotate"] = objects_to_annotate
    client.create_box_annotation_task(task_template)


def test_create_line_annotation_task(task_template, objects_to_annotate):
    task_template["min_vertices"] = 0
    task_template["max_vertices"] = 999
    task_template["objects_to_annotate"] = objects_to_annotate
    client.create_line_annotation_task(task_template)


def test_create_point_annotation_task(task_template, objects_to_annotate):
    task_template["objects_to_annotate"] = objects_to_annotate
    client.create_point_annotation_task(task_template)


def test_create_polygon_annotation_task(task_template, objects_to_annotate):
    task_template["min_vertices"] = 0
    task_template["max_vertices"] = 999
    task_template["objects_to_annotate"] = objects_to_annotate
    client.create_polygon_annotation_task(task_template)


def test_create_segmentation_task(task_template, objects_to_annotate):
    task_template["objects_to_annotate"] = objects_to_annotate
    client.create_segmentation_task(task_template)


def test_create_point_cloud_annotation_task(task_template, objects_to_annotate):
    task_template["objects_to_annotate"] = objects_to_annotate
    client.create_point_cloud_annotation_task(task_template)


def test_create_image_categorization_task(task_template):
    task_template["categories"] = ["category1", "category2"]
    client.create_image_categorization_task(task_template)


TEST_DELETE_TASK_ID = ""


def test_get_tasks():
    global TEST_DELETE_TASK_ID
    tasks = client.get_tasks({
        "limit": 1
    })
    assert len(tasks["data"]) == 1
    TEST_DELETE_TASK_ID = tasks["data"][0]["_id"]


def test_delete():
    result = client.delete_task(TEST_DELETE_TASK_ID)
    assert result["status"] == "success"


def test_create_project():
    client.create_project("pytest project")


TEST_DELETE_PROJECT_ID = ""


def test_get_projects():
    global TEST_DELETE_PROJECT_ID
    result = client.get_projects()
    TEST_DELETE_PROJECT_ID = result["data"][0]["_id"]


def test_delete_project():
    client.delete_project(TEST_DELETE_PROJECT_ID)

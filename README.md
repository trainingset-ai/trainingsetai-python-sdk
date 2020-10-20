# Trainingset.ai Python SDK

## Install

```sh
pip install trainingsetai
```

## Import and Initialize a client session

```python
from trainingsetai import TrainingsetClient

client = TrainingsetClient("api_key")
```

# Methods

You can use any parameters from the documentation available [here](https://documenter.getpostman.com/view/10426338/Szf9V75M?version=latest).

## Tasks

### Get tasks

You can load the tasks with `get_tasks` method:

```python
client.get_tasks({
    "limit": 1
})
```

## Create tasks

There is a method for each task type and it's very straightforward:

```python
annotation_task = {
    "attachment_url": "http://placekitten.com/1920/1080",
    "instructions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "objects_to_annotate": [{"label": "test", "color": "rgba(0, 0, 0, 0)"}]
}

client.create_box_annotation_task(annotation_task)
client.create_line_annotation_task(annotation_task)
client.create_point_annotation_task(annotation_task)
client.create_polygon_annotation_task(annotation_task)
client.create_segmentation_task(annotation_task)
client.create_point_cloud_annotation_task(annotation_task)

categorization_task = {
    "attachment_url": "http://placekitten.com/1920/1080",
    "instructions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "categories": ["category1", "category2"]
}

client.create_image_categorization_task(categorization_task)
```

## Projects

Managing projects is also a straightforward process:

```python
client.get_projects()
client.create_project("test_project")
client.delete_project("project_id")
```

import requests

BASE_URL = "https://api.trainingset.ai/api"


class TrainingsetException(Exception):
    def __init__(self, message, status_code):
        super(TrainingsetException, self).__init__(
            '<Response [{}]> {}'.format(status_code, message))
        self.code = status_code


class TrainingsetInvalidRequest(TrainingsetException, ValueError):
    pass


class TrainingsetClient:
    def __init__(self, api_key):
        self.session = requests.Session()
        self.session.headers.update({'user_key': api_key})

    def _get_request(self, endpoint, params={}):
        r = self.session.get(BASE_URL + endpoint, params=params)

        if r.status_code == 200:
            return r.json()
        else:
            try:
                error = r.json()
            except ValueError:
                error = r.text
            if r.status_code == 400:
                raise TrainingsetInvalidRequest(
                    error["message"], r.status_code)
            else:
                raise TrainingsetException(error["message"], r.status_code)

    def _post_request(self, endpoint, data):
        r = self.session.post(BASE_URL + endpoint, json=data)

        if r.status_code == 200:
            return r.json()
        else:
            try:
                error = r.json()
            except ValueError:
                error = r.text
            if r.status_code == 400:
                raise TrainingsetInvalidRequest(
                    error["message"], r.status_code)
            else:
                raise TrainingsetException(error["message"], r.status_code)

    def get_tasks(self, parameters={}):
        """
        Returns a list of tasks.

        parameters object:

        `sort`: [["attribute_name",1 or -1]], example: [["_id",1]], 1 is ascending, -1 is descending

        `rangeStart`: YYYY-MM-DD, example: "2020-01-31"

        `rangeEnd`: YYYY-MM-DD, example: "2020-12-31"

        `type`: "annotation-box" | "annotation-line" | "annotation-polygon" | "annotation-box" | "annotation-pcd" | "categorization-image" | "segmentation"

        `status`: "pending" | "completed" | "cancelled" | "error" | "ready" | "working"

        `project`: string, projectID, example: "5f6359d0838a1d868f54cac4"

        `limit`: integer

        `skip`: integer

        `id`: string, ID of the task

        `qa_status`: "accepted" | "pending" | "rejected"

        Check the documentation for more info:
        https://documenter.getpostman.com/view/10426338/Szf9V75M?version=latest#783c6a4f-373a-4559-a68a-30cd98808d73
        """
        return self._get_request("/task/by-custom-filter", parameters)

    def delete_task(self, task_id):
        """
        Deletes a task.
        """
        response = self.session.delete(BASE_URL + "/task/" + task_id)
        return response.json()

    def create_box_annotation_task(self, task):
        """
        Creates a box type annotation task.

        task object:

        `instructions`: Instructions for drawing the task (Required) (String)

        `attachment_url`: HTTP/HTTPS Image address where the drawing of the task is carried out (Required) (String)

        `min_height`: Minimum height of each box drawn in the task (Optional) (Number)

        `min_width`: Minimum width of each box drawn in the task (Optional) (Number)

        `with_labels`: Define if the task has tags (Optional) (Boolean)

        `objects_to_annotate`: List of objects to be annotated (Optional) (AnnotationObject Array)

        `project`: Name of the project that belongs to the task (Optional) (String)

        `callback_url`: URL to which you will get task results delivered (Optional) (String)

        `automatic_prelabel`: Automatically prelabel the picture (Optional) (Boolean)

        Check the documentation for more info:
        https://documenter.getpostman.com/view/10426338/Szf9V75M?version=latest#783c6a4f-373a-4559-a68a-30cd98808d73
        """
        return self._post_request("/task/annotation/box", task)

    def create_line_annotation_task(self, task):
        """
        Creates a line type annotation task.

        task object:

        `instructions`: Instructions for drawing the task (Required) (String)

        `attachment_url`: HTTP/HTTPS Image address where the drawing of the task is carried out (Required) (String)

        `min_vertices`: Minimum number of vertices that a polygon drawn in the task must have (Optional)(Number)

        `max_vertices`: Maximum number of vertices that a polygon drawn in the task must have (Optional)(Number)

        `with_labels`: Define if the task has tags (Optional) (Boolean)

        `objects_to_annotate`: List of objects to be annotated (Optional) (AnnotationObject Array)

        `project`: Name of the project that belongs to the task (Optional) (String)

        `callback_url`: URL to which you will get task results delivered (Optional) (String)

        `automatic_prelabel`: Automatically prelabel the picture (Optional) (Boolean)

        Check the documentation for more info:
        https://documenter.getpostman.com/view/10426338/Szf9V75M?version=latest#783c6a4f-373a-4559-a68a-30cd98808d73
        """
        return self._post_request("/task/annotation/line", task)

    def create_polygon_annotation_task(self, task):
        """
        Creates a line type annotation task.

        task object:

        `instructions`: Instructions for drawing the task (Required) (String)

        `attachment_url`: HTTP/HTTPS Image address where the drawing of the task is carried out (Required) (String)

        `min_vertices`: Minimum number of vertices that a polygon drawn in the task must have (Optional)(Number)

        `max_vertices`: Maximum number of vertices that a polygon drawn in the task must have (Optional)(Number)

        `with_labels`: Define if the task has tags (Optional) (Boolean)

        `objects_to_annotate`: List of objects to be annotated (Optional) (AnnotationObject Array)

        `project`: Name of the project that belongs to the task (Optional) (String)

        `callback_url`: URL to which you will get task results delivered (Optional) (String)

        `automatic_prelabel`: Automatically prelabel the picture (Optional) (Boolean)

        Check the documentation for more info:
        https://documenter.getpostman.com/view/10426338/Szf9V75M?version=latest#783c6a4f-373a-4559-a68a-30cd98808d73
        """
        return self._post_request("/task/annotation/polygon", task)

    def create_point_annotation_task(self, task):
        """
        Creates a line type annotation task.

        task object:

        `instructions`: Instructions for drawing the task (Required) (String)

        `attachment_url`: HTTP/HTTPS Image address where the drawing of the task is carried out (Required) (String)

        `with_labels`: Define if the task has tags (Optional) (Boolean)

        `objects_to_annotate`: List of objects to be annotated (Optional) (AnnotationObject Array)

        `project`: Name of the project that belongs to the task (Optional) (String)

        `callback_url`: URL to which you will get task results delivered (Optional) (String)

        `automatic_prelabel`: Automatically prelabel the picture (Optional) (Boolean)

        Check the documentation for more info:
        https://documenter.getpostman.com/view/10426338/Szf9V75M?version=latest#783c6a4f-373a-4559-a68a-30cd98808d73
        """
        return self._post_request("/task/annotation/point", task)

    def create_point_cloud_annotation_task(self, task):
        """
        Creates a line type annotation task.

        task object:

        `instructions`: Instructions for drawing the task (Required) (String)

        `attachment_url`: HTTP/HTTPS Image address where the drawing of the task is carried out (Required) (String)

        `with_labels`: Define if the task has tags (Optional) (Boolean)

        `objects_to_annotate`: List of objects to be annotated (Optional) (AnnotationObject Array)

        `project`: Name of the project that belongs to the task (Optional) (String)

        `callback_url`: URL to which you will get task results delivered (Optional) (String)

        `cameras`: Camera parameters, each camera is an object (Optional) (CameraObject Array)

        Check the documentation for more info:
        https://documenter.getpostman.com/view/10426338/Szf9V75M?version=latest#783c6a4f-373a-4559-a68a-30cd98808d73
        """
        return self._post_request("/task/annotation/pcd", task)

    def create_segmentation_task(self, task):
        """
        Creates a line type annotation task.

        task object:

        `instructions`: Instructions for drawing the task (Required) (String)

        `attachment_url`: HTTP/HTTPS Image address where the drawing of the task is carried out (Required) (String)

        `with_labels`: Define if the task has tags (Optional) (Boolean)

        `objects_to_annotate`: List of objects to be annotated (Optional) (AnnotationObject Array)

        `project`: Name of the project that belongs to the task (Optional) (String)

        `callback_url`: URL to which you will get task results delivered (Optional) (String)

        `automatic_prelabel`: Automatically prelabel the picture (Optional) (Boolean)

        Check the documentation for more info:
        https://documenter.getpostman.com/view/10426338/Szf9V75M?version=latest#783c6a4f-373a-4559-a68a-30cd98808d73
        """
        return self._post_request("/task/annotation/segmentation", task)

    def create_image_categorization_task(self, task):
        """
        Creates a line type annotation task.

        task object:

        `instructions`: Instructions for drawing the task (Required) (String)

        `categories`: Categories into which an image can be categorized (Required) (String Array)

        `attachment_url`: HTTP/HTTPS Image address where the drawing of the task is carried out (Required) (String)

        `allow_multiple`: Allow multiple categories to be selected (Optional) (Boolean)

        `with_labels`: Define if the task has tags (Optional) (Boolean)

        `project`: Name of the project that belongs to the task (Optional) (String)

        `callback_url`: URL to which you will get task results delivered (Optional) (String)

        Check the documentation for more info:
        https://documenter.getpostman.com/view/10426338/Szf9V75M?version=latest#783c6a4f-373a-4559-a68a-30cd98808d73
        """
        return self._post_request("/task/categorization/image", task)

    def create_project(self, project_name):
        """
        Creates a new project.
        """
        return self._post_request("/project", {"name": project_name})

    def get_projects(self):
        """
        Fetches a list of projects.
        """
        return self._get_request("/project")

    def delete_project(self, project_id):
        """
        Deletes a project by it's identifier.
        """
        response = self.session.delete(BASE_URL + "/project/" + project_id)
        return response.json()

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
                error = r.json()['error']
            except ValueError:
                error = r.text
            if r.status_code == 400:
                raise TrainingsetInvalidRequest(
                    error["message"], error["code"])
            else:
                raise TrainingsetException(error["message"], error["code"])

    def _post_request(self, endpoint, data):
        r = self.session.post(BASE_URL + endpoint, json=data)

        if r.status_code == 200:
            return r.json()
        else:
            try:
                error = r.json()['error']
            except ValueError:
                error = r.text
            if r.status_code == 400:
                raise TrainingsetInvalidRequest(
                    error["message"], error["code"])
            else:
                raise TrainingsetException(error["message"], error["code"])

    def get_tasks(self, parameters):
        """
        Returns a list of tasks.

        List of parameters, all of them are optional:

        sort: [["attribute_name",1 or -1]], example: [["_id",1]], 1 is ascending, -1 is descending

        rangeStart: YYYY-MM-DD, example: "2020-01-31"

        rangeEnd: YYYY-MM-DD, example: "2020-12-31"

        type: "annotation-box" | "annotation-line" | "annotation-polygon" | "annotation-box" | "annotation-pcd" | "categorization-image" | "segmentation"

        status: "pending" | "completed" | "cancelled" | "error" | "ready" | "working"

        project: string, projectID, example: "5f6359d0838a1d868f54cac4"

        limit: integer

        skip: integer

        id: string, ID of the task

        qa_status: "accepted" | "pending" | "rejected"
        """
        return self._get_request("/task/by-custom-filter", parameters)

    def delete_task(self, task_id):
        response = self.session.delete(BASE_URL + "/task/" + task_id)
        return response.json()

    def create_box_annotation_task(self, data):
        return self._post_request("/task/annotation/box", data)

    def create_line_annotation_task(self, data):
        return self._post_request("/task/annotation/line", data)

    def create_polygon_annotation_task(self, data):
        return self._post_request("/task/annotation/polygon", data)

    def create_point_annotation_task(self, data):
        return self._post_request("/task/annotation/point", data)

    def create_point_cloud_annotation_task(self, data):
        return self._post_request("/task/annotation/pcd", data)

    def create_segmentation_task(self, data):
        return self._post_request("/task/annotation/segmentation", data)

    def create_image_categorization_task(self, data):
        return self._post_request("/task/categorization/image", data)

    def create_project(self, project_name):
        return self._post_request("/project", {"name": project_name})

    def get_projects(self):
        return self._get_request("/project")

    def delete_project(self, project_id):
        response = self.session.delete(BASE_URL + "/project/" + project_id)
        return response.json()

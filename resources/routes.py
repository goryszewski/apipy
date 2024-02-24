from .task import TasksApi, TaskAPI

from .project import ProjectsApi, ProjectAPI

from .default import Default


def initialize_routes(api):
    api.add_resource(Default, "/readyz", "/livez")
    api.add_resource(TasksApi, "/api/tasks")
    api.add_resource(TaskAPI, "/api/tasks/<index>")

    api.add_resource(ProjectsApi, "/api/projects")
    api.add_resource(ProjectAPI, "/api/projects/<index>")

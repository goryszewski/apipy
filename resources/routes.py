from .task import TasksApi,TaskAPI

def initialize_routes(api):
    api.add_resource(TasksApi,'/api/tasks')
    api.add_resource(TaskAPI,'/api/tasks/<index>')

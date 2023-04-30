from ..models import Projects
from ariadne import convert_kwargs_to_snake_case

def list_projects_resolver(obj, info):
    try:
        projects = [project.to_dict() for project in Projects.query.all()]
        if not projects:
            raise Exception("No projects found")
        payload = {
            "success": True,
            "data": projects
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

@convert_kwargs_to_snake_case
def get_project_resolver(obj, info, id):
    try:
        project = Projects.query.get(id)
        payload = {
            "success": True,
            "data": project.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Activity matching {id} not found"]
        }
    return payload
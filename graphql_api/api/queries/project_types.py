from ..models import ProjectTypes
from ariadne import convert_kwargs_to_snake_case

def list_project_types_resolver(obj, info):
    try:
        project_types = [project_type.to_dict() for project_type in ProjectTypes.query.all()]
        if not project_types:
            raise Exception("No project types found.")
        payload = {
            "success": True,
            "data": project_types
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

@convert_kwargs_to_snake_case
def get_project_type_resolver(obj, info, id):
    try:
        project_type = ProjectTypes.query.get(id)
        payload = {
            "success": True,
            "data": project_type.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Project Type matching {id} not found"]
        }
    return payload
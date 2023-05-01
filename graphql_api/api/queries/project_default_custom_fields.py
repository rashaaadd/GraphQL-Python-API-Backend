from ..models import ProjectDefaultCustomFields
from ariadne import convert_kwargs_to_snake_case

def list_project_custom_fields_resolver(obj, info):
    try:
        project_custom_fields = [project_custom_field.to_dict() for project_custom_field in ProjectDefaultCustomFields.query.all()]
        if not project_custom_fields:
            raise Exception("No project custom fields found.")
        payload = {
            "success": True,
            "data": project_custom_fields
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

@convert_kwargs_to_snake_case
def get_project_custom_field_resolver(obj, info, id):
    try:
        project_custom_field = ProjectDefaultCustomFields.query.get(id)
        payload = {
            "success": True,
            "data": project_custom_field.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Project custom field matching ID: {id} not found"]
        }
    return payload
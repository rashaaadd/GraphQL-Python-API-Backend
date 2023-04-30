from ..models import CustomFields
from ariadne import convert_kwargs_to_snake_case

def list_custom_fields_resolver(obj, info):
    try:
        custom_fields = [custom_field.to_dict() for custom_field in CustomFields.query.all()]
        if not custom_fields:
            raise Exception("No custom fields found.")
        payload = {
            "success": True,
            "data": custom_fields
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

@convert_kwargs_to_snake_case
def get_custom_field_resolver(obj, info, id):
    try:
        custom_field = CustomFields.query.get(id)
        payload = {
            "success": True,
            "data": custom_field.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Custom field matching {id} not found"]
        }
    return payload
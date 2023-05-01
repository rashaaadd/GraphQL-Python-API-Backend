from ..models import Tags
from ariadne import convert_kwargs_to_snake_case

def list_tags_resolver(obj, info):
    try:
        tags = [tag.to_dict() for tag in Tags.query.all()]
        if not tags:
            raise Exception("No tags found.")
        payload = {
            "success": True,
            "data": tags
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

@convert_kwargs_to_snake_case
def get_tag_resolver(obj, info, id):
    try:
        tag = Tags.query.get(id)
        payload = {
            "success": True,
            "data": tag.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Tag matching {id} not found"]
        }
    return payload
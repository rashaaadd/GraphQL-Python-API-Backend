from ..models import Priorities
from ariadne import convert_kwargs_to_snake_case

def list_priorities_resolver(obj, info):
    try:
        priorities = [priority.to_dict() for priority in Priorities.query.all()]
        if not priorities:
            raise Exception("No priorities found.")
        payload = {
            "success": True,
            "data": priorities
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

@convert_kwargs_to_snake_case
def get_priority_resolver(obj, info, id):
    try:
        priority = Priorities.query.get(id)
        payload = {
            "success": True,
            "data": priority.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Priority matching {id} not found"]
        }
    return payload
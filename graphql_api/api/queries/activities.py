from ..models import Activities
from ariadne import convert_kwargs_to_snake_case

def list_activities_resolver(obj, info):
    try:
        activities = [activity.to_dict() for activity in Activities.query.all()]
        if not activities:
            raise Exception("No activities found")
        payload = {
            "success": True,
            "data": activities
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

@convert_kwargs_to_snake_case
def get_activity_resolver(obj, info, id):
    try:
        activity = Activities.query.get(id)
        payload = {
            "success": True,
            "data": activity.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Activity matching {id} not found"]
        }
    return payload
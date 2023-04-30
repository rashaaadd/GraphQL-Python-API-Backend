from ..models import Activities
from app import db


def create_activity_resolver(obj, info, action_name):
    try:
        activity = Activities(action_name=action_name)
        db.session.add(activity)
        db.session.commit()
        payload = {
            "success": True,
            "data": activity.to_dict()
        }
    except ValueError:
        payload = {
            "success": False,
            "errors": [f"Error creating activity."]
        }
    return payload


def update_activity_resolver(obj, info, id, action_name):
    try:
        activity = Activities.query.get(id)
        if activity:
            activity.action_name = action_name
            db.session.add(activity)
            db.session.commit()
            payload = {
                "success": True,
                "data": activity.to_dict()
            }
        else:
            payload = {
                "success": False,
                "errors": [f"Activity with ID:{id} not found"]
            }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Activity with ID:{id} not found"]
        }

    return payload


def delete_activity_resolver(obj, info, id):
    try:
        activity = Activities.query.get(id)
        if activity:
            db.session.delete(activity)
            db.session.commit()
            payload = {
                "success": True,
                "data": activity.to_dict()
            }
        else:
            payload = {
                "success": False,
                "errors": [f"Activity with ID:{id} not found"]
            }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Activity with ID:{id} not found"]
        }

    return payload

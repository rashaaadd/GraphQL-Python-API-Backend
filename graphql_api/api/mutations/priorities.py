from ..models import Priorities
from app import db


def create_priority_resolver(obj, info, priority_name):
    try:
        priority = Priorities(priority_name=priority_name)
        db.session.add(priority)
        db.session.commit()
        payload = {
            "success": True,
            "data": priority.to_dict()
        }
    except ValueError:
        payload = {
            "success": False,
            "errors": [f"Error creating priority."]
        }
    return payload


def update_priority_resolver(obj, info, id, priority_name):
    try:
        priority = Priorities.query.get(id)
        if priority:
            priority.priority_name = priority_name
            db.session.add(priority)
            db.session.commit()
            payload = {
                "success": True,
                "data": priority.to_dict()
            }
        else:
            payload = {
                "success": False,
                "errors": [f"Priority with ID:{id} not found"]
            }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Priority with ID:{id} not found"]
        }

    return payload


def delete_priority_resolver(obj, info, id):
    try:
        priority = Priorities.query.get(id)
        if priority:
            db.session.delete(priority)
            db.session.commit()
            payload = {
                "success": True,
                "data": priority.to_dict()
            }
        else:
            payload = {
                "success": False,
                "errors": [f"Priority with ID:{id} not found"]
            }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Priority with ID:{id} not found"]
        }

    return payload

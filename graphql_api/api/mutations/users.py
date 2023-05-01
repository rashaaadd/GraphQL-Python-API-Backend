from ..models import Users
from app import db


def create_user_resolver(obj, info, input):
    try:
        user = Users(**input)
        db.session.add(user)
        db.session.commit()
        payload = {
            "success": True,
            "data": user.to_dict()
        }
    except ValueError:
        payload = {
            "success": False,
            "errors": [f"Error creating user."]
        }
    return payload


def update_user_resolver(obj, info, id, input):
    try:
        user = Users.query.get(id)
        if user:
            for key, value in input.items():
                setattr(user, key, value)
            db.session.commit()
            payload = {
                "success": True,
                "data": user.to_dict()
            }
        else:
            payload = {
                "success": False,
                "errors": [f"User with ID:{id} not found"]
            }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"User with ID:{id} not found"]
        }

    return payload


def delete_user_resolver(obj, info, id):
    try:
        user = Users.query.get(id)
        if user:
            db.session.delete(user)
            db.session.commit()
            payload = {
                "success": True,
                "data": user.to_dict()
            }
        else:
            payload = {
                "success": False,
                "errors": [f"User with ID:{id} not found"]
            }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"User with ID:{id} not found"]
        }

    return payload

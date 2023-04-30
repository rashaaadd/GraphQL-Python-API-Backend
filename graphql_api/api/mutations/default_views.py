from ..models import DefaultViews
from app import db


def create_default_view_resolver(obj, info, title):
    try:
        default_view = DefaultViews(title=title)
        db.session.add(default_view)
        db.session.commit()
        payload = {
            "success": True,
            "data": default_view.to_dict()
        }
    except ValueError:
        payload = {
            "success": False,
            "errors": [f"Error creating default view."]
        }
    return payload


def update_default_view_resolver(obj, info, id, title):
    try:
        default_view = DefaultViews.query.get(id)
        if default_view:
            default_view.title = title
            db.session.add(default_view)
            db.session.commit()
            payload = {
                "success": True,
                "data": default_view.to_dict()
            }
        else:
            payload = {
                "success": False,
                "errors": [f"Default view with ID:{id} not found"]
            }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Default view with ID:{id} not found"]
        }

    return payload


def delete_default_view_resolver(obj, info, id):
    try:
        default_view = DefaultViews.query.get(id)
        if default_view:
            db.session.delete(default_view)
            db.session.commit()
            payload = {
                "success": True,
                "data": default_view.to_dict()
            }
        else:
            payload = {
                "success": False,
                "errors": [f"Default view with ID:{id} not found"]
            }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Default view with ID:{id} not found"]
        }

    return payload

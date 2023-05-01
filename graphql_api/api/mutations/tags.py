from ..models import Tags
from app import db


def create_tag_resolver(obj, info, title):
    try:
        tag = Tags(priority_name=title)
        db.session.add(tag)
        db.session.commit()
        payload = {
            "success": True,
            "data": tag.to_dict()
        }
    except ValueError:
        payload = {
            "success": False,
            "errors": [f"Error creating tag."]
        }
    return payload


def update_tag_resolver(obj, info, id, title):
    try:
        tag = Tags.query.get(id)
        if tag:
            tag.title = title
            db.session.add(tag)
            db.session.commit()
            payload = {
                "success": True,
                "data": tag.to_dict()
            }
        else:
            payload = {
                "success": False,
                "errors": [f"Tag with ID:{id} not found"]
            }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Tag with ID:{id} not found"]
        }

    return payload


def delete_tag_resolver(obj, info, id):
    try:
        tag = Tags.query.get(id)
        if tag:
            db.session.delete(tag)
            db.session.commit()
            payload = {
                "success": True,
                "data": tag.to_dict()
            }
        else:
            payload = {
                "success": False,
                "errors": [f"Tag with ID:{id} not found"]
            }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Tag with ID:{id} not found"]
        }

    return payload

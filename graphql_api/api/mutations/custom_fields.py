from ..models import CustomFields
from app import db


def create_custom_field_resolver(obj, info, title):
    try:
        custom_field = CustomFields(title=title)
        db.session.add(custom_field)
        db.session.commit()
        payload = {
            "success": True,
            "data": custom_field.to_dict()
        }
    except ValueError:
        payload = {
            "success": False,
            "errors": [f"Error creating custom field."]
        }
    return payload


def update_custom_field_resolver(obj, info, id, title):
    try:
        custom_field = CustomFields.query.get(id)
        if custom_field:
            custom_field.title = title
            db.session.add(custom_field)
            db.session.commit()
            payload = {
                "success": True,
                "data": custom_field.to_dict()
            }
        else:
            payload = {
                "success": False,
                "errors": [f"Custom field with ID:{id} not found"]
            }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Custom field with ID:{id} not found"]
        }

    return payload


def delete_custom_field_resolver(obj, info, id):
    try:
        custom_field = CustomFields.query.get(id)
        if custom_field:
            db.session.delete(custom_field)
            db.session.commit()
            payload = {
                "success": True,
                "data": custom_field.to_dict()
            }
        else:
            payload = {
                "success": False,
                "errors": [f"Custom field with ID:{id} not found"]
            }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Custom field with ID:{id} not found"]
        }

    return payload

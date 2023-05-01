from ..models import ProjectDefaultCustomFields
from app import db


def create_project_custom_field_resolver(obj, info, title):
    try:
        project_custom_field = ProjectDefaultCustomFields(priority_name=title)
        db.session.add(project_custom_field)
        db.session.commit()
        payload = {
            "success": True,
            "data": project_custom_field.to_dict()
        }
    except ValueError:
        payload = {
            "success": False,
            "errors": [f"Error creating project custom field."]
        }
    return payload


def update_project_custom_field_resolver(obj, info, id, title):
    try:
        project_custom_field = ProjectDefaultCustomFields.query.get(id)
        if project_custom_field:
            project_custom_field.title = title
            db.session.add(project_custom_field)
            db.session.commit()
            payload = {
                "success": True,
                "data": project_custom_field.to_dict()
            }
        else:
            payload = {
                "success": False,
                "errors": [f"Project custom field with ID:{id} not found"]
            }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Project custom field with ID:{id} not found"]
        }

    return payload


def delete_project_custom_field_resolver(obj, info, id):
    try:
        project_custom_field = ProjectDefaultCustomFields.query.get(id)
        if project_custom_field:
            db.session.delete(project_custom_field)
            db.session.commit()
            payload = {
                "success": True,
                "data": project_custom_field.to_dict()
            }
        else:
            payload = {
                "success": False,
                "errors": [f"Project custom field with ID:{id} not found"]
            }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Project custom field with ID:{id} not found"]
        }

    return payload

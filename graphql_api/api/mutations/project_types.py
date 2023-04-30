from ..models import ProjectTypes
from app import db


def create_project_type_resolver(obj, info, title):
    try:
        print("Hello")
        project_type = ProjectTypes(title=title)
        db.session.add(project_type)
        db.session.commit()
        payload = {
            "success": True,
            "data": project_type.to_dict()
        }
    except ValueError:
        payload = {
            "success": False,
            "errors": [f"Error creating project type."]
        }
    return payload


def update_project_type_resolver(obj, info, id, title):
    try:
        project_type = ProjectTypes.query.get(id)
        if project_type:
            project_type.title = title
            db.session.add(project_type)
            db.session.commit()
            payload = {
                "success": True,
                "data": project_type.to_dict()
            }
        else:
            payload = {
                "success": False,
                "errors": [f"Project type with ID:{id} not found"]
            }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Project type with ID:{id} not found"]
        }

    return payload


def delete_project_type_resolver(obj, info, id):
    try:
        project_type = ProjectTypes.query.get(id)
        if project_type:
            db.session.delete(project_type)
            db.session.commit()
            payload = {
                "success": True,
                "data": project_type.to_dict()
            }
        else:
            payload = {
                "success": False,
                "errors": [f"Project Type with ID:{id} not found"]
            }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Project Type with ID:{id} not found"]
        }

    return payload

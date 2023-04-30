from ..models import Projects
from app import db


def create_project_resolver(obj, info, input):
    try:
        project = Projects(**input)
        db.session.add(project)
        db.session.commit()
        payload = {
            "success": True,
            "data": project.to_dict()
        }
    except ValueError:
        payload = {
            "success": False,
            "errors": [f"Error creating project."]
        }
    return payload


def update_project_resolver(obj, info, id, project_name):
    try:
        project = Projects.query.get(id)
        if project:
            project.project_name = project_name
            db.session.add(project)
            db.session.commit()
            payload = {
                "success": True,
                "data": project.to_dict()
            }
        else:
            payload = {
                "success": False,
                "errors": [f"Project with ID:{id} not found"]
            }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Project with ID:{id} not found"]
        }

    return payload


def delete_project_resolver(obj, info, id):
    try:
        project = Projects.query.get(id)
        if project:
            db.session.delete(project)
            db.session.commit()
            payload = {
                "success": True,
                "data": project.to_dict()
            }
        else:
            payload = {
                "success": False,
                "errors": [f"Project with ID:{id} not found"]
            }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Project with ID:{id} not found"]
        }

    return payload

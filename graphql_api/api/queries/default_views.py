from ..models import DefaultViews
from ariadne import convert_kwargs_to_snake_case

def list_default_views_resolver(obj, info):
    try:
        default_views = [default_view.to_dict() for default_view in DefaultViews.query.all()]
        if not default_views:
            raise Exception("No default views found.")
        payload = {
            "success": True,
            "data": default_views
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

@convert_kwargs_to_snake_case
def get_default_view_resolver(obj, info, id):
    try:
        default_view = DefaultViews.query.get(id)
        payload = {
            "success": True,
            "data": default_view.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Default View matching {id} not found"]
        }
    return payload
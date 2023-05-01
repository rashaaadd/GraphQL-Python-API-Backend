from ..models import Users
from ariadne import convert_kwargs_to_snake_case

def list_users_resolver(obj, info):
    try:
        users = [user.to_dict() for user in Users.query.all()]
        if not users:
            raise Exception("No users found")
        payload = {
            "success": True,
            "data": users
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

@convert_kwargs_to_snake_case
def get_user_resolver(obj, info, id):
    try:
        user = Users.query.get(id)
        payload = {
            "success": True,
            "data": user.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["User matching {id} not found"]
        }
    return payload
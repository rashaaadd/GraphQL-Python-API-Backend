from api import app, db

from ariadne import ( 
    load_schema_from_path,
    make_executable_schema,
    graphql_sync,
    snake_case_fallback_resolvers,
    ObjectType,
)
from flask import request, jsonify
from api.queries import (
    activities as activities_queries,
    projects as projects_queries,
    project_types as project_types_queries,
    custom_fields as custom_fields_queires,
    default_views as default_views_queries
)
from api.mutations import (
    activities as activities_mutations,
    projects as projects_mutations,
    project_types as project_types_mutations,
    custom_fields as custom_fields_mutations,
    default_views as default_views_mutations
)

query = ObjectType("Query")
mutation = ObjectType("Mutation")

#Queries
query.set_field("getAllActivities", activities_queries.list_activities_resolver)
query.set_field("getActivity", activities_queries.get_activity_resolver)

query.set_field("getAllProjects", projects_queries.list_projects_resolver)
query.set_field("getProject", projects_queries.get_project_resolver)

query.set_field("getAllProjectTypes", project_types_queries.list_project_types_resolver)
query.set_field("getProjectType", project_types_queries.get_project_type_resolver)

query.set_field("getAllCustomFields", custom_fields_queires.list_custom_fields_resolver)
query.set_field("getCustomField", custom_fields_queires.get_custom_field_resolver)

query.set_field("getAllDefaultViews", default_views_queries.list_default_views_resolver)
query.set_field("getDefaultView", default_views_queries.get_default_view_resolver)

#Mutations
mutation.set_field("createActivity", activities_mutations.create_activity_resolver)
mutation.set_field("updateActivity", activities_mutations.update_activity_resolver)
mutation.set_field("deleteActivity", activities_mutations.delete_activity_resolver)

mutation.set_field("createProject", projects_mutations.create_project_resolver)
mutation.set_field("updateProject", projects_mutations.update_project_resolver)
mutation.set_field("deleteProject", projects_mutations.delete_project_resolver)

mutation.set_field("createProjectType", project_types_mutations.create_project_type_resolver)
mutation.set_field("updateProjectType", project_types_mutations.update_project_type_resolver)
mutation.set_field("deleteProjectType", project_types_mutations.delete_project_type_resolver)

mutation.set_field("createCustomField", custom_fields_mutations.create_custom_field_resolver)
mutation.set_field("updateCustomField", custom_fields_mutations.update_custom_field_resolver)
mutation.set_field("deleteCustomField", custom_fields_mutations.delete_custom_field_resolver)

mutation.set_field("createDefaultView", default_views_mutations.create_default_view_resolver)
mutation.set_field("updateDefaultView", default_views_mutations.update_default_view_resolver)
mutation.set_field("deleteDefaultView", default_views_mutations.delete_default_view_resolver)


type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs,
    query,
    mutation,
    snake_case_fallback_resolvers
)

@app.route('/graphql', methods=['GET'])
def graphql_playground():
    return "Healthy",200

@app.route('/graphql', methods=['POST'])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code
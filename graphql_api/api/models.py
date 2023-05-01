from app import db
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Boolean,
    DateTime,
    JSON
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

db.metadata.clear()


class Activities(db.Model):
    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    action_name = Column(String(32))

    def to_dict(self):
        return {
            "id": self.id,
            "action_name": self.action_name
        }


class Projects(db.Model):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    project_name = Column(String(512), nullable=False)
    project_type_id = Column(Integer, ForeignKey(
        "project_types.id"), nullable=False)
    avatar_url = Column(String(512))
    owner_user_id = Column(Integer)
    admin_user_id = Column(Integer)
    created_by_user_id = Column(Integer)
    default_view_id = Column(Integer, ForeignKey(
        "default_views.id"), nullable=False)
    created_ts = Column(DateTime(timezone=True), server_default=func.now())
    updated_ts = Column(DateTime(timezone=True), onupdate=func.now())
    workspace_id = Column(Integer)
    is_template = Column(Boolean, default=False)
    is_private = Column(Boolean, default=False)
    project_default_custom_fields = relationship(
        "ProjectDefaultCustomFields", back_populates="projects")
    project_status_templates = relationship(
        "ProjectStatusTemplates", back_populates="projects")
    project_tags = relationship("ProjectTags", back_populates="projects")
    project_task_lists = relationship(
        "ProjectTaskLists", back_populates="projects")
    project_teams = relationship("ProjectTeams", back_populates="projects")
    default_views = relationship("DefaultViews", back_populates="projects")
    project_types = relationship("ProjectTypes", back_populates="projects")

    def to_dict(self):
        return {
            "id": self.id,
            "project_name": self.project_name,
            "project_type_id": self.project_type_id,
            "avatar_url": self.avatar_url,
            "owner_user_id": self.owner_user_id,
            "admin_user_id": self.admin_user_id,
            "created_by_user_id": self.created_by_user_id,
            "default_view_id": self.default_view_id,
            "created_ts": self.created_ts,
            "updated_ts": self.updated_ts,
            "workspace_id": self.workspace_id,
            "is_template": self.is_template,
            "is_private": self.is_private,
        }


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = db.Column(String(255), nullable=True)
    last_name = db.Column(String(255), nullable=True)
    year_of_birth = db.Column(String(10), nullable=True)
    profile_pic_url = db.Column(String(2083), nullable=True)
    gender_id = db.Column(Integer, nullable=True)
    languages = db.Column(String(60), nullable=True)
    bio = db.Column(String(1024), nullable=True)
    created_ts = db.Column(DateTime, nullable=True, server_default=func.now())
    updated_ts = db.Column(DateTime, nullable=True, onupdate=func.now())

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "year_of_birth": self.year_of_birth,
            "profile_pic_url": self.profile_pic_url,
            "gender_id": self.gender_id,
            "languages": self.languages,
            "bio": self.bio,
            "created_ts": self.created_ts,
            "updated_ts": self.updated_ts,
        }


class CustomFields(db.Model):
    __tablename__ = 'custom_fields'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(64))

    project_default_custom_fields = relationship(
        "ProjectDefaultCustomFields", back_populates="custom_fields")
    tasks_custom_fields = relationship(
        "TasksCustomFields", back_populates="custom_fields")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title
        }


class DefaultViews(db.Model):
    __tablename__ = 'default_views'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(64))

    projects = relationship("Projects", back_populates="default_views")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title
        }


class Priorities(db.Model):
    __tablename__ = 'priorities'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    priority_name = Column(String(64))
    tasks = relationship("Tasks", back_populates="priorities")

    def to_dict(self):
        return {
            "id": self.id,
            "priority_name": self.priority_name
        }


class ProjectTypes(db.Model):
    __tablename__ = 'project_types'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(64))
    projects = relationship("Projects", back_populates="project_types")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title
        }


class Tags(db.Model):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(128), nullable=False)
    project_tags = relationship("ProjectTags", back_populates="tags")
    task_tags = relationship("TaskTags", back_populates="tags")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title
        }


class ProjectDefaultCustomFields(db.Model):
    __tablename__ = "project_default_custom_fields"

    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey(
        "projects.id", ondelete="NO ACTION", onupdate="NO ACTION"))
    custom_field_id = Column(Integer, ForeignKey(
        "custom_fields.id", ondelete="NO ACTION", onupdate="NO ACTION"))
    custom_field_value = Column(JSON)

    custom_fields = relationship(
        'CustomFields', back_populates='project_default_custom_fields')
    projects = relationship(
        'Projects', back_populates='project_default_custom_fields')

    def __repr__(self):
        return f"<ProjectDefaultCustomField {self.title}>"


class ProjectStatusTemplates(db.Model):
    __tablename__ = 'project_status_templates'

    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    status_template_id = Column(Integer, ForeignKey(
        'task_stage_templates.id'), nullable=False)

    projects = relationship(
        'Projects', back_populates='project_status_templates')
    task_stage_templates = relationship(
        'TaskStageTemplates', back_populates='project_status_templates')

    def __repr__(self):
        return f"<ProjectStatusTemplates {self.status_template_id, self.project_id}>"


class ProjectTags(db.Model):
    __tablename__ = "project_tags"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    tag_id = Column(Integer, ForeignKey("tags.id"))
    projects = relationship("Projects", back_populates="project_tags")
    tags = relationship("Tags", back_populates="project_tags")

    def __ref__(self):
        return f"<ProjectTags {self.project_id, self.tag_id}"


class ProjectTaskLists(db.Model):
    __tablename__ = 'project_task_lists'

    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey('projects.id'))
    title = Column(String(256))

    projects = relationship('Projects', back_populates='project_task_lists')
    tasks = relationship('Tasks', back_populates='project_task_lists')

    def __repr__(self):
        return f"<ProjectTaskLists {self.title}>"


class ProjectTeams(db.Model):
    __tablename__ = "project_teams"

    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    team_id = Column(Integer, ForeignKey("teams.id"))

    projects = relationship("Projects", back_populates="project_teams")
    teams = relationship("Teams", back_populates="project_teams")

    def __repr__(self):
        return f"<ProjectTaskLists {self.title}>"


class TaskActivities(db.Model):
    __tablename__ = 'task_activities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    task_id = Column(Integer, ForeignKey('tasks.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    created_ts = Column(DateTime(timezone=True), server_default=func.now())
    activity = Column(String(32))
    referenced_user_id = Column(Integer, ForeignKey('users.id'))
    referenced_task_to_do_id = Column(Integer)
    referenced_task_checklist_id = Column(
        Integer, ForeignKey('task_checklists.id'))
    previous_title = Column(String(256))
    new_title = Column(String(256))
    previous_template_status = Column(String(32))
    new_template_status = Column(String(32))
    priority = Column(String(32))
    referenced_task_message_id = Column(
        Integer, ForeignKey('task_messages.id'))

    tasks = relationship('Tasks', back_populates='task_activities')

    def __repr__(self):
        return f"<TaskActivities {self.activity}>"


class TaskAttachments(db.Model):
    __tablename__ = 'task_attachments'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    task_id = Column(Integer, ForeignKey('tasks.id'))
    uploaded_by_user_id = Column(Integer)
    attachment_link = Column(String(256))
    task_message_id = Column(Integer)
    size = Column(Integer)
    uploaded_ts = Column(DateTime(timezone=True), server_default=func.now())

    tasks = relationship('Tasks', back_populates='task_attachments')

    def __repr__(self):
        return f"<TaskAttachments {self.attachment_link}>"


class TaskChecklistItems(db.Model):
    __tablename__ = 'task_checklist_items'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    description = Column(String(1024))
    assigned_user_id = Column(Integer)
    is_completed = Column(Boolean)
    task_checklist_id = Column(Integer, ForeignKey('task_checklists.id'))

    task_checklists = relationship(
        'TaskChecklists', back_populates='task_checklist_items')

    def __repr__(self):
        return f"<TaskChecklistItems {self.description}>"


class TaskChecklists(db.Model):
    __tablename__ = "task_checklists"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    title = Column(String(256))

    tasks = relationship("Tasks", back_populates="task_checklists")
    task_checklist_items = relationship(
        "TaskChecklistItems", back_populates="task_checklists")

    def __repr__(self):
        return f"<TaskChecklists {self.title}>"


class TaskMessages(db.Model):
    __tablename__ = 'task_messages'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    task_id = Column(Integer, ForeignKey(
        'tasks.id', ondelete='NO ACTION', onupdate='NO ACTION'))
    user_id = Column(Integer)
    task_message = Column(String)
    created_ts = Column(DateTime(timezone=True), server_default=func.now())
    reply_to_task_message_id = Column(Integer, ForeignKey(
        'task_messages.id', ondelete='NO ACTION', onupdate='NO ACTION'))
    tasks = relationship('Tasks', back_populates='task_messages')

    def __repr__(self):
        return f"<TaskMessages {self.task_message}>"


class TaskStageTemplates(db.Model):
    __tablename__ = "task_stage_templates"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(64))
    is_default = Column(Boolean, default=False)
    created_ts = Column(DateTime(timezone=True), server_default=func.now())
    updated_ts = Column(DateTime(timezone=True), onupdate=func.now())
    project_status_templates = relationship(
        "ProjectStatusTemplates", back_populates="task_stage_templates")
    template_stages = relationship(
        "TemplateStages", back_populates="task_stage_templates")

    def __repr__(self):
        return f"<TaskStageTemplates {self.title}>"


class TaskTags(db.Model):
    __tablename__ = 'task_tags'

    id = Column(Integer, primary_key=True, autoincrement=True)
    task_id = Column(Integer, ForeignKey('tasks.id'))
    tag_id = Column(Integer, ForeignKey('tags.id'))

    tags = relationship('Tags', back_populates='task_tags')
    tasks = relationship('Tasks', back_populates='task_tags')

    def __repr__(self):
        return f"<TaskTags {self.task_id, self.tag_id}>"


class Tasks(db.Model):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(256), nullable=False)
    description = Column(String(2048))
    project_task_list_id = Column(Integer, ForeignKey(
        'project_task_lists.id'), nullable=False)
    template_status_id = Column(Integer, ForeignKey(
        'template_stages.id'), nullable=False)
    due_date = Column(DateTime)
    created_by_user_id = Column(Integer, nullable=False)
    priority_id = Column(Integer, ForeignKey('priorities.id'), nullable=False)
    created_ts = Column(DateTime(timezone=True), server_default=func.now())
    updated_ts = Column(DateTime(timezone=True), onupdate=func.now())
    assignee_user_ids = Column(JSON)
    watcher_user_ids = Column(JSON)
    parent_task_id = Column(Integer)
    is_subtask = Column(Boolean, default=False)

    task_activities = relationship('TaskActivities', back_populates='tasks')
    task_attachments = relationship('TaskAttachments', back_populates='tasks')
    task_checklists = relationship('TaskChecklists', back_populates='tasks')
    task_messages = relationship('TaskMessages', back_populates='tasks')
    task_tags = relationship('TaskTags', back_populates='tasks')
    priorities = relationship('Priorities', back_populates='tasks')
    project_task_lists = relationship(
        'ProjectTaskLists', back_populates='tasks')
    template_stages = relationship('TemplateStages', back_populates='tasks')
    tasks_custom_fields = relationship(
        'TasksCustomFields', back_populates='tasks')

    def __repr__(self):
        return f"<Tasks {self.description}>"


class TasksCustomFields(db.Model):
    __tablename__ = 'tasks_custom_fields'

    id = Column(Integer, primary_key=True, autoincrement=True)
    task_id = Column(Integer, ForeignKey(
        'tasks.id', ondelete='CASCADE', onupdate='NO ACTION'))
    custom_field_id = Column(Integer, ForeignKey(
        'custom_fields.id', ondelete='SET NULL', onupdate='SET NULL'))
    custom_field_value = Column(JSON)
    created_ts = Column(DateTime(timezone=True), server_default=func.now())
    updated_ts = Column(DateTime(timezone=True), onupdate=func.now())

    custom_fields = relationship(
        'CustomFields', back_populates='tasks_custom_fields')
    tasks = relationship('Tasks', back_populates='tasks_custom_fields')

    def __repr__(self):
        return f"<TasksCustomFields {self.task_id, self.custom_field_id}>"


class TeamMembers(db.Model):
    __tablename__ = "team_members"

    id = Column(Integer, primary_key=True, autoincrement=True)
    team_id = Column(Integer, ForeignKey("teams.id", ondelete="CASCADE"))
    user_id = Column(Integer, nullable=False)
    role_id = Column(Integer, nullable=False)
    added_ts = Column(DateTime(timezone=True),
                      nullable=False, server_default=func.now())
    updated_ts = Column(DateTime(timezone=True),
                        nullable=False, onupdate=func.now())
    teams = relationship("Teams", back_populates="team_members")

    def __repr__(self):
        return f"<TeamMembers {self.team_id, self.role_id}>"


class Teams(db.Model):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    created_by_user_id = Column(Integer)
    owner_user_id = Column(Integer)
    admin_user_id = Column(Integer)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now())
    project_teams = relationship("ProjectTeams", back_populates="teams")
    team_members = relationship("TeamMembers", back_populates="teams")

    def __repr__(self):
        return f"<Teams {self.title}>"


class TemplateStages(db.Model):
    __tablename__ = "template_stages"
    id = Column(Integer, primary_key=True, index=True)
    template_id = Column(Integer, ForeignKey("task_stage_templates.id"))
    title = Column(String(64))
    color = Column(String(32))
    is_completed = Column(Boolean)
    tasks = relationship("Tasks", back_populates="template_stages")
    task_stage_templates = relationship(
        "TaskStageTemplates", back_populates="template_stages")

    def __repr__(self):
        return f"<TemplateStages {self.title}>"

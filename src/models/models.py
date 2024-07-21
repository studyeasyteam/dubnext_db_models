from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Workspace(Base):
    __tablename__ = "workspaces"

    workspace_id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    owner = Column(String, nullable=False)
    projects = relationship("Project", back_populates="workspace")
    folders = relationship("Folder", back_populates="workspace")
    project_videos = relationship("Project_Videos", back_populates="workspace")

class Project(Base):
    __tablename__ = "projects"

    project_id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    workspace_id = Column(UUID(as_uuid=True), ForeignKey("workspaces.workspace_id"))
    workspace = relationship("Workspace", back_populates="projects")
    folders = relationship("Folder", back_populates="project")
    project_videos = relationship("Project_Videos", back_populates="project")

class Folder(Base):
    __tablename__ = "folders"

    folder_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    path = Column(String)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.project_id"))
    project = relationship("Project", back_populates="folders")
    workspace_id = Column(UUID(as_uuid=True), ForeignKey("workspaces.workspace_id"))
    workspace = relationship("Workspace", back_populates="folders")
    project_videos = relationship("Project_Videos", back_populates="folder")

class Project_Videos(Base):
    __tablename__ = "project_videos"

    file_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    file_name = Column(String)
    file_type = Column(String)
    file_size_bytes = Column(Integer)
    path = Column(String)
    folder_id = Column(Integer, ForeignKey("folders.folder_id"))
    folder = relationship("Folder", back_populates="project_videos")
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.project_id"))
    project = relationship("Project", back_populates="project_videos")
    workspace_id = Column(UUID(as_uuid=True), ForeignKey("workspaces.workspace_id"))
    workspace = relationship("Workspace", back_populates="project_videos")

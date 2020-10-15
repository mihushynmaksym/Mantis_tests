from model.project import Project
import random


def test_pass(app, db):
    if len(db.get_project_list()) == 0:
        app.project.create(Project(name="name_param",
                                   description="description_param"))
    old_project = db.get_project_list()
    project = random.choice(old_project)
    app.project.delete_project_by_id(project.id)
    new_project = db.get_project_list()
    old_project.remove(project)
    assert sorted(old_project, key=Project.id_or_max) == sorted(new_project, key=Project.id_or_max)
from model.project import Project


def test_add_project(app, db, json_project):
    projects = json_project
    old_project = db.get_project_list()
    app.project.create(projects)
    new_project = db.get_project_list()
    old_project.append(projects)
    assert sorted(old_project, key=Project.id_or_max) == sorted(new_project, key=Project.id_or_max)

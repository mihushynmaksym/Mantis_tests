from model.project import Project


def test_add_project(app, db, json_project):
    db.clear_project_list()  # preconditions for unics params for projects name/description
    projects = json_project
    old_project = app.soap.take_array_project('administrator', 'root')
    app.project.create(projects)
    new_project = app.soap.take_array_project('administrator', 'root')
    old_project.append(projects)
    assert sorted(old_project, key=Project.id_or_max) == sorted(new_project, key=Project.id_or_max)

from flask import ( render_template, redirect,
                   url_for, request)

from models import db, Projects, app
from datetime import datetime





@app.route('/')
def index():
    projects = Projects.query.all()
    return render_template('index.html', projects=projects)


@app.route('/projects/new', methods=['GET', 'POST'])
def create_project():
    if request.form:
        comp_date_str = request.form['date']

        try:
            comp_date = datetime.strptime(comp_date_str, '%Y-%m')
        except ValueError:
            return 'Invalid date format. Please use YYYY-MM.'

        new_project = Projects(title=request.form['title'],
                               comp_date=comp_date,
                               desc=request.form['desc'],
                               skills=request.form['skills'],
                               git_url=request.form['github']
                               )
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html')


@app.route('/projects/<id>/edit', methods=['GET', 'POST'])
def edit_project(id):
    project = Projects.query.get(id)
    if request.form:
        comp_date_str = request.form['date']

        try:
            comp_date = datetime.strptime(comp_date_str, '%Y-%m')
        except ValueError:
            return 'Invalid date format. Please use YYYY-MM.'
        project.title = request.form['title']
        project.comp_date = comp_date
        project.desc = request.form['desc']
        project.skills = request.form['skills']
        project.git_url = request.form['github']
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('editform.html', project=project)


@app.route('/projects/<id>/delete')
def delete_project(id):
    project = Projects.query.get(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/projects/<id>')
def detail_project(id):
    project = Projects.query.get(id)
    return render_template('detail.html', project=project)

@app.route('/about')
def about():
    return render_template('about.html')


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', msg=error), 404

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')

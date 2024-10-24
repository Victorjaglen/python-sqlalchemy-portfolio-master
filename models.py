from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)


class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column('Created', db.DateTime, default=datetime.datetime.now)
    title = db.Column('Title', db.String())
    comp_date = db.Column('Date', db.DateTime)
    desc = db.Column('Description', db.String())
    skills = db.Column('Skills', db.String())
    git_url = db.Column('Git_URL', db.String())

    def __repr__(self):
        return f'''
                <Project (Title: {self.title}
                Completion Date: {self.comp_date})
                Description: {self.desc}
                Skills: {self.skills}
                Git url: {self.git_url}
            '''
        


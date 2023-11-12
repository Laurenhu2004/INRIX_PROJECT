from flask import Flask
from flask import Flask, redirect, url_for, render_template, request, session, abort


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'alks;hf;khj'

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app
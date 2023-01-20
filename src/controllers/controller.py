from flask.views import MethodView
from flask import request, render_template, redirect
from src.db import pymysql


class IndexController(MethodView):
    def get(self):
        return 'Olá Mundo' 


    def post(self):

        code = request.form['code']
        name = request.form['name']
        stock = request.form['stock']
        value = request.form['value']
        category = request.form['category']




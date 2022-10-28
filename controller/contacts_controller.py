from flask import render_template, request, redirect
from main import app
from model import contacts

@app.route("/contatos")
def list_contatos():
    return render_template('contacts/list.html', contacts = contacts.all())

@app.route("/contatos/add", methods=['GET', 'POST'])
def add():
    if request.method == "GET":
        return render_template('contacts/add.html')
    elif request.method == "POST":
        contacts.add(**request.form)
        return redirect('/contatos')


@app.route("/contatos/edit/<id>", methods=['GET'])
def edit(id):
    if request.method == "GET":
        return render_template('/contacts/edit.html', contact = contacts.get_by_id(id))
    

@app.route("/contatos/edit", methods=['POST'])
def update():
    if request.method == "POST":
        contacts.update(**request.form)
        return redirect('/contatos')

@app.route("/contatos/delete/<id>", methods=['GET'])
def delete(id):
    contacts.delete(id)
    return redirect("/contatos")


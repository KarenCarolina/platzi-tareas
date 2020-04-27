from flask import( Flask,
	render_template,
	request, 
	make_response,
	redirect,
	url_for ) 
from tarea_funciones import *  
app=Flask(__name__)  

@app.route("/",methods=["GET","POST"])
def index():
	l=listar_tareas() 
	context={
		"tareas":l, 
	} 
	return(render_template("index.html",**context))


@app.route("/add_task")
def add_task():
	descripcion = request.args.get("descripcion")
	anadir_tareas(descripcion)
	return redirect(url_for("index"))


@app.route("/edit_task")
def edit_task():
	uid = request.args.get("edit-task")
	print("UID"+uid)
	nueva_tarea = request.args.get("nueva-tarea")
	editar_tareas(nueva_tarea,uid)
	return redirect(url_for("index"))


@app.route("/delete_task")
def delete_task(): 
	uid=request.args.get("delete-task")
	borrar_tareas(uid)
	return redirect(url_for("index"))


if __name__ == '__main__':
	app.run(debug=True)


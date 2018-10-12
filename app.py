from flask import Flask, render_template, request, redirect
from main_code import TestClassName
import main_code as mc

app = Flask(__name__)
app.debug = True



@app.route("/",methods=['GET','POST'])
def main():
	tool = TestClassName()
	tool_return = tool.start_process()
	if request.method == 'POST': #collecting all the values of features coming from form to vairables
		Feathers = request.form['Feathers']
		Eggs = request.form['Eggs']
		Milk = request.form['Milk']
		Airborne = request.form['Airborne']
		Aquatic = request.form['Aquatic']
		Predator = request.form['Predator']
		Toothed = request.form['Toothed']
		Backbone = request.form['Backbone']
		Venomous = request.form['Venomous']
		Legs = request.form['Legs']
		Tail = request.form['Tail']
		Check_Label = request.form['Category']

		name,accuracy,check_accuracy,check_label = mc.main_start(str(Feathers),str(Eggs),str(Milk),str(Airborne),str(Aquatic),str(Predator),str(Toothed),str(Backbone),str(Venomous),str(Legs),str(Tail),str(Check_Label))
		return render_template('index.html',tool_return = tool_return,name = name,accuracy = accuracy,check_accuracy = check_accuracy,check_label=check_label)



	return render_template('index.html', tool_return = tool_return)
	

if __name__ == "__main__":
    app.run(host='0.0.0.0',  threaded=True)
    #app.run()

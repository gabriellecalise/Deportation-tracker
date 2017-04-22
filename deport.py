#import flask and makes the templates
from flask import Flask, render_template, redirect, url_for
#import your python dict using the variable you made in deportlist.py
from statelist import STATES
app = Flask(__name__)

#you have to add this for the web hosting
application = app



#this retrieves the ids AND the states from the data and adds it to the list
def get_ids_and_states(source):
    ids_and_states = []
    for row in source:
        id = row["id"]
        state = row["state"]
        ids_and_states.append( [id, state] )
            #RETURN LINE HAS TO BE TABBED JUST RIGHT. IF IT ISNT INDENTED, THE LOOP WILL NOT WORK. THIS ONE NEEDS TO BE PARALLEL TO THE FOR ROW IN SOURCE LINE
    return ids_and_states

def get_state(source, id):
    for row in source:
        if id == str(row["id"]):
            state = row["state"]
            total_deport = row["total_deport"]
            map = row["map"]
            not_convicted = row["not_convicted"]
            top_reasons = row["top_reasons"]
            id = str(id)
            #RETURN LINE HAS TO BE TABBED JUST RIGHT. IF IT ISNT INDENTED, THE LOOP WILL NOT WORK. THIS ONE HAS TO BE PARALLEL TO THE ID=STR(ID). I DONT KNOW WHY BUT IT JUST WORKS
            return id, state, total_deport, map, not_convicted, top_reasons


#this is the route for the homepage of the site
@app.route('/')
@app.route('/index/')
def index():
    ids_and_states = get_ids_and_states(STATES)
    return render_template('index.html', pairs=ids_and_states)

#route for the detail page for each state
@app.route('/state/<id>.html/')
def state(id):
    id, state, total_deport, map, not_convicted, top_reasons = get_state(STATES, id)
    return render_template('states.html', state=state, total_deport=total_deport, map=map, not_convicted=not_convicted, top_reasons=top_reasons)


#run in debug mode
if __name__ == '__main__':
    app.run(debug=True)

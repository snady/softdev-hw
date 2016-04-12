from flask import Flask, render_template, session, request
from flask import redirect, url_for
from datetime import datetime
import mongoutils
import json
import authy
import diag

app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
@app.route("/login", methods = ['GET','POST'])
@diag.timer
@diag.logger
def login():
        all_rows = mongoutils.getAllUsers()
        for n in range(len(all_rows)):
                all_rows[n] = all_rows[n]['name']
        if request.method == 'POST':
                error = ""
                if request.form['location'] != '':
                    session['lati'] = json.loads(request.form['location'])['latitude']
                    session['longi'] = json.loads(request.form['location'])['longitude']
                if request.form.has_key('login'):
                        user = str(request.form['user'])
                        password = str(request.form['pass'])
                        if mongoutils.authenticate(user,password):
                                session['user'] = user
                                return redirect("/home")
                        else:
                                error = "Incorrect Username or Password. Try Again."
                                return render_template("index.html",error=error)            
                if request.form.has_key('register'):
                        user = str(request.form['reguser'])
                        password = str(request.form['regpass'])
                        email = str(request.form['email'])
                        if user in all_rows:
                                error = "Username already exists. Please try another"
                                return render_template("index.html",regerror=error)
                        else:
                                message = "Account Created!"
                                mongoutils.addUser(user,password,email)
                                session['user'] = user
                                return redirect("/home")
        return render_template("index.html") #login failed

@app.route('/like')
@diag.timer
@diag.logger
def like():
        if 'idu' not in request.args:
                return 'illegal access'
        idu = request.args.get('idu',0,type = int)
        idp = request.args.get('idp',0,type = int)
        likes = {}
        likes['likes'] = len(mongoutils.likePost(idu,idp))
        return json.dumps(likes)

@app.route('/see')
@diag.timer
@diag.logger
def see():
        if 'idp' not in request.args:
                return 'illegal access'
        idp = request.args.get('idp',0,type = int)
        likes = {}
        likes['people']=[]
        for i in mongoutils.getPost(idp)['likes']:
                likes['people'].append([i,mongoutils.getUserName(i)['name']])
        return json.dumps(likes)

@app.route("/makepost", methods = ['GET','POST'])
@diag.timer
@diag.logger
def makepost():
        if 'user' not in session:
                return redirect ("/login")
	if 'search' in request.args:
		return redirect(url_for("showposts", query = request.args['query'], search = request.args['search']))
        if request.method == 'POST':
                name = request.form['name']
                desc = request.form['description']
                img = request.form['path']
                if request.form['restid'] != '':
                        rest = request.form['restid']
                else:
                        rest = request.form['rest']
                price = request.form['price']
                tags = request.form['tags']
                user = session['user']
                idu = mongoutils.getUserId(user)
                idp = mongoutils.writePost(img,tags,name,price,desc,idu,rest)
                
                return redirect(url_for('showpost',idp=idp))
        else:
                return render_template("writepost.html")

@app.route("/post/<int:idp>", methods = ['GET','POST'])
@diag.timer
@diag.logger
def showpost(idp):
        if 'user' not in session:
                return redirect("/login")
	if 'search' in request.args:
		return redirect(url_for("showposts", query = request.args['query'], search = request.args['search']))
        if request.method == 'POST':
                if 'remove' in request.form:
                        mongoutils.removePost(idp)
                        return redirect(url_for('showposts'))
                elif 'removec' in request.form:
                        mongoutils.removeComment(int(request.form['removec']))
                else:
                        content = request.form['texty']
                        mongoutils.addComment(mongoutils.getUserId(session['user']),idp,content,datetime.now())
        posty = mongoutils.getPost(idp)
	if 'error' in posty:
		return render_template("post.html",posty=posty)
        posty['uname'] = mongoutils.getUserName(posty['uid'])
        commy = mongoutils.getComments(idp)
        uid = mongoutils.getUserId(session['user'])
        return render_template("post.html",posty=posty,commy=commy,uid=uid)


#shows newest limi number of posts
@app.route("/posts/", methods = ['GET', 'POST'])
@app.route("/posts/<int:limi>", methods = ['GET', 'POST'])
@diag.timer
@diag.logger
def showposts(limi=30):
        display_msg  = ""
        if 'user' not in session:
                return redirect("/login")
        if 'search' in request.args:
                posts = mongoutils.search(request.args['query'])
                display_msg = "Search for %s" % (request.args['query'])
        else:
                posts = mongoutils.getAllPosts()[::-1]
                display_msg = "Browse"
        for post in posts:
            post['restaurant'] = mongoutils.getRestaurantName(post['yelpid'])
        
        return render_template("posts.html",posts=posts,display_msg=display_msg)

@app.route("/restaurant/<yelpid>", methods = ['GET'])
@diag.timer
@diag.logger
def restaurant(yelpid):
    error = ""
    restaurant = []
    if 'user' not in session:
        return redirect("/login")
    if 'search' in request.args:
	return redirect(url_for("showposts", query = request.args['query'], search = request.args['search']))
    if mongoutils.getRestaurant(yelpid) == None:
        return render_template("restaurant.html",error="Restaurant does not exist or not registered on Yelp",restaurant=restaurant)
    else:
        restaurant = mongoutils.getRestaurant(yelpid)
        rposts = mongoutils.getRestaurantPosts(yelpid)[::-1]
        return render_template("restaurant.html",error="", restaurant=restaurant,rposts=rposts)


@app.route("/user/<int:idu>")
@diag.timer
@diag.logger
def user(idu):
        if 'user' not in session:
                return redirect("/login")
	if 'search' in request.args:
		return redirect(url_for("showposts", query = request.args['query'], search = request.args['search']))
        userposts = mongoutils.getUserPosts(idu)[::-1]
        username = mongoutils.getUserName(idu)
        return render_template("user.html",posts=userposts,username=username)
        
@app.route("/logout")
@diag.timer
@diag.logger
def logout():
        del session['user']
        return redirect("/login")

@app.route("/home", methods = ['GET','POST'])
@diag.timer
@diag.logger
def home():
    if 'user' not in session:
                return redirect ("/login")
    if 'lati' not in session or 'longi' not in session:
            return render_template("home.html", user={'lat':0,'lng':0},json=[],rests=[],location='')
    if 'search' in request.args:
	    return redirect(url_for("showposts", query = request.args['query'], search = request.args['search']))
    lati = session['lati']
    longi = session['longi']
    jason = mongoutils.getNearbyPosts(lati,longi)
    location = mongoutils.getCityState(lati,longi)
    user = json.dumps({'lat':lati,'lng':longi})
    for post in jason:
        post['restaurant'] = mongoutils.getRestaurantName(post['yelpid'])
	post['coords'] = mongoutils.getRestaurantCoords(post['yelpid'])
    return render_template("home.html",user=user,json=jason,rests=jason,location=location)
 
    

@app.route("/autocomplete")
@diag.timer
@diag.logger
def autocomplete():
        if 'term' not in request.args:
                return 'illegal access'
	name = request.args.get('term')
    	location = mongoutils.getCityState(session['lati'],session['longi'])
        location = location.replace(',','')
    	dic = authy.search(name,location,7)
    	cleaned = []
    	for i in dic['businesses']:
        	a={}
        	a['id']=i['id']
        	a['label']=i['name']
        	a['address']=[i['location']['address'][0],i['location']['city'],i['location']['state_code'],i['location']['postal_code']]
        	cleaned.append(a)
	return json.dumps(cleaned)

@app.route("/about")
@diag.timer
@diag.logger
def about():
	if 'user' not in session:
                return redirect("/login")
	if 'search' in request.args:
		return redirect(url_for("showposts", query = request.args['query'], search = request.args['search']))
        return render_template("about.html")

if __name__ == '__main__':
        app.secret_key = "hello"
        app.debug = True
        app.threaded = True
        app.run(host='0.0.0.0', port=8000)
else:
        app.secret_key = "hello"
        app.debug = True
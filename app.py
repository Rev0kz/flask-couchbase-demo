from flask import Flask 
from couchbase import Couchbase 
client  = Couchbase.connect(host = "localhost", bucket = "Users-data")

@app.route('/home', method=['GET'])
def home_page()
  return render_template('home.html')

@app.route('/home/create-memo'), method=['POST'])
def create_memo():
  if method == POST:
     diary = {  
       "memo" : request.form["memo"],
       "year" : request.form["year"],
      "month" : request.form["month"],
      "day" :  request.form["day"]
   }
  Key=uuid.uuid1.hex()
  user_doc=json.dumps(diary)
  client.set(key, user_doc)
  return redirect(url_for("index")
return render_view("create.html")


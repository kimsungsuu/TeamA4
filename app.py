from flask import Flask, render_template, request, jsonify, redirect
app = Flask(__name__)

from bson.objectid import ObjectId

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.awfowzp.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')


@app.route("/api", methods=["GET"])
def movie_get():
   all_myself = list(db.myself.find({},{'_id':True, 'name':True, 'mbti':True, 'introduction':True, 
                                         'strengths':True, 'collaboration_style':True ,'blog_url':True}))
    
   for myself in all_myself:
        myself['_id'] = str(myself['_id'])
    
   return jsonify({'result':all_myself})

@app.route("/api/new", methods=["GET"])
def get_write():

   return render_template('write.html')

@app.route("/api/new", methods=["POST"])
def post_write():
    name_receive = request.form['name_give']
    mbti_receive = request.form['mbti_give']
    introduction_receive = request.form['introduction_give']
    strengths_receive = request.form['strengths_give']
    collaboration_style_receive = request.form['collaboration-style_give']
    blog_url_receive = request.form['blog-url_give']
    
    doc = {
       'name' : name_receive,
       'mbti' : mbti_receive,
       'introduction' : introduction_receive,
       'strengths' : strengths_receive,
       'collaboration_style' : collaboration_style_receive,
       'blog_url' : blog_url_receive,
    }
    
    db.myself.insert_one(doc)

    return redirect('/')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
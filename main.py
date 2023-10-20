from flask import Flask, jsonify
import pandas as pd

articles_data = pd.read_csv('articles.csv')

app = Flask(__name__)

# extracting important information from dataframe
all_articles = articles_data[["url" , "title", "text" , "lang" , "total_events"]]

# variables to store data
likedarticles = []
dislikedarticles= []


# method to fetch data from database
def assignval():
  mdata = {
      "url": all_articles.iloc[0,0],
      "title":  all_articles.iloc[0,1],
      "text" : all_articles.iloc[0,2] or "n/a",
      "lang" :  all_articles.iloc[0,3],
      "total_events" :  all_articles.iloc[0,4]/2
  }
  return mdata 


# /articles api
@app.route("/articles")
def getarticles():
  articledata = assignval()
  return jsonify({
      "data":articledata,
      "status": "success"
  })

# /like api
@app.route("/like",methods = ["POST"])
def likedarticle():
  global all_articles
  articledata = assignval()
  likedarticles.append(articledata)
  all_articles.drop([0],inplace = True)
  all_articles = all_articles.reset_index(drop = True)
  return jsonify({
      "status":"success"
  })

# /dislike api
@app.route("/dislike",methods = ["POST"])
def dislikedarticle():
  global all_articles
  articledata = assignval()
  dislikedarticles.append(articledata)
  all_articles.drop([0],inplace = True)
  all_articles = all_articles.reset_index(drop = True)
  return jsonify({
      "status":"success"
  })


if __name__ == "__main__":
  app.run()
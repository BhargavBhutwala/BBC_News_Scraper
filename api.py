from flask import Flask, jsonify, request
from db import get_articles, delete_articles
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/articles', methods = ['GET'])
def get_all_articles():

   """Return all articles from the database with pagination support."""
   print("Received request for articles")
   page = int(request.args.get('page', 1))
   limit = int(request.args.get('limit', 10))

   articles = get_articles(page=page, limit=limit)

   return jsonify(articles)

@app.route('/articles/category/<category>', methods = ['GET'])
def get_articles_by_category(category):

   """Return articles from a specific category from the database."""
   page = int(request.args.get('page', 1))
   limit = int(request.args.get('limit', 10))

   articles = get_articles(where_clause="category = %s", params=(category,), page=page, limit=limit)

   return jsonify(articles)

@app.route('/articles/<int:article_id>', methods = ['DELETE'])
def delete_article(article_id):

   """Delete an article by its ID from the database."""
   delete_articles(article_id)

   return jsonify({"message": f"Article {article_id} deleted successfully"})
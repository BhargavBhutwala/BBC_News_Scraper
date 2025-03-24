import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG


# Create a database connection
def create_connection():
   try:
      connection = mysql.connector.connect(**DB_CONFIG)
      print("Connection to MySQL DB successful")
      return connection
   except Error as e:
      print("Error connecting to MySQL: ", e)
      return None
   

# Initialize database and create table articles if necessary
def init_db():

   connection = create_connection()

   if connection:
      cursor = connection.cursor()

      create_table_query = '''
      create table if not exists articles(
         id int auto_increment primary key,
         title text,
         summary text,
         url text,
         publication_date text,
         category text,
         unique(title(255), url(255))
      )
      '''

      cursor.execute(create_table_query)
      connection.commit()
      cursor.close()
      connection.close()

# Insert the article into the database
def insert_article(article):

   """Insert an article into the database, ignoring duplicates."""

   connection = create_connection()

   if connection:
      cursor = connection.cursor()

      insert_query = '''
         insert ignore into articles (title, summary, url, publication_date, category) values(%s, %s, %s, %s, %s)
      '''

      data = (
         article.get('title'),
         article.get('summary'),
         article.get('url'),
         article.get('publication_date'),
         article.get('category', 'BBC News')
      )

      try:
         cursor.execute(insert_query, data)
         connection.commit()
      except Error as e:
         print("Error inserting article: ", e)
      finally:
         cursor.close()
         connection.close()

# Get articles from database
def get_articles(where_clause='', params=(), page=1, limit=10):

   """Retrieve articles from the database with optional filtering and pagination."""

   offset = (page - 1) * limit

   connection = create_connection()

   if connection:
      cursor = connection.cursor()

      query = "select * from articles"
      if where_clause:
         query += " where " + where_clause
      query += " limit %s offset %s"

      try:
         cursor.execute(query, params + (limit, offset))
         rows = cursor.fetchall()
         return rows
      except Error as e:
         print("Error retrieving articles: ", e)
         return []
      finally:
         cursor.close()
         connection.close()

# Delete articles from database
def delete_articles(article_id):

   """Delete an article by its ID."""

   connection = create_connection()

   if connection:
      cursor = connection.cursor()

      delete_query = "delete from articles where id = %s"

      try:
         cursor.execute(delete_query, (article_id,))
         connection.commit()
      except Error as e:
         print("Error deleting article: ", e)
      finally:
         cursor.close()
         connection.close()

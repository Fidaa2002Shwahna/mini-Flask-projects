from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = pymysql.connect(
            host='sql12.freesqldatabase.com',
            database='sql12651524',
            user='sql12651524',
            password='DislAzX9fi',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor  
        )
    except pymysql.Error as e:
        print(e)
    return conn

@app.route('/books', methods=['GET', 'POST'])
def manage_books():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute('SELECT * FROM book')
        books = [dict(id=row['id'], author=row['author'], language=row['language'], title=row['title']) for row in cursor.fetchall()]
        conn.close()
        return jsonify(books)

    if request.method == 'POST':
        new_author = request.form['author']
        new_language = request.form['language']
        new_title = request.form['title']

        cursor.execute('INSERT INTO book (author, language, title) VALUES (%s, %s, %s)',
                       (new_author, new_language, new_title))
        conn.commit()
        conn.close()
        return jsonify({"message": "Book added successfully"}), 201

@app.route('/books/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_book(id):
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute('SELECT * FROM book WHERE id = %s', (id,))
        book = cursor.fetchone()
        if book:
            book_dict = {
                "id": book['id'],
                "author": book['author'],
                "language": book['language'],
                "title": book['title']
            }
            conn.close()
            return jsonify(book_dict)
        else:
            return jsonify({"message": "Book not found"}), 404

    if request.method == 'PUT':
        updated_author = request.form['author']
        updated_language = request.form['language']
        updated_title = request.form['title']

        cursor.execute('UPDATE book SET author=%s, language=%s, title=%s WHERE id=%s',
                       (updated_author, updated_language, updated_title, id))
        conn.commit()
        conn.close()
        return jsonify({"message": "Book updated successfully"})

    if request.method == 'DELETE':
        cursor.execute('DELETE FROM book WHERE id = %s', (id,))
        conn.commit()
        conn.close()
        return '', 204

if __name__ == "__main__":
    app.run(port=9001)

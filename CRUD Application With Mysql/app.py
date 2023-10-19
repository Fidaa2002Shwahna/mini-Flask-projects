from flask import Flask, request, render_template, flash, redirect, url_for
import mysql.connector

app = Flask(__name__)
app.secret_key = "a41171519374c423c9a8197c72ac2cff"

# Establish the database connection
db_connection = mysql.connector.connect(
    user='root',
    password='',  # Add your database password here
    host='localhost',
    database='students'
)


@app.route('/')
def index():
    cursor = db_connection.cursor()

    try:
        # Define the SQL query and execute it
        sql = "SELECT * FROM student"
        cursor.execute(sql)
        students = cursor.fetchall()  # Fetch all rows
        return render_template("index.html", students=students)
    except Exception as e:
        flash("Error: " + str(e))
    finally:
        cursor.close()
    return render_template("index.html", students=[])


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        flash("Data entered successfully")
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        # Create a cursor for database operations
        cursor = db_connection.cursor()

        try:
            # Define the SQL query and execute it
            sql = "INSERT INTO student (name, email, phone) VALUES (%s, %s, %s)"
            values = (name, email, phone)
            cursor.execute(sql, values)
            db_connection.commit()
        except Exception as e:
            flash("Error: " + str(e))
            db_connection.rollback()
        finally:
            cursor.close()
    return redirect(url_for('index'))


@app.route('/delete/<string:id_data>', methods=['GET'])
def delete(id_data):
    cursor = db_connection.cursor()

    try:
        # Define the SQL query and execute it
        sql = "DELETE FROM student WHERE id = %s"
        cursor.execute(sql, (id_data,))
        db_connection.commit()
        flash("Data deleted successfully")
    except Exception as e:
        flash("Error: " + str(e))
        db_connection.rollback()
    finally:
        cursor.close()

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True, port=5004)

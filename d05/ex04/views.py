import psycopg2

from django.shortcuts import render
from django.http import HttpResponse
from django.forms import Form

# Create your views here.

def drop_table(connection, tablename):
    curr = connection.cursor()
    print("""DROP TABLE %s""" % tablename)
    curr.execute("""DROP TABLE %s CASCADE""" % tablename)
    connection.commit()

def create_table(connection, tablename, content):
    sql_string = "(\n"
    i = 0
    curr = connection.cursor()
    for key, value in content.items():
        i += 1
        if i < len(content):
            sql_string += "    %s %s,\n" % (key, value)
        else:
            sql_string += "    %s %s\n" % (key, value)
    sql_string += ")"
    curr.execute("""CREATE TABLE %s %s""" % (tablename, sql_string))
    connection.commit()
    return connection


def remove_row(connection, tablename, key, value):
    sql_string = ''
    curr = connection.cursor()
    curr.execute(f"DELETE FROM {tablename} WHERE {tablename}.{key}='{value}';")
    connection.commit()
    return connection

def populate(request):
    buf = ""
    data = [
        {
            'title': "The Phantom Menace",
            'episode_nb': 1,
            'opening_crawl': "",
            'director': "George Lucas",
            'producer': "Rick McCallum",
            'release_date': "1999-05-19"
        },
        {
            'title': "Attack of the Clones",
            'episode_nb': 2,
            'opening_crawl': "",
            'director': "George Lucas",
            'producer': "Rick McCallum",
            'release_date': "2005-05-16"
        },
        {
            'title': "Revenge of the Sith",
            'episode_nb': 3,
            'opening_crawl': None,
            'director': "George Lucas",
            'producer': "Rick McCallum",
            'release_date': "2005-05-19"
        },
        {
            'title': "A New Hope",
            'episode_nb': 4,
            'opening_crawl': None,
            'director': "George Lucas",
            'producer': "Gary Kurtz, Rick McCallum",
            'release_date': "1999-05-19"
        },
        {
            'title': "The Empire Strikes Back",
            'episode_nb': 5,
            'opening_crawl': None,
            'director': "Irvin Kershner",
            'producer': "Gary Kutz, Rick McCallum",
            'release_date': "1980-05-17"
        },
        {
            'title': "Return of the Jedi",
            'episode_nb': 6,
            'opening_crawl': None,
            'director': "George Lucas",
            'producer': "Howard G. Kazanjian, George Lucas, Rick McCallum",
            'release_date': "1983-05-25"
        },
        {
            'title': "The Force Awakens",
            'episode_nb': 7,
            'opening_crawl': "",
            'director': "J. J. Abrams",
            'producer': "Kathleen Kennedy, J. J. Abrams, Bryan Burk",
            'release_date': "2015-12-11"
        },
    ]
    conn = psycopg2.connect(
            database='formationdjango',
            host='localhost',
            user='djangouser',
            password='secret'
        )
    cursor = conn.cursor()

    for movie in data:
        try:
            cursor.execute("""INSERT INTO ex02_movies 
            (title, episode_nb, opening_crawl,
             director, producer, release_date) 
            VALUES (%(title)s, %(episode_nb)s, %(opening_crawl)s, 
            %(director)s, %(producer)s, %(release_date)s)""", movie)
            conn.commit()
            buf += "OK<br>"
        except Exception as e:
            print(e)

            buf += "Error: %s :: %s<br>" % (movie['title'], e)
            conn.rollback()
    cursor.close()
    conn.close()
    return HttpResponse(buf)

def display(request):
    conn = psycopg2.connect(
            database='formationdjango',
            host='localhost',
            user='djangouser',
            password='secret'
        )
    curr = conn.cursor()
    try:
        curr.execute("""SELECT * from ex04_movies""")
    except Exception as e:
        print(e)
        return HttpResponse("No data available")
    response = curr.fetchall()
    
    curr.close()
    conn.close()
    if response:
        return render(request, 'ex04/display.html', {'data': response})
    else:
        return HttpResponse("No data available")

def init(request):
    conn = psycopg2.connect(
            database='formationdjango',
            host='localhost',
            user='djangouser',
            password='secret'
        )
    drop_table(conn,'ex04_movies')
    try:
        create_table(conn, 'ex04_movies', {
            'title': 'varchar(64) UNIQUE NOT NULL',
            'episode_nb': 'int PRIMARY KEY',
            'opening_crawl': 'text',
            'director': 'varchar(32) NOT NULL',
            'producer': 'varchar(128) NOT NULL',
            'release_date': 'date NOT NULL',
        })
        ret = "OK"
    except Exception as e:
        ret = str(e)
    conn.close()
    return HttpResponse(ret)

def remove(request):
    conn = psycopg2.connect(
        database='formationdjango',
        host='localhost',
        user='djangouser',
        password='secret'
    )

    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid() and request.POST['select']:
            remove_row(conn, 'ex04_movies', 'episode_nb', request.POST['select'])

    curr = conn.cursor()
    form = Form()
    try:
        curr.execute("""SELECT * from ex04_movies""")
    except Exception as e:
        return HttpResponse("No data available")
    response = curr.fetchall()
    curr.close()
    conn.close()
    if response:
        return render(request, 'ex04/remove.html', {'data': response, 'form': form})
    else:
        return HttpResponse("No data available")

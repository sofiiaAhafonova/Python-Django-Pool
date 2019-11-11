from django.shortcuts import render
import psycopg2
from django.http import HttpResponse
# Create your views here.
def init(request):
    try:
        conn = psycopg2.connect(
            database = 'formationdjango',
            host = '127.0.0.1',
            user = 'djangouser',
            password = 'secret'
            )
        
        cursor = conn.cursor()

        cursor.execute(""" CREATE TABLE IF NOT EXISTS ex02_movies (
            episode_nb serial PRIMARY KEY, 
            title varchar(64) NOT NULL,
            opening_crawl text,
            director varchar(32) NOT NULL,
            producer varchar(128) NOT NULL,
            release_date date NOT NULL
            )
            """)
        conn.commit()
    except psycopg2.Error as e:
        print('Error : ', e)
        retStr = 'Error :' + str(e)
        return HttpResponse(retStr)
    finally:
    #closing database connection.
        if(conn):
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")
    return HttpResponse('OK')

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
            buf += f"Error: {movie['title']} ::{e}<br>"
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
        curr.execute("""SELECT * from ex02_movies""")
    except Exception as e:
        return HttpResponse("No data available")
    response = curr.fetchall()
    conn.close()
    if response:
        return render(request, 'display.html', {'data': response})
    else:
        return HttpResponse("No data available")


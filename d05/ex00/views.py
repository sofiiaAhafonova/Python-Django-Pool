from django.shortcuts import render
import psycopg2
from contextlib import closing
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
		
		curr = conn.cursor()

		curr.execute(""" CREATE TABLE IF NOT EXISTS ex00_movies (
			episode_nb serial PRIMARY KEY, 
			title varchar(64) NOT NULL,
			opening_crawl text,
			director varchar(32) NOT NULL,
			producer varchar(128) NOT NULL,
			release_date date NOT NULL
			)
			""")
		conn.commit()
		conn.close()
	except psycopg2.Error as e:
		print('Error : ', e)
		retStr = 'Error :' + str(e)
		return HttpResponse(retStr)
	return HttpResponse('OK')
# django_Hello
practice the Django rest framework tutorial to build restful sever 

This code build a simple server that can receive 'hello World' information, 
also the server can add new information by 'POST' request. 
The 'hello World' information is saved in SQLite3 format, which is Django defaul database format.
It contains 7 fields, which is:

	id, it a auto-build data  
	name, the writer name
	title, the event title
	event, it is the content, required
	start_time, event start time, required
	end_time, event end time, required
	created, event created time, it records

To run the server, frist we should enter the server dir:
		
		$ cd django_Hello-master\test2

Second, run the server in port 3000:
		
		$ python manage.py runserver 3000
		
when the terminal displays the contents like:
		"Performing system checks...

		System check identified no issues (0 silenced).
		June 06, 2017 - 15:53:21
		Django version 1.11.1, using settings 'test1.settings'
		Starting development server at http://127.0.0.1:3000/
		Quit the server with CTRL-BREAK."
it means server start up successfully
Third, open another terminal, test the server using 'curl' or 'httpie',
I used 'httpie' to test the server, since it is more friendly for Windows
Then we can test:
	>http http://localhost:3000/helloworld/
	
	
	
	HTTP/1.0 200 OK
	Content-Length: 374
	Content-Type: application/json
	Date: Tue, 06 Jun 2017 20:00:03 GMT
	Server: WSGIServer/0.2 CPython/3.6.1
	X-Frame-Options: SAMEORIGIN
	[
		{
			"created": "2017-06-06T14:08:31.640525Z",
			"end_time": "2017-06-06T14:08:29Z",
			"event": "Hello World!",
			"id": 5,
			"name": "Yifan",
			"start_time": "2017-06-06T14:08:27Z",
			"title": "test3"
		}
	]
	
We also can use 'POST' request add new data, for example:

	>http POST http://localhost:3000/helloworld/ title=test1 name=Jiang end_time=2017-6-8T12:00:00Z event="hello again!" start_time=2017-8-8T13:00:00Z
	
	
	HTTP/1.0 201 Created
	Content-Length: 185
	Content-Type: application/json
	Date: Tue, 06 Jun 2017 19:34:17 GMT
	Server: WSGIServer/0.2 CPython/3.6.1
	X-Frame-Options: SAMEORIGIN

	{
		"created": "2017-06-06T19:34:16.962006Z",
		"end_time": "2017-06-08T12:00:00Z",
		"event": "hello again!",
		"id": 6,
		"name": "Jiang",
		"start_time": "2017-08-08T13:00:00Z",
		"title": "test1"
	}

	
Now we use 'GET' request, the result are:

>http http://localhost:3000/helloworld/

	HTTP/1.0 200 OK
	Content-Length: 374
	Content-Type: application/json
	Date: Tue, 06 Jun 2017 20:00:03 GMT
	Server: WSGIServer/0.2 CPython/3.6.1
	X-Frame-Options: SAMEORIGIN

	[
		{
			"created": "2017-06-06T14:08:31.640525Z",
			"end_time": "2017-06-06T14:08:29Z",
			"event": "Hello World!",
			"id": 5,
			"name": "Yifan",
			"start_time": "2017-06-06T14:08:27Z",
			"title": "test3"
		},
		{
			"created": "2017-06-06T19:34:16.962006Z",
			"end_time": "2017-06-08T12:00:00Z",
			"event": "hello again!",
			"id": 6,
			"name": "Jiang",
			"start_time": "2017-08-08T13:00:00Z",
			"title": "test1"
		}
	]

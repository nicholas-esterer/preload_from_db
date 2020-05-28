# Database loading on page reload with `dash`

When an app is run (e.g., `python app.py`) the website is served indefinitely.
In our case, when `app.py` starts up, it reads from a database to populate a
table with the values the database contains. When clients access the webapp
(e.g., from http://127.0.0.1:8000) they are served this initial version of the
webpage. That means if the database is updated by some external process after
`app.py` has been launched, clients will not be aware of the changes, and even
if a client presses "Refresh" in their browser, they will still only see the old
data.

This problem can be demonstrated by running

    python app.py

Then loading the page in a browser (at http://127.0.0.1:8000).
If you run

    python change_db.py

And then refresh the page, no change will be seen in the browser.

## The solution (at least for page refreshing)

You can run a server that dispatches workers to process each request from a
client. You can make it so that each worker only processes 1 request. This will
force a reloading of the entire application to process the request and repeating the demonstration above using the worker server will show that the database is updated correctly upon page reload.

To run a worker server, run

    gunicorn --max-requests 1 app:server

Then you can load the page and run `change_db.py` as above, and try refreshing:
the updates to the database should be displayed.

### Problems with this solution

It seems that the page load is noticeably slower when using the worker server
than the single server.

## Setting up

To run this example, first start a `virtualenv`

    virtualenv venv
    source venv/bin/activate

Then install the requirements

    pip install -r requirements.txt

Now you can run the above examples.


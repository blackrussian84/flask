# app.py
from flask import Flask, render_template, request

app = Flask(__name__)
post_counter = 0

@app.route('/health', methods=['GET'])
def health_check():
    """
    This endpoint returns a simple response indicating the health status of the application.
    """
    return 'OK', 200

@app.route('/', methods=['GET', 'POST'])
def counter():
    """
    This endpoint accepts both GET and POST requests.
    If the request method is POST, it increments the post_counter variable.
    Regardless of the request method, it renders the HTML template with the current post_counter value.
    """
    global post_counter
    if request.method == 'POST':
        post_counter += 1

    return render_template('index.html', post_counter=post_counter)

if __name__ == '__main__':
    # Run the application on port 80
    app.run(host='0.0.0.0', port=80 , debug=True )
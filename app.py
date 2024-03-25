from flask import Flask, request

app = Flask(__name__)
post_counter = 0

# Health check route
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
    Regardless of the request method, it returns a string indicating the number of POST requests served.
    """
    global post_counter
    if request.method == 'POST':
        post_counter += 1
    return '''
        <html>
            <head>
                <style>
                    body {{
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        font-family: Arial, sans-serif;
                        background-color: #F9A825;
                        animation: pulse 2s infinite;
                    }}
                    p {{
                        font-size: 24px;
                        text-align: center;
                        color: white;
                        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
                    }}
                    @keyframes pulse {{
                        0% {{ transform: scale(1); }}
                        50% {{ transform: scale(1.1); }}
                        100% {{ transform: scale(1); }}
                    }}
                </style>
                <meta http-equiv="refresh" content="5">
            </head>
            <body>
                <p>This server has served {} POST requests.</p>
            </body>
        </html>
    '''.format(post_counter)

if __name__ == '__main__':
    # Run the application on port 80
    app.run(host='0.0.0.0', port=7777)

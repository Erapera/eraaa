from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>Привет, жизнь!</title>
            <style>
                body {
                    background-color: #f2f2f2;
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding-top: 100px;
                }
                h1 {
                    color: #333;
                    font-size: 48px;
                }
                p {
                    color: #666;
                    font-size: 20px;
                }
            </style>
        </head>
        <body>
            <h1>Привет, жизнь! 🌍</h1>
            <p>Это мой первый сайт на FastAPI 🚀</p>
        </body>
    </html>
    """

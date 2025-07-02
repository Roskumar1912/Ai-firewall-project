from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    try:
        with open("blocked_ips.log", "r") as file:
            entries = file.readlines()
    except FileNotFoundError:
        entries = ["No blocked IPs yet."]

    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>🚨 AI Firewall Dashboard</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #121212;
                color: #f1f1f1;
                padding: 30px;
            }
            h1 {
                color: #ff4c4c;
                border-bottom: 2px solid #ff4c4c;
                padding-bottom: 10px;
            }
            ul {
                list-style: none;
                padding: 0;
            }
            li {
                background: #1e1e1e;
                margin: 10px 0;
                padding: 12px;
                border-left: 5px solid #ff4c4c;
                border-radius: 4px;
                font-size: 16px;
            }
            .footer {
                margin-top: 40px;
                font-size: 12px;
                color: #888;
            }
        </style>
    </head>
    <body>
        <h1>🛡️ Blocked IPs Log</h1>
        <ul>
            {% for line in entries %}
                <li>{{ line.strip() }}</li>
            {% endfor %}
        </ul>
        <div class="footer">© 2025 Roshan's AI Firewall</div>
    </body>
    </html>
    """
    return render_template_string(html, entries=entries)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

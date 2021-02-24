# pip install flask
# do following if you cant access from different computer on the network

# https://askubuntu.com/questions/224392/how-to-allow-remote-connections-to-flask
# sudo iptables -A INPUT -m state --state NEW -m tcp -p tcp --dport 5000 -j ACCEPT # 8553 in our example





from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_www():
    return "Hello World Wide Web!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 8553)




# https://askubuntu.com/questions/224392/how-to-allow-remote-connections-to-flask
# sudo iptables -A INPUT -m state --state NEW -m tcp -p tcp --dport 5000 -j ACCEPT

# Import thư viện chuẩn

# Import thư viện bên ngoài
from flask import Flask

# Import module, package trong project
from boitoan.route import boitoan

app = Flask(__name__)

# Register blueprint
app.register_blueprint(boitoan)


if __name__ == "__main__":
    # アプリ開始
    app.run(host="127.0.0.1", port=5000, debug=True)




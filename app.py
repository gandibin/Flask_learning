from flask import Flask

# 创建 Flask 应用
app = Flask(__name__)

# 定义一个路由，映射到根路径 '/'
@app.route('/')
def home():
    return "Hello, Flask!"

# 启动 Flask 应用
if __name__ == '__main__':
    app.run(debug=True)

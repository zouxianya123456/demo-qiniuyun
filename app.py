from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__)

# 确保static目录存在（用于存放后续可能添加的图片、CSS等静态文件）
if not os.path.exists('static'):
    os.makedirs('static')

# 主页面路由（访问网站根目录时触发）
@app.route('/')
def index():
    # 读取同目录下的index.html文件内容（相对路径，无需修改）
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    return render_template_string(html_content)

# 提供静态文件访问（如后续添加图片、CSS等，无需修改）
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)  # 启动本地服务器，默认地址：http://127.0.0.1:5000
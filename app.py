from flask import Flask, send_file
import os

app = Flask(__name__)

# Điền đúng tên file trong repo của bạn vào đây
FILENAME = "myfile.zip" 

@app.route('/')
def download_file():
    if os.path.exists(FILENAME):
        # as_attachment=True sẽ thêm header Content-Disposition: attachment
        # ép trình duyệt/terminal tải file về ngay lập tức
        return send_file(FILENAME, as_attachment=True)
    return "File not found", 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

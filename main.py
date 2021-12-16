from flask import Flask , request ,jsonify, render_template
import ddddocr

app = Flask(__name__)

@app.route('/api/img', methods=['POST'])
def api_img():
    print(request.files.get('img') , request.form.get('uuid'))
    if request.files.get('img') and request.form.get('uuid'):
        if request.form.get('uuid') != '666':
            return jsonify({'code':'404','message': '密码缺失'})
        response = request.files.get('img').read()
    else:
        return jsonify({'code':'404','message': '缺失参数'})
    ocr = ddddocr.DdddOcr()
    res = ocr.classification(response)
    return jsonify({'code':'200','res':res})

@app.route('/')
def index():
    return render_template('index.html')

app.debug = True
app.run()
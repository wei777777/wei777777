from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    user_response = request.form['response']
    
    # 根據使用者的回答進行條件判斷
    if user_response == 'yes':
        result = '恭喜郭小瑋獲得77公主的青睞 ~PS 不能反悔喔~'
    elif user_response == 'no':
        result = '請回到上一頁點選~是~'
    else:
        result = '請選擇一個答案！'

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

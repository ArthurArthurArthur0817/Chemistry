from flask import Flask, render_template, request, jsonify
import chemistry  # 假設 chemistry.py 處理化學模擬的邏輯
import rule  # 引入剛剛拆分出來的 rule.py

app = Flask(__name__)

# 路由1：首頁，顯示主畫面
@app.route('/')
def main_page():
    return render_template('index.html')

# 路由2：化學實驗教學頁面
@app.route('/chemistry')
def chemistry_page():
    return render_template('chemistry.html')

# 路由3：行為分類頁面
@app.route('/classification')
def classification():
    return render_template('rule.html')

# 路由4：其他頁面
@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/page3')
def page3():
    return render_template('page3.html')

# 化學模擬的 API，處理物質和指示劑
@app.route('/simulate', methods=['POST'])
def simulate():
    substance = request.form['substance']
    indicator = request.form['indicator']
    
    ph, color = chemistry.get_ph_and_color(substance, indicator)
    return jsonify({"ph": ph, "color": color})

# 行為分類的 API，接收前端的分類結果
@app.route('/submit', methods=['POST'])
def submit_classification():
    data = request.json
    safe = data.get('safe', [])
    danger = data.get('danger', [])

    # 使用 rule.py 中的函數來驗證分類正確性
    is_correct = rule.validate_classification(safe, danger)
    message = "分類完成！" if is_correct else "分類錯誤，請重新檢查！"
    
    return jsonify({"success": is_correct, "message": message})

if __name__ == '__main__':
    app.run(debug=True)

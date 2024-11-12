from flask import Flask, render_template, request, jsonify
import chemistry  # 假設 chemistry.py 處理化學模擬的邏輯
import gemini  # 新增 gemini.py 模組

app = Flask(__name__)

# 路由1：首頁，顯示主畫面
@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/chemistry')
def chemistry_page():
    return render_template('chemistry.html')


@app.route('/classification')
def classification():
    return render_template('rule.html')


@app.route('/teach')
def page2():
    return render_template('teach.html')

@app.route('/indicator')
def page3():
    return render_template('indicator.html')

@app.route('/pH')
def page4():
    return render_template('pH.html')

@app.route('/book')
def page5():
    return render_template('book.html')

# 化學模擬的 API，處理 pH 和指示劑
@app.route('/simulate', methods=['POST'])
def simulate():
    # 獲取 pH 和 indicator 值
    ph = float(request.form['ph'])  # 接收 pH 值，並轉換為浮點數
    indicator = request.form['indicator']
    
    # 根據 pH 和 indicator 獲取顏色
    ph, color = chemistry.get_ph_and_color(ph, indicator)
    return jsonify({"ph": ph, "color": color})  # 返回 pH 和顏色


# 新增 Gemini 問答頁面
@app.route('/gemini')
def gemini_page():
    return render_template('gemini.html')

# 處理 Gemini 問答 API
@app.route('/gemini_answer', methods=['POST'])
def gemini_answer():
    data = request.get_json()
    question = data.get('question', '')
    answer = gemini.get_gemini_response(question)
    return jsonify({"answer": answer})



if __name__ == '__main__':
    app.run(debug=True)

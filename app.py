from flask import Flask, render_template, request, jsonify
import chemistry  # 假設 chemistry.py 處理化學模擬的邏輯
import rule  # 引入剛剛拆分出來的 rule.py

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

# 化學模擬的 API，處理 pH 和指示劑
@app.route('/simulate', methods=['POST'])
def simulate():
    # 獲取 pH 和 indicator 值
    ph = float(request.form['ph'])  # 接收 pH 值，並轉換為浮點數
    indicator = request.form['indicator']
    
    # 根據 pH 和 indicator 獲取顏色
    ph, color = chemistry.get_ph_and_color(ph, indicator)
    return jsonify({"ph": ph, "color": color})  # 返回 pH 和顏色




if __name__ == '__main__':
    app.run(debug=True)

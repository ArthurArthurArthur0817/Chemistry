import google.generativeai as genai
import os
import re

# 配置 Gemini API 金鑰
api_key = 'AIzaSyBqaiNcZhtRz5wRf6FU4ZYZ_xJxblhvh6E'
genai.configure(api_key=api_key)

def get_gemini_response(question):
    # 使用 Gemini 模型來生成回答
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
     # 格式化處理，將多餘的「*」符號去除或適當替換
    formatted_text = re.sub(r'\*+', '', response.text)  # 去除多餘的星號
    formatted_text = formatted_text.replace('\n', '\n')  # 保留換行
    formatted_text = formatted_text.replace('•', '・')  # 改成日本點樣式
    return response.text

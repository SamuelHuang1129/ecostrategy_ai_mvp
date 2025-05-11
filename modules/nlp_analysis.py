# modules/nlp_analysis.py

import streamlit as st
import re

def run():
    st.subheader("商業模式敘述分析 (NLP Demo)")

    # 確認 session_state 是否有 bm_description
    if "answers" not in st.session_state or "bm_description" not in st.session_state["answers"]:
        st.warning("目前尚未填寫商業模式，請先到問卷頁面填寫。")
        return

    text = st.session_state["answers"]["bm_description"]

    st.markdown("### ✏️ 商業模式原文")
    st.write(text)

    st.markdown("### 🔍 初步關鍵詞提取")

    # 簡單斷詞（以中英文空格、標點分隔）
    words = re.split(r'\W+', text.lower())
    words = [word for word in words if word and len(word) > 1]  # 移除空字與過短字

    # 預設關鍵字範例
    keywords = ["產品", "客戶", "銷售", "平台", "供應鏈", "生產", "設計", "服務", "線上", "離線", "科技", "金融", "能源"]

    found_keywords = [word for word in words if word in keywords]

    if found_keywords:
        st.success(f"找到關鍵詞：{', '.join(found_keywords)}")
    else:
        st.info("未發現明確關鍵詞。")
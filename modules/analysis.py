# modules/analysis.py

import streamlit as st
import pandas as pd
import jieba
import os

def run():
    st.subheader("分析工具（正式版）")

    if "answers" not in st.session_state or "bm_description" not in st.session_state["answers"]:
        st.warning("請先填寫問卷資料。")
        return

    description = st.session_state["answers"]["bm_description"]
    st.markdown("### ✏️ 商業模式原文")
    st.write(description)

    # 中文分詞
    words = set(jieba.lcut(description))
    st.markdown("### 📝 中文分詞結果")
    st.write(words)

    # 推薦元素
    recommended_elements = []
    excel_path = os.path.join(os.getcwd(), "data", "element_info.xlsx")
    if not os.path.exists(excel_path):
        st.error(f"資料庫檔案不存在：{excel_path}")
        return

    try:
        df = pd.read_excel(excel_path)
        for _, row in df.iterrows():
            element = row["元素"]
            keywords = row["關鍵詞"].split(",")
            if any(keyword.strip() in words for keyword in keywords):
                recommended_elements.append(element)

        st.session_state["recommended_elements"] = recommended_elements  # ✅ 儲存到session
    except Exception as e:
        st.error(f"讀取資料庫失敗：{e}")
        return

    st.markdown("### 🔍 建議相關元素")
    if recommended_elements:
        st.success("推薦元素：" + "、".join(recommended_elements))
    else:
        st.info("未發現推薦元素。") 
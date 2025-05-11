# modules/business_logic.py

import streamlit as st
import pandas as pd
import jieba
import os

def run():
    st.subheader("商業模式推薦分析 (資料庫比對 + Debug版)")

    # ✅ 顯示當前工作目錄
    current_path = os.getcwd()
    st.info(f"當前工作目錄：{current_path}")

    # ✅ 確認問卷內容是否存在
    if "answers" not in st.session_state or "bm_description" not in st.session_state["answers"]:
        st.warning("請先填寫問卷中的商業模式描述。")
        return

    description = st.session_state["answers"]["bm_description"]
    st.markdown("### ✏️ 商業模式原文")
    st.write(description)

    # ✅ 確認 data/element_info.xlsx 是否存在
    excel_path = os.path.join(current_path, "data", "element_info.xlsx")
    if not os.path.exists(excel_path):
        st.error(f"資料庫檔案不存在：{excel_path}")
        return
    else:
        st.success(f"已找到資料庫檔案：{excel_path}")

    # ✅ 讀取 Excel 並顯示
    try:
        df = pd.read_excel(excel_path)
        st.markdown("### 📋 資料庫內容：")
        st.dataframe(df)
    except Exception as e:
        st.error(f"讀取資料庫失敗：{e}")
        return

    # ✅ 中文分詞
    words = jieba.lcut(description)
    words = set(words)
    st.markdown("### 📝 中文分詞結果：")
    st.write(words)

    # ✅ 元素推薦分析
    st.markdown("### 🔍 建議相關元素")
    recommended_elements = []

    for _, row in df.iterrows():
        element = row["元素"]
        keywords = row["關鍵詞"].split(",")
        if any(keyword.strip() in words for keyword in keywords):
            recommended_elements.append(element)

    if recommended_elements:
        st.success("推薦相關元素：" + "、".join(recommended_elements))
    else:
        st.info("未發現相關元素。")
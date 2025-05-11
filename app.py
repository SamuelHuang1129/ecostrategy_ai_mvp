# app.py

import streamlit as st
from modules import questionnaire, speech_to_text, analysis, business_logic, report_generator, admin_panel

def main():
    st.sidebar.title("EcoStrategy AI 系統")
    page = st.sidebar.radio("選擇功能", ("問卷填寫", "語音轉文字", "分析工具", "管理後台", "報告產出"))

    if page == "問卷填寫":
        questionnaire.run()
    elif page == "語音轉文字":
        speech_to_text.run()
    elif page == "分析工具":
        analysis.run()   # ✅ Day 9新正式分析模組
    elif page == "管理後台":
        admin_panel.run()
    elif page == "報告產出":
        report_generator.run()

if __name__ == "__main__":
    main() 
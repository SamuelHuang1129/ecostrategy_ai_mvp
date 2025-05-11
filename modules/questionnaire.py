# modules/questionnaire.py

import streamlit as st

def run():
    st.subheader("企業基本資料 + 問題1填寫")

    # ✅ 初始化 session_state["answers"]
    if "answers" not in st.session_state:
        st.session_state["answers"] = {}

    answers = st.session_state["answers"]

    with st.form("eco_strategy_form"):
        company_name = st.text_input("公司名稱", value=answers.get("company_name", ""))
        job_title = st.text_input("您的職稱", value=answers.get("job_title", ""))
        contact_name = st.text_input("我該怎麼稱呼您？", value=answers.get("contact_name", ""))
        industry_list = ["半導體", "電子零組件", "通訊設備", "醫療設備", "製造業", "農業", "金融", "保險", "運輸", "其他"]
        employees_list = ["15人以下", "15~50人", "50~100人", "100~200人", "200~300人", "500~1000人", "2000人以上"]
        revenue_list = ["100萬美金以下", "100~500萬美金", "500~1000萬美金", "1000萬美金以上", "5000萬美金以上"]

        industry = st.selectbox("公司主要產業", industry_list, index=answers.get("industry_index", 0))
        employees = st.selectbox("公司目前大約有員工？", employees_list, index=answers.get("employees_index", 0))
        revenue = st.selectbox("公司年營業額大約在？", revenue_list, index=answers.get("revenue_index", 0))

        # ✅ Day 4：新增問題1
        bm_description = st.text_area(
            "問題1：請簡單描述您公司目前的商業模式",
            value=answers.get("bm_description", "")
        )

        submitted = st.form_submit_button("送出")
        if submitted:
            # 儲存所有資料到 session_state["answers"]
            st.session_state["answers"] = {
                "company_name": company_name,
                "job_title": job_title,
                "contact_name": contact_name,
                "industry": industry,
                "industry_index": industry_list.index(industry),
                "employees": employees,
                "employees_index": employees_list.index(employees),
                "revenue": revenue,
                "revenue_index": revenue_list.index(revenue),
                "bm_description": bm_description
            }
            st.success("資料已送出！")

    # ✅ 顯示目前答案（方便Debug）
    if st.session_state["answers"]:
        st.markdown("### ✔️ 當前填寫內容：")
        st.json(st.session_state["answers"])
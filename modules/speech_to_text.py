# modules/speech_to_text.py

import streamlit as st
import whisper
import tempfile

def run():
    st.subheader("語音轉文字測試 (Whisper)")

    uploaded_file = st.file_uploader("請上傳語音檔案 (mp3, wav, m4a)", type=["mp3", "wav", "m4a"])

    if uploaded_file is not None:
        st.info("檔案已上傳，開始轉換中...")
        
        # 儲存為臨時檔案
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_file_path = tmp_file.name

        # 加載 Whisper 模型
        model = whisper.load_model("base")  # 也可以換成 "small" 或 "medium"
        result = model.transcribe(tmp_file_path)
        
        st.success("轉換完成！")
        st.markdown("### 🎙️ 語音辨識結果：")
        st.text(result["text"])
import streamlit as st
from translate import translate_text
from utils import extract_text_from_image
from PIL import Image
from PIL import Image
from utils import generate_qr_code

st.set_page_config(page_title="이미지 번역기", layout="centered")
st.title("📷 이미지 속 텍스트 번역기")

uploaded_file = st.file_uploader("이미지를 업로드하세요", type=["jpg", "png", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="업로드한 이미지", use_container_width=True)

    with st.spinner("텍스트를 추출하고 번역 중입니다..."):
        extracted = extract_text_from_image(uploaded_file) 
        translation = translate_text(extracted)

    st.subheader("🔍 인식된 텍스트:")
    st.write(extracted)

    st.subheader("🌐 번역 결과:")
    st.success(translation)

app_url = "https://share.streamlit.io/image_translator/app.py"
qr_path = generate_qr_code(app_url, "app_site_qr.png")

st.subheader("🔗 웹앱 접속용 QR 코드")
st.image(Image.open(qr_path), caption="📱 이 코드를 스캔하여 접속하세요", use_container_width=False)

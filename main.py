import streamlit as st

st.set_page_config(page_title="Portfolio Distance Delivery",
                   layout="wide", page_icon=":rocket:")
#st.title('Portofolio Distance Food Delivery')
#st.title("Portfolio Saya")
#st.header("Data Scientist & Developer")
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman",
                        ["About Project", "EDA", "Machine Learning"])

if page == 'Machine Learning':
    import predict
    predict.prediksi()
elif page == 'EDA':
    import Eksplorasi
    Eksplorasi.eksplorasi_data()
elif page == 'About Project':
    import Introduction
    Introduction.project()
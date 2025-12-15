import streamlit as st

st.set_page_config(
    page_title="Struktur Kelas TI-A",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Struktur Kelas TI-A")
st.write("Berikut adalah susunan anggota kelas.")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/andi.jpg", width=160)
    st.subheader("Andi Pratama")
    st.caption("Ketua Kelas")

with col2:
    st.image("images/budi.jpg", width=160)
    st.subheader("Budi Santoso")
    st.caption("Wakil Ketua")

with col3:
    st.image("images/siti.jpg", width=160)
    st.subheader("Siti Aminah")
    st.caption("Sekretaris")

st.divider()
st.caption("Website dibuat dengan Streamlit")

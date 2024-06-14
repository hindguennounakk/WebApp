import streamlit as st 

with st.form("form"):

    st.title("Formulaire")

    st.subheader('Merci de renseignez les champs suivants')

    st.write("Nom")

    user_name = st.text_input('Renseignez ici')

    st.write("Prénom")
    
    Usaer_name = st.text_input('ton pénom')

    st.write("age")

    age= st.select_slider("selectioner votre age",
                            options=range(18,99))

    user_diplome =st.selectbox(
        "Quel est votre niveau d'étude?",
        ("Sans Diplome", "BAC", "BAC+2", "Bac+5","Bac+8",)
    )
    if st.form_submit_button("envoyer"):
        st.write('Formulaire envoyer')
        if int(age) <18 : 
            st.write("Vous êtes mineur")
        if int(age) <18 :    
            st.write("Vous êtes majeur")



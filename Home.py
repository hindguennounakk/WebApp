# python3 -m streamlit run Home.py
import streamlit as st 

st.title("Hello World !")
#sous-titre
st.subheader('c est un sous-titre')

#Texte 
st.write(" renseignez votre texte")

#champs de saisie
user_input = st.text_input('tape ton text')

# Afficher à l'ecran ce que l'utilisateur à e saisi
st.write(user_input)
#Afficher une image sur mon application
st.image('https://s2.qwant.com/thumbr/474x230/7/2/e1b3c3173edc474478b43e26238855e8a681605c34c9901480ea6b6786702b/th.jpg?u=https%3A%2F%2Ftse.mm.bing.net%2Fth%3Fid%3DOIP.czf6PQ0Ke_aKhq7jGcwM2wHaDm%26pid%3DApi&q=0&b=1&p=0&a=0')
#Créattion d'un formulaire
with st.form('Form'):

    user_name = st.text_input('Tape your name')
    if st.form_submit_button("Send"):
    #On affiche le nom de l'utilisateur
        st.write(user_name)
import streamlit as st
import socket

# Fonction pour récupérer les messages du canal IRC sur Freenode
def get_irc_messages():
    server = "irc.freenode.net"  # Serveur IRC de Freenode
    port = 6667  # Port IRC
    channel = "#anonymous"  # Le canal IRC à rejoindre

    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    irc.connect((server, port))

    irc.send(bytes("USER anonymous * * :anonymous\r\n", "UTF-8"))
    irc.send(bytes("NICK anonymous_bot\r\n", "UTF-8"))
    irc.send(bytes(f"JOIN {channel}\r\n", "UTF-8"))

    messages = []

    # Enregistrement des messages du canal
    while len(messages) < 5:  # Limite le nombre de messages affichés
        response = irc.recv(2048).decode("UTF-8")
        if "PING" in response:
            irc.send(bytes("PONG :" + response.split(":")[1] + "\r\n", "UTF-8"))
        if f"PRIVMSG {channel}" in response:
            message = response.split(f"PRIVMSG {channel} :")[1]
            messages.append(message)

    return messages

# Configuration de la page Streamlit
st.set_page_config(page_title="Opérations Anonymous", page_icon="🕵️")

# Affichage du titre et logo
st.title("Opérations Anonymous en cours")
st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Anonymous_logo.svg/640px-Anonymous_logo.svg.png', width=150)  # Logo Anonymous

# Injecter du CSS dans la page Streamlit pour un thème sombre et contrasté
st.markdown(
    """
    <style>
        body {
            background-color: #111;
            color: #fff;
            font-family: 'Courier New', Courier, monospace;
            margin: 0;
            padding: 0;
        }
        h1 {
            text-align: center;
            font-size: 36px;
            color: #FF0000;
            text-transform: uppercase;
            background: linear-gradient(90deg, #ffcc00, #ff6666, #66ccff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            padding: 20px 0;
        }
        .stButton>button {
            background-color: #FF0000;
            color: white;
            border: 2px solid #FF0000;
            border-radius: 10px;
            font-size: 18px;
            padding: 10px 20px;
            box-shadow: 0 0 15px rgba(255, 0, 0, 0.5);
            transition: all 0.3s ease-in-out;
        }
        .stButton>button:hover {
            background-color: #ff6666;
            box-shadow: 0 0 20px rgba(255, 0, 0, 0.7);
        }
        .operation {
            padding: 20px;
            margin-bottom: 10px;
            background-color: #222;
            border-radius: 8px;
            border: 2px solid #FF0000;
            transition: all 0.3s ease-in-out;
        }
        .operation:hover {
            background-color: #333;
            box-shadow: 0 0 15px rgba(255, 0, 0, 0.6);
        }
        .operation h3 {
            font-size: 24px;
            color: #ffcc00;
        }
        .operation p {
            font-size: 16px;
            color: #ccc;
        }
    </style>
    """, unsafe_allow_html=True)

# Affichage dynamique des messages provenant d'IRC
messages = get_irc_messages()

if messages:
    for message in messages:
        st.markdown(f"<div class='operation'>", unsafe_allow_html=True)
        st.markdown(f"<h3>Message IRC:</h3>", unsafe_allow_html=True)
        st.markdown(f"<p>{message}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
else:
    st.warning("Aucun message trouvé dans le canal IRC.")

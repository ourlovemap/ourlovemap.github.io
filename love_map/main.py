from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/food_markers")
def get_food_markers():
    markers = [
        {
            "title": "Rascal Fattoria",
            "subtitle": "xx/xx/xxxx",
            "location": [-23.5591, -46.6608],
            "description": "...",
            "image": "../images/mm_logo.png"
        }
    ]
    # Rascal, Baruk, La Pergoletta, Andiamo, Pecorino, La Piadina Cucina, Bistro Faria Lima, Izakaya Kuroda, Caires, Z Deli, Hito Vegano, El Huarique, MOMA, Sushimar Vegano, Marakuthai, Walnuts, De Segunda, 
    return jsonify(markers)

@app.route("/api/date_markers")
def get_date_markers():
    markers = [
        {
            "title": "Primeiro Date",
            "subtitle": "Gorila Beer House - 26/03/2022",
            "location": [-23.5870, -46.6480], 
            "description": "O primeiro momento em que nossos olhos se encontraram. Me lembro até hoje da surpresa que foi cruzar a rua e encontrar a futura dona do meu coração.",
            "image": "../images/mm_logo.png"
        },
        {
            "title": "Segundo Date", 
            "subtitle": "Kinoplex Itaim - 27/03/2022",
            "location": [-23.5845, -46.6747], 
            "description": "Confesso que até tinha me esquecido do filme que fomos assistir, mas não me esqueço nem sequer por um milésimo de segundo do seu cheiro e do seu olhar enquanto estávamos sentados no banco.",
            "image": "../images/mm_logo.png"
        },
    ]
        # Segundo Date (Kinoplex Itaim)
            # Banquinho do Kinoplex
        # Terceiro Date (Av Paulista)
        # Date do pedido de namoro (Astronauta Café, Paróquia Bar o Santto Chopp)
        # Date que conheci os pais dela (Bar do Gê, Esquina do Souza)
        # Museu Lasar Segall
        # Beco do Batman
        # Feira Benedito Calixto
        # Expo Center Norte (formatura)
        # Meu Karaoke Box, Blitz Haus
        # Barbixas
        # Conjunto Nacional
        # SESC Pompeia
        # Veloso Bar
        # Banquinho no Edgard
        # Nossos endereços
            # Algumas das conversas mais pessoais que já tivemos
    return jsonify(markers)

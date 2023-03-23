from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/food_markers")
def get_food_markers():
    markers = [
        {
            "title": "La Piadina Cucina",
            "subtitle": "18/03/2023",
            "location": [-23.5951, -46.6787],
            "description": "Aproveitar restaurantes com você é, com certeza, o que mais amo. Foram duas das melhores horas que já vivi, conversando e aproveitando a tranquilidade da noite ao seu lado. A burrata, o pedaço colossal de entrecôte e nosso tiramisu de todo dia... Cada minuto daquele dia se transformou em felicidade extrema.",
            "image": "../images/la_piadina_cucina.png"
        },
        {
            "title": "Damp Sorvetes",
            "subtitle": "12/02/2023",
            "location": [-23.5920, -46.6021],
            "description": "Estar com sua família, rodeado de tanto amor, é uma benção. Um simples errinho vira um novo sorvete pra você, e se torna uma nova memória nossa. Memórias boas, queridas, aconchegantes",
            "image": "../images/damp_sorvetes.png"
        },
        {
            "title": "Caires",
            "subtitle": "Vários e vários dias",
            "location": [-23.5865, -46.6727],
            "description": "Um bar que marcou nossa proximidade. Tantas e tantas vezes que já estivemos nele com seus amigos, compartilhando risadas, histórias, problemas... Momentos como esses mostram todo o amor e felicidade que nos rodeiam e que fazem parte da nossa rotina.",
            "image": "../images/caires.png"
        },
        {
            "title": "Z Deli",
            "subtitle": "29/01/2023",
            "location": [-23.5883, -46.6805],
            "description": "O dia que também visitamos a baleia. Mais um dia em que você me ensinou mais do que eu sequer conseguiria, me mostrando caminhos, pensamentos e acalmando a pressão que eu sentia no momento. Você é esse brilho na minha vida.",
            "image": "../images/z_deli.png"
        },
    ]
    # Rascal, Baruk, La Pergoletta, Andiamo, Pecorino, La Piadina Cucina, Bistro Faria Lima, Izakaya Kuroda, Caires, Z Deli, Hito Vegano, El Huarique, MOMA, Sushimar Vegano, Marakuthai, Walnuts, De Segunda, 
    return jsonify(markers)

@app.route("/api/date_markers")
def get_date_markers():
    markers = [
        {
            "title": "Primeiro Date",
            "subtitle": "Gorila Beer House - 26/02/2022",
            "location": [-23.5870, -46.6480], 
            "description": "O primeiro momento em que nossos olhos se encontraram. Me lembro até hoje da surpresa que foi cruzar a rua e encontrar a futura dona do meu coração.",
            "image": "../images/gorila_beer_house.png"
        },
        {
            "title": "Segundo Date", 
            "subtitle": "Kinoplex Itaim - 27/02/2022",
            "location": [-23.5845, -46.6747], 
            "description": "Confesso que até tinha me esquecido do filme que fomos assistir, mas não me esqueço nem sequer por um milésimo de segundo do seu cheiro e do seu olhar enquanto estávamos sentados no banco.",
            "image": "../images/kinoplex_itaim.png"
        },
        {
            "title": "Terceiro Date", 
            "subtitle": "Av Paulista - 02/03/2022",
            "location": [-23.5629, -46.6549], 
            "description": "Já estava totalmente apaixonado por você nesse dia. Passeamos por toda a Av Paulista, comemos bem (mesmo com o caos da Casa das Rosas), visitamos exposições e nos aproximamos. Guardo esse dia com todo o carinho do mundo no meu coração, não faria nada diferente.",
            "image": "../images/av_paulista.png"
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

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
        {
            "title": "Baruk", 
            "subtitle": "Vários e vários dias",
            "location": [-23.5829, -46.6760], 
            "description": "Esse é outro lugar muito especial. Fez parte do nosso maior desastre de carnaval da história, assim como fez parte dos nossos primeiros almoços. Amo tanto cada memória que criamos nele e não as trocaria por nada.",
            "image": "../images/baruk.png"
        },
        {
            "title": "MOMA", 
            "subtitle": "04/08/2022",
            "location": [-23.5819, -46.6798], 
            "description": "Amo como você se esforça para conhecer melhor meus amigos. Esse dia foi tão incrível, em que nós 4 estávamos em sintonia com as conversas, risadas, fofocas. Mesmo com a comida não sendo das melhores, o dia fechou com chave de ouro quando nos reunimos em casa.",
            "image": "../images/moma.png"
        },
        # Pecorino
        # Si Senor 20/05/2022
        # Sushimar Vegano 19/06/2022
        # Hecho en Mexico 23/06/2022
        # Hito Vegano 16/12/2022
    ]
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
        {
            "title": "De Segunda", 
            "subtitle": "17/03/2022",
            "location": [-23.5835, -46.6754], 
            "description": "Conhecer novos restaurantes com você é algo mágico. Sentir novos sabores a cada prato que pedimos, escutar de leve as conversas das outras mesas, ou perder totalmente o rumo das nossas... Com você tudo é mais divertido.",
            "image": "../images/de_segunda.png"
        },
        {
            "title": "Astronauta Café", 
            "subtitle": "27/03/2022",
            "location": [-23.5859, -46.6436], 
            "description": "O dia em que nosso namoro começou. Nada melhor para definir o nosso namoro do que um café, bar e um dia repleto de nós dois. Sempre ao seu lado... Continuo, desejo a continuação e amamos.",
            "image": "../images/astronauta_cafe.png"
        },
        {
            "title": "Bar do Gê", 
            "subtitle": "02/04/2022",
            "location": [-23.5383, -46.6752], 
            "description": "Conhecer seus pais só me fez ter mais certeza do amor, carinho e apoio que te rodeia. Amor de ponta a ponta, demonstrado em cada pedacinho de interação entre vocês. Carinho com todos que estão em volta, acolhendo e apoiando de todas as formas possíveis.",
            "image": "../images/bar_do_ge.png"
        },
        {
            "title": "Banquinho do Edgard", 
            "subtitle": "Vários dates",
            "location": [-23.5850, -46.6710], 
            "description": "Se fosse para definir o lugar mais importante para o nosso namoro, esse estaria facilmente no Top 3. Conversar, rir, acalmar e viver tanto com você em intervalos tão curtos de tempo me deu certezas que eu nem sequer cogitava. Sempre foi tão fácil estar com você.",
            "image": "../images/banco_edgard.png"
        },
        {
            "title": "Centro Cultural", 
            "subtitle": "Vários dates",
            "location": [-23.5708, -46.6402], 
            "description": "Date com leituras, pudim, docinhos. Passear com você nesses lugares é tão divertido, tranquilo... Ficar ao seu lado enquanto líamos nossos quadrinhos foi muito sincero, uma conversa sem palavras, diretamente do nosso mundinho.",
            "image": "../images/centro_cultural.png"
        },
        # {
        #     "title": "Conjunto Nacional", 
        #     "subtitle": "Vários dates",
        #     "location": [-23.5587, -46.6597], 
        #     "description": "",
        #     "image": "../images/.png"
        # },
        {
            "title": "Dates, dates, dates", 
            "subtitle": "Av Paulista - 22/04/2022",
            "location": [-23.5629, -46.6549], 
            "description": "Dias tão maravilhosos, com passeios tão tranquilos e divertidos. Lembro da foto que tirei de você, que tiramos juntos e também das conversas que tivemos sem parar. Amo e guardo cada momento desses no coração.",
            "image": "../images/banquinho_shopping.png"
        },
        {
            "title": "Veloso Bar", 
            "subtitle": "24/04/2022",
            "location": [-23.5851, -46.6351], 
            "description": "Date de diminutivos, com coxinha e caipirinha. Mais um da saga de comidas e bebidas deliciosas que aproveitamos juntinhos, sempre com as nossas conversas e piadas. A melhor definição de amor que criamos.",
            "image": "../images/veloso_bar.png"
        },
        {
            "title": "Theatro Municipal", 
            "subtitle": "10/07/2022",
            "location": [-23.5452, -46.6382], 
            "description": "Eu nunca imaginaria que assistir qualquer peça de teatro, balé, orquestra poderia ser tão divertido. Nossa definição de aproveitar o momento é a única que desejo pra minha vida. Amo você.",
            "image": "../images/teatro_municipal.png"
        },
        {
            "title": "SESC Pompeia", 
            "subtitle": "16/07/2022",
            "location": [-23.5253, -46.6833], 
            "description": "Passear em exposições encaixa tão bom com a gente. Lendo cada peça ali exposta, contemplando os detalhes das obras, conversando sobre e rindo como sempre. Amor.",
            "image": "../images/sesc_pompeia.png"
        },
        {
            "title": "Beco do Batman", 
            "subtitle": "22/10/2022",
            "location": [-23.5565, -46.6861], 
            "description": "Ainda precisamos refazer esse date pra aproveitar o único e fantástico pudim do Mori. Tomar aquela cerveja indo em direção a Benedito Calixto, olhar todas as vendinhas com antiguidades... Tudo nesse date foi perfeito.",
            "image": "../images/beco_do_batman.png"
        },
        {
            "title": "Exposição dos Dinossauros", 
            "subtitle": "16/11/2022",
            "location": [-23.5859, -46.6549], 
            "description": "A exposição diferente que se transformou num date completo pelo Ibirapuera. Amo aprender sobre qualquer coisa ao seu lado. Admiro demais sua inteligência e o jeito que você sempre está disposta a aprender.",
            "image": "../images/dinossauro.png"
        },
        # {
        #     "title": "Museu Lasar Segall", 
        #     "subtitle": "04/12/2022",
        #     "location": [-23.5945, -46.6357], 
        #     "description": "",
        #     "image": "../images/.png"
        # },
        {
            "title": "Teatro Alfa", 
            "subtitle": "17/12/2022",
            "location": [-23.6507, -46.7211], 
            "description": "Uma verdadeira obra de arte. Esse date assistindo balé foi impecável. Nos encantamos com o quão incrível essa peça foi, nos encantamos com os passos que tivemos a sorte de observar e recordo até hoje da nossa conversa na volta, com você me contando tudo que sabia sobre balé. Te amo.",
            "image": "../images/teatro_alfa.png"
        },
        {
            "title": "Oscar Freire", 
            "subtitle": "29/05/2022",
            "location": [-23.5615, -46.6705], 
            "description": "Outro passeio leve, divertido e que até hoje tenho marcado na minha memória. Seu vestido, seu sorriso e seu batom... Mais um dia que me senti conquistado por todo o seu amor e encanto. Minha princesa.",
            "image": "../images/havaianas.png"
        }
    ]
    return jsonify(markers)

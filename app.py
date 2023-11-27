#primerio impotar o flask e a renderizações
from flask import Flask, render_template, url_for

#aqui inicia a aplicação (cria)
app = Flask(__name__)


#aqui indentifica a rota ou caminho
@app.route('/')
def index():
#apos criar funão, fazer a renderização da pagina
    return render_template('index1.html')

#criar uma nova nota para cada página nova
@app.route('/index.html')
def texto_linux():

#nessa função resulta o abertura de texto no modo r(read=ler) como "arquivo"
    with open('linux.txt', 'r', encoding="utf-8") as arquivo:
        texto_pronto = arquivo.read()
        return render_template('index.html', linux=texto_pronto)


@app.route('/python.html')
def texto_python():

    with open('python.txt', 'r', encoding="utf-8") as arquivopy:
        texto_py = arquivopy.read()
        return render_template('python.html', arquivopy=texto_py)


#
if __name__ == '__main__':
#aqui serve para rodar o app com debug para melhoria na atualização da página
    app.run(debug=True)

from flask import Flask, request

app = Flask(__name__)

filmes = [
    {"nome": "Gentegrande", "infos":
        [
            {"genero": "Comedia", "bilheteria": 271430189}
        ]
    },
     {"nome": "Bladerunner2049", "infos":
        [
            {"genero": "Ficcao", "bilheteria": 267430189}
        ]
    }
    ]
#get
#127.0.0.1:5000/filmes
@app.get("/filmes")
def get_filmes():
    return {"filmes": filmes}

#get
#127.0.0.1:5000/filmes/nome
@app.get("/filmes/<string:nome>")
def get_filmes_by_nome(nome):
    for filme in filmes:
        if filme["nome"] == nome:
            return filme
    return {"message": "filme not found"}, 404

#get
#127.0.0.1:5000/filmes/nome/info
@app.get("/filmes/<string:nome>/info/")
def get_info_in_filmes(nome):
    for filme in filmes:
        if filme["nome"] == nome:
            return {"infos": filme["infos"]}
    return {"message": "filme not found"}, 404

#post
#127.0.0.1:5000/filmes
@app.post("/filmes")
def create_filmes():
    request_data = request.get_json() #pega o conteudo do body
    new_filmes = {"nome": request_data["nome"], "infos": []}
    filmes.append(new_filmes) #insere o payload na filmes
    return new_filmes, 201

#post
#127.0.0.1:5000/filmes
@app.post("/filmes/<string:nome>/info")
def create_info(nome):
    request_data = request.get_json()
    for filme in filmes:
        if filme["nome"] == nome:
            new_info = {"genero": request_data["genero"], "bilheteria": request_data["bilheteria"]}
            filme["infos"].append(new_info)
            return new_info, 201
    return {"message": "nome nao encontrado "}, 404


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True)

const express = require("express"); // Importando o express
const app = express(); // Iniciando o express

app.get("/", function(requisicao, resposta) {
    resposta.send("Bem vindo!!"); // Resposta só pode enviar uma vez
    // resposta.send("NãO PODE DUAS RESPOSTAS")
});

app.get("/blog", function(req, res) {
    res.send("Bem vindo ao meu blog!!");
});

app.get("/ola/:nome/:sobrenome?", function(req, res) {
    // REQUISIÇÃO: dados enviados pelo usuário
    // Resposta: resposta que vai ser enviada para o usuário
    var nome = req.params.nome;
    var sobrenome = req.params.sobrenome;

    if(sobrenome) {
        res.send("Oi " + nome + " " + sobrenome + "!");
    } else {
        res.send("Oi " + nome + " !");
    }
});

app.get("/canal/youtube", function(req, res) {
    var canal = req.query["canal"]

    if(canal) {
        res.send(canal)
    } else {
        res.send("Nenhum canal fornecido!")
    }
});

app.listen(4000, function(erro){
    if(erro){
        console.log("Ocorreu um erro!");
    } else {
        console.log("Servidor iniciado com sucesso!");
    }
})

// npm install nodemon -g


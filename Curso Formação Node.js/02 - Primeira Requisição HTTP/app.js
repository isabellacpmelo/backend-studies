var http = require("http");
// console.log(http);

// http://localhost:8181/
// A porta pode ser qualquer uma
http.createServer(function(requisicao, resposta){
    resposta.end("<h1>Bem vindo ao meu site!</h1><h4>Isabella Melo</h4>")
}).listen(8181);
console.log('Meu servidor está rodando!');
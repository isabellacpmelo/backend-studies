console.log("Hello World!");
console.log("Meu nome é Isabella!");
console.log("E eu estou aprendendo Node.js com o Guia do programador");

var mostrarSite = true;
const site = "www.guiadoprogramador.com";
if(mostrarSite){ // Se mostrar site
    console.log(site); // Printe o site
}

var calculadora = require("./calculadora");

console.log(calculadora.mult(10,20));
console.log(calculadora.soma(20,40));
calculadora.nome = "Calculadora da Isabella!"
console.log(calculadora.nome);

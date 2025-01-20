// El principal objetivo de este desafío es fortalecer tus habilidades en lógica de programación. Aquí deberás desarrollar la lógica para resolver el problema.

    let amigos =  [];
    let ListanumerosSorteados=[];
    let i=0;



//id="amigo" "Escribe un nombre">
// "agregarAmigo()">Añadir</button>
function agregarAmigo(){
    let amigo = document.getElementById('amigo').value;
    if(amigo==""){
        alert("Por favor, inserte un nombre.")
    } else {
        amigos.push(amigo);
        console.log(amigos)
        let campoAmigo=document.querySelector('#amigo');
        campoAmigo.value="";

        // Crear un nuevo elemento <li>
        let verAmigo = document.createElement("li");
        // Crear un nodo de texto con el contenido del nuevo elemento
        let contenido = document.createTextNode(amigo);
        // Añadir el nodo de texto al nuevo elemento <li>
        verAmigo.appendChild(contenido);
        // Añadir el nuevo elemento <li> a la lista
        document.getElementById("listaAmigos").appendChild(verAmigo);
    }
}

 function generarAleatorio(){
    let largoAmigos=amigos.length;
    let posicionAleatoria = Math.floor(Math.random()*largoAmigos);
    if (ListanumerosSorteados.includes(posicionAleatoria)){
        return generarAleatorio();
    } else {
        ListanumerosSorteados.push(posicionAleatoria);
        return posicionAleatoria;
    }
 }

 function sortearAmigo(){
    if (amigos.length==0){
        alert("no se puede sortear, la lista esta vacia")
    } else{
        let posicion=generarAleatorio();
        let ganador=amigos[posicion];
        alert(`El ganador o ganadora es: ${ganador}`)
        let ListaAmigo=document.querySelector('#listaAmigos');
        ListaAmigo.innerHTML="";
        amigos=[];
    }
 }

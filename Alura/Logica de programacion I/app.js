
let limite = parseInt(prompt("De 1 hasta que numero quieres jugar: "));
let numeroSecreto = parseInt(Math.random()*limite)+1;
let numeroUsuario = 0;
let contador=0;
while (numeroUsuario != numeroSecreto) {
        contador++;
    if(contador==4){
        alert(`Llegaste al numero maximo de intentos...F 
intentos: ${contador-1}`)
        break;
    }
    numeroUsuario = parseInt(prompt(`Me indicas un numero entre 1 y ${limite} por favor: `));
    console.log(`intento N°${contador}, numero: ${numeroUsuario}`);
    console.log(numeroSecreto)
    if(numeroUsuario == numeroSecreto){
        alert(`Acertaste!!, el numero es: ${numeroSecreto}
con ${contador} intentos`);
    } else {
            alert(`el numero es ${numeroUsuario > numeroSecreto ? "menor" : "mayor" } bro`);
        }
    if(contador>3){
        alert(`Llegaste al numero maximo de intentos...F 
intentos: ${contador-1}`)
        break;
    }
}

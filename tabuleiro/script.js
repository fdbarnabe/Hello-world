function virarCarta(cartaId){
    console.log(cartaId);
    let elemento = document.getElementById(cartaId);
    if (elemento.classList.contains('carta-virada')){
        elemento.classList.remove('carta-virada');
    }else{
        elemento.classList.add('carta-virada');
    }
}
function virarCarta(cartaId){
    console.log(cartaId);
    let elemento = document.getElementById(cartaId);
    if (elemento.classList.contains('carta-virada')){
        element.classList.remove('carta-virada');
    }else{
        element.classList.add('carta-virada');
    }
}
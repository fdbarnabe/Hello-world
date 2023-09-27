let cartaVirada1 = null;
let cartaVirada2 = null;

let imagens = ["bull.jpg", "jaguar.jpg"];

function init(){
    let elementos = document.getElementsByClassName('carta');
    for (let i = 0; i< elementos.length; i++){
        elementos[i].style.background = "url('./img/tiger.jpg')";
    }
}


function virarCarta(cartaId){
    /* console.log(cartaId); */

    let elemento = document.getElementById(cartaId);
    console.log(elemento.getAttribute('data-par'));
    if (elemento.classList.contains('carta-virada')){
        return;
    }
    elemento.classList.toggle("carta-virada");
    if (cartaVirada1 != null){
        cartaVirada2 = elemento;
        if (cartaVirada2.getAttribute('data-par') == cartaVirada1.getAttribute('data-par')){
            console.log("AS CARTAS SÃO IGUAIS");
            cartaVirada1.classList.add('carta-par');
            cartaVirada2.classList.add('carta-par');
        }else{
            console.log("AS CARTAS NÃO SÃO IGUAIS");
            cartaVirada1.classList.remove('carta-virada');
            cartaVirada2.classList.remove('carta-virada');
        }
        cartaVirada1 = null;
        cartaVirada2 = null;
    } else{
        cartaVirada1 = elemento;
    }

}



init();
const cards = document.querySelectorAll('.task')



cards.forEach((card)=>{
    card.addEventListener("click", ()=>{
        if(card.className == "task"){
            card.className = "task-detailed"
        }else{
            card.className = "task"
        }
    })
})
var canvas, ctx;
window.onload = iniciarAnimacao;

function iniciarAnimacao(){
    canvas = document.querySelector('#meuCanvas');
    ctx = canvas.getContext('2d');
    canvas. width = window.innerWidth;
    canvas. height = window.innerHeight;   
    loop();    
}
function loop(){
    desenhar();  
}

function randomNum(n){
    return Math.round(Math.random()*n);
}
function desenharBola(){
    ctx.fillStyle= 'rgb('+randomNum(255)+','+randomNum(255)+','+randomNum(255)+')';
    ctx.arc(randomNum(window.innerWidth),randomNum(window.innerHeight),randomNum(100),0,2*Math.PI);
    ctx.fill();
}

function desenhar(){
     
    for(let i = 0; i<5;i++){
        ctx.save();
        ctx.beginPath();
        desenharBola();
        ctx.restore();  
    }
}
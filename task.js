function add(){
    let a = Number(document.getElementById("n1").value);
    let b = Number(document.getElementById("n2").value);
    document.getElementById("res").innerText = a + b;
    
}
function sub(){
    let a = Number(document.getElementById("n1").value);
    let b = Number(document.getElementById("n2").value);
    document.getElementById("res").innerText = a - b;
}
function mul(){
    let a = Number(document.getElementById("n1").value);
    let b = Number(document.getElementById("n2").value);
    document.getElementById("res").innerText = a * b;
    
}
function div(){
    let a = Number(document.getElementById("n1").value);
    let b = Number(document.getElementById("n2").value);
    document.getElementById("res").innerText = a / b;
}
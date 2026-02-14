//function btnclick(){
  //  alert("button is clicked");
//    document.getElementById("b1").innerText="clicked";
    //document.body.style.backgroundColor="red";
//}

city=["Delhi","Mumbai","Chennai","Kolkata","Bangalore"];
function filterCity(){
    const filteredCity=cityArr.filter((city)=>
    city.toLowerCase().startsWith(dataInput.toLowerCase()));
    Mydata="";
    filteredCity.forEach((city)=>{
        Mydata+=`<li>${city}</li>`;
    });
}
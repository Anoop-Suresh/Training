var cont=document.getElementById("content")

var btn= document.getElementById("btn");
btn.addEventListener("click",function(){

var ourRequest=new XMLHttpRequest();
ourRequest.open('GET',"https://learnwebcode.github.io/json-example/animals-1.json");
ourRequest.onload=function(){
var ourData=JSON.parse(ourRequest.responseText);
renterHTML(ourData);
};
ourRequest.send();


});

function renterHTML(data){
var htmlstring='';
for(i=0;i<data.length;i++){
htmlstring+="<p>"+data[i].name+" "+data[i].species+".</p>";
}
cont.insertAdjacentHTML('beforeend',htmlstring);

}
function sub(){
alert('Registration Completed');
}

function sel(){
let dropdown = document.getElementById('state');
dropdown.length = 0;

let defaultOption = document.createElement('option');
defaultOption.text = 'Choose State';

dropdown.add(defaultOption);
dropdown.selectedIndex = 0;
let sl=document.getElementById("ld");
const url = 'http://battuta.medunes.net/api/region/'+sl.value+'/all/?key=0c5882d3537bb027ab201d08bbcde432'

const request = new XMLHttpRequest();
request.open('GET', url, true);

request.onload = function() {
 if (request.status === 200) {
   const data = JSON.parse(request.responseText);
   let option;
   for (let i = 0; i < data.length; i++) {
     option = document.createElement('option');
     option.text = data[i].region;
     option.value = data[i].code;
     dropdown.add(option);
   }
  } else {
 }
}

request.onerror = function() {
 console.error('An error occurred fetching the JSON from ' + url);
};

request.send();
}



let dropdown = document.getElementById('ld');
dropdown.length = 0;

let defaultOption = document.createElement('option');
defaultOption.text = 'Choose country';

dropdown.add(defaultOption);
dropdown.selectedIndex = 0;

const url = 'http://battuta.medunes.net/api/country/all/?key=36e9feb192ef2bfa911b66470637e20d';

const request = new XMLHttpRequest();
request.open('GET', url, true);

request.onload = function() {
 if (request.status === 200) {
   const data = JSON.parse(request.responseText);
   let option;
   for (let i = 0; i < data.length; i++) {
     option = document.createElement('option');
     option.text = data[i].name;
     option.value = data[i].code;
     dropdown.add(option);
   }
  } else {
 }
}

request.onerror = function() {
 console.error('An error occurred fetching the JSON from ' + url);
};

request.send();

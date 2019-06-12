function validate(){
var name = document.getElementById("name").value;
var age = document.getElementById("age").value;
var email = document.getElementById("email").value;
var number = document.getElementById("number").value;
if(name =="")
{
alert("Name Required");
return false;

}

var regex = /^([\w]){1,}\@([a-zA-Z0-9]){1,}\.([a-z]){2,4}$/;
if(email =="")
{
alert("E-mail address required");
return false;
}

if(email !="")
{
if(regex.test(email))
{
if(age =="")
{
alert("Age required");
return false;
}
if(age !="")
{
if(age<0 || age>110)
{
alert("Enter a valid age");
return false;
}

else{
if (number =="")
{
alert("Registration Successful")
return true;
}
else{
if (number !="")
{
var re = /^\+91([6-9])([0-9]){9}$/
if(re.test(number))
{
alert("Registration Successful");
return true;
}
else{
alert("Enter a valid phone number");
return false;
}
}
}
}

}



}
else{
alert("Enter a valid email address")
}
}

}



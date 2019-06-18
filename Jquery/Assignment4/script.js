$(document).ready(function(){
		$("#view").hide();
		var id=0;
		
		//Save
		$('#b1').click(function(){
			//save();

					id=id+1;
			savemultiple(id);
		}
		)
		//View
		$('#b4').click(function()
		{
			display();
		})
		$('#b2').click(function(){
			save();
		})		
		//list
		$('#b5').click(function()
		{
			displayMultiply();
		})
		$("#b3").click(function() 
		{
    		deleteMultiply();
		});

		function save()
		{
			if (typeof(Storage) !== "undefined")
			 {
			 	var id=localStorage.length;
				if($('#name').val()!=="" && $('#age').val()!==""){
					localStorage.setItem("Sid",id);
					localStorage.setItem("Fname",$('#fname').val());
					localStorage.setItem("Lname",$('#lname').val());
					localStorage.setItem("Mname",$('#mname').val());
					localStorage.setItem("Mobile",$('#mobile').val());
					localStorage.setItem("Email",$('#email').val());
					localStorage.setItem("Phone",$('#phone').val());
					localStorage.setItem("Pemail",$('#pemail').val());
					localStorage.setItem("Year",$('#year').val());

					alert("Record saved successfully");
					//document.getElementById("s1").innerHTML = localStorage.getItem("Name");
					//$('#ssid').html(localStorage.getItem("Fname")+localStorage.getItem("Sid"));
				}
			}
			else {
  				$('#s1').html("Sorry, your browser does not support Web Storage...");
			}
		}
		function savemultiple(id)
		{
			if (typeof(Storage) !== "undefined")
			 {
				if($('#name').val()!=="" && $('#age').val()!==""){
					var sid=("Sid",$('#sid').val());
					var fname=$('#fname').val();
					var lname=$('#lname').val();
					var mname=$('#mname').val();
					var mobile=$('#mobile').val();
					var email=$('#email').val();
					var phone=$('#phone').val();
					var pemail=$('#pemail').val();
					var year=$('#year').val();
					
					//create array
					var array=[];
					array.push(sid,fname,lname,mname,mobile,email,phone,pemail,year);
					localStorage.array+=JSON.stringify({"Sid":id,"Fname":fname,"Lname":lname,"Mname":mname,"Mobile":mobile,"Email":email,"Phone":phone,"Pemail":pemail,"Year":year})
					//location.reload();
					alert("Record saved successfully");
					//document.getElementById("s1").innerHTML = localStorage.getItem("Name");
					//$('#ssid').html(localStorage.getItem("Fname")+localStorage.getItem("Sid"));
				}
			}
			else {
  				$('#s1').html("Sorry, your browser does not support Web Storage...");
			}
		}
		function display()
		{
			//console.log(localStorage);
			//console.log(localStorage.length);
			console.log(localStorage.key(2));
			$('#view').show();	
			if (typeof(Storage) !== "undefined")
			 {

					$('#ssid').val(localStorage.getItem("Sid"));
					$('#sfname').val(localStorage.getItem("Fname"));
					$('#slname').val(localStorage.getItem("Lname"));	
					$('#smname').val(localStorage.getItem("Mname"));	
					$('#smobile').val(localStorage.getItem("Mobile"));	
					$('#semail').val(localStorage.getItem("Email"));	
					$('#sphone').val(localStorage.getItem("Phone"));	
					$('#spemail').val(localStorage.getItem("Pemail"));	
					$('#syear').val(localStorage.getItem("Year"));	
							
									
			}
			else {
  				$('#s1').html("Sorry, your browser does not support Web Storage...");
		}
	}
	function displayMultiply()
	{
		
    	for(let i=0;i<localStorage.length;i++)
			{
				var key=localStorage.key(i);
				var value=localStorage.getItem(key);
				console.log(key+""+value);
				disp.innerHTML+=`${key}: ${value}</br>`;
				//location.reload();
			}
	}
	function deleteMultiply()
	{
		
   //  	for(let i=0;i<localStorage.length;i++)
			// {
			// 	var key=localStorage.key(i);
			// 	var value=localStorage.removeItem(key);
			// 	console.log(key+""+value);
			// 	//disp.innerHTML+=`${key}: ${value}</br>`;
			// 	$('#dis').location.reload();
			// }
			window.localStorage.clear();
	}

});

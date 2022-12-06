
// toggling the paly/pause button
button = document.getElementById("play")
button.addEventListener("click",function(){
	if(button.innerText === "Play"){
		button.innerText = "Pause";
	}	
	else{
		button.innerText = "Play";
	}	
	}
);

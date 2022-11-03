
// toggling the paly/pause button
button = document.getElementById("play")
button.addEventListener("onclick",function toggle(){
	if(button.innerHTML === "Play"){
		button.innerHTML = "Pause";
	}	
	else{
		button.ineerHTML = "Play";
	}	
	}
);

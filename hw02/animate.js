var c = document.getElementById("flag"); //searches the DOM for an element with the given ID and returns it (null if none iirc)
var ctx = c.getContext("2d"); //gives the canvas a context with which we can interact/draw on it with

var circle = document.getElementById("circle");

ctx.fillStyle = '#FF0000'; //sets the color/style for filling (doesn't actually fill)

function drawBorder(){
	ctx.strokeRect(0,0,500,500); //really cheap border lol
}

drawBorder();

var r = 0;
var grow = true;

var draw = function(){
	if( grow ){
		r += 1;
	}else{
		r -= 1;
	}
	if( r >= c.width/2 ){
		grow = false;
	}
	if( r == 0 ){
		grow = true;
	}

	ctx.clearRect(0,0,500,500);
	drawBorder();
	ctx.beginPath();
	ctx.arc(c.width/2,c.height/2,r,0,Math.PI*2);
	ctx.fill();
	ctx.closePath();

	window.requestAnimationFrame(draw);
}

circle.addEventListener("click", draw);
var c = document.getElementById("screen");
var ctx = c.getContext("2d");

var circle = document.getElementById("dvd");
var stop = document.getElementById("stop");

var logo = new Image();
logo.src = "logo.jpg";

var lwidth = 100;
var lheight = 75;

ctx.fillStyle = '#FF0000';

function drawBorder(){
	ctx.strokeRect(0,0,500,500);
}

drawBorder();

var x = Math.floor((Math.random() * (c.width-lwidth))); //to ensure it won't start out of bounds
var y = Math.floor((Math.random() * (c.height-lheight)));
var xvel = 2;
var yvel = 2;
var stopped = false;

var draw = function(){
	if( stopped ){
		return; //not really efficient but eh
	}
	if( x <= 0 || x >= (500 - lwidth) ){
		xvel = -xvel;
	}
	if( y <= 0 || y >= (500 - lheight) ){
		yvel = -yvel;
	}

	x+=xvel;
	y+=yvel;

	ctx.clearRect(0,0,500,500);
	drawBorder();
	ctx.beginPath();
	ctx.drawImage(logo,x,y,lwidth,lheight);
	ctx.closePath();
	drawBorder(); //draw it again in case the image overlaps the border

	window.requestAnimationFrame(draw);
}

circle.addEventListener("click", draw);
stop.addEventListener("click", function(){
	stopped = true; //as it works now, once it it stopped it can't be started again 
})
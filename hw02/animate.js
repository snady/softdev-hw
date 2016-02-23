var c = document.getElementById("flag");
var ctx = c.getContext("2d");

var circle = document.getElementById("circle");
var stop = document.getElementById("stop");

ctx.fillStyle = '#FF0000';

function drawBorder(){
	ctx.strokeRect(0,0,500,500);
}

drawBorder();

var r = 0;
var grow = true;
var stopped = false;

var draw = function(){
	if( stopped ){
		return;
	}
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
stop.addEventListener("click", function(){
	stopped = true;
})
var c = document.getElementById("playground"); //searches the DOM for an element with the given ID and returns it (null if none iirc)
var ctx = c.getContext("2d"); //gives the canvas a context with which we can interact/draw on it with

var clear = document.getElementById("clear");

ctx.fillStyle = '#FF0000'; //sets the color/style for filling (doesn't actually fill)
ctx.strokeStyle = '#FF0000';

function drawBorder(){
	ctx.strokeRect(0,0,538,538); //really cheap border lol
}

drawBorder();

/* VERSION 2 
The first version had an issue of varying line thicknesses between points because the entire path was stroked with each new point
This version corrects that issue, but the line overlaps with the circles
*/

ctx.beginPath();

c.addEventListener("click", function(e){
	
	var mouseX = e.offsetX;
	var mouseY = e.offsetY;

	//console.log(mouseX);
	//console.log(mouseY);

	ctx.lineTo(mouseX,mouseY);
	ctx.moveTo(mouseX,mouseY);
	ctx.arc(mouseX,mouseY,10,0,Math.PI*2);

	ctx.stroke();
	ctx.fill();

	ctx.closePath();
	ctx.beginPath();
	ctx.moveTo(mouseX,mouseY);
	
});

clear.addEventListener("click", function(e){
	ctx.clearRect(0,0,538,538);
	drawBorder();
	ctx.closePath();
	ctx.beginPath();
});
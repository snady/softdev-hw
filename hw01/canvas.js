var c = document.getElementById("ftb2maga"); //searches the DOM for an element with the given ID and returns it (null if none iirc)
var ctx = c.getContext("2d"); //gives the canvas a context with which we can interact/draw on it with


ctx.fillStyle = '#FF0000'; //sets the color/style for filling (doesn't actually fill)
ctx.fillRect(10,10,50,50); //fills a rectangle at x,y with length and width specified

ctx.strokeStyle = '#FF0000'; //sets the color/style for strokes (doesn't actually stroke)

ctx.beginPath(); //creates a new path

ctx.moveTo(100,100); //'moves' to x,y and sets it to the current point in the context
ctx.lineTo(100,125); // draws a line from the current point in context to specified x,y

ctx.moveTo(200,100); 
ctx.lineTo(200,125);

ctx.moveTo(150,150);

ctx.arc(150,150,75,Math.PI,0,true); //draws an arc given center x,y, radius, start and end

ctx.closePath(); //ends the current path

ctx.stroke(); //strokes the path
ctx.fill(); //fills the path

ctx.font = '30px tahoma'; //sets the font style

ctx.fillText('Killer Whale Party',50,275); //displays text at given x,y



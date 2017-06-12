$(document).ready(function(){
	function drawLine() {
		var c1 = document.getElementById("myCanvas");
		var ctx1 = c1.getContext("2d");
		ctx1.moveTo(0,0);
		ctx1.lineTo(200,100);
		ctx1.strokeStyle="#FF0000";
		ctx1.stroke();
	}
	
	function drawCircle() {
		var c2 = document.getElementById("myCanvas");
		var ctx2 = c2.getContext("2d");
		ctx2.beginPath();
		ctx2.arc(95, 50, 40, 0, 2*Math.PI);  // (x,y,r,startangle,endangle)
		ctx2.strokeStyle="#FF00FF";
		ctx2.stroke();
	}

	function drawText(){
		var c3 = document.getElementById("myCanvas");
		var ctx3 = c3.getContext("2d");
		ctx3.font = "30px Comic Sans MS";
		ctx3.fillStyle = "blue";
		ctx3.textAlign = "center";
		ctx3.fillText("Hello World", c3.width/2, c3.height/2); 
	}

	function drawStrokeText(){
		var c4 = document.getElementById("myCanvas");
		var ctx4 = c4.getContext("2d");
		ctx4.font = "30px Arial";
		ctx4.strokeText("Hello World", 10, 50);
	}

	function drawGradientStroke() {
		var c5 = document.getElementById("myCanvas");
		var ctx5 = c5.getContext("2d");

		ctx5.font = "30px Verdana";
		// Create gradient
		var gradient1 = ctx5.createLinearGradient(0,0,c5.width,0);
		gradient1.addColorStop("0","magenta");
		gradient1.addColorStop("0.5","blue");
		gradient1.addColorStop("1.0","red");
		// Fill with gradient
		ctx5.strokeStyle = gradient1;
		ctx5.strokeText("Big smile!", 10, 50);
	}

	function drawLinearGradient(){
		var c6 = document.getElementById("myCanvas");
		var ctx6 = c6.getContext("2d");

		// Create gradient.  (starting: x,y, ending: x1,y1)
		var grd = ctx6.createLinearGradient(50, 30, 200, 0);  // left - right
		// var grd = ctx.createLinearGradient(0, 0, 0, 200);  // top - bottom
		grd.addColorStop(0, "red");
		grd.addColorStop(0.3, "yellow");
		grd.addColorStop(0.7, "white");
		grd.addColorStop(1, "green");

		// Fill with gradient
		ctx6.fillStyle = grd;
		ctx6.fillRect(70, 170, 200, 80);  // (pos: x, py, size: x1, y1)
	}

	function drawCircularGradient(){
		var c7 = document.getElementById("myCanvas");
		var ctx7 = c7.getContext("2d");

		// Create gradient.  (x,y,r,x1,y1,r1)
		var grd = ctx7.createRadialGradient(75, 50, 5, 90, 60, 100);
		grd.addColorStop(0, "red");
		grd.addColorStop(1, "white");

		// Fill with gradient
		ctx7.fillStyle = grd;
		ctx7.fillRect(10, 10, 150, 80);
	}

	function drawGradientRect() {
		var c8 = document.getElementById("myCanvas");
		var ctx8 = c8.getContext("2d");

		var gradient2 = ctx8.createLinearGradient(0,0,170,0);
		gradient2.addColorStop("0","magenta");
		gradient2.addColorStop("0.5","blue");
		gradient2.addColorStop("1.0","red");

		// Fill with gradient
		ctx8.strokeStyle = gradient2;
		ctx8.lineWidth = 5;
		ctx8.strokeRect(20,20,150,100);
	}

	function drawImage(){
		var c9 = document.getElementById("myCanvas");
		var ctx9 = c9.getContext("2d");
		var img = document.getElementById("scream");
		ctx9.drawImage(img, 10, 10);  // (x, y, h, w)
	}

	function drawImageRepeat(){
		var c10 = document.getElementById("myCanvas");
		var ctx10 = c10.getContext("2d");
		var img = document.getElementById("lamp");
		// 'repeat', 'no-repeat', 'repeat-x', or 'repeat-y'
		var pat = ctx10.createPattern(img, "repeat");
		ctx10.rect(0,0,150,100);
		ctx10.fillStyle = pat;
		ctx10.fill();
	}

	function drawCanvas(){
		// drawLinearGradient();
		// drawCircularGradient();
		// drawGradientRect();
		// drawImage();
		// drawImageRepeat();
		// drawLine();
		// drawCircle();
		// drawText();
		// drawStrokeText();
		drawGradientStroke();
		
	}
	window.onload = drawCanvas();
});
let char_width = 12;
let bg = 34;

class Traveler {
	constructor(start){
		this.y = start;
		this.x = 0;
	}

	step(){
		strokeWeight(2);
		stroke(127, 63, 255);

		if ( random(1) > 0.5 )
			line(this.x,this.y, this.x+char_width, this.y+char_width);
		else
			line(this.x,this.y + char_width, this.x+char_width, this.y);

		fill(bg);
		stroke(bg);
		this.x += char_width;
		if(this.x > width){
			this.x = 0;
			rect(this.x, this.y, char_width, char_width)
		}
		rect(this.x+char_width, this.y, char_width, char_width)
	}
}

let col_arr = [];
function init_arr() {
	var counter = 0;
	while (counter <= height){
		col_arr.push(new Traveler(counter));
		counter += char_width;
	}
}

let p5canvas;
function setup() {
	var p = document.getElementById("canvasContain");
	p5canvas = createCanvas(windowWidth, p.clientHeight);
	p5canvas.parent("canvasContain");
	//resizeCanvas(windowWidth, canvas.height);
	background(bg);
	init_arr();
	document.documentElement.style.overflow = 'hidden';
	frameRate(15);
}

function draw() {
	background(bg,bg,bg,04);
	col_arr.forEach( col => { col.step(); });
}

function windowResized() {
	var p = document.getElementById("canvasContain");
	resizeCanvas(windowWidth, p.clientHeight);
	background(bg);
	col_arr = [];
	init_arr();
}

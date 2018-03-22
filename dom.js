let content = [];
let head = [];
let dates = [];

function setup(){
	content = selectAll(".content");
	head = selectAll("h2", ".content");
	dates = selectAll("h6",".content");
	console.log("heck");
	for( var i = 0; i < content.length; i++){
		if ( i % 3 == 0 ){
			content[i].style('background-color', "#7f3fff");
			content[i].style('color', "#fff");
			head[i].style("color", "#fff");
			head[i].style("padding-top", content[i].height /2 - head[i].height+ "px");
			dates[i].style("color","#323232");
		}else if (i % 3 ==2){
			content[i].style('background-color', "#fff");
			content[i].style('color', "#7f3fff");
			head[i].style("padding-top", content[i].height /2 - head[i].height+ "px");
			dates[i].style("color","#323232");
		}else {
			content[i].style('background-color', "#9D61FE");
			content[i].style('color', "#323232");
			head[i].style("color", "#323232");
			head[i].style("padding-top", content[i].height /2 - head[i].height+ "px");
			dates[i].style("color","#323232");
		}
	}
}

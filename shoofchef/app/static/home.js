var bg;
var sf;
var i;

var lst = {};

function preload() {
    bg = loadImage("./static/img/photo.png")
    inst= loadImage("./static/inst.png")
}

function setup() {
    createCanvas(bg.width, bg.height);
    background(100)
    image(bg, 0, 0)
    inst.resize(bg.width/2,0)
    image(inst,(bg.width/2)-(inst.width/2),0)
    sf = 1 * (bg.width / data["width"]);
}

function draw() {
    stroke(74, 134, 232);
    strokeWeight(4);
    for (i = 0; i < data["response"].length; i++) {
        line(data["response"][i]["boundingPoly"]["vertices"][3]["x"] * sf,
            data["response"][i]["boundingPoly"]["vertices"][3]["y"] * sf,
            data["response"][i]["boundingPoly"]["vertices"][2]["x"] * sf,
            data["response"][i]["boundingPoly"]["vertices"][2]["y"] * sf);
    }
}

function mouseClicked() {
    console.log(mouseX,mouseY);
    console.log(data["response"][0]["boundingPoly"]["vertices"][3]["x"] * sf,
            data["response"][0]["boundingPoly"]["vertices"][3]["y"] * sf - 40,
            data["response"][0]["boundingPoly"]["vertices"][2]["x"] * sf,
            data["response"][0]["boundingPoly"]["vertices"][2]["y"] * sf + 40)
    for (i = 0; i < data["response"].length; i++) {
        if(mouseX >= (data["response"][i]["boundingPoly"]["vertices"][3]["x"] * sf)
            && (mouseX <= data["response"][i]["boundingPoly"]["vertices"][2]["x"] * sf)
            && (mouseY >= data["response"][i]["boundingPoly"]["vertices"][3]["y"] * sf - 40)
            && (mouseY <= data["response"][i]["boundingPoly"]["vertices"][2]["y"]  * sf + 40)) {
                        console.log(mouseX,mouseY);
            if(data["response"][i]["description"] == "Hommus") {
                document.location.href ="http://localhost:8000/views/0/";
            } else if (data["response"][i]["description"] == "Baba") {
                document.location.href ="http://localhost:8000/views/1/";
            } else if (data["response"][i]["description"] == "ghannuge") {
                document.location.href ="http://localhost:8000/views/1/";
            } else if (data["response"][i]["description"] == "Koossa" ) {
                document.location.href ="http://localhost:8000/views/2/";
            } else if (data["response"][i]["description"] == "bil") {
                document.location.href ="http://localhost:8000/views/2/";
            }
            else if (data["response"][i]["description"] == "tahine") {
                document.location.href ="http://localhost:8000/views/2/";
            }
        }
    }
}



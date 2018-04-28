var bg;
var sf;
var i;

function preload() {
    bg = loadImage("./static/img/photo.png")
}

function setup() {
    createCanvas(bg.width, bg.height);
    background(100)
    image(bg, 0, 0)
    sf = 1 * (bg.width / 1275);
}

function draw() {
    stroke(74, 134, 232)
    strokeWeight(4)
    for (i = 1; i < data.length; i++) {
        line(data[i]["boundingPoly"]["vertices"][3]["x"] * sf,
            data[i]["boundingPoly"]["vertices"][3]["y"] * sf,
            data[i]["boundingPoly"]["vertices"][2]["x"] * sf,
            data[i]["boundingPoly"]["vertices"][2]["y"] * sf);
    }

}
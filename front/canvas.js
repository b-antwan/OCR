//Canvas Script for drawing
var canvas = document.getElementById("can");
canvas.height = 700;
canvas.width = 700;
var bounds = document.getElementById("can").getBoundingClientRect();

var image = new Array(400);
image.fill(0);

var mouse = 0;
document.body.onmousedown = function () {
  mouse = 1;
}
document.body.onmouseup = function () {
  mouse = 0;
}

var ctx = canvas.getContext('2d');

function initCanvas(width) {
  image.fill(0);
  ctx.clearRect(0, 0, bounds.width, bounds.height);

  /** initialisation du dessin sur Canvas */
  ctx.beginPath();
  ctx.lineWidth = 2;
  ctx.strokeStyle = "black";

  for (let i = 0; i < bounds.width; i += bounds.width / 20.0) {
    ctx.moveTo(i, 0);
    ctx.lineTo(i, bounds.width);
  }
  ctx.stroke();

  for (let i = 0; i < bounds.width; i += bounds.width / 20.0) {
    ctx.moveTo(0, i);
    ctx.lineTo(bounds.width, i);
  }
  ctx.stroke();

  ctx.closePath();

  canvas.setAttribute("border", "2px solid black ");

  canvas.addEventListener('click', clickHandler);
  canvas.addEventListener('mousemove', clickHandler);

}


function getIndex(e) {
  return [e.layerX / (bounds.width / 20) - 0.34, e.layerY / (bounds.width / 20) - 0.34];
}



function clickHandler(e) {
  if (mouse) {
    let x = Math.floor(getIndex(e)[0]);
    let y = Math.floor(getIndex(e)[1]);

    //fill x y square
    ctx.fillStyle = "black";

    ctx.fillRect(x * bounds.width / 20, y * bounds.width / 20, bounds.width / 20, bounds.width / 20);
    image[x + 20 * y] = 1;
  }
}


async function sendTable() {
  let toSend = { content: image };
  let lol = fetch("http://127.0.0.1:8000/items/",
    {
      method: "POST",
      body: JSON.stringify(toSend)
    }).then(async function (result) {
      res = await result.json();
      document.getElementById("bars").innerHTML = "";
      console.log(res);
      for(let i = 0; i < 10; i++){
        document.getElementById("bars").innerHTML += "<div class='max'><div class='progres' id='"+i+"bar'><div>";
        document.getElementById(i+"bar").innerHTML = i;
        document.getElementById(i+"bar").style = "width: " + (res[0][i]*100)  + "%";
      }

    });

}

async function getResults() {
  fetch("http://127.0.0.1:8000/items/result/",
    {
      method: "GET",
    }).then(function (res) { return res.json();})
      .then(result => console.log(result));
}


async function sendTrainingTable() {
  let e = document.getElementById("selector");
  let value = e.value;

  let toSend = {
    content: image,
    val: parseInt(value)
  }
  const response = await fetch("http://127.0.0.1:8000/items/training/",
    {
      method: "POST",
      body: JSON.stringify(toSend),
    })
  return response;

}

async function trainFromFiles() {
  const response = await fetch("http://127.0.0.1:8000/items/training/files/",
    {
      method: "GET",
    })
  return response;
}

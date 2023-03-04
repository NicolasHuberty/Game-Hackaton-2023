var bonus1 = true;
var bonus2 = true;
var bonus3 = true;
var bonus4 = true;
var pointsPlayer1 = 0;
var activeBonus = []
var pause = false 

function pauseGame() {
    if (pause == false){
    pause = true;
    document.getElementById('pause-button').textContent = 'Play'
    }
    else{
        pause = false;
        document.getElementById('pause-button').textContent = 'Pause'
    }
}

function changePlayerPoint(number){
    pointsPlayer1 = number
    document.getElementById('points-player1').textContent = number;
}

function setBonusActive(bonus) {
  if (bonus === 'bonus1') {
    bonus1 = false;
    activeBonus.push('bonus1')
  }
  else if (bonus === 'bonus2') {
    bonus2 = false;
    activeBonus.push('bonus2')
  }
  else if (bonus === 'bonus3') {
    bonus3 = false;
    activeBonus.push('bonus3')
  }
  else if (bonus === 'bonus4') {
    bonus4 = false;
    activeBonus.push('bonus4')
  }
}

setInterval(function() {
    if (!pause) {
    document.querySelector('.container').innerHTML = '';
    if (bonus1) {
        document.querySelector('.container').innerHTML += '<button class="bonus-button" onclick="setBonusActive(\'bonus1\')">bonus1</button>';
    }
    if (bonus2) {
        document.querySelector('.container').innerHTML += '<button class="bonus-button" onclick="setBonusActive(\'bonus2\')">bonus2</button>';
    }
    if (bonus3) {
        document.querySelector('.container').innerHTML += '<button class="bonus-button" onclick="setBonusActive(\'bonus3\')">bonus3</button>';
    }
    if (bonus4) {
        document.querySelector('.container').innerHTML += '<button class="bonus-button" onclick="setBonusActive(\'bonus4\')">bonus4</button>';
    }
    }
    else{
        document.querySelector('.container').innerHTML = '<h1>The Game is paused </h1>';
    }


}, 500);
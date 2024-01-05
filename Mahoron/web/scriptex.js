// widow.onload = jsStartUp;
let isPlaying = false;


function jsPlayNext() {

    eel.nextTrack();
    eel.timely();
    isPlaying = true;
    document.getElementById("playpause").className = "fas fa-pause fa-lg";
    document.getElementById("seek-slider").value = 0;
}



function jsPlayPrevious() {
    eel.previousTrack();
    eel.timely()
    isPlaying = true;
    document.getElementById("playpause").className = "fas fa-pause fa-lg";
    document.getElementById("seek-slider").value = 0;
}

eel.expose(jsPlayPause);
function jsPlayPause() {

    eel.PlayPause();
    if (!isPlaying) {
        isPlaying = true;
        document.getElementById("playpause").className = "fas fa-pause fa-lg";
    }
    else {

        isPlaying = false;
        document.getElementById("playpause").className = "fas fa-play fa-lg";
    }
}




/* Set the width of the side navigation to 250px */
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}

function openNav2() {
    document.getElementById("mySidenav2").style.width = "250px";
}

function openNav3() {

}

/* Set the width of the side navigation to 0 */
function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}

function closeNav2() {
    document.getElementById("mySidenav2").style.width = "0";
}

function Megu() {
    document.getElementById("animegif").src = "megu.gif";
}

function Chika() {
    document.getElementById("animegif").src = "chika.gif";
}

function Zerotwo() {
    document.getElementById("animegif").src = "zerotwo.gif";
}
function Amat() {
    document.getElementById("animegif").src = "amaterasu.gif";
}

eel.expose(rename);
function rename(title) {
    title = title.replace('.mp3', '');
    document.getElementById("songTitle").innerHTML = title;
}

eel.expose(timely)
function timely() {
    eel.timely()
}

eel.expose(updatemaxdur)
function updatemaxdur(dur) {
    document.getElementById("seek-slider").max = dur;
}


eel.expose(sstomm);
function sstomm(durslide) {
    document.getElementById("duration").innerHTML = durslide;
    document.getElementById("cropend").value = durslide;


}


eel.expose(slidevalue);
//Slider Value
function slidevalue(outputVar) {
    var output = document.getElementById("seek-slider");
    output.value = outputVar;
    console.log("slide value " + output.value);
    eel.setpos(output.value);
}





var interval = setInterval(continousvalue, 1000);


eel.expose(continousvalue);
function continousvalue() {
    if (isPlaying == true) {
        output = parseInt(document.getElementById("seek-slider").value);
        output = output + 1;
        document.getElementById("seek-slider").value = output;
        console.log("output " + output);
        console.log("seeker value " + document.getElementById("seek-slider").value)
        mm = continoussstomm(document.getElementById("seek-slider").value)
        document.getElementById("current-time").innerHTML = mm
    }
}



function continoussstomm(totalSeconds) {
    totalSeconds %= 3600;
    minutes = Math.floor(totalSeconds / 60);
    seconds = totalSeconds % 60;
    if (seconds < 10) {
        return "0" + minutes + ":" + "0" + seconds
    }
    else {
        return "0" + minutes + ":" + seconds
    }
}


eel.expose(tozero)
function tozero() {
    document.getElementById("seek-slider").value = 0;
}

function crop() {
    eel.cropwrap()
}

eel.expose(convert)
function convert() {
    con = document.querySelector('input[name="audioform"]:checked').value;
    alert("Consider it done" + con)

    if (con == "ogg") {
        eel.convert2ogg()
    }
    else if (con == "wav") {
        eel.convert2wav()
    }
    else if (con == "flv") {
        eel.convert2flv()
    }
}



function endgame() {
    document.location='index3.html';

}

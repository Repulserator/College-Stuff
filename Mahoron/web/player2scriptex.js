let isPlaying2 = false;


function init() {
    eel.StartUp2();
    eel.timely();
    document.getElementById("seekslider1").value = document.getElementById("seekslider1").max;
    eel.timely2();
    eel.initi();

}


eel.expose(rename2);
function rename2(title) {
    title = title.replace('.mp3', '');
    document.getElementById("songTitle2").innerHTML = title;
}


eel.expose(jsPlayPause2);
function jsPlayPause2() {

    eel.PlayPause2();
    if (!isPlaying2) {
        isPlaying2 = true;
        document.getElementById("playpause2").className = "fas fa-pause fa-lg";
    }
    else {

        isPlaying2 = false;
        document.getElementById("playpause2").className = "fas fa-play fa-lg";
    }
}



function jsPlayNext2() {

    eel.p2nextTrack();
    eel.timely2()
    document.getElementById("playpause").className = "fas fa-play fa-lg";
    document.getElementById("seekslider2").value = 0;
}


function jsPlayPrevious2() {
    eel.p2previousTrack();
    eel.timely2()
    document.getElementById("playpause").className = "fas fa-pause fa-lg";
    document.getElementById("seekslider2").value = 0;
}

eel.expose(updatemaxdur1)
function updatemaxdur1(dur) {
    console.log("maxgiven")
    document.getElementById("seekslider1").max = dur;
    document.getElementById("seekslider2").max = dur;
    document.getElementById("seekslider1").value = dur;
}


eel.expose(updatemaxdur2)
function updatemaxdur2(dur) {
    document.getElementById("seekslider3").max = dur;
    document.getElementById("seekslider4").max = dur;
    document.getElementById("seekslider3").value = dur;
}


eel.expose(sstomm2);
function sstomm2(durslide) {
    document.getElementById("duration2").innerHTML = durslide;
}



var interval = setInterval(continousvalue, 1000);
function continousvalue() {
    if (isPlaying == true) {
        output = parseInt(document.getElementById("seekslider2").value);
        output = output + 1;
        document.getElementById("seekslider2").value = output;
        console.log("output " + output);
        console.log("seeker value " + document.getElementById("seekslider2").value)
        mm = continoussstomm(document.getElementById("seekslider2").value)
        document.getElementById("current-time").innerHTML = mm
    }
}


eel.expose(slidevalue);
//Slider Value
function slidevalue(outputVar) {
    var output = document.getElementById("seekslider2");
    output.value = outputVar;
    console.log("slide value " + output.value);
    eel.setpos(output.value);
}



var interval = setInterval(continousvalue2, 1000);
function continousvalue2() {
    if (isPlaying2 == true) {
        output = parseInt(document.getElementById("seekslider4").value);
        output = output + 1;
        document.getElementById("seekslider4").value = output;
        console.log("output " + output);
        console.log("seeker value " + document.getElementById("seekslider4").value)
        mm = continoussstomm(document.getElementById("seekslider4").value)
        document.getElementById("current-time2").innerHTML = mm
    }
}


eel.expose(slidevalue2);
//Slider Value
function slidevalue2(outputVar) {
    var output = document.getElementById("seekslider4");
    output.value = outputVar;
    console.log("slide value " + output.value);
    eel.setpos2(output.value);
    if(isPlaying2==true){
        jsPlayPause2()
        isPlaying2=false
    }
}


function p1max(value){
    output = parseInt(document.getElementById("seekslider1").value);
    document.getElementById("seekslider1").value = output;
    mm = continoussstomm(document.getElementById("seekslider1").value)
    document.getElementById("duration").innerHTML = mm
}


function p2max(value){
    output = parseInt(document.getElementById("seekslider3").value);
    document.getElementById("seekslider3").value = output;
    mm = continoussstomm(document.getElementById("seekslider3").value)
    document.getElementById("duration2").innerHTML = mm
}


function Overlay(){
eel.overlaylocal()
}


eel.expose(durend)
function durend(){
    variable0 = document.getElementById("seekslider2").value
    variable1 = document.getElementById("seekslider1").value
    variable2 = document.getElementById("seekslider4").value
    variable3 = document.getElementById("seekslider3").value
    variable4 = document.getElementById("offset").value
    var3=variable0+","+variable1+","+variable2+","+variable3+","+variable4
    eel.durends(var3)

}


/*
function clear() {
  document.getElementById('uid').value = '';
  document.getElementById('pwd').value = '';
}
*/

function vpass() {
  var pwd = document.f1.pwd.value;
  var l = pwd.length;
  if (l == 0) {} else if (l < 6) {
    alert("The password needs to be at least 6 characters (Currently:" + pwd.length + ")");
    document.f1.pwd.className = "inp2";
    document.f1.pwd.focus();
  } else if (l > 16) {
    alert("The password exceed 16 characters (Currently:" + pwd.length + ")");
  }
}


var dc = 3;

function verify() {
  if (dc == 0) {
    alert("You have been locked out for too many failed attempts");
    window.close();
  } else {

    var user = document.f1.uid.value;
    var pwd = document.f1.pwd.value;
    var fl = 0;
    var c = 0;
    var k = 0;
    var b = 0;
    var x = 1;
    var y = 0;
    var spc = new Array("#", "$", "%", "^", "#", "(", ")", "&", "!", "[", "]", "*");
    var cmb = new Array('Baam', 'khun', 'rachel', 'rak', 'web', 'ica');
    var pass = new Array(':/');

    if (user.length == 0) {
      alert("Username cant be blank can it?");

    } else if (pwd.length == 0) {
      alert("Password cant be blank can it?");
      b = b + 1;
    }

    for (i = 0; i < user.length; i++) {
      for (i = 0; i < spc.length; i++) {
        if (spc[i] == user[i]) {
          alert("Thats a bit too unique, no special characters");
          y=1;
        }
      }
    }

    for (i = 0; i < cmb.length; i++) {
      if (user == cmb[i] && pwd == 'towerofgod') {
        window.navigator.vibrate(200);
        setTimeout(function() {
          document.location.href = "partn.html";
        }, 100);
        x=0;
        alert("Now redirecting");
      } else if (user == cmb[i]) {
        if (pwd != 'bhavans') {
          c++;
        }
      } else if (user != cmb[i]) {
        fl++;
      }
    }
    if (c == 1) {
      alert("Incorrect password");
      dc = dc - 1;
    }
    if (fl == 6 && y==0) {
      alert("Such a user does not exist");
    }
    if (x == 1) {
      alert("You have " + dc + " tries remaining");
    }
  }
}

function hamburger() {
    var ham_menu = document.getElementById("ham-menu");
    if (ham_menu.style.opacity === "1") {
        ham_menu.style.opacity = "0";
    }
    else{
        ham_menu.style.opacity = "1";
    }

    var line1 = document.querySelector(".line1");
    var line2 = document.querySelector(".line2");
    var line3 = document.querySelector(".line3");

    if ((line1.classList.contains("line1rotate")) && ((line3.classList.contains("line3rotate"))) && (line2.style.opacity === "0")) {
        line1.classList.remove("line1rotate");
        line3.classList.remove("line3rotate");
        line2.style.opacity = "1";
    }
    else{
        line1.classList.add("line1rotate");
        line3.classList.add("line3rotate");
        line2.style.opacity = "0";
    }

    let lines = document.getElementsByClassName("lines");
    Array.from(lines).forEach(function (e) {
        if (e.style.background === "black") {
            e.style.background = "white";
        }
        else{
            e.style.background = "black"
        }
    });

    let ham_links = document.querySelector(".hamburger-links");
    let ham_ls_btn = document.querySelector(".gayab-mode-off");
    if ((ham_links.classList.contains("ham-menu-transition") && (ham_ls_btn.classList.contains("ham-menu-transition")))) {
        ham_links.classList.remove("ham-menu-transition");
        ham_ls_btn.classList.remove("ham-menu-transition")
    }
    else{
        ham_links.classList.add("ham-menu-transition");
        ham_ls_btn.classList.add("ham-menu-transition")
    }
}

var txt = "Welcome to India's Online Management Service";
var i = 0;

function typewriter() {
    if (i < txt.length) {
        document.getElementById("txt").innerHTML += txt.charAt(i);
        i++;
        setTimeout(typewriter, 60);
    }
}
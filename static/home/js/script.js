var txt = "Welcome to India's Online Management Service";
var i = 0;

function typewriter() {
    if (i < txt.length) {
        document.getElementById("txt").innerHTML += txt.charAt(i);
        i++;
        setTimeout(typewriter, 60);
    }
}

var slideIndex = 0;
showSlides();

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("testimonial-head");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}
  slides[slideIndex-1].style.display = "block";
  setTimeout(showSlides, 3000); // Change image every 2 seconds
}
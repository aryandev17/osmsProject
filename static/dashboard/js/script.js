var id_profile_picture = document.getElementById("id_profile_picture");
var pp_label = document.getElementById("pp_label");

function image() {
    if (id_profile_picture.files.length !== 0) {
        pp_label.style.display = "none";
        id_profile_picture.style.display = "block";
    }
}

id_profile_picture.addEventListener("change", image)

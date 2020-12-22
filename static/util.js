
let cross = document.getElementsByClassName("cross");
Array.from(cross).forEach((element)=>{
    element.addEventListener("click", (e)=>{
        if (e.target.parentElement.style.display === "none"){
            e.target.parentElement.style.display = "block";
        }
        else{
            e.target.parentElement.style.display = "none";
        }
    })
})
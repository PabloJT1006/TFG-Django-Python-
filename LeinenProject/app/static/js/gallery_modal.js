
modal=document.getElementsByClassName("modal")

document.querySelectorAll(".modal img").forEach(el=>{
    el.addEventListener("click", function(ev){
    ev.stopPropagation();
    this.parentNode.classList.add("active");
    })

});

document.querySelectorAll(".modal").forEach(el=>{
    el.addEventListener("click", function(ev){
    this.classList.remove("active");
    })

});


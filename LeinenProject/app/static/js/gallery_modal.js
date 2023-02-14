// modal=document.getElementsByClassName("modal")

// $("img").click(function (e) { 
//     e.stopPropagation();
//     $(modal).addClass("active");
    

// });

// $(".modal").click(function (e) { 
//     $(modal).removeClass("active");
    

// });




document.querySelectorAll(".modal img").forEach(el=>{
    el.addEventListener("click", function(ev){
    ev.stopPropagation();
    this.parentNode.classList.add("active");
    })

});

document.querySelectorAll(".modal, img").forEach(el=>{
    el.addEventListener("click", function(ev){
    this.classList.remove("active");
    })

});


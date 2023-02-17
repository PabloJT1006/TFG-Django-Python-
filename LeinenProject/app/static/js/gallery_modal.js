// modal=document.getElementsByClassName("modal")

// $("img").click(function (e) { 
//     e.stopPropagation();
//     $(modal).addClass("active");
    

// });

// $(".modal").click(function (e) { 
//     $(modal).removeClass("active");
    

// });


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


document.querySelectorAll(".modal img").forEach(el=>{
    el.addEventListener("click", function(ev){
        console.log("klk")

    this.parentNode.classList.remove("active");
    })

});


// if (modal.className == "active"){
//     console.log("la concha d etu hermana")
//     document.querySelectorAll(" img").forEach(el=>{
//         el.addEventListener("click", function(ev){
//         this.parentNode.classList.remove("active");
//         })

//     });
// }

console.log(modal)
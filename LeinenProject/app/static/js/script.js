if (document.body.className == 'home'){
    const header = document.querySelector('header');
    
    let prevY= window.scrollY;

    window.addEventListener('scroll',function(){

        if (window.scrollY > 70){
            header.classList.add('solid');
        }else{
            header.classList.remove('solid');
        }
        prevY=window.scrollY;
        
        
    });
    
}

//Configuracion header responsive
hamburger = document.querySelector(".hamburguer");
hamburger.onclick = function(){
    navBar = document.querySelector("nav");
    navBar.classList.toggle("active");
    header.classList.add('solid');
}
//Configuracion del carousel

const nextIcon= '<i class="fa-solid fa-chevron-right"></i>';
const prevIcon= '<i class="fa-solid fa-chevron-left"></i>';


$('.owl-carousel').owlCarousel({
    loop:true,
    margin:0,
    nav:true,
    items:3,
    margin:5,
    responsive:true,
    fluidSpeed:true,
    

    navText:[
        prevIcon,
        nextIcon
    ],
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:3
        }
    }
})

// video carousel



// if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
//     // que se le añada al body de la home la clase mobile, que lo unico que hara será añadirle el boton de ver mas 
//     console.log("klk desde mobiel");
//     if (document.body.className == 'home'){
//         document.body.classList.add("mobile");
//     }

//   } else {
//     // code for desktop devices
//   }




if(/Android|iPad|Windows NT|Silk/i.test(navigator.userAgent) && !/Mobile/i.test(navigator.userAgent)) {
    
    if (document.body.className == "about") {
        
        document.body.classList.add("tablet");
    }
  } 

if(/iPad/i.test(navigator.userAgent)) {
    if (document.body.className == "about") {
        
        document.body.classList.add("tablet");
    }
 
} 
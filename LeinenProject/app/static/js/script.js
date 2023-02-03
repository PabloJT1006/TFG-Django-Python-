if (document.body.className == 'home'){
    const header = document.querySelector('header');
    console.log(header)
    let prevY= window.scrollY;

    window.addEventListener('scroll',function(){
        // if (prevY > window.scrollY){
            
        //     header.classList.remove('off');
        //     console.log('subiendo');
        // }
        // else {
        //     console.log(header)
        //     header.classList.add('off');
        //     console.log('bajando');
        // }


        if (window.scrollY > 70){
            header.classList.add('solid');
        }else{
            header.classList.remove('solid');
        }
        prevY=window.scrollY;


    });

}

//Configuracion del carousel

const nextIcon= '<i class="fa-solid fa-chevron-right"></i>';
const prevIcon= '<i class="fa-solid fa-chevron-left"></i>';


$('.owl-carousel').owlCarousel({
    loop:true,
    margin:10,
    nav:true,
    items:3,
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
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
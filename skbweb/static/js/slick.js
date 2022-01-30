$( document ).ready(function(){
    $('.slider').slick({
        arrows:true,
        dots:true,
        adaptiveHeight: true,
        speed:1000,
        easing:'ease',
        autoplay:true,
        autoplaySpeed:1000,
        infinity:true,
        slidesToShow: 1,
        responsive: [
         
          {
            breakpoint: 650,
            settings: {
              slidesToShow: 1,
              arrows:false,
             
            }
          },
       
        ]
    });
});
$( document ).ready(function(){
  $('.slider2').slick({
      arrows:true,
      dots:true,
      adaptiveHeight: true,
      speed:1000,
      easing:'ease',
      autoplaySpeed:2000,
      infinity:true,
      responsive: [
        
        {
          breakpoint: 900,
          settings: {
          
            arrows:false,
           
          },
         
        },
       
      ]
  });
});
$( document ).ready(function(){
  $('.slides').slick({
      arrows:true,
      dots:true,
      adaptiveHeight: true,
      speed:1000,
      easing:'ease',

      autoplaySpeed:2000,
      infinity:true,
      responsive: [
        
        {
          breakpoint: 900,
          settings: {
          
            arrows:false,
           
          },
         
        },
    
      ]
  });
});

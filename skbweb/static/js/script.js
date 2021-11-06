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
        responsive: [
          {
            breakpoint: 1024,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1,
              infinite: true,
              dots: true,
              

            }
          },
          {
            breakpoint: 600,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1
            }
          },
          {
            breakpoint: 480,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1
            }
          }
          // You can unslick at a given breakpoint now by adding:
          // settings: "unslick"
          // instead of a settings object
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
      autoplay:false,
      autoplaySpeed:1000,
      infinity:true,
      responsive: [
        {
          breakpoint: 1024,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1,
            infinite: true,
            dots: true
          }
        },
        {
          breakpoint: 600,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1
          }
        },
        {
          breakpoint: 480,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1
          }
        }
        // You can unslick at a given breakpoint now by adding:
        // settings: "unslick"
        // instead of a settings object
      ]
  });
});
$( document ).ready(function(){

    $('.yak1').on('click', function(e){
        $('html,body').stop().animate({ scrollTop: $('.con-one').offset().top }, 1000);
        e.preventDefault();
      });
    $('.yak2').on('click', function(e){
        $('html,body').stop().animate({ scrollTop: $('.con-two').offset().top }, 1000);
        e.preventDefault();
      });
    $('.yak3').on('click', function(e){
        $('html,body').stop().animate({ scrollTop: $('.con-three').offset().top }, 1000);
        e.preventDefault();
      });
    $('.yak4').on('click', function(e){
        $('html,body').stop().animate({ scrollTop: $('.con-four').offset().top }, 1000);
        e.preventDefault();
      });
    $('.arrow-up').on('click', function(e){
        $('html,body').stop().animate({ scrollTop: $('header').offset().top }, 1000);
        e.preventDefault();
      });
})


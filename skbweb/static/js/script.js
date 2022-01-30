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
        $('html,body').stop().animate({ scrollTop: $('.block4').offset().top }, 1000);
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


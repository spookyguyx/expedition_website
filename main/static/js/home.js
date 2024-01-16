let swiper = new Swiper(".mySwiper", {
    cssMode: true,
    navigation: {
      nextEl: ".anons_btn_next",
      prevEl: ".anons_btn_prev",
    },
    pagination: {
      el: ".swiper-pagination",
    },
    mousewheel: true,
    keyboard: true,
  });

let swiper2 = new Swiper(".partners-slider", {
    slidesPerView: 1,
    spaceBetween: 40,
    navigation: {
        nextEl: ".patners_btn_next",
        prevEl: ".patners_btn_prev",
    },
    breakpoints: {
        320: {
            slidesPerView: 3,
            spaceBetween: 0,
        },
        767: {
            slidesPerView: 4,
        },
        1200: {
            slidesPerView: 5,
            spaceBetween: 10,
        },
    },
  });
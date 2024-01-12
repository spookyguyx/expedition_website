let swiper = new Swiper(".partners-slider", {
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
            slidesPerView: 5,
        },
        1024: {
            slidesPerView: 5,
            spaceBetween: 10,
        },
    },
  });
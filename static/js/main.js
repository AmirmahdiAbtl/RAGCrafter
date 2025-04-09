/*=============== CHANGE BACKGROUND HEADER ===============*/

const scrollHeader = () =>{
    const header = document.getElementById('header')
    // When the scroll is greater than 50 viewport height, add the scroll-header class to the header tag
    this.scrollY >= 50 ? header.classList.add('scroll-header') 
                       : header.classList.remove('scroll-header')
}
window.addEventListener('scroll', scrollHeader)


/*=============== SERVICES MODAL ===============*/
const modalViews = document.querySelectorAll(".services__modal"),
      modalBtns = document.querySelectorAll(".services__button"),
      modalClose = document.querySelectorAll(".services__modal-close")

let modal = function(modalClick){
    modalViews[modalClick].classList.add("active-modal")
}
modalBtns.forEach((mb, i) =>{
    mb.addEventListener('click', () => {
        modal(i)
    })
})
modalClose.forEach((mc) => {
    mc.addEventListener("click", () => {
        modalViews.forEach((mv) =>{
            mv.classList.remove('active-modal')
        })
    })
})
/*=============== MIXITUP FILTER FOR FORMS ===============*/
/*=============== MIXITUP FILTER FOR FORMS ===============*/
var mixerForms = mixitup(".form__container", {
    selectors: {
        target: '.form__section'
    },
    animation: {
        duration: 300
    },
    load: {
        filter: '.form-a' // This will show only Form A on page load
    }
});

/* Link active tab */
const formTabs = document.querySelectorAll(".work__item");

function activeFormTab() {
    formTabs.forEach(tab => tab.classList.remove("active-work"));
    this.classList.add("active-work");
}

formTabs.forEach(tab => tab.addEventListener("click", activeFormTab));
/*=============== SWIPER TESTIMONIAL ===============*/
var swiperTestimonial = new Swiper(".testimonial__container", {
    spaceBetween: 24,
    loop: true,
    grabCursor: true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    breakpoints: {
        576: {
          slidesPerView: 2,
        },
        768: {
          slidesPerView: 2,
          spaceBetween: 48,
        },
        1052: {
            slidesPerView: 4,
        }
      },
  });

/*=============== SCROLL SECTIONS ACTIVE LINK ===============*/
const sections = document.querySelectorAll('section[id]')
    
const scrollActive = () => {
    const scrollY = window.pageYOffset

    sections.forEach(current => {
        const sectionHeight = current.offsetHeight,
            sectionTop = current.offsetTop - 58,
            sectionId = current.getAttribute('id'),
            sectionsClass = document.querySelector('.nav__menu a[href="#' + sectionId + '"]')

        if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
            sectionsClass.classList.add('active-link')
        } else {
            // Check if sectionsClass is not null before attempting to remove the class
            if (sectionsClass) {
                sectionsClass.classList.remove('active-link')
            }
        }
    })
}

window.addEventListener('scroll', scrollActive)
/*=============== LIGHT DARK THEME ===============*/ 
const themeButton = document.getElementById('theme-button')
const lightTheme = 'light-theme'
const iconTheme = 'bx-sun'

// Previously selected topic (if user selected)
const selectedTheme = localStorage.getItem('selected-theme')
const selectedIcon = localStorage.getItem('selected-icon')

// We obtain the current theme that the interface has by validating the dark-theme class
const getCurrentTheme = () => document.body.classList.contains(lightTheme) ? 'dark' : 'light'
const getCurrentIcon = () => themeButton.classList.contains(iconTheme) ? 'bx bx-moon' : 'bx bx-sun'

// We validate if the user previously chose a topic
if (selectedTheme) {
  // If the validation is fulfilled, we ask what the issue was to know if we activated or deactivated the dark
  document.body.classList[selectedTheme === 'dark' ? 'add' : 'remove'](lightTheme)
  themeButton.classList[selectedIcon === 'bx bx-moon' ? 'add' : 'remove'](iconTheme)
}

// Activate / deactivate the theme manually with the button
themeButton.addEventListener('click', () => {
    // Add or remove the dark / icon theme
    document.body.classList.toggle(lightTheme)
    themeButton.classList.toggle(iconTheme)
    // We save the theme and the current icon that the user chose
    localStorage.setItem('selected-theme', getCurrentTheme())
    localStorage.setItem('selected-icon', getCurrentIcon())
})

/*=============== SCROLL REVEAL ANIMATION ===============*/
const sr = ScrollReveal({
    origin: 'top',
    distance: '60px',
    duration: 2500, 
    delay: 400,
})
sr.reveal(".home__data")
sr.reveal(".home__handle", {delay: 700})
sr.reveal(".home__social .home__scroll", {delay: 900, origin: "bottom"})
function openPopup_dc() {
    document.getElementById("popup_dc").style.display = "block";
}
function closePopup_dc() {
    document.getElementById("popup_dc").style.display = "none";
}

function openPopup_ml() {
    document.getElementById("popup_ml").style.display = "block";
}
function closePopup_ml() {
    document.getElementById("popup_ml").style.display = "none";
}

function openPopup_dl() {
    document.getElementById("popup_dl").style.display = "block";
}
function closePopup_dl() {
    document.getElementById("popup_dl").style.display = "none";
}

function openPopup_gan() {
    document.getElementById("popup_gan").style.display = "block";
}
function closePopup_gan() {
    document.getElementById("popup_gan").style.display = "none";
}

function openPopup_nlp() {
    document.getElementById("popup_nlp").style.display = "block";
}
function closePopup_nlp() {
    document.getElementById("popup_nlp").style.display = "none";
}

function openPopup_ds() {
    document.getElementById("popup_ds").style.display = "block";
}
function closePopup_ds() {
    document.getElementById("popup_ds").style.display = "none";
}

function openPopup_kaggle() {
    document.getElementById("popup_kaggle").style.display = "block";
}
function closePopup_kaggle() {
    document.getElementById("popup_kaggle").style.display = "none";
}

function openPopup_coursera() {
    document.getElementById("popup_coursera").style.display = "block";
}
function closePopup_coursera() {
    document.getElementById("popup_coursera").style.display = "none";
}

function openPopup_tensorflow() {
    document.getElementById("popup_tensorflow").style.display = "block";
}
function closePopup_tensorflow() {
    document.getElementById("popup_tensorflow").style.display = "none";
}
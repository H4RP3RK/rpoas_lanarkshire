console.log('hello');

function sendMail(contactForm) {
    const centerForm = document.querySelector(".contact__form");
    
    emailjs.init("user_80Z1Wpez4mTay5lvoIqSm");

    emailjs.send("gmail", "rpoas", {
        "from_name": contactForm.fullName.value,
        "from_email": contactForm.emailAddress.value,
        "email_details": contactForm.query.value,
    })
    .then(
        function(response) {
            console.log('SUCCESS!', response);
            centerForm.innerHTML = `<h1 class="email-message text-center form-section">Thanks for your email, ${contactForm.fullName.value}. We'll be in touch soon.<br><i class="far fa-thumbs-up"></i></h1>`;
        }, 
        function(error) {
            console.log('FAILED...', error);
            centerForm.innerHTML = `<h1 class="email-message text-center form-section">Sorry ${contactForm.fullName.value}. There's seems to be a problem. Please try to send the email again</h1>`;
        });
    return false;
};

console.log("hello");


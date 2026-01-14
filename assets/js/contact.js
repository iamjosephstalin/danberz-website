document.addEventListener('DOMContentLoaded', () => {
    const contactForm = document.querySelector('form[footerform]');
    if (!contactForm) return;

    const submitBtn = contactForm.querySelector('a[role="button"]');
    const nameInput = contactForm.querySelector('#name');
    const emailInput = contactForm.querySelector('#e-mail');
    const messageInput = contactForm.querySelector('#message');

    const successMsg = document.getElementById('form-success');
    const sendingMsg = document.getElementById('form-sending');
    const errorValidateMsg = document.getElementById('form-error-validate');
    const errorSendingMsg = document.getElementById('form-error-sending');

    function hideMessages() {
        successMsg.classList.add('hidden');
        sendingMsg.classList.add('hidden');
        errorValidateMsg.classList.add('hidden');
        errorSendingMsg.classList.add('hidden');
    }

    function sanitizeInput(str) {
        const temp = document.createElement('div');
        temp.textContent = str;
        return temp.innerHTML;
    }

    function validateEmail(email) {
        return String(email)
            .toLowerCase()
            .match(
                /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
            );
    }

    submitBtn.addEventListener('click', (e) => {
        e.preventDefault();
        hideMessages();

        // 1. Validation
        let isValid = true;
        [nameInput, emailInput, messageInput].forEach(input => {
            input.classList.remove('error');
            if (!input.value.trim()) {
                input.classList.add('error');
                isValid = false;
            }
        });

        if (isValid && !validateEmail(emailInput.value)) {
            emailInput.classList.add('error');
            isValid = false;
        }

        if (!isValid) {
            errorValidateMsg.classList.remove('hidden');
            return;
        }

        // 2. Sanitization (Client-side)
        const formData = {
            name: sanitizeInput(nameInput.value.trim()),
            email: sanitizeInput(emailInput.value.trim()),
            message: sanitizeInput(messageInput.value.trim())
        };

        // 3. Simulated Submission
        sendingMsg.classList.remove('hidden');
        submitBtn.classList.add('pointer-events-none', 'opacity-50');

        // Simulate 2 second delay for network request
        setTimeout(() => {
            sendingMsg.classList.add('hidden');
            submitBtn.classList.remove('pointer-events-none', 'opacity-50');
            successMsg.classList.remove('hidden');
            contactForm.reset();
        }, 2000);
    });
});

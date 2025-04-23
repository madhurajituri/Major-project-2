document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('dataForm');
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        if (validateForm()) {
            form.submit();
        }
    });

    function validateForm() {
        const requiredFields = document.querySelectorAll('[required]');
        let isValid = true;

        requiredFields.forEach(field => {
            if (!field.value.trim()) {
                isValid = false;
                showError(field, 'This field is required.');
            } else {
                hideError(field);
            }
        });

        return isValid;
    }

    function showError(field, message) {
        const errorMessage = field.parentNode.querySelector('.error-message');
        if (errorMessage) {
            errorMessage.textContent = message;
        } else {
            const errorDiv = document.createElement('div');
            errorDiv.classList.add('error-message');
            errorDiv.textContent = message;
            field.parentNode.appendChild(errorDiv);
        }
    }

    function hideError(field) {
        const errorMessage = field.parentNode.querySelector('.error-message');
        if (errorMessage) {
            errorMessage.textContent = '';
        }
    }
});

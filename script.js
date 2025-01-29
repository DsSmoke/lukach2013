// script.js

// Handle form submission
const form = document.getElementById('appointment-form');

form.addEventListener('submit', async (event) => {
    event.preventDefault(); // Prevent the form from submitting the traditional way

    const formData = {
        name: document.getElementById('name').value,
        phone: document.getElementById('phone').value,
        branch: document.getElementById('branch').value,
        service: document.getElementById('service').value
    };

    try {
        const response = await fetch('http://localhost:5000/api/appointments', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        if (response.ok) {
            alert('Запись успешно отправлена!');
            form.reset();
        } else {
            alert('Ошибка при отправке. Попробуйте снова.');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Ошибка при подключении к серверу.');
    }
});

// Highlight selected service
const serviceSelect = document.getElementById('service');
const services = document.querySelectorAll('.service');

serviceSelect.addEventListener('change', () => {
    services.forEach(service => {
        service.classList.remove('highlight');
        if (service.querySelector(`option[value="${serviceSelect.value}"]`)) {
            service.classList.add('highlight');
        }
    });
});

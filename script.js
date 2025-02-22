// script.js
document.addEventListener('DOMContentLoaded', () => {
    const input = document.getElementById('user-input');
    const btn = document.getElementById('send-btn');
    const responseContainer = document.getElementById('response-container');

    async function sendCommand(command) {
        try {
            const response = await fetch('http://localhost:5000/process', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ command })
            });
            
            const data = await response.json();
            appendResponse(data.response);
        } catch (error) {
            appendResponse("Error connecting to J.A.R.V.I.S system");
        }
    }

    function appendResponse(text) {
        const responseElement = document.createElement('div');
        responseElement.textContent = `> ${text}`;
        responseContainer.appendChild(responseElement);
        responseContainer.scrollTop = responseContainer.scrollHeight;
    }

    btn.addEventListener('click', () => {
        const command = input.value.trim();
        if (command) {
            appendResponse(`User: ${command}`);
            sendCommand(command);
            input.value = '';
        }
    });
});

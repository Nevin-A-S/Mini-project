const chatMessages = document.querySelector('.chat-messages');
const messageInput = document.querySelector('#messageInput');
const sendButton = document.querySelector('#sendButton');

sendButton.addEventListener('click', sendMessage);
messageInput.addEventListener('keyup', function(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});

function sendMessage() {
    const message = messageInput.value.trim();
    if (message) {
        const userMessage = createMessageElement('user', message);
        chatMessages.appendChild(userMessage);
        messageInput.value = '';

        fetch('/get_bot_response', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ question: message })
        })
        .then(response => response.json())
        .then(data => {
            const botMessage = createMessageElement('bot', data.response);
            chatMessages.appendChild(botMessage);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
}

function createMessageElement(type, message) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', type);
    messageElement.textContent = message;
    return messageElement;
}

// Web summarizer functionality
const summarizeForm = document.querySelector('#summarizeForm');
const summaryContent = document.querySelector('.summary-content');

summarizeForm.addEventListener('submit', function(event) {
    event.preventDefault();
    const url = this.elements.url.value.trim();
    if (url) {
        print(url)
        print('gigiig')
        fetch('/get_summary', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url: url })
        })
        .then(response => response.json())
        .then(data => {
            summaryContent.textContent = data.summary;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
});
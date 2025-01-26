document.getElementById("send-button").addEventListener("click", function() {
    const userInput = document.getElementById("user-input").value;
    const chatWindow = document.getElementById("chat-window");

    if (userInput) {
        const userMessage = document.createElement("div");
        userMessage.textContent = `You: ${userInput}`;
        chatWindow.appendChild(userMessage);
        document.getElementById("user-input").value = "";

        fetch("http://localhost:5005/webhooks/rest/webhook", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ sender: "user", message: userInput })
        })
        .then(response => response.json())
        .then(data => {
            data.forEach(item => {
                const botMessage = document.createElement("div");
                botMessage.textContent = `Bot: ${item.text}`;
                chatWindow.appendChild(botMessage);
            });
        });
    }
});

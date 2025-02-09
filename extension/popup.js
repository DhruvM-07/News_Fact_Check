document.addEventListener("DOMContentLoaded", function () {
    // Get the score from local storage
    chrome.storage.local.get("credibilityScore", function (data) {
        let scoreElement = document.getElementById("score");
        let messageElement = document.getElementById("message");

        if (data.credibilityScore !== undefined) {
            let score = data.credibilityScore;

            // Display the score
            scoreElement.textContent = `Credibility Score: ${score}`;

            // Set message based on score range
            if (score >= 71) {
                messageElement.textContent = "✅ This website is reliable.";
                messageElement.style.color = "green";
            } else if (score >= 35) {
                messageElement.textContent = "⚠️ This website is unchecked/unreliable.";
                messageElement.style.color = "orange";
            } else {
                messageElement.textContent = "❌ This website may contain fake news!";
                messageElement.style.color = "red";
            }
        } else {
            scoreElement.textContent = "No data available.";
            messageElement.textContent = "";
        }
    });
});

document.addEventListener("DOMContentLoaded", function () {
    chrome.runtime.onMessage.addListener(function (message) {
        if (message.action === "displayScore") {
            let scoreElement = document.getElementById("score");
            if (message.score !== null) {
                scoreElement.textContent = `Credibility Score: ${message.score}/100`;
                scoreElement.style.color = getScoreColor(message.score);
            } else {
                scoreElement.textContent = "No data available";
                scoreElement.style.color = "gray";
            }
        }
    });

    function getScoreColor(score) {
        if (score >= 71) return "green";       // Real news
        if (score >= 35) return "orange";      // Unchecked/Unreliable
        return "red";                          // Fake news
    }
});

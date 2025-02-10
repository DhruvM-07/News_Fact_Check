// Function to extract text content from the webpage
function extractContent() {
  let pageText = document.body.innerText; // Extract all visible text from the page
  return pageText.substring(0, 5000); // Limit to 5000 characters to prevent overflow
}

// Function to send the extracted content to the backend API
async function analyzeCredibility(textContent) {
  try {
      let response = await fetch("http://127.0.0.1:8000/analyze", { // Ensure this matches your backend API
          method: "POST",
          headers: {
              "Content-Type": "application/json"
          },
          body: JSON.stringify({ text: textContent, url: window.location.href })
      });

      if (!response.ok) {
          throw new Error("Failed to fetch credibility score");
      }

      let data = await response.json();
      return data.score; // The credibility score from the backend
  } catch (error) {
      console.error("Error analyzing credibility:", error);
      return null;
  }
}

// Function to handle the result and send it to the popup
async function sendCredibilityScore() {
  let content = extractContent();
  let score = await analyzeCredibility(content);

  chrome.runtime.sendMessage({ action: "displayScore", score: score });
}

// Execute when the page loads
sendCredibilityScore();

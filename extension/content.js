// Function to extract text content from the webpage
function extractContent() {
  let pageText = document.body.innerText; // Extracts all visible text from the page
  return pageText.substring(0, 5000); // Limit to 5000 characters to prevent overflow
}

// Function to send the extracted content to the backend API
async function analyzeCredibility(textContent) {
  try {
      let response = await fetch("http://127.0.0.1:8000/analyze", { // Ensure this matches your backend endpoint
          method: "POST",
          headers: {
              "Content-Type": "application/json"
          },
          body: JSON.stringify({ text: textContent, url: window.location.href })
      });

      let data = await response.json();
      return data.score; // The credibility score from the backend
  } catch (error) {
      console.error("Error analyzing credibility:", error);
      return null;
  }
}

// Function to update the extension badge with the score
function updateBadge(score) {
  let color = "gray";
  if (score >= 71) color = "green";
  else if (score >= 35) color = "orange";
  else color = "red";

  chrome.runtime.sendMessage({ action: "updateBadge", score: score, color: color });
}

// Main function to run when the page loads
async function main() {
  let content = extractContent();
  let score = await analyzeCredibility(content);

  if (score !== null) {
      updateBadge(score);
      chrome.runtime.sendMessage({ action: "updatePopup", score: score });
  }
}

// Run the script after the page loads
window.onload = main;

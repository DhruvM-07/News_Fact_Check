// Listen for messages from content.js
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === "updateBadge") {
      // Update the badge text with the score
      chrome.action.setBadgeText({ text: message.score.toString(), tabId: sender.tab.id });

      // Set badge color based on credibility score
      chrome.action.setBadgeBackgroundColor({ color: message.color, tabId: sender.tab.id });
  } else if (message.action === "updatePopup") {
      // Store the credibility score in local storage to be accessed by popup.js
      chrome.storage.local.set({ credibilityScore: message.score });
  }
});

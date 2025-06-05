// File: sample.ts

const userInput = '<script>alert("XSS vulnerability");</script>';
const message = `Hello, ${userInput.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#39;')}!`;
const outputElement = document.getElementById('output');
if (outputElement) {
  outputElement.textContent = message;
}
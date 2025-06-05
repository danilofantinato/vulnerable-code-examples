const rootEl = document.getElementById('root');
const queryParams = new URLSearchParams(document.location.search);
const input = queryParams.get("input");

const sanitizedInput = input ? input.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#39;') : '';

rootEl.textContent = sanitizedInput;
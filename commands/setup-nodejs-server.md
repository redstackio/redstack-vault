---
data: >-
  const http = require("http"); http.createServer((request, response) => { let
  body = []; request.on("error", (err) => { response.end("Request Error: " +
  err); }).on("data", (chunk) => { body.push(chunk); }).on("end", () => { body =
  Buffer.concat(body).toString(); console.log("Response");
  console.log(request.headers); console.log(body); console.log("---");
  response.on("error", (err) => { response.end("Response Error: " + err); });
  response.end("Body length: " + body.length.toString() + " Body: " + body); });
  }).listen(5000);
tags:
  - node.js
  - server
type: command
executor: javascript
platforms:
  - Node.js
id: 276c4e05-9cb2-4004-81db-fa704d234d90
created_at: '2025-12-13T09:01:17.219Z'
updated_at: '2025-12-13T09:01:17.219Z'
verified: false
validated: true
submitted: true
---
# Setup Nodejs Server

## Command

```javascript
const http = require("http"); http.createServer((request, response) => { let body = []; request.on("error", (err) => { response.end("Request Error: " + err); }).on("data", (chunk) => { body.push(chunk); }).on("end", () => { body = Buffer.concat(body).toString(); console.log("Response"); console.log(request.headers); console.log(body); console.log("---"); response.on("error", (err) => { response.end("Response Error: " + err); }); response.end("Body length: " + body.length.toString() + " Body: " + body); }); }).listen(5000);
```

## Description

Sets up a Node.js HTTP server that listens on port 5000, processes incoming requests, logs headers and body, and responds with body details. Used to create a test server for reproducing the vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `listen(5000)` | Port to listen on | Yes |

## Examples

### Basic Usage

```javascript
node server.js
```

## Expected Output

Server starts listening on port 5000 and logs request details upon receiving requests.

## Related

- [[procedures/Setup-Node.js-Test-Server]]

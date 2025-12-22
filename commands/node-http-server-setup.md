---
data: >-
  const http = require('http'); http.createServer((request, response) => { let
  body = []; request.on('error', (err) => { response.end("error while reading
  body: " + err) }).on('data', (chunk) => { body.push(chunk); }).on('end', () =>
  { body = Buffer.concat(body).toString(); response.on('error', (err) => {
  response.end("error while sending response: " + err) });
  response.end(JSON.stringify({ "URL": request.url, "Headers": request.headers,
  "Length": body.length, "Body": body, }) + "\n"); }); }).listen(80);
tags:
  - node.js
  - http-server
type: command
executor: javascript
platforms:
  - Node.js
id: 0a59fbb3-f922-4e0c-90da-2dc9a765ac43
created_at: '2025-12-13T09:01:17.375Z'
updated_at: '2025-12-13T09:01:17.375Z'
verified: false
validated: true
submitted: true
---
# Node HTTP Server Setup

## Command

```javascript
const http = require('http'); http.createServer((request, response) => { let body = []; request.on('error', (err) => { response.end("error while reading body: " + err) }).on('data', (chunk) => { body.push(chunk); }).on('end', () => { body = Buffer.concat(body).toString(); response.on('error', (err) => { response.end("error while sending response: " + err) }); response.end(JSON.stringify({ "URL": request.url, "Headers": request.headers, "Length": body.length, "Body": body, }) + "\n"); }); }).listen(80);
```

## Description

Creates a simple Node.js HTTP server that listens on port 80 and echoes back the received request's URL, headers, body length, and body content in JSON format. Used for testing HTTP request parsing vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `listen(80)` | Specifies the port to listen on | Yes |

## Examples

### Basic Usage

```javascript
// Run in Node.js environment
node server.js
```

## Expected Output

Server starts listening on port 80 and responds with JSON-formatted request details upon receiving requests.

## Related

- [[procedures/Setup-Node.js-Test-Server-for-Vulnerability-Testing]]

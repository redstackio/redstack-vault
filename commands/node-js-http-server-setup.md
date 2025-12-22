---
data: >-
  const http = require('http'); http.createServer((request, response) => { let
  body = []; request.on('error', (err) => { response.end('error while reading
  body: ' + err) }).on('data', (chunk) => { body.push(chunk); }).on('end', () =>
  { body = Buffer.concat(body).toString(); response.on('error', (err) => {
  response.end('error while sending response: ' + err) });
  response.end(JSON.stringify({ 'Headers': request.headers, 'Length':
  body.length, 'Body': body, }) + '\n'); }); }).listen(80);
tags:
  - node-js
  - http-server
type: command
executor: javascript
platforms:
  - Node.js
id: d53de9eb-7f60-4799-9a80-ffefa4958e03
created_at: '2025-12-13T09:01:17.316Z'
updated_at: '2025-12-13T09:01:17.316Z'
verified: false
validated: true
submitted: true
---
# node-js-http-server-setup

## Command

```javascript
const http = require('http'); http.createServer((request, response) => { let body = []; request.on('error', (err) => { response.end('error while reading body: ' + err) }).on('data', (chunk) => { body.push(chunk); }).on('end', () => { body = Buffer.concat(body).toString(); response.on('error', (err) => { response.end('error while sending response: ' + err) }); response.end(JSON.stringify({ 'Headers': request.headers, 'Length': body.length, 'Body': body, }) + '\n'); }); }).listen(80);
```

## Description

Sets up a Node.js HTTP server that listens on port 80, handles incoming requests by collecting the body, and responds with JSON containing headers, body length, and body. Used for testing vulnerability in request parsing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `listen` | Specifies the port (80) to listen on | Yes |
| `createServer` | Creates the HTTP server with request and response handlers | Yes |

## Examples

### Basic Usage

```javascript
const http = require('http'); http.createServer((request, response) => { let body = []; request.on('error', (err) => { response.end('error while reading body: ' + err) }).on('data', (chunk) => { body.push(chunk); }).on('end', () => { body = Buffer.concat(body).toString(); response.end(JSON.stringify({ 'Headers': request.headers, 'Length': body.length, 'Body': body, }) + '\n'); }); }).listen(80);
```

## Expected Output

Server starts listening on port 80 and processes requests accordingly.

## Related

- [[procedures/Set-Up-Node-js-Test-HTTP-Server-for-Vulnerability-Testing]]
- [[tools/Node-js]]

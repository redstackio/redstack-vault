---
id: proc-002
tags:
  - node-js
  - http2
  - server-setup
type: procedure
tools:
  - '[[tools/Node.js]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Linux
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:36.750Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Setup-Vulnerable-Node.js-HTTP2-Server

## Summary

This procedure sets up a secure Node.js HTTP2 server using version 12.19.0, which is vulnerable to the unknownProtocol event handling issue, listening on port 50000 with SSL.

## Description

The server is created with the http2 module, loading provided key and cert files. When malformed HTTP/1.1 requests are received over SSL, it triggers the unknownProtocol event in lib/internal/http2/core.js, leading to leaks if the client closes prematurely without responding.

## Requirements

1. Node.js 12.19.0 installed
2. SSL key and certificate files (e.g., key.pem, cert.pem)
3. Write access to filesystem for script creation

## Defense

Defensive measures and detection strategies:

- Upgrade to patched Node.js versions
- Configure ulimit for file descriptors
- Log and alert on unknownProtocol events

## Objectives

1. Deploy a vulnerable HTTP2 server
2. Ensure it handles SSL connections
3. Prepare for attack simulation

## Instructions

### Step 1: Create Server Script

**Context**: Write the JavaScript code to initialize the HTTP2 server.

**Command**:
```bash
cat > server.js << EOF
const http2 = require('http2');
const fs = require('fs');
const server = http2.createSecureServer({
  key: fs.readFileSync('key.pem'),
  cert: fs.readFileSync('cert.pem')
});
server.on('error', (err) => console.error(err));
server.on('unknownProtocol', (socket) => {
  socket.destroy(new Error('Unknown protocol'));
});
server.listen(50000);
console.log('Server running on 50000');
EOF
```

> Creates server.js with basic HTTP2 setup. Expected output: File created.

### Step 2: Run the Server

**Context**: Start the Node.js process.

**Command**:
```bash
node server.js
```

> Launches the server. Expected output: 'Server running on 50000' logged.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Node.js]]

## Tags

- node-js
- http2
- server-setup

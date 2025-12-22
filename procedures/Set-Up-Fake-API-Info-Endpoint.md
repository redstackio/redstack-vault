---
id: proc-fake-api-info-endpoint
tags:
  - api
  - fake-server
  - bypass
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:23:32.824Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Set-Up-Fake-API-Info-Endpoint

## Summary

This procedure sets up a minimal /api/info endpoint returning empty JSON to mimic a legitimate Rocket.Chat server, allowing the Electron app's 'Add new server' feature to proceed and load the subsequent malicious webpage.

## Description

Rocket.Chat's desktop app requires a valid /api/info response before loading the server's index.html. This procedure creates a fake endpoint returning {} to pass validation. It uses a simple web server setup and is a prerequisite for the exploitation chain. Target environment: Any HTTP server accessible to the victim. Expected outcomes: App accepts the server URL without error, enabling page load and JS execution.

## Requirements

1. Web server capable of handling GET requests (e.g., Node.js Express or Python Flask).
2. The same server hosting the malicious HTML from the prior procedure.
3. Port 80 or 443 open for HTTP/HTTPS.

## Defense

Defensive measures and detection strategies:

- Validate API responses with expected schema (e.g., check for version, build info).
- Rate-limit server addition attempts in the app.
- Log and alert on additions of unknown server URLs.

## Objectives

1. Satisfy app's API validation to allow page loading.
2. Maintain stealth by returning minimal valid JSON.
3. Enable chaining to the RCE payload.

## Instructions

### Step 1: Implement the Endpoint

**Context**: Add a route for /api/info that returns empty JSON to pass the app's check.

Example using Node.js and Express (install via npm if needed):

```javascript
const express = require('express');
const app = express();

app.get('/api/info', (req, res) => {
  res.json({}); // Empty JSON as required
});

app.use(express.static('./')); // Serve static files like index.html

app.listen(80, () => console.log('Server running on port 80'));
```

> Save as server.js and run with `node server.js`. Expected: curl http://localhost/api/info returns {}.

### Step 2: Verify Endpoint

**Context**: Test the endpoint to ensure it responds correctly.

Use curl:

```bash
curl http://your-ip/api/info
```

> Expected output: {} (empty JSON object). If not, check server logs for errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[api]]
- [[web-server]]
- [[validation-bypass]]

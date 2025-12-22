---
tags:
  - express
  - web-app
  - xss-vector
type: procedure
tools:
  - '[[tools/node]]'
  - '[[tools/express]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Node.js
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:02.710Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 4f9ce0f3-2a4f-4205-8df7-830d1bb08472
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Develop-Vulnerable-Express-Application

## Summary

This procedure builds a Node.js Express application that uses scrape-metadata to fetch metadata from a malicious URL and renders it unsafely in an HTML response, creating the condition for XSS execution.

## Description

Targeting Node.js web apps that display scraped metadata, this step implements a simple server with an endpoint that performs the scrape and uses template literals with JSON.stringify without additional escaping. The attack scenario involves browser access triggering the payload. Prerequisites: Installed dependencies and basic JavaScript knowledge.

## Requirements

1. Node.js v8.9.3 or compatible
2. scrape-metadata and express installed
3. Text editor for coding the app

## Defense

Defensive measures and detection strategies:

- Escape output using libraries like escape-html
- Validate and sanitize scraped content before rendering
- Implement input/output encoding in templates

## Objectives

1. Create scraping endpoint
2. Render metadata without sanitization
3. Expose the XSS vulnerability on a local port

## Instructions

### Step 1: Write the Application Code

**Context**: Develop scrap.js to require modules, set up the route, and handle the scrape.

No command; code manually.

```javascript
const express = require('express');
const scrape = require('scrape-metadata');
const app = express();

app.get('/scrap', async (req, res) => {
  const meta = await scrape('http://pokegen.in/test.html');
  console.log(meta);
  res.send(`<p>site title: ${JSON.stringify(meta)}</p>`);
});

app.listen(8080, () => {
  console.log('Server running on port 8080');
});
```

> The JSON.stringify includes the og:title payload, which breaks out when rendered in HTML.

### Step 2: Verify Code

**Context**: Ensure no syntax errors.

Run node -c scrap.js (if available) or proceed to execution.

> Expected: No errors, ready for run.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/node]]
- [[tools/express]]

## Tags

- express
- web-app

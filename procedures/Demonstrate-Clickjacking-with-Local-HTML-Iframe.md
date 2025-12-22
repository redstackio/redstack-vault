---
tags:
  - clickjacking
  - ui-redressing
  - iframe
  - x-frame-options
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 44d7d99f-6717-4828-ab06-c939e73856b3
created_at: '2025-12-14T17:28:05.308Z'
updated_at: '2025-12-14T17:28:05.308Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Demonstrate Clickjacking with Local HTML Iframe

## Summary

This procedure tests for Clickjacking (UI Redressing) vulnerabilities by creating a local HTML file that embeds the target website in an iframe. It confirms if the site lacks proper frame-busting protections like the X-Frame-Options header, allowing malicious sites to overlay invisible elements and trick users into performing unintended actions such as form submissions or data exposure.

## Description

Clickjacking exploits the ability to embed web pages in iframes without restrictions, enabling attackers to create overlapping transparent or disguised layers that capture user clicks on the framed content. In this case, the Legal Robot website at https://www.legalrobot.com/ is hosted on AWS S3, which does not natively support custom security headers like X-Frame-Options. Although CloudFlare CDN was in use, it was not configured to add the necessary headers at the time of discovery. The procedure simulates an attacker's malicious page and verifies embedding success, highlighting risks like unauthorized account actions or confidential data disclosure. Prerequisites include a local machine with a text editor and browser; no network privileges or credentials are needed beyond internet access.

## Requirements

1. Text editor for creating and editing HTML files (e.g., Notepad on Windows, TextEdit on macOS, or VS Code).
2. Modern web browser (e.g., Chrome, Firefox) to load and render the local HTML file.
3. Internet connection to fetch the target URL content into the iframe.

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN header on all responses to prevent framing.
- Use Content-Security-Policy (CSP) with frame-ancestors directive to restrict embedding sources.
- For AWS S3-hosted sites, proxy through a server like CloudFlare or AWS CloudFront to add custom headers.
- Monitor for anomalous iframe embeddings via web application firewall (WAF) logs or browser developer tools.

## Objectives

1. Verify if the target site can be embedded in an external iframe without restrictions.
2. Demonstrate potential for UI redressing by loading the framed site locally.
3. Assess impact on user interactions, such as tricking clicks on hidden elements.

## Instructions

### Step 1: Create and Prepare HTML File

**Context**: Start by setting up the malicious page structure that will host the iframe.

Manually create a new file named clickjacking-test.html using your text editor.

> This file will act as the attacker's webpage. Ensure it's saved in an accessible local directory.

### Step 2: Insert Iframe Code to Embed Target

**Context**: Add the iframe element to load the vulnerable site, simulating the attack setup.

Paste the following HTML code into the file and save it:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Clickjacking Demo</title>
</head>
<body>
    <h1>This is a malicious page!</h1>
    <p>If you can see the Legal Robot site below, it's vulnerable to clickjacking.</p>
    <iframe src="https://www.legalrobot.com/" width="500" height="500"></iframe>
</body>
</html>
```

> The iframe src points to the target URL. Dimensions (500x500) are set for visibility; in a real attack, these could be adjusted or made transparent for overlay. Expected output: No syntax errors on save.

### Step 3: Load File in Browser and Validate

**Context**: Execute the test by rendering the page to confirm the vulnerability.

Open the clickjacking-test.html file in your web browser by double-clicking it or using the browser's open file dialog.

> The Legal Robot site should load fully within the iframe without any frame-denied errors. Use browser developer tools (F12) to inspect network requests and confirm no X-Frame-Options header is present in the response.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[ui-redressing]]
- [[web-vulnerability]]

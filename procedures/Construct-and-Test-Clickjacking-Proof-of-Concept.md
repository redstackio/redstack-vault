---
tags:
  - clickjacking
  - iframe
  - x-frame-options
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:13.020Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 96b78eef-a674-44c9-878c-334d753f36dc
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Construct-and-Test-Clickjacking-Proof-of-Concept

## Summary

This procedure outlines the creation and testing of a proof-of-concept (PoC) HTML page that exploits a clickjacking vulnerability on Twitter Periscope subdomains by embedding them in an unrestricted iframe, leveraging the deprecated X-Frame-Options header to enable UI redressing attacks where users can be tricked into performing actions like account deactivation.

## Description

Clickjacking occurs when an attacker embeds a vulnerable webpage in an iframe on a malicious site, overlaying invisible elements to capture user clicks on unintended actions. In this case, the subdomains canary-web.pscp.tv and canary-web.periscope.tv set X-Frame-Options to ALLOW-FROM https://twitter.com/, a value not supported by modern browsers like Chrome and Firefox, allowing arbitrary framing from any origin. The procedure involves manually creating a simple HTML file with an iframe, saving it, and loading it in a browser to confirm the vulnerability. This PoC can be extended to a live malicious site for real attacks, targeting users via drive-by compromise.

## Requirements

1. A text editor to create HTML files (e.g., built-in OS editor or VS Code)
2. A modern web browser (Chrome, Firefox, or Edge) to test embedding
3. Internet access to load the vulnerable subdomains
4. Basic knowledge of HTML and browser developer tools for header inspection

## Defense

Defensive measures and detection strategies:

- Set X-Frame-Options to DENY or SAMEORIGIN to prevent all or cross-origin framing
- Use Content-Security-Policy (CSP) frame-ancestors directive to restrict embedding sources
- Monitor for anomalous iframe usage in web traffic logs and implement frame-busting JavaScript
- Educate users on phishing risks and enable browser protections like SmartScreen

## Objectives

1. Confirm the vulnerability by successfully embedding the subdomain in an iframe
2. Demonstrate potential for clickjacking by verifying interactive elements load without restrictions
3. Validate that the deprecated header allows framing from external sites

## Instructions

### Step 1: Create a New HTML File

**Context**: Start with an empty HTML document to serve as the malicious page base.

Use a text editor to create an empty file. No commands are needed; simply open your preferred editor and begin a new file.

**Expected Output**: An empty .html file ready for content insertion.

### Step 2: Insert Iframe Tag Pointing to the Vulnerable Site

**Context**: Add the iframe element to embed the target subdomain, simulating the attacker's malicious page.

Insert the following HTML code into the file:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Clickjacking PoC</title>
</head>
<body>
    <iframe src="https://canary-web.pscp.tv" frameborder="0" width="100%" height="600"></iframe>
    <!-- Overlay invisible elements here for exploitation, e.g., <button style="position:absolute; opacity:0;">Deactivate</button> -->
</body>
</html>
```

Replace the src with https://canary-web.periscope.tv if testing the other subdomain. This embeds the page without borders, allowing overlays.

**Expected Output**: HTML file with iframe code that, when loaded, attempts to frame the vulnerable site.

### Step 3: Save the HTML File

**Context**: Ensure the file is saved in a browser-executable format.

Save the file with a .html extension, e.g., clickjacking-poc.html, in an accessible local directory.

**Expected Output**: A saved HTML file ready for browser loading.

### Step 4: Open the HTML File in a Browser

**Context**: Test the PoC to confirm the vulnerability by loading the local file and observing the iframe behavior.

Double-click the file or open it via File > Open in your browser. Inspect the network tab in dev tools to verify the X-Frame-Options header is present but ignored, allowing the embed.

**Expected Output**: The Periscope subdomain loads fully within the iframe without denial or restrictions, confirming clickjacking feasibility.

**Success Indicators**:
- No frame-busting errors or blank iframe
- Vulnerable page content is visible and clickable inside the frame
- Browser console shows no blocking for cross-origin framing

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- clickjacking
- iframe-embedding
- web-exploit

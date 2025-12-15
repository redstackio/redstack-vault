---
tags:
  - clickjacking
  - iframe
  - poc
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:12.768Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 8071b34f-5b63-4c92-a512-594b41c62565
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Clickjacking-Iframe-PoC

## Summary

This procedure creates a simple HTML proof-of-concept (PoC) file to demonstrate clickjacking on join.nordvpn.com by embedding the site in an iframe without restrictions, exploiting the absence of X-Frame-Options headers. It enables attackers to overlay invisible elements for tricking users into unintended actions, such as subscribing to services.

## Description

Clickjacking occurs when a malicious site loads a target site in an iframe and overlays transparent elements to capture user clicks on sensitive actions. The join.nordvpn.com site lacks frame-busting protections, allowing embedding from external domains. This PoC verifies the vulnerability locally and can be extended for social engineering attacks. The impact is low severity, primarily facilitating phishing-like coercion without direct data compromise. Prerequisites include a text editor and web browser; no server setup is needed.

## Requirements

1. Text editor installed on the local machine (e.g., Notepad on Windows, TextEdit on macOS, or VS Code)
2. Modern web browser with internet access to load the target URL
3. Basic HTML knowledge for editing the file

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN headers on web servers to prevent iframe embedding
- Use Content-Security-Policy (CSP) with frame-ancestors directive to restrict framing sources
- Monitor for unusual iframe embeddings via web application firewalls (WAF) or browser security tools
- Educate users on verifying site context to avoid social engineering tricks

## Objectives

1. Verify the site's susceptibility to clickjacking by successful iframe embedding
2. Demonstrate potential for user interaction manipulation
3. Highlight the need for header-based protections

## Instructions

### Step 1: Create New HTML File

**Context**: Start a new file to serve as the PoC container for the iframe.

Use a text editor to create a blank HTML file. No specific command is needed; simply open the editor and create a new document.

> This sets up the base structure for embedding the target.

### Step 2: Insert Iframe Code

**Context**: Add the iframe element to load the vulnerable site, specifying dimensions for visibility.

Edit the HTML file and insert the following code:

```html
<!DOCTYPE html>
<html>
<body>
<iframe src="https://join.nordvpn.com" width="500" height="500"></iframe>
</body>
</html>
```

> The iframe src points to the target URL. Adjust width and height as needed. This embeds the site without any frame restrictions.

### Step 3: Save the HTML File

**Context**: Persist the PoC for execution in a browser.

Save the file with a .html extension, e.g., clickjacking-poc.html, in an accessible directory.

> Ensure the file is saved in a location where it can be easily opened by the browser.

### Step 4: Open in Browser

**Context**: Load the PoC to demonstrate the vulnerability.

Open the saved HTML file in a web browser by double-clicking it or using the browser's file open dialog.

> The NordVPN join page should load fully in the iframe. Use browser developer tools (F12) to inspect network requests and confirm no blocking headers like X-Frame-Options are present. To simulate an attack, add overlay elements like transparent divs positioned over buttons.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- clickjacking
- iframe
- web-vulnerability
- poc

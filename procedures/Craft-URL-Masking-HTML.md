---
id: proc-uuid-placeholder
tags:
  - phishing
  - url-masking
  - html-spoofing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Phishing]]'
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:28:04.860Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
  - '[[T1566.002]]'
---
# Craft-URL-Masking-HTML

## Summary

This procedure creates a simple HTML file that exploits URL masking in browsers like Brave by using the `onmouseover` event to spoof the status bar URL, making a link appear to point to a trusted site while actually redirecting to a malicious domain for phishing purposes.

## Description

In the context of the Brave browser vulnerability (based on Chromium/Muon 2.0.19), this procedure involves crafting an HTML link where the visual cues (link text and status bar on hover) suggest navigation to `google.com`, but the actual `href` attribute leads to a malicious site such as `datarift.blogspot.in`. This enables social engineering attacks by tricking users into clicking deceptive links. The technique relies on the browser's handling of the `window.status` property without validation, allowing visual deception. Prerequisites include a text editor and access to save or host HTML files. Expected outcomes include a functional spoofed link that demonstrates the phishing vector.

## Requirements

1. Text editor installed on Windows (e.g., Notepad)
2. Brave browser for testing
3. Optional: Web server to host the HTML file remotely

## Defense

Defensive measures and detection strategies:

- Educate users to verify URLs in the address bar, not just status bar or link text
- Browser extensions like uBlock Origin or NoScript to block suspicious redirects
- Enable strict site isolation and hover URL verification in browser settings
- Monitor for anomalous network traffic to unexpected domains

## Objectives

1. Create a deceptive HTML link for phishing simulation
2. Spoof browser status bar to mimic legitimate navigation
3. Demonstrate redirection to malicious site without user awareness

## Instructions

### Step 1: Create the HTML File

**Context**: Build the core HTML structure with the spoofed link using `onmouseover` to set the status bar text.

No command required; use a text editor to write:

```html
<!DOCTYPE html>
<html>
<head><title>Spoof Test</title></head>
<body>
<a href="http://datarift.blogspot.in" onmouseover="window.status='http://google.com';return true" onmouseout="window.status=''">Click here for Google</a>
</body>
</html>
```

> This code sets the link's href to the malicious URL but overrides the status bar on hover to show google.com, creating the mask.

### Step 2: Save and Prepare for Testing

**Context**: Save the file locally or upload to a server to simulate a real attack vector.

Save as `click.html` in a local directory or host at a URL like http://hackies.in/click.html.

> Expected output: File ready for browser loading, confirming no syntax errors by opening in a basic viewer.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Phishing]] Phishing
- [[T1566.002]] Spearphishing Link

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[url-masking]]
- [[browser-exploitation]]

---
tags:
  - clickjacking
  - frameset
  - html-creation
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
updated_at: '2025-12-14T17:28:12.671Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: f7a08ff7-437f-432e-83ad-4633adef447b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create-HTML-Frameset-to-Embed-Multiple-Semrush-Pages

## Summary

This procedure creates a malicious HTML file using a frameset to embed multiple vulnerable Semrush URLs, demonstrating the potential for clickjacking by framing unprotected pages.

## Description

In a clickjacking attack, an attacker crafts an HTML page that embeds the victim's site in a frame or iframe without the target's knowledge. Here, due to the absence of X-Frame-Options header set to DENY or SAMEORIGIN on Semrush pages, multiple URLs can be framed cross-origin. This setup allows overlaying invisible elements to trick users into clicking on hidden buttons or submitting forms, leading to unauthorized actions like account modifications or data exfiltration. The procedure targets URLs such as https://www.semrush.com/?l=us, https://www.semrush.com/academy/, and https://www.semrush.com/ranking-factors/.

## Requirements

1. Text editor (e.g., Notepad, VS Code) for HTML creation
2. Local file system access to save files
3. Internet access to Semrush domain

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN header on all web pages
- Use Content-Security-Policy (CSP) with frame-ancestors directive to restrict framing
- Monitor for unusual iframe or frameset usage in web traffic logs

## Objectives

1. Construct a frameset that loads multiple Semrush pages without restrictions
2. Simulate a malicious site capable of UI redressing
3. Validate the vulnerability setup for further exploitation testing

## Instructions

### Step 1: Define Frameset Structure

**Context**: Set up the basic HTML structure with a frameset to divide the page into columns for embedding targets.

Create the following HTML content:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Clickjacking Test</title>
</head>
<frameset cols="25%,*,25%">
    <frame src="https://www.semrush.com/?l=us">
    <frame src="https://www.semrush.com/academy/">
    <frame src="https://www.semrush.com/ranking-factors/">
</frameset>
</html>
```

> This creates three columns: left (25%) for one URL, center (full remaining) for another, and right (25%) for the third. Save as frameset.html.

### Step 2: Save and Prepare File

**Context**: Ensure the file is ready for browser loading to test framing.

Save the HTML file to your local directory. No additional commands needed; proceed to verification in the next procedure.

> Expected: File saved without errors, ready for opening in a browser.

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
- [[frameset]]
- [[web-attack]]

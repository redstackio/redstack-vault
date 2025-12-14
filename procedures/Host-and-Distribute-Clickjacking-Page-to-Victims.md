---
id: proc-uuid-3-1171403
tags:
  - phishing
  - hosting
  - xss
  - clickjacking
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:12.737Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Host-and-Distribute-Clickjacking-Page-to-Victims

## Summary

This procedure hosts the clickjacking HTML page on a server and distributes the link to victims via social engineering, inducing clicks that trigger the chained reflected XSS for JavaScript execution and potential data theft.

## Description

After creating the malicious page, hosting it on an external server (e.g., free hosting service) makes it accessible. Distribution leverages phishing emails or links disguised as legitimate DoD communications, tricking users into clicking the overlay, which executes the XSS payload in their authenticated session. This amplifies the attack's reach on sensitive targets, leading to session hijacking. Requires a hosting provider and basic social engineering skills.

## Requirements

1. Web hosting service (e.g., GitHub Pages, VPS, or local server with ngrok for tunneling)
2. Completed clickjacking HTML and image files
3. Distribution channels (email, social media, etc.)
4. Monitoring capability for exploit success (e.g., via callback in payload)

## Defense

Defensive measures and detection strategies:

- Educate users on phishing and suspicious links via security awareness training
- Implement URL filtering and safe browsing tools to block malicious domains
- Monitor for unexpected JavaScript execution or iframe loads in browser telemetry
- Use endpoint detection to flag anomalous browser behavior like sudden alerts or data exfiltration

## Objectives

1. Deploy page for public access
2. Lure victims to interact via deceptive distribution
3. Achieve XSS execution for session theft or data collection

## Instructions

### Step 1: Upload Files to Server

**Context**: Place HTML and image on hosting platform.

Copy the HTML file and '1.png' to server root directory, ensuring public readability.

> Verify by accessing the hosted URL directly.

### Step 2: Generate and Test Link

**Context**: Create shareable URL and confirm functionality.

Obtain the hosted link (e.g., https://attacker.com/clickjack.html) and test in an incognito browser to ensure click triggers XSS.

> Expected: Invisible interaction leads to alert without errors.

### Step 3: Distribute to Victims

**Context**: Send link via targeted phishing.

Craft an email or message: "Urgent DoD update: Click here to view" linking to the page. Target DoD personnel.

> Track opens/clicks if using tracking pixels; monitor for exfiltrated data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[hosting]]

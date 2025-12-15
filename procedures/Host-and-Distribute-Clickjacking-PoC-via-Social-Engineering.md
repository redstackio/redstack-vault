---
tags:
  - phishing
  - hosting
  - social-engineering
  - credential-theft
type: procedure
tools:
  - '[[tools/sites-google-com]]'
tactics:
  - '[[Credential Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 2e2887ec-ad46-445c-ac2c-991a025febc2
created_at: '2025-12-14T17:28:05.381Z'
updated_at: '2025-12-14T17:28:05.381Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Host-and-Distribute-Clickjacking-PoC-via-Social-Engineering

## Summary

This procedure hosts the clickjacking PoC on a public site and distributes it via phishing to trick victims into visiting and entering MailChimp credentials, enabling account takeover.

## Description

After creating the PoC, upload it to a free hosting service like Google Sites. Use social engineering (e.g., emails posing as Stripo support) to send links, luring users to the malicious page where the invisible iframe captures their inputs. Successful exfiltration provides attackers with credentials for MailChimp access, allowing email campaign abuse or data theft.

## Requirements

1. Account on a hosting platform like sites.google.com
2. Phishing delivery method (email, social media)
3. Monitoring setup for received credentials

## Defense

Defensive measures and detection strategies:

- Block or scan links from unknown sources
- Implement multi-factor authentication on OAuth flows
- Use URL scanners to detect malicious redirects or iframes

## Objectives

1. Make the PoC publicly accessible
2. Deceive targets into interaction
3. Collect and utilize stolen credentials

## Instructions

### Step 1: Host the PoC Page

**Context**: Upload the HTML to a hosting service for public access.

Create a new site on sites.google.com, upload the PoC HTML, and publish it (e.g., at sites.google.com/view/jason-gardner-app-dev/xss-test-poc).

> Ensure the page loads the iframe correctly; test by visiting the URL and verifying credential capture simulation.

### Step 2: Distribute via Phishing

**Context**: Send targeted links to potential victims to initiate the attack.

Craft phishing emails like "Update your Stripo MailChimp integration here: [PoC URL]" and send to users likely using both services. Include keyloggers or exfil scripts in the page to capture inputs.

> Monitor server logs for POST requests containing captured data, confirming credential receipt for MailChimp login.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/sites-google-com]]

## Tags

- [[Phishing]]
- [[hosting]]
- [[social-engineering]]
- [[credential-theft]]

---
tags:
  - delivery
  - phishing
  - xss
  - csrf
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
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:57.653Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 406b583c-2704-4be0-bce7-8d36e031ebe7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Deliver-Malicious-CSRF-Page-to-Victim

## Summary

This procedure involves tricking a victim into visiting a hosted CSRF PoC page, triggering the POST to the vulnerable endpoint and executing the reflected XSS payload.

## Description

In the scenario, the attacker uses social engineering to direct the victim to the PoC URL. Upon load, JavaScript auto-submits the form, sending the CSRF request from the victim's browser. If the victim is authenticated to the target, this can lead to session hijacking. Requires the PoC from prior steps and a delivery vector like email. Expected outcome is JS execution in victim context.

## Requirements

1. Hosted CSRF PoC page accessible via URL
2. Social engineering vector (e.g., email, link sharing)
3. Victim with potential authentication to target site

## Defense

Defensive measures and detection strategies:

- Educate users on phishing and suspicious links
- Implement browser protections like uBlock or CSP
- Log and alert on cross-site POSTs without tokens

## Objectives

1. Induce victim to load the malicious page
2. Trigger CSRF POST and XSS execution
3. Achieve impact like alert or data exfiltration

## Instructions

### Step 1: Host the PoC Page

**Context**: Deploy the HTML PoC to a web server for public access.

Use a simple HTTP server or cloud hosting to serve the file, obtaining a URL like http://attacker.com/xss-poc.html.

### Step 2: Craft Delivery Message

**Context**: Create a phishing pretext to lure the victim.

Example email: "Check this funny Urban Dictionary echo: [PoC URL]"

### Step 3: Monitor Execution

**Context**: Observe the attack by proxying victim traffic or enhancing payload for callback.

If using Burp, configure to capture the POST; otherwise, use JS in payload to beacon back to attacker server.

> Successful execution shows alert or network request from victim.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- delivery
- phishing
- execution

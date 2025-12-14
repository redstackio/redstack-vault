---
id: proc-uuid-3
tags:
  - csrf
  - xss
  - delivery
  - phishing
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
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:49.349Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
---

# Deliver-and-Execute-CSRF-XSS-PoC

## Summary

This procedure delivers the crafted CSRF HTML PoC to a victim, triggering unauthorized login to the attacker's account on Drive2.ru and executing XSS for potential session hijacking or data exfiltration.

## Description

In a drive-by compromise scenario, host or email the malicious HTML to the victim. When loaded in a browser where the user is authenticated to Drive2.ru, it submits the form, bypassing protections and injecting XSS to steal cookies or perform actions.

## Requirements

1. Hosted location for the HTML (e.g., GitHub Pages or personal server)
2. Delivery method (email, social engineering, or malicious link)
3. Victim with an active Drive2.ru session

## Defense

Defensive measures and detection strategies:

- Educate users on phishing and not clicking untrusted links
- Implement referrer checks and same-site cookies
- Log and alert on login CSRF attempts
- Deploy web application firewall (WAF) rules for anomalous form posts

## Objectives

1. Induce victim to load the PoC page
2. Achieve session takeover via forced login
3. Execute XSS for additional payload delivery

## Instructions

### Step 1: Host the PoC

**Context**: Make the HTML accessible via a URL.

Upload the file to a web server or free host. Note the URL, e.g., http://attacker-site.com/csrf-poc.html.

> Ensure the page loads without errors.

### Step 2: Deliver to Victim

**Context**: Use social engineering to get the victim to visit the URL while logged into Drive2.ru.

Send a phishing email: "Click here to view exclusive content: [URL]". Or embed in a forum post.

> Victim clicks and loads the page in their browser.

### Step 3: Verify Execution

**Context**: Monitor for success indicators post-delivery.

Check Drive2.ru for new logins from victim's IP or watch for XSS alert in victim reports.

> Expected: Victim's account performs actions as attacker, confirming hijack.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[xss]]
- [[Phishing]]

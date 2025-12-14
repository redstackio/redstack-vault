---
tags:
  - csrf
  - delivery
  - phishing
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
updated_at: '2025-12-14T17:27:15.108Z'
sub_techniques: []
id: dd1fc8d8-731c-44b2-ad99-10ef4e418d15
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Deliver CSRF Payload

## Summary

This procedure delivers the malicious HTML page to an authenticated Localize user, leveraging social engineering to trigger the CSRF attack and cause unauthorized group deletion.

## Description

Delivery methods include hosting the HTML on a controlled server and sending a phishing link via email or chat, or embedding it in a seemingly legitimate page. The attack succeeds because the victim's browser uses their active session cookies to authenticate the forged request to Localize.

## Requirements

1. Hosting capability (e.g., simple web server or file sharing)
2. Contact method for victim (email, messaging)
3. Victim must be logged into Localize during visit

## Defense

Defensive measures and detection strategies:

- Implement user training on suspicious links
- Use web application firewalls (WAF) to detect anomalous POST patterns
- Enable multi-factor authentication (MFA) for sensitive actions like deletions

## Objectives

1. Ensure victim loads the page while authenticated
2. Achieve stealthy execution
3. Confirm deletion impact

## Instructions

### Step 1: Host the HTML File

**Context**: Make the exploit accessible via a URL.

Upload the HTML to a web server (e.g., GitHub Pages, ngrok for local hosting) to get a public link like http://attacker.com/exploit.html.

**Expected Output**: Stable URL that serves the HTML without errors.

### Step 2: Send to Victim

**Context**: Use social engineering to lure the victim.

Craft a phishing email: "Check this urgent update: [link]". Ensure the link points to the exploit page.

**Expected Output**: Victim clicks and loads the page, triggering the form submission.

### Step 3: Verify Impact

**Context**: Monitor for success via follow-up or logs.

Ask the victim indirectly or check if the group is deleted (if possible).

**Success Indicators**:
- Victim reports page load
- Group deletion confirmed in Localize account

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[payload-delivery]]

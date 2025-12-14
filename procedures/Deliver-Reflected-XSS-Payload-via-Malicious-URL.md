---
id: proc-deliver-xss-payload-url
tags:
  - xss
  - phishing
  - url-delivery
  - session-theft
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[T1566.001]]'
updated_at: '2025-12-13T23:52:38.869Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[T1566.001]]'
---
# Deliver-Reflected-XSS-Payload-via-Malicious-URL

## Summary

This procedure outlines the construction and delivery of a malicious URL exploiting the reflected XSS in Revive Adserver's 'compact' parameter, tricking an admin into executing injected JavaScript.

## Description

The full exploit URL incorporates the crafted payload into the admin-search.php endpoint with other required parameters to mimic a legitimate search. Delivery via phishing or direct link leads to immediate script execution, allowing cookie theft, redirects, or defacement in the victim's session.

## Requirements

1. Valid target URL for the Revive Adserver instance
2. Crafted payload from prior procedure
3. Method for social engineering (e.g., email or chat)

## Defense

Defensive measures and detection strategies:

- Train users on phishing recognition and URL verification
- Deploy email filters to block suspicious links
- Log and alert on anomalous access to admin endpoints

## Objectives

1. Assemble a complete exploitable URL
2. Successfully deliver to and execute on victim browser
3. Achieve data exfiltration or unauthorized action

## Instructions

### Step 1: Construct Exploit URL

**Context**: Build the URL with all parameters to ensure the page loads and reflects the payload.

Form the URL: http://target-ip/www/admin/admin-search.php?affiliate=1&banner=1&campaign=1&client=1&compact=1'><script>alert(document.cookie)</script>&keyword=1&zone=1. Include dummy values for other params to avoid errors.

> Verify URL syntax and encode special characters if necessary for transmission.

### Step 2: Deliver to Victim

**Context**: Use social engineering to get the admin to visit the URL, triggering the XSS.

Send the URL via email pretending it's a legitimate admin report link. Upon click, the browser processes the reflected payload, executing the script in the admin context.

> Monitor for execution via a beacon in the payload (e.g., fetch to attacker server) to confirm success.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[T1566.001]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Phishing]]

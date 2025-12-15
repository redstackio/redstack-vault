---
tags:
  - csrf
  - exploitation
  - drive-by
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:29.959Z'
sub_techniques: []
id: c19e654b-a471-4617-977f-948159889a9f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute-CSRF-Attack-via-Victim-Page-Visit

## Summary

This procedure demonstrates the full exploitation by inducing a victim to visit the malicious HTML page, resulting in automatic comment manipulation on their Teavana wishlist.

## Description

With the victim authenticated on teavana.com, loading the attacker-controlled HTML triggers an immediate POST to the vulnerable endpoint using the browser's session cookies. This bypasses user consent, allowing remote addition or editing of comments. The attack relies on social engineering to lure the victim (e.g., via email link) and succeeds silently due to the onload auto-submit. Impact includes potential spam, misinformation, or account tampering.

## Requirements

1. Hosted malicious HTML accessible via URL
2. Victim authenticated on teavana.com
3. Method to deliver the link (e.g., phishing)

## Defense

Defensive measures and detection strategies:

- Educate users on phishing and unexpected links
- Implement referrer checks or origin validation
- Monitor account for anomalous comment changes

## Objectives

1. Deliver the PoC to the victim
2. Confirm exploitation via wishlist inspection
3. Evaluate real-world impact

## Instructions

### Step 1: Host and Distribute the PoC

**Context**: Make the HTML available for victim access.

Upload csrf-poc.html to a web server (e.g., GitHub Pages or local ngrok) and obtain the URL. Send the link to the victim via email or social engineering.

**Expected Output**: Victim receives and clicks the link.

### Step 2: Monitor Exploitation

**Context**: Verify the attack's success post-visit.

After the victim loads the page, check their wishlist on teavana.com for the injected comment.

**Expected Output**: Unauthorized comment added or edited.

**Success Indicators**:
- Comment appears without victim action
- No errors in browser console

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[exploitation]]
- [[drive-by]]

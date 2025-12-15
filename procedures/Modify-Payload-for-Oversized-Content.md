---
tags:
  - payload-modification
  - bypass
  - dos
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 38a2c729-2796-4ddd-a023-5a67c779aff0
created_at: '2025-12-14T17:26:56.513Z'
updated_at: '2025-12-14T17:26:56.513Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-Payload-for-Oversized-Content

## Summary

This procedure alters the intercepted JSON payload in Twitter's Moments creation request to include excessively large strings in title or description fields, bypassing frontend limits.

## Description

Targeting the Moments API endpoint, this involves editing the request body in Burp Suite to insert oversized content (e.g., 1.95M characters), exploiting the absence of server-side length validation. Prerequisites include an intercepted request. Outcomes prepare for DoS by creating payloads that exhaust resources on processing.

## Requirements

1. Intercepted POST request from previous procedure
2. Burp Suite Repeater or Intruder tab access
3. Pre-prepared large text files (e.g., payload_1.txt with 1,950,000 '%2Fa' repeats for server DoS)
4. Knowledge of JSON structure and URL encoding

## Defense

Defensive measures and detection strategies:

- Enforce server-side input length validation and sanitization
- Log and alert on oversized request bodies (e.g., >1KB)
- Use WAF rules to block anomalous JSON payloads

## Objectives

1. Inflate payload size beyond frontend limits (60/250 chars)
2. Ensure payload is processable without immediate rejection
3. Test variations for server vs. client impact

## Instructions

### Step 1: Load Request into Repeater

**Context**: Switch to Burp's Repeater for safe editing without affecting the live session.

In Burp Suite, right-click the intercepted request and send to Repeater. Verify the original empty fields in the JSON body.

### Step 2: Edit JSON Payload

**Context**: Replace the target field with oversized content to simulate bypass.

In the Repeater's request pane, locate the 'title' or 'description' key in the JSON. Replace the empty string "" with content from a file: paste 1,950,000 characters of repeated '%2Fa' (URL-encoded '/a' to avoid issues) for server exhaustion, or 200,001 characters for app DoS. Use a text editor to generate the string if needed.

**Expected Output**: Updated JSON like {"title":"%2Fa%2Fa... (1.95M chars)","description":"",...}.

### Step 3: Validate Modification

**Context**: Ensure the payload is correctly formed and large enough.

Check the request length in Burp (should exceed ~1MB for large payloads). Preview the JSON to confirm no syntax errors.

**Expected Output**: Valid, oversized JSON ready for sending.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[payload-modification]]
- [[bypass]]
- [[dos]]

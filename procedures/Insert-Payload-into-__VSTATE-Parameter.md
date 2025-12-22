---
id: 4e7dc722-844c-4887-8eed-d34a2b2508fc
name: Insert-Payload-into-__VSTATE-Parameter
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:42.139Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
tags:
  - rce
  - deserialization
platforms:
  - Web
tools: []
commands: []
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Insert-Payload-into-__VSTATE-Parameter

## Summary

This procedure involves embedding the generated deserialization payload into the __VSTATE form parameter of a HigherLogic platform page to prepare for RCE exploitation.

## Description

The __VSTATE parameter in ASP.NET forms stores serialized ViewState data. By replacing it with a malicious base64-encoded payload, submission triggers unsafe deserialization on the server. This targets public-facing forms without authentication, assuming the HigherLogic integration lacks proper validation.

## Requirements

1. Encoded payload from payload generation step
2. Access to a form endpoint on the target site (e.g., community login or post form)
3. Browser or proxy tool for form manipulation

## Defense

Defensive measures and detection strategies:

- Validate and sanitize ViewState inputs server-side
- Limit ViewState size and reject oversized payloads
- Log and alert on unusual __VSTATE modifications

## Objectives

1. Successfully place the payload in the form without detection
2. Ensure the form remains submittable
3. Prepare for immediate triggering

## Instructions

### Step 1: Locate Target Form

**Context**: Identify a page with a POST form using __VSTATE, such as a community forum post or login on HigherLogic.

**Instructions**: Navigate to the target URL (e.g., ██.8x8.com/community) and inspect the form using developer tools to find the __VSTATE hidden input.

> Expected: Hidden input field named __VSTATE with existing base64 value.

### Step 2: Replace __VSTATE Value

**Context**: Overwrite the existing __VSTATE with the malicious encoded payload.

**Instructions**: Copy the base64 string from payload generation and paste it into the __VSTATE field's value attribute or POST body.

> Use tools like Burp Suite to intercept and modify if needed. Expected: Form data now includes the full malicious payload.

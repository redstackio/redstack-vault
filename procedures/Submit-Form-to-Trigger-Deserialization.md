---
id: 6c40a5c4-e5f9-47a9-babc-f433ed3dc678
name: Submit-Form-to-Trigger-Deserialization
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:42.127Z'
tactics:
  - '[[Execution]]'
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
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Submit-Form-to-Trigger-Deserialization

## Summary

This procedure submits the tampered form to the server, causing deserialization of the malicious __VSTATE and executing the gadget chain for RCE.

## Description

Upon POST submission, the ASP.NET server deserializes the __VSTATE using LosFormatter, activating the TypeConfuseDelegate gadget to run the embedded command. This exploits the lack of type validation in the HigherLogic integration.

## Requirements

1. Tampered form ready with malicious __VSTATE
2. Valid session or public access to the endpoint
3. No additional tools beyond browser/proxy

## Defense

Defensive measures and detection strategies:

- Disable or restrict LosFormatter usage
- Implement deserialization blacklisting/whitelisting
- Monitor server logs for deserialization exceptions

## Objectives

1. Trigger server-side code execution
2. Avoid client-side validation failures
3. Confirm via subsequent OOB monitoring

## Instructions

### Step 1: Submit the Form

**Context**: Send the POST request with the modified __VSTATE to the target endpoint.

**Instructions**: Click submit in the browser or send via curl/Burp: Ensure all other form fields are valid to bypass any checks.

> Example curl (adapt to actual form):
```bash
curl -X POST https://██.8x8.com/community/form -d "__VSTATE=malicious_base64_payload&other_field=value"
```
Expected: Server response (may be normal page or error, but RCE occurs server-side).

---
id: proc-submit-form-ssrf
tags:
  - ssrf
  - submit
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:13.431Z'
skill_level: intermediate
impact_level: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit-Form-to-Trigger-SSRF

## Summary

This procedure submits the modified form containing the arbitrary URL, causing the server to fetch the resource and potentially enabling SSRF to access internal services.

## Description

The final exploitation step where the server processes the URL as a photo source without validation, leading to SSRF. This can exfiltrate data or probe internals if URLs target metadata services like AWS S3 or instance metadata.

## Requirements

1. Completed URL input in modified form
2. Active session on target site
3. Monitoring for server response

## Defense

Defensive measures and detection strategies:

- Implement URL allowlisting and blacklist internal IPs
- Use web application firewalls (WAF) to block suspicious fetches
- Audit server logs for unexpected outbound requests

## Objectives

1. Force server-side URL fetch
2. Confirm SSRF success via profile update
3. Assess impact on internal access

## Instructions

### Step 1: Prepare Submission

**Context**: Ensure form is ready without errors.

No command; review input.

> Verify URL is present. Expected output: Form valid.

### Step 2: Submit the Form

**Context**: Trigger the request to server.

Click 'Update Profile' or press Enter.

> Form submits via POST. Expected output: Profile photo updates with remote image; potential SSRF if URL is internal.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[ssrf]]
- [[submit]]

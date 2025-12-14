---
id: proc-uuid-4
tags:
  - csrf-submit
  - profile-modification
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
updated_at: '2025-12-14T17:27:29.625Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit-CSRF-Form-to-Modify-Profile

## Summary

This procedure executes the CSRF attack by submitting the HTML form, modifying the authenticated user's profile and demonstrating the reusable nonce flaw.

## Description

Submitting the PoC form sends a POST request to the savePublicInformation endpoint using the victim's session cookies, altering fields like website to a malicious URL. The nonce's reusability allows multiple submissions without invalidation, as shown in PoC videos changing the website repeatedly. Impact includes social engineering, as victims may visit their profile and click injected links leading to phishing or malware.

## Requirements

1. Loaded CSRF PoC in authenticated browser
2. Visible submit button or JavaScript auto-submit
3. Access to verify profile changes post-submission

## Defense

Defensive measures and detection strategies:

- Validate CSRF tokens server-side with expiration and uniqueness
- Rate-limit profile updates and require re-authentication for sensitive changes
- Scan for anomalous requests from non-standard referers in server logs

## Objectives

1. Successfully modify profile fields without user consent
2. Exploit nonce reusability for repeated attacks
3. Enable follow-on social engineering

## Instructions

### Step 1: Trigger Form Submission

**Context**: Initiate the POST request via button click or auto-submit.

Click the submit button on the PoC page.

**Expected Output**: Request sent; no errors in browser console.

### Step 2: Verify Modification

**Context**: Check LGTM profile for changes.

Navigate to the user's profile page on LGTM.

**Expected Output**: Updated fields (e.g., website changed to malicious link).

### Step 3: Test Nonce Reusability

**Context**: Submit the same PoC multiple times to confirm vulnerability.

Reload and resubmit the HTML form 2-3 times.

**Expected Output**: Multiple successful modifications without nonce regeneration.

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
- [[modification]]

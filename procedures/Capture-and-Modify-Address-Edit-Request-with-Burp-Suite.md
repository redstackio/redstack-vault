---
id: proc-openmage-idor-capture-001
tags:
  - idor
  - burp-suite
  - web-proxy
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:33.613Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Capture-and-Modify-Address-Edit-Request-with-Burp-Suite

## Summary

This procedure uses Burp Suite to intercept, analyze, and modify an address edit request in OpenMage, replacing the address ID with one from another account to exploit IDOR and create unauthorized addresses.

## Description

The IDOR vulnerability in OpenMage's address editing endpoint fails to validate ownership of the referenced address ID, allowing an attacker to edit (and effectively create duplicates of) another user's address on their own account. This procedure captures a legitimate edit request via Burp proxy, forwards it to Repeater for modification of the address_id parameter in the GET URL and Referer header, and submits the altered request. It targets the web endpoint like /customer/address/edit/ and requires an authenticated session. Successful exploitation results in a new address on the attacker's account without errors.

## Requirements

1. Burp Suite installed and running with proxy enabled (default 127.0.0.1:8080)
2. Browser configured to use Burp as proxy
3. Active sessions for attacker and victim accounts
4. Known address IDs from both accounts

## Defense

Defensive measures and detection strategies:

- Server-side ownership checks for address IDs against the authenticated user
- Input validation on address_id parameters to prevent tampering
- Logging and alerting on mismatched user-ID references in requests

## Objectives

1. Demonstrate IDOR by creating unauthorized addresses
2. Validate lack of authorization enforcement
3. Prepare for automation in DoS escalation

## Instructions

### Step 1: Intercept Legitimate Edit Request

**Context**: Capture the structure of a normal address edit to identify modifiable parameters.

Configure Burp proxy and perform an edit on attacker's address:

Intercept the GET request (e.g., GET /customer/address/edit/address_id=123 HTTP/1.1) and forward to Repeater.

> Expected output: Request details in Repeater, including address_id=123 and Referer header.

### Step 2: Modify Parameters for IDOR

**Context**: Swap the address_id to a victim's ID to test bypass.

In Repeater, edit the URL to address_id=456 (victim's ID) and update Referer: https://demo.openmage.org/customer/address/edit/address_id=456.

> Expected output: Modified request ready for sending.

### Step 3: Submit and Verify

**Context**: Execute the tampered request to confirm exploitation.

Click 'Send' in Repeater and check response.

> Expected output: HTTP 200 with success; new address in attacker's account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- idor
- burp-suite
- web-proxy

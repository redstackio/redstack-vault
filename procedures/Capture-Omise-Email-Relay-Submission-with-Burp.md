---
tags:
  - csrf
  - capture
  - burp
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/omise-add-email-relay-post]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:15.209Z'
sub_techniques: []
id: a3d24295-439e-4bbd-87dc-271b94f4535b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Capture-Omise-Email-Relay-Submission-with-Burp

## Summary

Intercept and capture a POST request for adding an email relay in Omise using Burp Suite to obtain the reusable authenticity token.

## Description

This procedure involves submitting a legitimate form while proxying traffic through Burp Suite to capture the HTTP POST request. The request includes the CSRF authenticity_token, which can be reused due to the vulnerability in the Rails session management. This token is critical for crafting the CSRF PoC.

## Requirements

1. Burp Suite running and browser proxied to it (e.g., 127.0.0.1:8080)
2. Active Omise session
3. Test email address for submission

## Defense

Defensive measures and detection strategies:

- Enable CSRF token per-request regeneration in Rails
- Log and alert on repeated use of the same token

## Objectives

1. Capture the full POST request details
2. Extract authenticity_token and parameters
3. Forward to Repeater for analysis

## Instructions

### Step 1: Configure Proxy and Submit Form

**Context**: Intercept the submission to grab the request.

Fill the form with email_relay[address]=testaccount1@gmail.com, select event groups (accounting, chargebacks), and submit while proxied.

> Burp Proxy captures the request; inspect headers like Cookie and Content-Type: application/x-www-form-urlencoded.

### Step 2: Send to Repeater

**Context**: Prepare for replay and inspection.

In Burp, send the captured request to Repeater.

Execute [[commands/omise-add-email-relay-post]] in Repeater or via curl equivalent:

```bash
curl -X POST https://dashboard.omise.co/test/subscriptions \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Cookie: session=...; session.sig=...' \
  -d 'utf8=%E2%9C%93&authenticity_token=UoPkXa4uMwSgxUG1d3a7l5PodACsA9LBagoeTlLNDZWAx1kzUeVH1%2FbeJdeXMr8Z5NYkgEX%2B1kaFci3i%2F%2BV%2Fqg%3D%3D&email_relay%5Baddress%5D=testaccount1%40gmail.com&email_relay%5Bsupported_event_groups%5D%5B%5D=accounting&email_relay%5Bsupported_event_groups%5D%5B%5D=chargebacks&button='
```

> Response: 302 redirect to /test/subscriptions on success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/omise-add-email-relay-post]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[csrf]]
- [[capture]]

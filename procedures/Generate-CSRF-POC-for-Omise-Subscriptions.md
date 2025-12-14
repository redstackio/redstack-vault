---
tags:
  - csrf
  - poc
  - generation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:15.195Z'
sub_techniques: []
id: 2da8ecb2-cce3-42d6-9001-31b7695a9cc9
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
---
# Generate-CSRF-POC-for-Omise-Subscriptions

## Summary

Use Burp Suite to generate an HTML CSRF proof-of-concept from the captured Omise POST request, enabling auto-submission for exploitation.

## Description

Burp's CSRF PoC generator converts the intercepted HTTP request into client-side HTML that automatically submits the form when loaded. This exploits the reusable token by embedding it in the PoC, allowing an attacker to forge requests from the victim's browser in the same session.

## Requirements

1. Captured POST request in Burp Repeater
2. Burp Suite Professional or Community with Engagement Tools

## Defense

Defensive measures and detection strategies:

- Validate referer headers for cross-origin requests
- Use SameSite cookies to mitigate CSRF

## Objectives

1. Create auto-submitting HTML form
2. Include all request parameters and token
3. Save as executable file

## Instructions

### Step 1: Generate PoC

**Context**: Transform request into HTML.

In Burp Repeater, right-click the POST /test/subscriptions request > Engagement tools > Generate CSRF PoC > Select HTML with auto-submit.

> Generates file with <form method="POST" action="https://dashboard.omise.co/test/subscriptions"> including hidden inputs for utf8, authenticity_token, email_relay params, and submit button.

### Step 2: Test PoC Locally

**Context**: Verify functionality before modification.

Save and open the HTML in a browser (proxied if testing); it should submit and redirect on success.

> Confirms PoC works with the token.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[csrf]]
- [[poc]]

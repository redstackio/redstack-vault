---
tags:
  - captcha
  - web-form
  - initial-access
type: procedure
tools:
  - '[[tools/HTTP-Proxy-Burp-Suite]]'
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
updated_at: '2025-12-14T17:28:36.278Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 90a18f98-cf28-498f-8583-592c0c80fab5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Initial-Approval-Request-with-Valid-CAPTCHA

## Summary

This procedure involves submitting a legitimate approval request form on the Instagram Brand Site to generate and capture a valid reCAPTCHA token, setting the stage for subsequent tampering.

## Description

The Instagram Brand Site uses a WordPress-based form at https://en.instagram-brand.com/requests/new for approval requests, requiring fields like campaign name, description, client details, dates, audience reach, media value, assets, sizes, files, and a reCAPTCHA token. The backend API endpoint /wp-json/brc/v1/approval-requests handles POST requests for creation. By completing the form legitimately, an attacker obtains a valid g-recaptcha-response token from Google's API, which can later be reused due to validation flaws. This step requires no special access and simulates normal user behavior to avoid detection.

## Requirements

1. Browser access to the public form
2. Proxy tool configured for interception (e.g., Burp Suite)
3. Ability to solve reCAPTCHA manually or via browser

## Defense

Defensive measures and detection strategies:

- Implement client-side and server-side CAPTCHA validation with token expiration
- Monitor for unusual form submission patterns from single IPs
- Rate-limit API endpoints for approval requests

## Objectives

1. Generate a valid reCAPTCHA token for reuse
2. Capture the full POST request payload
3. Establish baseline for legitimate request structure

## Instructions

### Step 1: Navigate to Form and Fill Details

**Context**: Access the public form and input sample data to trigger reCAPTCHA.

No command required; use browser to visit https://en.instagram-brand.com/requests/new and fill fields:
- Campaign Name: Test Campaign
- Description: Test description
- Client: Test Client
- Start/End Dates: Current dates
- Audience Reach: 1000
- Media Value: 100
- Assets: Test asset
- Sizes: Medium
- Files: Upload a dummy image if required

Solve the reCAPTCHA widget to obtain the token.

> Expected output: Form ready for submission with g-recaptcha-response populated in hidden field.

### Step 2: Submit Form with Proxy Active

**Context**: Intercept the submission to capture the token.

Ensure proxy (e.g., Burp Suite) is intercepting HTTPS traffic, then submit the form.

> Expected output: Intercepted POST request body containing form data and g-recaptcha-response token.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/HTTP-Proxy-Burp-Suite]]

## Tags

- [[captcha]]
- [[web-form]]

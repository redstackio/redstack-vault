---
tags:
  - initial-access
  - web-app
  - authentication
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
updated_at: '2025-12-14T17:32:48.214Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 639c78d2-2ea2-44a5-824f-8f2cbb1abb69
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-Insurance-Quote-Authentication

## Summary

This procedure triggers the OTP-based authentication flow in the MTN Group device insurance quote process by submitting a target phone number, setting the stage for intercepting the leaked OTP in subsequent API responses.

## Description

In the MTN Group application, the device insurance quote feature requires phone number verification via OTP. By accessing the customer insurance portal and initiating a quote, an attacker can submit any valid MTN phone number, prompting the backend API to generate and send an OTP to that number. Due to the vulnerability, this OTP is also echoed back in the API response, but this procedure focuses on the initiation to enable traffic interception. The target environment is the public web portal at https://corporate.admyntec.co.za/customerInsurance, accessible without authentication. Expected outcomes include the application advancing to OTP entry, with the API call vulnerable to monitoring.

## Requirements

1. Web browser or HTTP client with proxy support
2. Valid MTN South Africa phone number (e.g., starting with 08)
3. Network access to the MTN corporate domain

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on quote requests per IP or phone number
- Monitor for anomalous OTP generation volumes
- Use client-side certificate pinning to prevent proxy interception

## Objectives

1. Trigger OTP generation for a target phone number
2. Advance the authentication flow to expose the vulnerable API endpoint
3. Prepare for traffic analysis in the next phase

## Instructions

### Step 1: Access the Insurance Portal

**Context**: Navigate to the MTN customer insurance page to begin the quote process.

No specific command; use a browser to visit https://corporate.admyntec.co.za/customerInsurance and select the device insurance quote option.

> This loads the form for entering device and contact details, including phone number.

### Step 2: Submit Phone Number

**Context**: Enter and submit a valid MTN phone number to initiate OTP request.

No command; fill the form with the target phone number (e.g., +27821234567) and proceed to authentication.

> The application sends an API request to verify the number and generate OTP, advancing to the verification screen.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[initial-access]]
- [[web-app]]
- [[authentication]]

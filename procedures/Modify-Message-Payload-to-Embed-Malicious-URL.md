---
tags:
  - payload-modification
  - api-exploit
  - url-injection
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:18.065Z'
sub_techniques: []
id: daa4e46c-470a-4a93-bbed-6c4f90ded98c
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-Message-Payload-to-Embed-Malicious-URL

## Summary

This procedure modifies the intercepted JSON payload in LinkedIn's createMessage API request to replace the GIF URL with an attacker-controlled URL, exploiting insufficient validation to enable client-side information disclosure.

## Description

The vulnerability stems from the lack of sanitization or allowlisting on the externalMedia.media.url parameter, allowing arbitrary URLs. Using Burp Suite, the attacker alters the payload while the request is intercepted, then forwards it. This causes the victim's client to fetch the malicious URL disguised as a GIF, without server-side checks. Applicable to web and mobile LinkedIn clients.

## Requirements

1. Intercepted request from previous step in Burp Suite
2. Burp Collaborator server running to generate unique callback URL
3. Knowledge of JSON structure for the endpoint

## Defense

Defensive measures and detection strategies:

- Validate and allowlist external media URLs to trusted domains only
- Sanitize API inputs to prevent arbitrary URL embedding
- Log and alert on unusual external URL patterns in messages

## Objectives

1. Inject malicious URL into the message payload
2. Ensure the modification bypasses API validation
3. Prepare for victim-side execution

## Instructions

### Step 1: Isolate Endpoint

**Context**: Forward requests to reach the vulnerable endpoint.

In Burp Suite Proxy:

1. Intercept and forward all preliminary requests (auth, etc.)
2. Stop at POST /voyager/api/voyagerMessagingDashMessengerMessages?action=createMessage

> Expected output: Full JSON payload displayed in Inspector or Raw tab.

### Step 2: Edit URL Parameter

**Context**: Replace the legitimate URL with malicious one.

In Burp Repeater or directly in Proxy:

1. Locate 'message.renderContentUnions.externalMedia.media.url' in JSON
2. Change value to Burp Collaborator URL, e.g., "https://uniqueid.burpcollaborator.net"
3. Ensure JSON remains valid (quotes, escapes)
4. Click Forward to send

> Expected output: API response indicating successful message creation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Burp-Collaborator]]

## Tags

- [[payload-modification]]
- [[api-exploit]]
- [[url-injection]]

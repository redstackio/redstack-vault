---
id: proc-uuid-1
name: Intercept-Comment-Creation-to-Obtain-ID
tags:
  - idor
  - intercept
  - web
  - vimeo
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
updated_at: '2025-12-14T17:25:23.400Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-Comment-Creation-to-Obtain-ID

## Summary

This procedure involves posting a comment on a private Vimeo video using an authenticated account and intercepting the HTTP request to capture the generated unique comment ID, which is later used for IDOR exploitation.

## Description

In the context of Vimeo's web application, comments on private videos are assigned sequential or unique IDs upon creation. By using a proxy tool to monitor network traffic during comment submission, an attacker can extract this ID without direct API access. This step requires access to a private video and sets up the target ID for unauthorized retrieval in subsequent steps. Expected outcome is the comment_id value, enabling bypass of access controls.

## Requirements

1. Valid Vimeo account with permission to comment on private videos
2. Web proxy tool (e.g., Burp Suite) configured to intercept HTTPS traffic
3. Access to a private video URL on vimeo.com

## Defense

Defensive measures and detection strategies:

- Implement client-side certificate pinning to prevent proxy interception
- Monitor for unusual request patterns from authenticated sessions
- Rate-limit comment creation and editing endpoints

## Objectives

1. Capture the unique ID of a newly created private comment
2. Prepare for IDOR exploitation by obtaining referenceable object identifier
3. Validate private video comment functionality

## Instructions

### Step 1: Configure Proxy and Authenticate

**Context**: Set up interception and log in to Vimeo with the source account to access the private video.

Navigate to the private video page in a browser proxied through Burp Suite. Ensure the proxy is capturing all requests.

### Step 2: Post Comment and Intercept

**Context**: Submit a test comment to trigger ID generation and capture it in the request/response.

Enter and submit a comment like "Test private comment" on the private video. Intercept the POST request to /api/v2/videos/<video_id>/comments or similar endpoint.

Examine the response body for the comment_id, e.g., {"id": 1301116}.

**Expected Output**: JSON response with comment_id field populated.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[idor]]
- [[web]]
- [[vimeo]]

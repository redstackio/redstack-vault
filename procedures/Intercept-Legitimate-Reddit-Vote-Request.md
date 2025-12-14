---
id: proc-uuid-001
tags:
  - intercept
  - proxy
  - burp
  - reddit
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
updated_at: '2025-12-14T17:32:39.105Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept Legitimate Reddit Vote Request

## Summary

This procedure captures a legitimate HTTP request to Reddit's /api/vote endpoint using a proxy tool, providing a template for subsequent modifications in IDOR exploitation.

## Description

In the context of exploiting access control flaws in Reddit's voting API, intercepting a normal vote request allows attackers to replicate the structure while altering parameters to target unauthorized resources. This step requires a valid Reddit session and focuses on web traffic interception without direct API calls.

## Requirements

1. Burp Suite installed and running
2. Browser proxy configured to route through Burp (e.g., 127.0.0.1:8080)
3. Logged-in Reddit account with ability to vote on public posts
4. Target post ID for private subreddit obtained separately (e.g., via enumeration)

## Defense

Defensive measures and detection strategies:

- Monitor for anomalous proxy traffic or tool signatures like Burp User-Agent
- Implement client-side certificate pinning to prevent proxy interception
- Rate-limit API requests from suspicious IPs

## Objectives

1. Capture a valid /api/vote POST request template
2. Ensure request includes necessary headers and session cookies
3. Prepare for parameter modification without alerting the server

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp Suite to intercept HTTPS traffic from the browser.

Install Burp CA certificate in the browser trust store to handle Reddit's TLS.

### Step 2: Perform Legitimate Vote

**Context**: Trigger a vote on a public post to generate the request.

Navigate to a public subreddit post in the browser, click the upvote/downvote button while proxy is active.

**Expected Output**: Request appears in Burp Proxy history as POST /api/vote with JSON body {"id": "public_post_id", "dir": 1}.

### Step 3: Forward to Repeater

**Context**: Move the request to Repeater for modification.

Right-click the intercepted request in Proxy and select "Send to Repeater".

**Expected Output**: Request loaded in Repeater tab, ready for editing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[intercept]]
- [[proxy]]
- [[burp]]
- [[reddit]]

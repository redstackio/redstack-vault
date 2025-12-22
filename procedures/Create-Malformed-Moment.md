---
tags:
  - moment-creation
  - api-exploit
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: b8598109-0998-4798-a430-f1fce25be3b8
created_at: '2025-12-14T17:26:56.487Z'
updated_at: '2025-12-14T17:26:56.487Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Malformed-Moment

## Summary

This procedure forwards the modified oversized payload to Twitter's API, resulting in the creation of a malformed Moment that the server accepts without validation.

## Description

By sending the altered POST request via Burp Suite, the API stores the excessive content, which may return success but sets up downstream failures. Targets the Moments creation endpoint; requires prior interception and modification. Leads to persistent DoS vectors through the created content.

## Requirements

1. Modified request in Burp Repeater
2. Active Twitter session
3. Network connectivity to Twitter servers

## Defense

Defensive measures and detection strategies:

- Validate and truncate input lengths server-side before storage
- Scan stored content for anomalies post-creation
- Implement payload size limits in API gateways

## Objectives

1. Successfully create and store the oversized Moment
2. Obtain a link to the malformed content for further exploitation
3. Confirm server acceptance without immediate rejection

## Instructions

### Step 1: Review and Send Request

**Context**: Final check before submission to ensure payload integrity.

In Burp Repeater, review the full request (headers, body). Click 'Send' to forward to the Twitter endpoint.

**Expected Output**: Response code 200 OK, with JSON confirming Moment creation (e.g., including moments-id).

### Step 2: Verify Creation

**Context**: Confirm the Moment exists on the profile.

Refresh https://twitter.com/{username}/moments in the browser. Look for the new Moment entry, noting its ID from the response.

**Expected Output**: Malformed Moment visible in the list, though content may not render fully.

### Step 3: Extract Moment ID

**Context**: Capture the ID for subsequent interactions.

From the 200 response, note the moments-id (e.g., in redirect or body). Save the shareable link: https://twitter.com/i/moments/{moments-id}.

**Expected Output**: Usable ID and link for DoS triggering.

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

- [[moment-creation]]
- [[api-exploit]]

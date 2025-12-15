---
tags:
  - analysis
  - disclosure
  - burp
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:24:56.422Z'
sub_techniques: []
id: abc3d943-5191-46c0-aa22-a315e8e0f812
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
  - '[[Account Discovery]]'
---
# Execute-and-Analyze-Burp-Intruder-Attack

## Summary

This procedure launches the Burp Intruder fuzzing attack and examines responses to identify information disclosures, such as leaked usernames from enumerated API categories.

## Description

Launching the attack sends requests with varying category IDs to endpoints like /c/{category}/{id}.json. Analysis focuses on 200 OK responses with JSON bodies containing user arrays. In the Brave forum case, this discloses usernames across categories, aiding reconnaissance. Expected outcome is a list of valid IDs and extracted sensitive data.

## Requirements

1. Payloads configured in Burp Intruder
2. Stable network to target
3. Tools for JSON parsing (Burp's built-in viewer or external like jq)

## Defense

Defensive measures and detection strategies:

- Access controls on API endpoints (e.g., require auth for category listing)
- Response filtering to exclude sensitive fields or anomaly detection in logs for fuzzing patterns

## Objectives

1. Probe all potential category IDs
2. Extract and validate disclosed information
3. Assess impact of the disclosure

## Instructions

### Step 1: Start the Attack

**Context**: Initiate the fuzzing to send batched requests.

In Burp Intruder, click "Start Attack". Monitor progress in the new attack window.

> Requests fire sequentially or in threads (default 10), with real-time status updates.

### Step 2: Analyze Responses

**Context**: Inspect for successful disclosures.

Pause or wait for completion, then sort results by status (200 OK) and length. Click responses to view JSON in Inspector; grep for "username" or user objects.

> Valid categories show JSON with "topic_list" > "topics" > "posters" arrays containing usernames; 404s indicate invalid IDs.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Vulnerability Scanning]] Vulnerability Scanning
- [[Account Discovery]] Account Discovery

### Sub-Techniques

-

## Commands Used

-

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[analysis]]
- [[information-disclosure]]

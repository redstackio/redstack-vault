---
tags:
  - pixiv
  - network-analysis
  - csrf
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:27:49.790Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques:
  - '[[Vulnerability Scanning]]'
id: f79f5aac-9f31-44f9-bae9-3762e8a0cb56
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Analyze-Pixiv-Import-Request

## Summary

This procedure details inspecting the legitimate chatstory import process on Pixiv to uncover the vulnerable POST endpoint and parameter structure for CSRF exploitation.

## Description

By simulating a valid import as an authenticated user, the attacker uses browser tools to capture the network request, revealing the lack of CSRF protection on https://chatstory.pixiv.net/imported. Key parameters include id, text, comment, title, user_id, x_restrict, and is_original. This reconnaissance enables forging identical requests from a malicious site. Prerequisites include an authenticated session and developer tools.

## Requirements

1. Authenticated Pixiv account
2. Web browser with Network inspector (e.g., Chrome DevTools)
3. Access to a novel page on Pixiv

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints
- Log and monitor import requests for anomalies (e.g., unusual referers)
- Use SameSite cookies to mitigate cross-site requests

## Objectives

1. Identify vulnerable endpoint and parameters
2. Confirm absence of anti-CSRF measures
3. Document request format for forgery

## Instructions

### Step 1: Navigate to Novel Page

**Context**: Set up the legitimate import scenario to trigger the request.

Go to https://www.pixiv.net/novel/show.php?id=10997105 while authenticated.

### Step 2: Trigger Import and Inspect Network

**Context**: Capture the POST request details using dev tools.

Open DevTools (F12), go to Network tab, click 'チャットストーリーを作る' button. Filter for POST to chatstory.pixiv.net/imported.

> Inspect request body: id=10997105&text=<content>&comment=<comment>&title=<title>&user_id=39570048&x_restrict=0&is_original=true. Note no CSRF token.

### Step 3: Document Parameters

**Context**: Record all elements for replication in CSRF form.

Copy parameters and verify by replaying in a tool like Postman if needed.

**Expected Output**: Full request specification.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

- [[Vulnerability Scanning]] Vulnerability Scanning

## Commands Used


## Tools Used


## Tags

- [[pixiv]]
- [[request-analysis]]

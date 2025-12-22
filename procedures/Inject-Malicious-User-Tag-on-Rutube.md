---
tags:
  - xss
  - injection
  - rutube
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:55.432Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: c7d4df51-10a4-4ce3-ada7-972332bd35fe
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-User-Tag-on-Rutube

## Summary

This procedure involves creating a user account on Rutube.ru and injecting a malicious XSS payload into the user tag associated with a video, storing the vulnerability for later exploitation in external search engines like DuckDuckGo.

## Description

In the attack scenario, the attacker registers on Rutube, a video hosting site, and sets their user tag to include an XSS payload such as `"> <img src = x onerror = alert (1)>`. This tag is fetched and rendered unsanitized by DuckDuckGo when displaying video details, leading to stored XSS. The target environment is any web browser with access to Rutube. Prerequisites include internet access; no special permissions are needed beyond free account creation. Expected outcomes include the payload being persisted in the video metadata for repeated exploitation.

## Requirements

1. Web browser (e.g., Chrome, Firefox)
2. Access to Rutube.ru (no VPN required)
3. Basic knowledge of HTML/JavaScript for payload crafting

## Defense

Defensive measures and detection strategies:

- Sanitize all user-generated content from external sources before rendering
- Implement Content Security Policy (CSP) to block inline scripts and unsafe image sources
- Monitor for anomalous alert() calls or img src errors in browser logs

## Objectives

1. Persist XSS payload in external video platform
2. Prepare for reflection in search engine results
3. Enable arbitrary JS execution on viewers

## Instructions

### Step 1: Create Rutube Account

**Context**: Register a new account to gain the ability to set custom user tags.

Navigate to https://rutube.ru and complete the registration form with any valid email and password. Verify the account if prompted via email.

### Step 2: Associate Video and Inject Payload

**Context**: Upload or select a video and edit the user profile tag to include the XSS payload, ensuring it's stored with the video metadata.

Select or upload a video (e.g., at https://rutube.ru/video/83a4775f020b3fd68efd3dc9a73031e8/). In the user profile or video edit section, set the tag field to: `"> <img src = x onerror = alert (1)>`. Save changes and confirm the tag appears in the video details.

> The payload breaks out of any attribute context and injects a script-executing img tag.

### Step 3: Verify Storage

**Context**: Confirm the malicious tag is persisted and viewable.

Refresh the video page or view in incognito mode to ensure the tag displays without execution (it should render as text on Rutube).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- injection
- stored-xss

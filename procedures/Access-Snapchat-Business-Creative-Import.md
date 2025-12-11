---
id: 93db0683-88f3-45b9-b184-bbec34c5f17d
name: Access Snapchat Business Creative Import
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T06:10:15.622Z'
updated_at: '2025-12-11T06:10:15.622Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - ssrf
  - web-access
commands:
  - '[[commands/flask-app-run]]'
  - '[[commands/flask-sleep]]'
  - '[[commands/flask-print-log]]'
  - '[[commands/flask-set-log-level]]'
platforms:
  - Web
tools:
  - '[[tools/Flask]]'
  - '[[tools/flask_cors]]'
  - '[[tools/XMLHttpRequest]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---

# Access Snapchat Business Creative Import

## Summary

This procedure involves logging into the Snapchat business portal and navigating to the creative import function to access the vulnerable endpoint for SSRF exploitation.

## Description

The procedure targets the /api/v1/media/import endpoint on business.snapchat.com, which lacks proper URL validation, allowing arbitrary URL fetching. This is the entry point for triggering SSRF attacks.

## Requirements

1. Valid Snapchat business account credentials
2. Web browser access to https://business.snapchat.com/
3. No additional tools required

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation and whitelisting on import endpoints
- Monitor for unusual URL submissions in API logs

## Objectives

1. Access the media import functionality
2. Prepare for URL submission
3. Enable SSRF trigger

## Instructions

### Step 1: Login and Navigate

**Context**: Access the Snapchat business site and navigate to the creative import function.

Login to https://business.snapchat.com/, go to Creative Library -> New Creative -> Topsnap Media -> Create, select a template, load it, click on an image -> Replace -> Import.

> This positions you at the vulnerable import interface.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[ssrf]]
- [[web-access]]

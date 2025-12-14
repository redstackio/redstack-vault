---
id: proc-infogram-access-project-001
tags:
  - web-access
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-05T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T04:39:18.601Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Access-Infogram-User-Project-Page

## Summary

This procedure outlines navigating to a specific user project page on Infogram, serving as the entry point for exploiting the SSRF vulnerability in the JSON Feed feature.

## Description

In the context of SSRF exploitation, accessing the project page allows interaction with the editing interface where malicious URLs can be injected. The target environment is the Infogram web application, and success enables subsequent steps for port scanning via error message observation. Prerequisites include a valid Infogram login and knowledge of a project ID.

## Requirements

1. Web browser with JavaScript enabled
2. Valid Infogram user account
3. Project identifier (e.g., from URL https://infogram.com/app/[user-project])

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on project page accesses
- Monitor for unusual navigation patterns to edit interfaces
- Use CAPTCHA on login to prevent automated access

## Objectives

1. Gain access to the project editing environment
2. Position for JSON input exploitation
3. Enable reconnaissance via SSRF

## Instructions

### Step 1: Open Browser and Navigate

**Context**: Launch a browser and directly access the project URL to load the Infogram page.

No command required; use browser address bar:

```plaintext
https://infogram.com/app/[user-project]
```

> Replace [user-project] with the actual project identifier. The page should load displaying the visualization, confirming access.

### Step 2: Verify Page Load

**Context**: Ensure the project is editable and no errors occur.

Inspect the page for edit buttons.

**Expected Output**: Project visualization renders; edit options available.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web-access]]
- [[Reconnaissance]]

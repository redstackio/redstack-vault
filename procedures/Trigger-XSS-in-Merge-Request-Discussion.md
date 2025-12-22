---
id: proc-uuid-4
tags:
  - xss
  - execution
  - trigger
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:03.855Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-in-Merge-Request-Discussion

## Summary

This procedure views the imported project's merge request discussion to execute the stored XSS payload, potentially affecting any user who accesses the public project.

## Description

The injected note_html renders directly in the discussion view, executing JavaScript like an alert on document.domain. This persistent XSS can lead to session hijacking, data theft, or further attacks on viewers, exploiting GitLab's public project visibility.

## Requirements

1. Imported project with malicious notes
2. Web browser access to GitLab
3. Victim or tester account to view discussions

## Defense

Defensive measures and detection strategies:

- Sanitize all rendered HTML in discussions
- Implement Content Security Policy (CSP) to block inline scripts
- Monitor for anomalous JavaScript execution in browser consoles

## Objectives

1. Execute arbitrary JavaScript in viewer context
2. Demonstrate impact on public project viewers
3. Enable potential account takeover or exfiltration

## Instructions

### Step 1: Access Imported Project

**Context**: Navigate to the merge request in the browser.

Log in (or view publicly) and open the project, then select the merge request.

### Step 2: View Discussion

**Context**: Load the discussion thread to trigger rendering.

Click into the discussion containing the Note object. The note_html should execute the payload.

**Expected Output**: JavaScript alert or other effects, e.g., alert(document.domain).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Browser]]

## Tags

- [[xss]]
- [[Execution]]
- [[trigger]]

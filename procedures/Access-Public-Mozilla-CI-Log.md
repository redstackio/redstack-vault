---
id: proc-001
tags:
  - reconnaissance
  - ci-cd
  - public-logs
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
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:31:52.742Z'
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
# Access-Public-Mozilla-CI-Log

## Summary

This procedure accesses publicly available Mozilla TaskCluster CI logs to identify potential sensitive information leaks in pipeline outputs.

## Description

Mozilla's TaskCluster CI system exposes live logs for tasks, which can inadvertently include unmasked secrets if logging is not properly configured. This step targets a specific public log URL to retrieve raw CI output, setting the stage for credential discovery in an attack scenario involving information disclosure.

## Requirements

1. Web browser or HTTP client for accessing public URLs
2. Internet access to Mozilla's CI services
3. No authentication required

## Defense

Defensive measures and detection strategies:

- Restrict CI log visibility to authenticated users only
- Implement secret masking in CI/CD pipelines (e.g., using TaskCluster secrets)
- Monitor public logs for access patterns indicating scraping

## Objectives

1. Retrieve raw CI log content
2. Identify verbose logging outputs
3. Enable subsequent token extraction

## Instructions

### Step 1: Navigate to Log URL

**Context**: Directly access the public log endpoint to view live CI output.

No command required; use a browser.

> Open https://firefox-ci-tc.services.mozilla.com/tasks/d5NRF8FdQamV9XdPO_mTBQ/runs/0/logs/public/logs/live.log. The log displays real-time or historical pipeline executions, including commands run during Netlify deployments.

**Expected Output**: Scrollable log text with build steps, potentially including echoed tokens.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[ci-cd]]

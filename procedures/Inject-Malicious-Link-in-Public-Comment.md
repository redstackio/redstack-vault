---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - xss
  - injection
  - markdown
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:43.816Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Link-in-Public-Comment

## Summary

This procedure injects a malicious markdown link into a public GitLab issue comment, referencing a private issue with an HTML-encoded XSS payload in the link text to evade initial rendering checks.

## Description

Using the unauthorized account, post a comment in a public project linking to the private issue. The payload, like `&lt;img onerror=alert(1) src=x&gt;`, is encoded in the link text and stored in the 'data-original' attribute. When redacted, it unescapes and executes. Targets public issues in GitLab; requires comment permissions. Outcome: Stored payload ready for victim triggering.

## Requirements

1. Access to public project with comment permissions
2. Knowledge of private issue URL
3. Encoded payload prepared

## Defense

Defensive measures and detection strategies:

- Sanitize all link text and attributes server-side before storage
- Scan comments for encoded HTML patterns
- Rate-limit comment posting in public projects

## Objectives

1. Store the XSS payload in public content via private reference
2. Ensure payload survives initial markdown rendering
3. Position for redaction-based execution

## Instructions

### Step 1: Navigate to Public Issue

**Context**: Select or create a public project issue for commenting.

**Command** (UI Action):
Go to a public project > Issues > Select or create issue.

> Expected: Issue page loads with comment box.

### Step 2: Post Malicious Comment

**Context**: Add the encoded link in markdown format.

**Command** (UI Action):
In comment box, enter: `[link](https://gitlab.com/wbowling/private-project/-/issues/1 "title")xss &lt;img onerror=alert(1) src=x&gt;`, then submit.

> Expected: Comment appears; for authorized viewers, link shows normally without execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[injection]]

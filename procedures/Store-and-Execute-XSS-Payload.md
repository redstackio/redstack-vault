---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567894
tags:
  - xss
  - stored-xss
  - payload-execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:37.999Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Store-and-Execute-XSS-Payload

## Summary

This procedure confirms the storage of the XSS payload in the forum content and demonstrates its execution when viewed by other users, leading to arbitrary JavaScript in victim browsers.

## Description

After redirection, Invision Community stores the fetched (malicious) iFrame content in the post/profile database. When victims load the page, the embedded iFrame executes the JavaScript, potentially compromising sessions or stealing data. Target: User views of affected content. Prerequisites: Successful interception and injection. Outcomes: Persistent XSS affecting multiple users, fixed in v4.4.9.1 by improved validation.

## Requirements

1. Injected payload from prior interception
2. Victim browser or session to test execution
3. Access to view the stored post/profile

## Defense

Defensive measures and detection strategies:

- Sanitize stored embed content post-fetch
- Implement XSS filters and CSP on rendered pages
- Scan for JS in stored iFrame sources

## Objectives

1. Verify payload persistence in database
2. Trigger execution on victim load
3. Assess impact like data theft

## Instructions

### Step 1: Verify Storage

**Context**: Check if the malicious content is saved.

View the post/profile in edit mode or database (if accessible); confirm the iFrame src points to injected payload.

### Step 2: Induce Victim View

**Context**: Load the page in a new session to simulate victim.

Open the affected post/profile in an incognito browser or share with a test user.

### Step 3: Observe Execution

**Context**: Confirm JS runs in victim context.

Monitor console for alerts or exfil requests; expect cookie theft or DOM manipulation.

> Success: Arbitrary code executes, e.g., sending session data to attacker server.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]

---
id: proc-uuid-2
tags:
  - xss
  - trigger
  - search-reflection
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
updated_at: '2025-12-14T00:11:09.545Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-via-Author-Search

## Summary

This procedure triggers the execution of a stored XSS payload by searching for the malicious nickname in the forum's Author field, causing JavaScript to run in the context of any searching user.

## Description

Once the payload is stored in the nickname via the modification feature, the forum's search functionality reflects the unsanitized nickname content when querying authors. By entering keywords from the malicious nickname in the Author search field, the search results page renders the payload, executing arbitrary JavaScript. This affects victims who perform searches matching the attacker's nickname, potentially leading to data theft or phishing. The target environment is the web-based forum at forum.acronis.com, requiring no special access beyond public search capabilities.

## Requirements

1. Injected payload already stored in a nickname
2. Access to the forum's search interface (public or logged-in)
3. Victim browser to observe execution

## Defense

Defensive measures and detection strategies:

- Sanitize all reflected content in search results, escaping HTML entities
- Use Content Security Policy (CSP) to block inline scripts
- Log and alert on searches containing suspicious patterns like script tags

## Objectives

1. Reflect the stored payload in search results
2. Execute JavaScript in the victim's browser session
3. Demonstrate potential for session hijacking or data exfiltration

## Instructions

### Step 1: Navigate to Search Function

**Context**: Access the forum's search page to prepare for triggering the stored payload.

Go to forum.acronis.com and locate the search form, typically available on the main navigation or forum index.

### Step 2: Enter Malicious Keywords and Submit

**Context**: Input search terms matching the injected nickname to cause reflection and execution of the payload.

In the Author field of the search form, enter keywords from the modified nickname (e.g., `OriginalNick` or parts including the payload trigger). Submit the search.

> The search results will unsafely render the nickname, executing `<script>alert(0)</script>` as an alert popup; in a real attack, replace with code to steal document.cookie or redirect to phishing sites.

**Expected Output**: JavaScript execution, such as an alert dialog; inspect page source to confirm payload reflection.

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
- [[search]]

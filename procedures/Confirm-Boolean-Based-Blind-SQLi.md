---
id: 650770f4-e6e9-497a-a1ce-713b6d7bc67a
name: Confirm-Boolean-Based-Blind-SQLi
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:09.859Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - sqli
  - confirmation
  - blind
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Confirm-Boolean-Based-Blind-SQLi

## Summary

This procedure confirms a boolean-based blind SQL injection by injecting conditional payloads into the User-Agent header and analyzing response differences in a SharePoint application.

## Description

In blind SQLi, no direct errors are returned, so this procedure relies on true/false conditions (e.g., AND 8074=8074) to cause observable changes like response times or content variations. It targets MySQL backends where queries are concatenated from unsanitized headers.

## Requirements

1. Confirmed injectable header from prior identification
2. Burp Suite or similar for precise payload control
3. Timing analysis tools if needed

## Defense

Defensive measures and detection strategies:

- Parameterize all dynamic SQL queries
- Implement response time normalization to obscure blind techniques
- Intrusion detection systems monitoring for conditional SQL patterns

## Objectives

1. Verify blind SQLi type as boolean-based
2. Establish baseline for exploitation
3. Ensure no false positives from initial tests

## Instructions

### Step 1: Inject True Condition

**Context**: Send a request with a always-true boolean to establish normal behavior.

Set User-Agent: 'Mozilla/5.0 AND 8074=8074' and note response time/content.

> Normal application response indicates successful query execution.

### Step 2: Inject False Condition

**Context**: Compare with a false condition to detect differences.

Set User-Agent: 'Mozilla/5.0 AND 8074=8075' and observe.

> Altered or delayed response confirms boolean evaluation in blind context.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[sqli]]
- [[confirmation]]
- [[blind]]

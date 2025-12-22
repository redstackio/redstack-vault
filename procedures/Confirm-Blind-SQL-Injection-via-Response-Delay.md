---
id: proc-uuid-3
tags:
  - blind-sqli
  - time-based
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-sqli-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:05.161Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Confirm-Blind-SQL-Injection-via-Response-Delay

## Summary

This procedure verifies the blind SQL injection by measuring response time delays caused by the sleep function in the injected payload, confirming vulnerability without visible errors.

## Description

Since the SQLi is blind (no direct output), time-based techniques like MySQL's SLEEP(10) are used. A normal request to the endpoint responds in <1 second, while the payload delays by 10 seconds, proving execution. This confirmation allows chaining to extract data via conditional sleeps or unions in production WooCommerce sites.

## Requirements

1. Executed injection from prior procedure
2. Timing tool or manual stopwatch
3. Burp Suite Repeater for precise measurements

## Defense

Defensive measures and detection strategies:

- Rate-limit admin requests to detect delays
- Audit SQL queries for time functions in logs
- Deploy database monitoring for unusual sleep executions

## Objectives

1. Validate payload execution via timing
2. Differentiate vulnerable from non-vulnerable responses
3. Assess potential for further exploitation

## Instructions

### Step 1: Send Baseline Request

**Context**: Establish normal response time without payload.

**Command** ([[commands/curl-sqli-payload]] with benign coupon_codes):

```bash
curl -X GET "http://<target>/wp-admin/admin.php?page=wc-reports&tab=orders&report=coupon_usage&coupon_codes=test" -H "Cookie: <session_cookie>" -w "%{time_total}\n"
```

> Time total should be <1 second. Note the value.

### Step 2: Send Payload and Time

**Context**: Inject payload and measure delay using Burp or curl with timing flags.

Use the same command as Step 1 but with payload; in Burp Repeater, send and note response time.

> Delay of ~10 seconds confirms blind SQLi.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-sqli-payload]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- blind-sqli
- timing-attack

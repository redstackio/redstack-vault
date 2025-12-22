---
id: uuid-confirm-payload
tags:
  - sqli
  - blind-sqli
  - time-based
type: procedure
tools:
  - '[[tools/sqlmap]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-sleep-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:09.918Z'
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
# Confirm-SQL-Injection-with-Payloads

## Summary

This procedure tests for time-based blind SQL injection by injecting a SLEEP payload into the search parameter, observing response delays to confirm vulnerability without extracting data directly.

## Description

Time-based blind SQL injection exploits unsanitized inputs to execute conditional delays in the database query. Here, the search parameter in /reader_api/stories.php is targeted on a MySQL database, where a 5-second sleep confirms execution without visible errors.

## Requirements

1. Baseline knowledge of the endpoint from prior reconnaissance
2. Ability to time HTTP responses accurately
3. Tools for sending modified GET requests

## Defense

Defensive measures and detection strategies:

- Parameterize all SQL queries to prevent injection
- Log and alert on unusual response latencies
- Employ intrusion detection systems (IDS) for payload patterns

## Objectives

1. Verify the injection point executes arbitrary SQL
2. Confirm blind nature (no data in response)
3. Assess stability for further exploitation

## Instructions

### Step 1: Inject Sleep Payload

**Context**: Append a time-delay payload to the search parameter to test database interaction.

**Command** ([[commands/curl-sleep-payload]]):
```bash
curl "https://docs.atavist.com/reader_api/stories.php?limit=10&offset=20&organization_id=88822&search=0'%20AND%20SLEEP(5)%20AND%20'wRIg'%20LIKE%20'wRIg'&sort="
```

> The payload causes a 5-second delay if injected successfully. Compare timing to baseline request.

### Step 2: Validate Delay

**Context**: Time multiple requests to rule out network issues.

**Command** (Repeat the above command 3-5 times):

> Consistent 5-second delays indicate successful blind injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-sleep-payload]]

## Tools Used

- [[tools/sqlmap]]

## Tags

- sqli
- blind-sqli

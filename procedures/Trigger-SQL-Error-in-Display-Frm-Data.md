---
id: proc-trigger-error-003
tags:
  - sqli
  - blind-sqli
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-trigger-sql-error]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:10.005Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-SQL-Error-in-Display-Frm-Data

## Summary

This procedure injects malicious order parameters into the [display-frm-data] shortcode to trigger an SQL error in the ORDER BY clause, proving lack of sanitization.

## Description

The shortcode parameters order_by and order are directly concatenated into SQL queries for form entry IDs. Using 'order=zzz' causes a syntax error as it's invalid for MySQL sorting. The error may not be visible in responses (blind), but affects server logs. This confirms the injection point before full exploitation.

## Requirements

1. Successful shortcode injection
2. curl tool
3. Access to server logs if possible for verification

## Defense

Defensive measures and detection strategies:

- Parameterize queries with prepared statements in plugin code
- Enable SQL error logging and monitor for ORDER BY anomalies
- Update to patched Formidable Pro version

## Objectives

1. Cause query failure via invalid ORDER BY
2. Confirm unsanitized parameter insertion
3. Validate blind error behavior

## Instructions

### Step 1: Inject Malicious Order Parameter

**Context**: Modify shortcode to include invalid order value, disrupting the query.

**Command** ([[commands/curl-trigger-sql-error]]):
```bash
curl -s -i 'https://www.drivegrab.com/wp-admin/admin-ajax.php' --data 'action=frm_forms_preview&after_html=XXX[display-frm-data id=835 order_by=id limit=1 order=zzz]YYY'
```

> Posts shortcode with order=zzz; expected: empty or partial response, with MySQL error like 'Unknown column zzz' in logs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-trigger-sql-error]]

## Tools Used

- [[tools/curl]]

## Tags

- sqli
- blind-sqli

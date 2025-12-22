---
id: ba8230d5-6b5b-47aa-9cd4-96ee21ede2c2
name: padded-admin-username-for-truncation
type: code
language: Bash
verified: true
created_at: '2023-04-06T03:56:34.879236+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - payload
  - sql-injection
  - truncation
validated: true
---

# padded-admin-username-for-truncation

## Code

```bash
username = "admin               a"
```

## Description

This bash variable assignment sets a padded username payload for SQL injection, using spaces to exploit MySQL varchar truncation (e.g., fills to 20 chars, truncating to 'admin' followed by partial injection like quote or comment).

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| username | The payload string to inject into login form | "admin               a" |

## Usage

Assign and use in scripts or curl commands for login bypass: export username="admin               a"; then curl ... -d "username=$username' -- ". Adjust padding based on field length. Referenced in [[procedures/Bypass-Admin-Login-via-MySQL-Injection-and-Truncation]] for admin authentication evasion.

## Detection

- WAF rules for unusually long usernames with trailing spaces.
- Log analysis for inputs exceeding varchar limits without errors (due to truncation).
- Input length validation at app level.

## Related

- [[procedures/Bypass-Admin-Login-via-MySQL-Injection-and-Truncation]]

---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - access-control
  - verification
  - web
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:29:44.448Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Verify Insufficient Privileges on Admin Page

## Summary

This procedure verifies that an unauthenticated user lacks access to the admin portal in an Oracle APEX application, setting the stage for demonstrating a subsequent access control bypass.

## Description

In the context of testing Oracle APEX Express applications, this step involves attempting direct access to the admin page (e.g., page 45) without credentials. The expected outcome is a denial due to insufficient privileges, confirming that normal access controls are in place before exploiting the vulnerability. This is crucial for validating the impact of the bypass in a real attack scenario targeting DoD-hosted applications.

## Requirements

1. Web browser with no prior session cookies for the target domain
2. Network access to the target URL (https://████.mil/apexcrrel/)
3. No authentication credentials

## Defense

Defensive measures and detection strategies:

- Implement strict session validation and role-based access control (RBAC) on all pages
- Log all access attempts to admin endpoints and alert on unauthorized tries
- Use web application firewalls (WAF) to block direct URL manipulation

## Objectives

1. Confirm baseline access denial for non-admin users
2. Document the denial message for comparison post-bypass
3. Ensure no prior admin session exists

## Instructions

### Step 1: Attempt Direct Access to Admin Page

**Context**: Navigate to the admin page URL to trigger the access control check.

No specific command required; use browser navigation.

```plaintext
Visit: https://████.mil/apexcrrel/f?p=165:45
```

> The page should load an error indicating insufficient privileges, such as "ORA-01031: insufficient privileges" or a custom denial page. No admin features should be accessible.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- access-control
- oracle-apex
- verification

---
tags:
  - cookie-forgery
  - auth-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Use Alternate Authentication Material]]'
updated_at: '2025-12-14T17:33:12.131Z'
sub_techniques:
  - '[[Default Accounts]]'
id: 13955653-62eb-48a2-91b8-5ac595848d8e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Use Alternate Authentication Material]]'
---
# Forge PROD_CAS_SESSION Cookie

## Summary

This procedure manipulates the PROD_CAS_SESSION cookie by setting its value to a target's 6-digit User ID, bypassing authentication checks due to the absence of validation or integrity mechanisms.

## Description

The vulnerability stems from the application's reliance on an unverified cookie for user identification. By editing the cookie via browser tools, an attacker can impersonate any user whose ID is known. This targets web sessions in the specified DoD application, leading to full account access.

## Requirements

1. Browser developer tools enabled
2. Victim's 6-digit User ID (e.g., 195141)
3. Active session on the target domain **███**

## Defense

Defensive measures and detection strategies:

- Enforce cookie integrity with HMAC or signing
- Implement server-side session validation beyond cookie values
- Log and alert on cookie modifications

## Objectives

1. Set cookie to victim's ID
2. Establish forged authentication
3. Enable impersonation

## Instructions

### Step 1: Open Developer Tools

**Context**: Access cookie storage for editing.

Right-click on the page and select 'Inspect' or press F12 to open dev tools. Navigate to the 'Application' tab (Chrome) or 'Storage' tab (Firefox), then expand 'Cookies' under the target domain **███**.

**Expected Output**: List of existing cookies, including PROD_CAS_SESSION if present.

### Step 2: Edit Cookie Value

**Context**: Directly modify the session cookie.

Locate PROD_CAS_SESSION, double-click its value field, and set it to the victim's 6-digit ID (e.g., 195141). Save changes.

Alternatively, use the console to set via JavaScript:

```javascript
document.cookie = "PROD_CAS_SESSION=195141; domain=███; path=/";
```

> This command sets the cookie programmatically. Verify in the Application tab that the value updated.

**Expected Output**: Cookie value persists as the new ID without browser errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]
- [[Use Alternate Authentication Material]]

### Sub-Techniques

- [[Default Accounts]]

## Commands Used


## Tools Used


## Tags

- [[cookie-forgery]]
- [[auth-bypass]]

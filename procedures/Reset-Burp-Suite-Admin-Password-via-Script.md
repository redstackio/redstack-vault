---
id: proc-burp-password-reset-001
tags:
  - password-reset
  - session-management
  - admin-console
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/resetAdministratorPassword]]'
verified: false
platforms:
  - Java
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:07.134Z'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Reset-Burp-Suite-Admin-Password-via-Script

## Summary

This procedure resets the administrator password in Burp Suite Enterprise using the official reset script, demonstrating that this action does not invalidate existing sessions, which is key to exploiting persistent access vulnerabilities.

## Description

The procedure targets the admin console's password reset functionality in Burp Suite Enterprise, a Java-based application. By executing the resetAdministratorPassword script on the server, the password is changed, but active sessions remain valid due to the root cause of improper session invalidation. This is typically run in a scenario where an admin attempts to regain control after a compromise. Expected outcome: password updated, but prior sessions persist.

## Requirements

1. Server access to the Burp Suite Enterprise installation directory
2. Java runtime environment (included with Burp Suite)
3. Knowledge of the new password to set

## Defense

Defensive measures and detection strategies:

- Configure session invalidation on password changes in application settings
- Log and alert on password reset events
- Enforce session revocation mechanisms like token blacklisting

## Objectives

1. Change the admin password to simulate lockout attempt
2. Highlight failure to invalidate sessions
3. Prepare for persistence verification

## Instructions

### Step 1: Locate and Prepare the Script

**Context**: Navigate to the Burp Suite Enterprise installation directory on the server.

No specific command; use file explorer or terminal to cd to the directory containing the script (e.g., /opt/burp-enterprise/scripts).

> Ensure the script is executable and Java is in PATH.

### Step 2: Execute the Password Reset Script

**Context**: Run the reset script to change the admin password, following documentation guidelines.

**Command** ([[commands/resetAdministratorPassword]]):
```bash
./resetAdministratorPassword
```

> The script prompts for the new password. Enter it twice for confirmation. Expected output: Success message indicating password reset, with no errors. This does not affect existing sessions.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/resetAdministratorPassword]]

## Tools Used


## Tags

- password-reset
- session-management

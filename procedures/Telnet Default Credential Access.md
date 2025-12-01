---
id: c4e7f9a2-1d8b-4e3c-9f5a-6b2d3e8c1a7f
name: Telnet Default Credential Access
type: procedure
verified: true
submitted: true
created_at: '2023-12-09T00:00:00.000000+00:00'
updated_at: '2025-11-30T21:55:00.000000+00:00'
platforms:
- Linux
- Windows
tags:
- telnet
- default credentials
- initial access
- unencrypted
- metasploitable2
mitre_tactics:
- TA0001  # Initial Access
mitre_techniques:
- T1078   # Valid Accounts
- T1078.001  # Default Accounts
skill_level: beginner
impact_level: medium
detection_risk: medium
commands:
- '[[telnet connect to target]]'
tools:
- '[[telnet]]'
---

# Telnet Default Credential Access

**Status**: ✓ Verified

## Summary

Gain remote shell access to Metasploitable2 system using default credentials (msfadmin:msfadmin) via the unencrypted Telnet service on port 23.

## Description

Telnet provides unencrypted remote terminal access. Metasploitable2 ships with default credentials that are widely known, allowing immediate access without any exploitation. This represents a common misconfiguration in production environments.

## MITRE ATT&CK Mapping

**Tactics:** TA0001 - Initial Access
**Techniques:** T1078.001 - Default Accounts

## Instructions

### Step 1: Connect via Telnet

```bash
telnet <target_ip>
```

**Example:**
```bash
telnet 192.168.137.128
```

### Step 2: Authenticate

When prompted:
- **Username:** `msfadmin`
- **Password:** `msfadmin`

### Step 3: Verify Access

```bash
whoami
id
```

## Expected Outcomes

✅ Remote shell obtained
✅ User-level access (msfadmin user)

## Detection & Evasion

**Detection Risk:** 🟡 Medium

**Detection Methods:**
- Telnet service logs
- Unencrypted network traffic capture
- Authentication logs in /var/log/auth.log

## Platforms

- Linux
- Windows

## Tags

- telnet
- default credentials
- initial access
- unencrypted
- metasploitable2

## References

- [MITRE ATT&CK T1078.001](https://attack.mitre.org/techniques/T1078/001/)
- Metasploitable2 Exploitation Walkthrough - Rajesh Kumar

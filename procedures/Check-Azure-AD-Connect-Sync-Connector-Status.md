---
id: 3a54b0ce-0306-47c3-aa85-204e110ff425
name: Check-Azure-AD-Connect-Sync-Connector-Status
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:16.079057+00:00'
updated_at: '2023-04-10T20:19:23.011905+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Network Service Scanning|T1046 - Network Service Scanning]]'
sub_techniques: []
tags:
  - '[[tags/Azure AD Connect]]'
  - '[[tags/Cloud - Azure]]'
commands:
  - '[[commands/get-adsyncconnector-query-sync-connectors]]'
platforms:
  - Windows
  - Azure
tools: []
validated: true
---

# Check-Azure-AD-Connect-Sync-Connector-Status

## Summary

This procedure checks the status of Azure AD Connect synchronization connectors on a server to determine if synchronization between on-premises Active Directory and Azure AD is functioning properly. Attackers use this to identify active sync configurations, which can facilitate credential harvesting, lateral movement, or persistence in hybrid environments.

## Description

Azure AD Connect is a Microsoft tool that synchronizes identities between on-premises Active Directory and Azure Active Directory. By querying the sync connectors, an attacker with access to the sync server can enumerate connector details such as names, types, status (enabled/disabled), and versions. This discovery step helps assess the hybrid environment's setup, revealing potential paths for exploiting sync processes, such as injecting malicious attributes or harvesting synced credentials. The procedure requires execution on the Azure AD Connect server, typically a Windows domain-joined machine with the AD Sync PowerShell module loaded. It assumes initial access via valid credentials or compromise of the server.

## Requirements

1. Administrative access to the Azure AD Connect server (local or domain admin privileges).
2. PowerShell execution policy allowing script runs (e.g., RemoteSigned or Unrestricted).
3. Azure AD Connect installed and the AD Sync module imported (Import-Module ADSync).
4. Network connectivity to the server if executing remotely via PowerShell remoting.

## Defense

- Regularly audit and monitor PowerShell execution on Azure AD Connect servers using tools like Microsoft Defender for Identity or Azure AD logs.
- Implement least-privilege access: Restrict admin rights on sync servers and enable Just-In-Time (JIT) access.
- Use Azure AD Privileged Identity Management (PIM) to monitor and alert on suspicious queries to sync services.
- Enable synchronization service monitoring and set up alerts for unauthorized access or configuration changes.

## Objectives

1. Enumerate installed synchronization connectors and their status to confirm active Azure AD Connect setup.
2. Identify connector types and versions for potential exploitation vectors in the sync process.
3. Gather intelligence on the hybrid identity environment to support further lateral movement or credential access.

## Instructions

### Step 1: Import AD Sync Module and Query Connectors

**Context**: Begin by ensuring the AD Sync PowerShell module is loaded, then execute the query to retrieve connector details. This step verifies the presence and status of sync connectors without altering the environment.

**Command** ([[commands/get-adsyncconnector-query-sync-connectors]]):
```powershell
Import-Module ADSync -Force
Get-ADSyncConnector
```

> The Import-Module command loads the necessary PowerShell module for Azure AD Connect. The Get-ADSyncConnector command then retrieves details on all configured connectors. If the module is not installed, this will fail—indicating Azure AD Connect may not be present or properly set up. Review the output for connector names (e.g., 'contoso.com - AAD'), types (e.g., AD or Azure AD), and status (Enabled/Disabled). If no connectors are returned, synchronization is likely not configured.

**Expected Output**:
```
Name                      : contoso.com - AAD
Type                      : Azure AD
B2BType                   : None
Status                    : Enabled
...
Name                      : contoso.com - AAD
Type                      : AD
...
```

### Step 2: Analyze Output for Vulnerabilities

**Context**: Parse the command output to identify active connectors and note any outdated versions or unusual configurations that could indicate misconfigurations exploitable for credential harvesting.

> Manually inspect the output for enabled connectors linking on-premises AD to Azure AD. Look for version information to check against known vulnerabilities (e.g., older versions susceptible to attribute injection). If multiple connectors exist, document their scopes for targeted follow-up procedures like credential dumping from the sync database.

**Expected Output**: Structured list of connectors with attributes like Name, Type, Status, and Version. Success is indicated by at least one enabled connector confirming sync capability.

**Success Indicators**:
- Module imports without errors.
- Output lists one or more enabled connectors.
- No permission denied errors during execution.

---
id: e3fd9f63-6f7d-4916-92dc-48d3a40f2936
name: SCCM Network Access Account Credential Theft
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:08.245825+00:00'
updated_at: '2023-04-10T20:26:02.182056+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/SCCM Network Access Accounts]]'
commands:
  - '[[commands/Check-CIM-Repository-ACL]]'
  - '[[commands/Retrieve-SCCM-Network-Access-Account-Blob]]'
  - '[[commands/Decrypt-SCCM-Blobs-With-SharpDPAPI]]'
  - '[[commands/Retrieve-NAA-Credentials-With-SharpSCCM]]'
platforms:
  - Windows
tools:
  - '[[tools/SharpDPAPI]]'
  - '[[tools/SharpSCCM]]'
validated: true
---

# SCCM Network Access Account Credential Theft

## Summary

This procedure details how to steal credentials from SCCM Network Access Accounts (NAA) by querying the local WMI repository for encrypted blobs and decrypting them using specialized tools. These accounts often have elevated privileges for SCCM client communications, allowing lateral movement or persistence in Active Directory environments.

## Description

System Center Configuration Manager (SCCM) stores Network Access Account credentials in encrypted blobs within the WMI repository on client machines. Attackers with local access to an SCCM-managed Windows host can extract these blobs and decrypt them to obtain domain credentials. This technique targets the 'root\ccm\policy\Machine\ActualConfig' namespace and uses tools like SharpDPAPI for decryption and SharpSCCM for querying additional NAA details from the SCCM database. The attack assumes initial foothold on a domain-joined machine with SCCM client installed and requires sufficient permissions to read WMI objects. Successful execution yields plaintext credentials for high-privilege accounts, enabling further compromise such as accessing network shares or escalating privileges.

## Requirements

1. Local administrator access or equivalent permissions on a Windows machine with SCCM client installed.
2. Domain credentials (low-privilege) to authenticate queries against the SCCM database if using SharpSCCM.
3. Tools: SharpDPAPI.exe and SharpSCCM.exe downloaded and executable on the target (Windows x64).
4. PowerShell execution policy allowing script execution.

## Defense

- Restrict WMI namespace access via ACLs on the CIM repository (C:\Windows\System32\wbem\Repository\OBJECTS.DATA).
- Enable DPAPI protection and monitor for unauthorized decryption attempts using Event ID 4776 (credential validation).
- Use privileged access workstations (PAWs) for SCCM administration and implement just-in-time privileges for NAA accounts.
- Monitor for anomalous PowerShell and executable executions (e.g., via Sysmon Event ID 1 for process creation).

## Objectives

1. Verify permissions to access SCCM-related WMI objects.
2. Extract encrypted NAA credentials from the local WMI repository.
3. Decrypt the blobs to obtain usable credentials.
4. Query the SCCM database for additional NAA details and confirm theft.

## Instructions

### Step 1: Verify CIM Repository Permissions

**Context**: Before querying SCCM data, confirm the attacker has read access to the WMI repository by checking the ACL on the OBJECTS.DATA file. This ensures no permission errors during blob retrieval.

**Command** ([[commands/Check-CIM-Repository-ACL]]):
```powershell
Get-Acl C:\Windows\System32\wbem\Repository\OBJECTS.DATA | Format-List -Property PSPath, Sddl
```

> This command retrieves the security descriptor for the CIM repository file. Review the Sddl output to confirm the current user or group has read permissions. If access is denied, escalate privileges or modify ACLs (not covered here).

### Step 2: Retrieve Encrypted NAA Blob

**Context**: Query the WMI namespace to extract the encrypted Network Access Account configuration, including username and password blobs stored as CDATA.

**Command** ([[commands/Retrieve-SCCM-Network-Access-Account-Blob]]):
```powershell
Get-WmiObject -Namespace "root\ccm\policy\Machine\ActualConfig" -Class "CCM_NetworkAccessAccount"
```

> The output displays NetworkAccessUsername and NetworkAccessPassword fields containing encrypted blobs (e.g., starting with E600000001). Save these for decryption. If no output, confirm SCCM client is installed and configured.

### Step 3: Decrypt SCCM Blobs

**Context**: Use SharpDPAPI to decrypt the SCCM-specific blobs extracted in the previous step. This tool handles DPAPI-encrypted data common in SCCM configurations.

**Command** ([[commands/Decrypt-SCCM-Blobs-With-SharpDPAPI]]):
```powershell
.\SharpDPAPI.exe sccm
```

> Run this from the directory containing SharpDPAPI.exe. It automatically targets SCCM blobs in the local context. Expected output includes decrypted credentials if the tool can access the master keys (requires local admin). Pipe or redirect output to capture plaintext.

### Step 4: Retrieve NAA Credentials from SCCM Database

**Context**: With domain credentials, use SharpSCCM to query the SCCM SQL database for Network Access Account details, confirming and extracting additional credential information.

**Command** ([[commands/Retrieve-NAA-Credentials-With-SharpSCCM]]):
```powershell
.\SharpSCCM.exe get naa -u $DOMAIN_USERNAME -p $DOMAIN_PASSWORD
```

> Replace $DOMAIN_USERNAME and $DOMAIN_PASSWORD with valid domain credentials. This queries the SCCM database remotely or via config. Success yields NAA username and decrypted password, usable for lateral movement.

---
id: 24fde44b-95fa-41a7-b68d-e725b6facf97
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.448051+00:00'
updated_at: '2023-05-24T22:11:13.092661+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Azure Storage]]'
  - '[[tags/Azure Storage Blob]]'
  - '[[tags/Cloud - Azure]]'
  - '[[tags/Enumerate blobs]]'
  - '[[tags/Enumeration]]'
commands:
  - '[[commands/load-microburst-enumerate-azure-blobs-script]]'
  - '[[commands/invoke-enumerate-azure-blobs-microburst]]'
platforms:
  - Cloud
tools:
  - '[[tools/Microburst]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Azure-Storage-Blob-Enumeration

## Summary

This procedure enumerates blobs in an Azure Storage Account to discover sensitive data such as credentials or configuration files, enabling further attacks like data exfiltration or lateral movement in cloud environments. It leverages the Microburst toolkit to interact with the Azure Storage API, assuming valid storage account credentials are available.

## Description

Azure Blob Storage is used to store unstructured data in the cloud, and enumerating its contents can reveal valuable information for attackers. By authenticating with a storage account name and key, this procedure queries the API to list blobs across containers, including public or misconfigured ones. This is particularly useful in red team engagements targeting Azure tenants, where exposed blobs might contain backups, logs, or secrets. The technique focuses on discovery without modification, mapping to MITRE ATT&CK for cloud service enumeration. It requires PowerShell execution on a system with Azure module access and is effective against environments with overly permissive storage policies.

## Requirements

1. Valid Azure Storage Account credentials (account name and access key).
2. Network access to Azure endpoints (*.blob.core.windows.net).
3. Installed Microburst toolkit or the specific script file.
4. PowerShell environment (Windows or compatible).

## Defense

- Implement least-privilege access controls on storage accounts using RBAC and shared access signatures (SAS) with limited scopes.
- Enable logging and monitoring for API calls to storage services via Azure Monitor or Sentinel to detect anomalous enumeration patterns.
- Encrypt all blobs with Azure Storage Service Encryption and use private endpoints to restrict public access.

## Objectives

1. Retrieve a list of accessible blobs and containers in the target storage account.
2. Identify potentially sensitive files based on names or metadata.
3. Gather intelligence for subsequent cloud-based attacks, such as credential theft or persistence.

## Instructions

### Step 1: Load the Microburst Enumeration Script

**Context**: Before executing the enumeration, load the Invoke-EnumerateAzureBlobs script from the Microburst toolkit into the current PowerShell session. This imports the necessary functions for interacting with Azure Storage APIs.

**Command** ([[commands/load-microburst-enumerate-azure-blobs-script]]):
```powershell
. $_SCRIPT_PATH
```

> This command sources the script file, making the Invoke-EnumerateAzureBlobs function available. Replace $_SCRIPT_PATH with the full path to the script (e.g., C:\Tools\MicroBurst\Misc\InvokeEnumerateAzureBlobs.ps1). Expected output is minimal—no errors if the script loads successfully, confirming the function is ready for use.

### Step 2: Enumerate Azure Blobs Using Microburst

**Context**: With the script loaded and Azure credentials configured (via environment variables or login), run the enumeration function to scan for storage accounts and list their blobs. This step brute-forces or queries based on the provided base domain to discover accessible blob endpoints.

**Command** ([[commands/invoke-enumerate-azure-blobs-microburst]]):
```powershell
Invoke-EnumerateAzureBlobs -Base $_SHORT_DOMAIN -OutputFile $_OUTPUT_FILE
```

> Replace $_SHORT_DOMAIN with the target tenant's short domain (e.g., contoso) and $_OUTPUT_FILE with the desired output path (e.g., azureblobs.txt). The command will output discovered storage accounts and save detailed blob listings to the file. If successful, it lists endpoints like *.blob.core.windows.net; decision point: if no accounts are found, verify credentials or expand the base domain.

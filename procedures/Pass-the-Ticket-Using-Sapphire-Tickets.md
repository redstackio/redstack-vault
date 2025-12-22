---
id: cc8280b8-3593-420e-9949-4f3d57fcbf1d
name: Pass-the-Ticket-Using-Sapphire-Tickets
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:04.909937+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Lateral-Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Pass-the-Ticket|T1550.001 - Pass the Ticket]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Kerberos Tickets]]'
  - '[[tags/Pass-the-Ticket Sapphire Tickets]]'
commands:
  - '[[commands/ticketer-py-request-sapphire-ticket]]'
platforms:
  - Windows
tools:
  - '[[tools/Impacket-Ticketer]]'
validated: true
---

# Pass-the-Ticket-Using-Sapphire-Tickets

## Summary

This procedure demonstrates how to perform a Pass-the-Ticket attack using Sapphire Tickets, a type of forged Kerberos ticket that mimics a legitimate Privilege Attribute Certificate (PAC) to impersonate a domain administrator. It allows attackers with compromised domain user credentials to generate a ticket for unauthorized access to restricted network resources, enabling lateral movement and privilege escalation in Active Directory environments.

## Description

The Pass-the-Ticket attack with Sapphire Tickets involves forging a Kerberos Ticket Granting Ticket (TGT) by closely replicating the PAC structure of a legitimate domain admin ticket. This technique is effective in Windows Active Directory domains where the attacker has initial access to a domain-joined machine and credentials of a domain user (ideally with some privileges). The forged ticket, known as a Sapphire Ticket, can be used to authenticate to services and resources as the impersonated domain admin without needing the actual admin password. This method bypasses some Kerberos validation checks by using known encryption keys like the krbtgt AES key. It is commonly used post-compromise for lateral movement, accessing sensitive servers, or extracting data from domain controllers.

## Requirements

1. Valid credentials for a domain user account (preferably with local admin rights on a domain-joined machine).
2. Access to a domain-joined Windows machine where the attack can be executed.
3. The Impacket suite installed, specifically the ticketer.py script for generating the Sapphire Ticket.
4. Knowledge of the domain SID, krbtgt AES key for the target service, and the domain name.
5. A way to export and use the generated ticket (e.g., via .ccache files for tools like kinit or Impacket scripts).

## Defense

- Implement strong password policies, regular key rotation for krbtgt accounts, and multi-factor authentication to prevent initial credential compromise.
- Monitor Kerberos authentication logs for anomalous TGT requests, unusual PAC structures, or tickets with mismatched SIDs using tools like Windows Event ID 4768/4769.
- Enable Protected Users group and restrict delegation to limit ticket usage; use Group Managed Service Accounts (gMSAs) instead of static service accounts.
- Deploy network segmentation, endpoint detection tools to flag suspicious ticket usage, and regular audits of domain admin privileges.

## Objectives

1. Forge a Sapphire Ticket to impersonate a domain administrator.
2. Authenticate to network resources using the forged ticket for lateral movement.
3. Escalate privileges to access restricted domain resources.
4. Exfiltrate sensitive data or maintain persistence in the environment.

## Instructions

### Step 1: Prepare Sapphire Ticket Generation

**Context**: Gather necessary domain information and ensure the ticketer.py tool is available. This step sets up the environment for forging the ticket by collecting the domain SID, krbtgt AES key, and target impersonation details. The krbtgt AES key can be extracted from a compromised domain controller or via prior attacks like DCSync.

**Command** ([[commands/ticketer-py-request-sapphire-ticket]]):
```bash
ticketer.py -request -impersonate $_DOMAIN_ADMIN -domain $_DOMAIN -user $_DOMAIN_USER -password $_PASSWORD -aesKey $_AES_KEY -domain-sid $_DOMAIN_SID $_TARGET_USER
```

> This command uses the compromised domain user credentials to request a forged TGT that impersonates the specified domain admin. The -request flag generates the ticket, -impersonate sets the target admin user, and the AES key ensures proper encryption mimicking a legitimate ticket. The baduser argument ($_TARGET_USER) is ignored in the PAC but included for compatibility. Expected output includes a .ccache file containing the Sapphire Ticket, which can be verified by checking the file creation and using klist to inspect the ticket details.

### Step 2: Load and Use the Sapphire Ticket

**Context**: Export the generated ticket and load it into the current session for immediate use. This allows tools like psexec.py or smbclient.py from Impacket to authenticate with the forged ticket.

**Instructions**: Set the KRB5CCNAME environment variable to point to the generated .ccache file:
```bash
export KRB5CCNAME=/path/to/sapphire_ticket.ccache
```
Then test access to a remote resource, such as a domain controller share:
```bash
smbclient.py $_DOMAIN/$DOMAIN_ADMIN@$_TARGET_DC -k
```

> Success is indicated by successful authentication without prompting for credentials and access to admin-restricted shares. If the ticket is loaded correctly, commands like klist should show the impersonated user's principal.

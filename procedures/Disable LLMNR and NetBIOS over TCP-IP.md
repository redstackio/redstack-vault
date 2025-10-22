---
id: b7cc2f2c-e9bf-4faf-8f4b-64d9aa353758
name: Disable LLMNR and NetBIOS over TCP/IP
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:05.437839+00:00'
updated_at: '2023-04-10T20:25:45.083041+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
- '[[Network Sniffing|T1040 - Network Sniffing]]'
- '[[Pass the Hash|T1075 - Pass the Hash]]'
- '[[Remote Services|T1021 - Remote Services]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Man-in-the-Middle attacks & relaying]]'
- '[[SMB Signing Disabled and IPv4]]'
commands:
- '[[Disable Multicast Name Resolution]]'
- '[[Disable NetBIOS over TCP/IP]]'
---

# Disable LLMNR and NetBIOS over TCP/IP

## Summary

This procedure disables LLMNR and NetBIOS over TCP/IP in group policy to prevent man-in-the-middle attacks and relaying attacks. These attacks can occur when SMB signing is disabled and IPv4 is being used. By disabling LLMNR and NetBIOS over TCP/IP, attackers can't use these protocols to intercept 

## Description

# Description

This procedure disables LLMNR and NetBIOS over TCP/IP in group policy to prevent man-in-the-middle attacks and relaying attacks. These attacks can occur when SMB signing is disabled and IPv4 is being used. By disabling LLMNR and NetBIOS over TCP/IP, attackers can't use these protocols to intercept authentication requests and relay them to gain access to sensitive information. This procedure can help prevent attackers from gaining access to user credentials and sensitive information, and can help protect the organization from data breaches and other security incidents.

## Requirements

1. Access to group policy settings

1. Knowledge of LLMNR and NetBIOS over TCP/IP protocols

## Defense

1. Enable SMB signing to prevent man-in-the-middle attacks

1. Use IPv6 instead of IPv4 to prevent relaying attacks

1. Implement multi-factor authentication to prevent credential stuffing and pass the hash attacks

## Objectives

1. Prevent man-in-the-middle attacks and relaying attacks

1. Protect sensitive information and user credentials

1. Reduce the risk of data breaches and other security incidents

# Instructions

1. To disable LLMNR via group policy, follow these steps:

**Code**: [[Open gpedit.msc and navigate to Computer Configura]]

> 1. Open the Group Policy Editor by typing gpedit.msc in the Start menu search bar and pressing Enter.

2. Navigate to Computer Configuration > Administrative Templates > Network > DNS Client.

3. Locate the 'Turn off multicast name resolution' policy and double-click on it.

4. Select the 'Enabled' option and click on 'OK'.

This will disable LLMNR via group policy on the computer.

**Command** ([[Disable Multicast Name Resolution]]):

```bash
Open gpedit.msc and navigate to Computer Configuration > Administrative Templates > Network > DNS Client > Turn off multicast name resolution and set to Enabled
```

2. To disable NetBIOS over TCP/IP, follow these steps:
1. Open the Network and Sharing Center.
2. Click on Change adapter settings.
3. Right-click on the network adapter you want to change and select Properties.
4. Scroll down and click on Internet Protocol Version 4 (TCP/IPv4) and then click on Properties.
5. Click on Advanced.
6. Click on the WINS tab.
7. Under "NetBIOS setting", select Disable NetBIOS over TCP/IP.
8. Click OK to save changes.

**Code**: [[This can be achieved by navigating through the GUI]]

> NetBIOS over TCP/IP (NBT-NS) is an outdated protocol that is no longer needed in modern networks. Disabling it can improve network performance and security. This command provides step-by-step instructions on how to disable NBT-NS on a Windows machine through the GUI.

**Command** ([[Disable NetBIOS over TCP/IP]]):

```bash
Navigate through the GUI to Network card > Properties > IPv4 > Advanced > WINS and then under "NetBIOS setting" select Disable NetBIOS over TCP/IP
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]
- [[Network Sniffing|T1040 - Network Sniffing]]
- [[Pass the Hash|T1075 - Pass the Hash]]
- [[Remote Services|T1021 - Remote Services]]

## Commands Used

- [[Disable Multicast Name Resolution]]
- [[Disable NetBIOS over TCP/IP]]

## Tags

- [[Active Directory Attacks]]
- [[Man-in-the-Middle attacks & relaying]]
- [[SMB Signing Disabled and IPv4]]

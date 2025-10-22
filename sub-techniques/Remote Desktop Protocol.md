---
id: 926f3fc7-a753-4a42-8a46-87c5b0f16520
name: Remote Desktop Protocol
type: sub-technique
mitre_id: T1021.001
mitre_url: null
created_at: '2023-04-06T00:31:27.126438+00:00'
updated_at: '2023-04-06T00:31:27.126438+00:00'
parent_technique: '[[Remote Services|T1021 - Remote Services]]'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
procedures:
- '[[Go Application Proxification with Graftcp]]'
- '[[Inter-User Messaging]]'
- '[[Network Pivoting with plink Port Forwarding]]'
- '[[Ruby Bind Shell]]'
- '[[SSH Beacon Payload with Cobalt Strike]]'
---

# Remote Desktop Protocol

**MITRE ID**: T1021.001

**Parent Technique**: [[Remote Services|T1021 - Remote Services]]

This is a sub-technique of T1021 - Remote Services.

## Summary

Adversaries may use [Valid Accounts](https://attack.mitre.org/techniques/T1078) to log into a computer using the Remote Desktop Protocol (RDP). The adversary may then perform actions as the logged-on user.

Remote desktop is a common feature in operating systems. It allows a user to log into an inte

## Description

Adversaries may use [Valid Accounts](https://attack.mitre.org/techniques/T1078) to log into a computer using the Remote Desktop Protocol (RDP). The adversary may then perform actions as the logged-on user.

Remote desktop is a common feature in operating systems. It allows a user to log into an interactive session with a system desktop graphical user interface on a remote system. Microsoft refers to its implementation of the Remote Desktop Protocol (RDP) as Remote Desktop Services (RDS).(Citation: TechNet Remote Desktop Services) 

Adversaries may connect to a remote system over RDP/RDS to expand access if the service is enabled and allows access to accounts with known credentials. Adversaries will likely use Credential Access techniques to acquire credentials to use with RDP. Adversaries may also use RDP in conjunction with the [Accessibility Features](https://attack.mitre.org/techniques/T1546/008) or [Terminal Services DLL](https://attack.mitre.org/techniques/T1505/005) for Persistence.(Citation: Alperovitch Malware)

## Tactics

This sub-technique is used in the following tactics:

- [[Lateral Movement|TA0008 - Lateral Movement]]

## Related Procedures

There are 5 procedures using this sub-technique:

- [[Go Application Proxification with Graftcp]]
- [[Inter-User Messaging]]
- [[Network Pivoting with plink Port Forwarding]]
- [[Ruby Bind Shell]]
- [[SSH Beacon Payload with Cobalt Strike]]

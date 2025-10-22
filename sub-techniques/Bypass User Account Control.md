---
id: c4b4d68a-7892-48a7-87aa-5a352c6f6e20
name: Bypass User Account Control
type: sub-technique
mitre_id: T1548.002
mitre_url: null
created_at: '2023-04-06T00:31:25.575860+00:00'
updated_at: '2023-04-06T00:31:25.575860+00:00'
parent_technique: '[[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control
  Mechanism]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
procedures:
- '[[Abusing Active Directory ACLs/ACEs - GenericWrite and Remote Connection Manager]]'
- '[[Abusing Golden Privileges with Juicy Potato]]'
- '[[Abusing Linux cgroup v1 with CAP_SYS_ADMIN]]'
- '[[Active Directory Certificate Services Access Control Vulnerabilities]]'
- '[[Application Escape and Breakout via Unassociated Protocols in Internet Explorer]]'
- '[[EFSPotato Privilege Escalation]]'
- '[[Golden Certificate Domain Persistence]]'
- '[[JEA for Limiting PowerShell Usage]]'
- '[[Linux - Privilege Escalation via Doas]]'
- '[[Linux - SUDO NOPASSWD Privilege Escalation via Vim]]'
- '[[PrinterNightmare Privilege Escalation]]'
- '[[Vulnerable Certificate Authority Access Control]]'
- '[[Windows - EoP Privileged File Write via DiagHub Standard Collector Service]]'
---

# Bypass User Account Control

**MITRE ID**: T1548.002

**Parent Technique**: [[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]

This is a sub-technique of T1548 - Abuse Elevation Control Mechanism.

## Summary

Adversaries may bypass UAC mechanisms to elevate process privileges on system. Windows User Account Control (UAC) allows a program to elevate its privileges (tracked as integrity levels ranging from low to high) to perform a task under administrator-level permissions, possibly by prompting the user 

## Description

Adversaries may bypass UAC mechanisms to elevate process privileges on system. Windows User Account Control (UAC) allows a program to elevate its privileges (tracked as integrity levels ranging from low to high) to perform a task under administrator-level permissions, possibly by prompting the user for confirmation. The impact to the user ranges from denying the operation under high enforcement to allowing the user to perform the action if they are in the local administrators group and click through the prompt or allowing them to enter an administrator password to complete the action.(Citation: TechNet How UAC Works)

If the UAC protection level of a computer is set to anything but the highest level, certain Windows programs can elevate privileges or execute some elevated [Component Object Model](https://attack.mitre.org/techniques/T1559/001) objects without prompting the user through the UAC notification box.(Citation: TechNet Inside UAC)(Citation: MSDN COM Elevation) An example of this is use of [Rundll32](https://attack.mitre.org/techniques/T1218/011) to load a specifically crafted DLL which loads an auto-elevated [Component Object Model](https://attack.mitre.org/techniques/T1559/001) object and performs a file operation in a protected directory which would typically require elevated access. Malicious software may also be injected into a trusted process to gain elevated privileges without prompting a user.(Citation: Davidson Windows)

Many methods have been discovered to bypass UAC. The Github readme page for UACME contains an extensive list of methods(Citation: Github UACMe) that have been discovered and implemented, but may not be a comprehensive list of bypasses. Additional bypass methods are regularly discovered and some used in the wild, such as:

* <code>eventvwr.exe</code> can auto-elevate and execute a specified binary or script.(Citation: enigma0x3 Fileless UAC Bypass)(Citation: Fortinet Fareit)

Another bypass is possible through some lateral movement techniques if credentials for an account with administrator privileges are known, since UAC is a single system security mechanism, and the privilege or integrity of a process running on one system will be unknown on remote systems and default to high integrity.(Citation: SANS UAC Bypass)

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

## Related Procedures

There are 13 procedures using this sub-technique:

- [[Abusing Active Directory ACLs/ACEs - GenericWrite and Remote Connection Manager]]
- [[Abusing Golden Privileges with Juicy Potato]]
- [[Abusing Linux cgroup v1 with CAP_SYS_ADMIN]]
- [[Active Directory Certificate Services Access Control Vulnerabilities]]
- [[Application Escape and Breakout via Unassociated Protocols in Internet Explorer]]
- [[EFSPotato Privilege Escalation]]
- [[Golden Certificate Domain Persistence]]
- [[JEA for Limiting PowerShell Usage]]
- [[Linux - Privilege Escalation via Doas]]
- [[Linux - SUDO NOPASSWD Privilege Escalation via Vim]]
- [[PrinterNightmare Privilege Escalation]]
- [[Vulnerable Certificate Authority Access Control]]
- [[Windows - EoP Privileged File Write via DiagHub Standard Collector Service]]

---
id: fe825c46-d9c0-4ba9-b55f-a0d8eac825a3
name: Abuse Elevation Control Mechanism
type: technique
mitre_id: T1548
mitre_url: null
created_at: '2023-04-06T00:31:26.269524+00:00'
updated_at: '2023-04-06T03:56:32.672603+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege-Escalation-via-Direct-URL-Access|TA0004 - Privilege Escalation]]'
procedures:
- '[[Abusing Active Directory ACLs/ACEs - GenericWrite and Remote Connection Manager]]'
- '[[Abusing-Golden-Privileges-with-Juicy-Potato]]'
- '[[Abuse-Linux-Cgroup-v1-with-CAP-SYS-ADMIN-for-Host-Privilege-Escalation]]'
- '[[Active-Directory-Certificate-Services-Access-Control-Vulnerabilities]]'
- '[[Request-Alternative-Name-Certificate-via-AD-CS]]'
- '[[Application-Escape-and-Breakout-via-Unassociated-Protocols-in-Firefox]]'
- '[[Enumerate-DB2-User-Privileges]]'
- '[[efs-potato-privilege-escalation]]'
- '[[Golden-Certificate-Domain-Persistence]]'
- '[[implement-jea-to-limit-powershell-cmdlet-usage]]'
- '[[Kerberos-Unconstrained-Delegation-with-SpoolService-Abuse]]'
- '[[Linux-List-Capabilities-of-Executables]]'
- '[[Linux-Privilege-Escalation-via-Doas-Misconfiguration]]'
- '[[linux-privilege-escalation-via-ld_preload-and-nopasswd]]'
- '[[Linux-Privilege-Escalation-via-SUDO-Injection]]'
- '[[Linux-Privilege-Escalation-via-Systemd-Timers]]'
- '[[Linux Privilege Escalation via Writable /etc/sudoers]]'
- '[[Linux-SUDO-NOPASSWD-Privilege-Escalation-via-Vim]]'
- '[[Linux-SUID-Binary-Persistence]]'
- '[[Linux - Writable /etc/sysconfig/network-scripts/ Privilege Escalation]]'
- '[[MS-EFSRPC-Abuse-via-PetitPotam-and-Unconstrained-Delegation]]'
- '[[Pass-The-Certificate-Attack]]'
- '[[PrinterNightmare-Privilege-Escalation]]'
- '[[Printer-Spooler-Service-Elevation-of-Privilege]]'
- '[[Vulnerable-Certificate-Authority-Access-Control]]'
- '[[Windows-AlwaysInstallElevated-Privilege-Escalation]]'
- '[[Windows - EoP Privileged File Write via DiagHub Standard Collector Service]]'
---

# Abuse Elevation Control Mechanism

**MITRE ID**: T1548

## Description

Adversaries may circumvent mechanisms designed to control elevate privileges to gain higher-level permissions. Most modern systems contain native elevation control mechanisms that are intended to limit privileges that a user can perform on a machine. Authorization has to be granted to specific users in order to perform tasks that can be considered of higher risk. An adversary can perform several methods to take advantage of built-in control mechanisms in order to escalate privileges on a system.



## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege-Escalation-via-Direct-URL-Access|TA0004 - Privilege Escalation]]

## Related Procedures (27)

- [[Abusing Active Directory ACLs/ACEs - GenericWrite and Remote Connection Manager]]
- [[Abusing-Golden-Privileges-with-Juicy-Potato]]
- [[Abuse-Linux-Cgroup-v1-with-CAP-SYS-ADMIN-for-Host-Privilege-Escalation]]
- [[Active-Directory-Certificate-Services-Access-Control-Vulnerabilities]]
- [[Request-Alternative-Name-Certificate-via-AD-CS]]
- [[Application-Escape-and-Breakout-via-Unassociated-Protocols-in-Firefox]]
- [[Enumerate-DB2-User-Privileges]]
- [[efs-potato-privilege-escalation]]
- [[Golden-Certificate-Domain-Persistence]]
- [[implement-jea-to-limit-powershell-cmdlet-usage]]
- [[Kerberos-Unconstrained-Delegation-with-SpoolService-Abuse]]
- [[Linux-List-Capabilities-of-Executables]]
- [[Linux-Privilege-Escalation-via-Doas-Misconfiguration]]
- [[linux-privilege-escalation-via-ld_preload-and-nopasswd]]
- [[Linux-Privilege-Escalation-via-SUDO-Injection]]
- [[Linux-Privilege-Escalation-via-Systemd-Timers]]
- [[Linux Privilege Escalation via Writable /etc/sudoers]]
- [[Linux-SUDO-NOPASSWD-Privilege-Escalation-via-Vim]]
- [[Linux-SUID-Binary-Persistence]]
- [[Linux - Writable /etc/sysconfig/network-scripts/ Privilege Escalation]]

*...and 7 more*



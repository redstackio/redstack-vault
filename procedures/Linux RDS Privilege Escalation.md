---
id: cca1342c-143e-469d-b8b7-f1fce4297313
name: Linux RDS Privilege Escalation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:19.694679+00:00'
updated_at: '2023-04-10T20:34:23.699437+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Registry Run Keys / Startup Folder|T1060 - Registry Run Keys / Startup Folder]]'
tags:
- '[[CVE-2010-3904 (RDS)]]'
- '[[Kernel Exploits]]'
- '[[Linux - Privilege Escalation]]'
commands:
- '[[Add malicious file]]'
---

# Linux RDS Privilege Escalation

## Summary

Linux RDS Privilege Escalation is a technique used by attackers to elevate their privileges on a Linux system. The CVE-2010-3904 vulnerability in the RDS (Remote Desktop Services) protocol in Linux kernel versions 2.6.30 through 2.6.36-rc8 can be exploited to gain root-level access on the target sy

## Description

# Description

Linux RDS Privilege Escalation is a technique used by attackers to elevate their privileges on a Linux system. The CVE-2010-3904 vulnerability in the RDS (Remote Desktop Services) protocol in Linux kernel versions 2.6.30 through 2.6.36-rc8 can be exploited to gain root-level access on the target system. By exploiting this vulnerability, attackers can bypass access controls and gain unauthorized access to sensitive information. This technique is commonly used by attackers to gain persistence on a compromised system, allowing them to maintain access and continue to steal data over a long period of time.

Technical Explanation: The RDS protocol is used by Linux systems for remote desktop services. The vulnerability allows attackers to send a specially crafted packet to the target system, which triggers a buffer overflow in the kernel. This buffer overflow can be used to execute arbitrary code with root-level privileges.

Business Value: This technique is a serious threat to organizations as it allows attackers to gain complete control over a Linux system. This can lead to data theft, ransomware attacks, and other types of cybercrime. By exploiting this vulnerability, attackers can gain persistence on a compromised system, allowing them to maintain access and continue to steal data over a long period of time.

## Requirements

1. Access to a Linux system with the RDS protocol enabled

1. Knowledge of the CVE-2010-3904 vulnerability

1. Ability to execute the Linux RDS exploit

## Defense

1. Apply security patches to the Linux kernel to mitigate the CVE-2010-3904 vulnerability

1. Disable the RDS protocol if it is not required for business operations

1. Implement network segmentation and access controls to limit the impact of a potential attack

## Objectives

1. Gain root-level access on a Linux system

1. Maintain persistence on a compromised system

# Instructions

1. This exploit targets a vulnerability in the Linux Kernel and can be used to gain root access to the system. To use this exploit, download the code from the provided link and execute it on the target system. Please note that this exploit should only be used for ethical hacking purposes and with the permission of the system owner.

**Code**: [[https://www.exploit-db.com/exploits/15285/]]

> The exploit targets a vulnerability in the Linux Kernel that allows an attacker to gain root access to the system. This vulnerability can be exploited by sending a specially crafted packet to the target system. The exploit code provided in the link is written in C and can be compiled on the target system using a C compiler. Once the exploit is executed, the attacker will have root access to the system and can perform any action they desire. It is important to note that this exploit should only be used for ethical hacking purposes and with the permission of the system owner.

**Command** ([[Add malicious file]]):

```bash
../../../../windows/system32/calc.exe
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Registry Run Keys / Startup Folder|T1060 - Registry Run Keys / Startup Folder]]

## Commands Used

- [[Add malicious file]]

## Tags

- [[CVE-2010-3904 (RDS)]]
- [[Kernel Exploits]]
- [[Linux - Privilege Escalation]]

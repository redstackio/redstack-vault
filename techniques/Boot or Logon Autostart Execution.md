---
id: d0f82713-94f7-4874-b8c2-4f124602b910
name: Boot or Logon Autostart Execution
type: technique
mitre_id: T1547
mitre_url: null
created_at: '2023-04-06T00:31:25.692148+00:00'
updated_at: '2023-05-25T04:23:14.566185+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
procedures:
- '[[Abuse Group Policy Objects with pyGPOAbuse]]'
- '[[Linux - Privilege Escalation via LD_PRELOAD and NOPASSWD]]'
- '[[Linux Reverse Shell Persistence with Ncat]]'
- '[[Linux - SSH Key Predictable PRNG Privilege Escalation]]'
- '[[Linux - Startup Service Backdoor with Reverse Shell]]'
- '[[Windows Simple User Startup Persistence]]'
- '[[Windows VM Persistence with VirtualBox and VHD]]'
---

# Boot or Logon Autostart Execution

**MITRE ID**: T1547

## Description

Adversaries may configure system settings to automatically execute a program during system boot or logon to maintain persistence or gain higher-level privileges on compromised systems. Operating systems may have mechanisms for automatically running a program on system boot or account logon.(Citation: Microsoft Run Key)(Citation: MSDN Authentication Packages)(Citation: Microsoft TimeProvider)(Citation: Cylance Reg Persistence Sept 2013)(Citation: Linux Kernel Programming) These mechanisms may include automatically executing programs that are placed in specially designated directories or are referenced by repositories that store configuration information, such as the Windows Registry. An adversary may achieve the same goal by modifying or extending features of the kernel.

Since some boot or logon autostart programs run with higher privileges, an adversary may leverage these to elevate privileges.

## Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

## Related Procedures (7)

- [[Abuse Group Policy Objects with pyGPOAbuse]]
- [[Linux - Privilege Escalation via LD_PRELOAD and NOPASSWD]]
- [[Linux Reverse Shell Persistence with Ncat]]
- [[Linux - SSH Key Predictable PRNG Privilege Escalation]]
- [[Linux - Startup Service Backdoor with Reverse Shell]]
- [[Windows Simple User Startup Persistence]]
- [[Windows VM Persistence with VirtualBox and VHD]]

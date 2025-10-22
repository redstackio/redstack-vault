---
id: 2d86f0d4-74da-43b8-ab97-2226d0d0e191
name: Hypervisor
type: technique
mitre_id: T1062
mitre_url: null
created_at: '2019-08-28T21:17:17.804212+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
---

# Hypervisor

**MITRE ID**: T1062

## Description

A type-1 hypervisor is a software layer that sits between the guest operating systems and system's hardware. [1] It presents a virtual running environment to an operating system. An example of a common hypervisor is Xen. [2] A type-1 hypervisor operates at a level below the operating system and could be designed with Rootkit functionality to hide its existence from the guest operating system. [3] A malicious hypervisor of this nature could be used to persist on systems through interruption.

# Detection

Type-1 hypervisors may be detected by performing timing analysis. Hypervisors emulate certain CPU instructions that would normally be executed by the hardware. If an instruction takes orders of magnitude longer to execute than normal on a system that should not contain a hypervisor, one may be present. [4]

# Mitigation

Prevent adversary access to privileged accounts necessary to install a hypervisor.

# Footnotes

[1] Wikipedia. (2016, May 23). Hypervisor. Retrieved June 11, 2016.

[2] Xen. (n.d.). In Wikipedia. Retrieved November 13, 2014.

[3] Myers, M., and Youndt, S. (2007). An Introduction to Hardware-Assisted Virtual Machine (HVM) Rootkits. Retrieved November 13, 2014.

[4] virtualization.info. (Interviewer) & Liguori, A. (Interviewee). (2006, August 11). Debunking Blue Pill myth [Interview transcript]. Retrieved November 13, 2014.

## Defense

Prevent adversary access to privileged accounts necessary to install a hypervisor.

## Tactics

- [[Persistence|TA0003 - Persistence]]

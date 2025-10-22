---
id: 9e3c647b-6ef0-41e5-a20c-8bd8a99cd00c
name: Windows Service
type: sub-technique
mitre_id: T1543.003
mitre_url: null
created_at: '2023-04-06T00:31:25.777300+00:00'
updated_at: '2023-04-06T00:31:25.777300+00:00'
parent_technique: '[[Create or Modify System Process|T1543 - Create or Modify System
  Process]]'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
procedures:
- '[[AWS SSH Persistence with Authorized Keys]]'
- '[[Bashrc Backdoor Persistence]]'
- '[[IIS Raid Backdoor Persistence]]'
- '[[Linux - Backdooring User Startup File]]'
- '[[Linux - Startup Service Backdoor with Reverse Shell]]'
- '[[Windows Simple User Startup Persistence]]'
- '[[Windows Subsystem for Linux Persistence]]'
---

# Windows Service

**MITRE ID**: T1543.003

**Parent Technique**: [[Create or Modify System Process|T1543 - Create or Modify System Process]]

This is a sub-technique of T1543 - Create or Modify System Process.

## Summary

Adversaries may create or modify Windows services to repeatedly execute malicious payloads as part of persistence. When Windows boots up, it starts programs or applications called services that perform background system functions.(Citation: TechNet Services) Windows service configuration information

## Description

Adversaries may create or modify Windows services to repeatedly execute malicious payloads as part of persistence. When Windows boots up, it starts programs or applications called services that perform background system functions.(Citation: TechNet Services) Windows service configuration information, including the file path to the service's executable or recovery programs/commands, is stored in the Windows Registry.

Adversaries may install a new service or modify an existing service to execute at startup in order to persist on a system. Service configurations can be set or modified using system utilities (such as sc.exe), by directly modifying the Registry, or by interacting directly with the Windows API. 

Adversaries may also use services to install and execute malicious drivers. For example, after dropping a driver file (ex: `.sys`) to disk, the payload can be loaded and registered via [Native API](https://attack.mitre.org/techniques/T1106) functions such as `CreateServiceW()` (or manually via functions such as `ZwLoadDriver()` and `ZwSetValueKey()`), by creating the required service Registry values (i.e. [Modify Registry](https://attack.mitre.org/techniques/T1112)), or by using command-line utilities such as `PnPUtil.exe`.(Citation: Symantec W.32 Stuxnet Dossier)(Citation: Crowdstrike DriveSlayer February 2022)(Citation: Unit42 AcidBox June 2020) Adversaries may leverage these drivers as [Rootkit](https://attack.mitre.org/techniques/T1014)s to hide the presence of malicious activity on a system. Adversaries may also load a signed yet vulnerable driver onto a compromised machine (known as "Bring Your Own Vulnerable Driver" (BYOVD)) as part of [Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1068).(Citation: ESET InvisiMole June 2020)(Citation: Unit42 AcidBox June 2020)

Services may be created with administrator privileges but are executed under SYSTEM privileges, so an adversary may also use a service to escalate privileges. Adversaries may also directly start services through [Service Execution](https://attack.mitre.org/techniques/T1569/002). To make detection analysis more challenging, malicious services may also incorporate [Masquerade Task or Service](https://attack.mitre.org/techniques/T1036/004) (ex: using a service and/or payload name related to a legitimate OS or benign software component).

## Tactics

This sub-technique is used in the following tactics:

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

## Related Procedures

There are 7 procedures using this sub-technique:

- [[AWS SSH Persistence with Authorized Keys]]
- [[Bashrc Backdoor Persistence]]
- [[IIS Raid Backdoor Persistence]]
- [[Linux - Backdooring User Startup File]]
- [[Linux - Startup Service Backdoor with Reverse Shell]]
- [[Windows Simple User Startup Persistence]]
- [[Windows Subsystem for Linux Persistence]]

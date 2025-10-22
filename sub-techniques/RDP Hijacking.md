---
id: ba31ed24-37f1-4563-93cc-683063529246
name: RDP Hijacking
type: sub-technique
mitre_id: T1563.002
mitre_url: null
created_at: '2023-04-06T00:31:27.062875+00:00'
updated_at: '2023-04-06T00:31:27.062875+00:00'
parent_technique: '[[Remote Service Session Hijacking|T1563 - Remote Service Session
  Hijacking]]'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
procedures:
- '[[DCOM Shell Command Execution via MMC Application Class]]'
- '[[RDP Session Takeover with Mimikatz]]'
- '[[RDP Session Takeover with Mimikatz]]'
- '[[Subdomain Enumeration and Takeover using Hostile Subdomain Bruteforcer]]'
---

# RDP Hijacking

**MITRE ID**: T1563.002

**Parent Technique**: [[Remote Service Session Hijacking|T1563 - Remote Service Session Hijacking]]

This is a sub-technique of T1563 - Remote Service Session Hijacking.

## Summary

Adversaries may hijack a legitimate user’s remote desktop session to move laterally within an environment. Remote desktop is a common feature in operating systems. It allows a user to log into an interactive session with a system desktop graphical user interface on a remote system. Microsoft refers 

## Description

Adversaries may hijack a legitimate user’s remote desktop session to move laterally within an environment. Remote desktop is a common feature in operating systems. It allows a user to log into an interactive session with a system desktop graphical user interface on a remote system. Microsoft refers to its implementation of the Remote Desktop Protocol (RDP) as Remote Desktop Services (RDS).(Citation: TechNet Remote Desktop Services)

Adversaries may perform RDP session hijacking which involves stealing a legitimate user's remote session. Typically, a user is notified when someone else is trying to steal their session. With System permissions and using Terminal Services Console, `c:\windows\system32\tscon.exe [session number to be stolen]`, an adversary can hijack a session without the need for credentials or prompts to the user.(Citation: RDP Hijacking Korznikov) This can be done remotely or locally and with active or disconnected sessions.(Citation: RDP Hijacking Medium) It can also lead to [Remote System Discovery](https://attack.mitre.org/techniques/T1018) and Privilege Escalation by stealing a Domain Admin or higher privileged account session. All of this can be done by using native Windows commands, but it has also been added as a feature in red teaming tools.(Citation: Kali Redsnarf)

## Tactics

This sub-technique is used in the following tactics:

- [[Lateral Movement|TA0008 - Lateral Movement]]

## Related Procedures

There are 4 procedures using this sub-technique:

- [[DCOM Shell Command Execution via MMC Application Class]]
- [[RDP Session Takeover with Mimikatz]]
- [[RDP Session Takeover with Mimikatz]]
- [[Subdomain Enumeration and Takeover using Hostile Subdomain Bruteforcer]]

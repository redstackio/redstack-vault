---
id: 8a6531f4-4862-479a-9b2a-2b54c7ef86f5
name: Event Triggered Execution
type: technique
mitre_id: T1546
mitre_url: null
created_at: '2023-04-06T00:31:26.777905+00:00'
updated_at: '2023-04-06T03:56:30.024945+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
procedures:
- '[[Abuse Group Policy Objects with pyGPOAbuse]]'
- '[[Abusing Shadow Copies for Privilege Escalation]]'
- '[[AWS Lambda Function Policy Enumeration]]'
- '[[Cobalt Strike Elevate Kit with Beacon Command Elevators]]'
- '[[Dart Reverse PowerShell Shell]]'
- '[[DCOM Shell Command Execution via MMC Application Class]]'
- '[[LAPS Password Expiration Time Persistence]]'
- '[[Linux - Docker Privilege Escalation]]'
- '[[Linux Password Looting via Recently Modified Files]]'
- '[[Linux Privilege Escalation via Capabilities Edit]]'
- '[[Linux - TMUX Session Hijacking]]'
- '[[Patching amsi.dll AmsiScanBuffer to bypass AMSI by rasta-mouse]]'
- '[[PrinterNightmare Privilege Escalation]]'
- '[[Printer Spooler Service Elevation of Privilege]]'
- '[[Windows Privilege Escalation using PowerUp, PrivescCheck, and WES-NG]]'
- '[[Windows - Privilege Escalation via Universal Printer Driver]]'
---

# Event Triggered Execution

**MITRE ID**: T1546

## Description

Adversaries may establish persistence and/or elevate privileges using system mechanisms that trigger execution based on specific events. Various operating systems have means to monitor and subscribe to events such as logons or other user activity such as running specific applications/binaries. Cloud environments may also support various functions and services that monitor and can be invoked in response to specific cloud events.(Citation: Backdooring an AWS account)(Citation: Varonis Power Automate Data Exfiltration)(Citation: Microsoft DART Case Report 001)

Adversaries may abuse these mechanisms as a means of maintaining persistent access to a victim via repeatedly executing malicious code. After gaining access to a victim system, adversaries may create/modify event triggers to point to malicious content that will be executed whenever the event trigger is invoked.(Citation: FireEye WMI 2015)(Citation: Malware Persistence on OS X)(Citation: amnesia malware)

Since the execution can be proxied by an account with higher permissions, such as SYSTEM or service accounts, an adversary may be able to abuse these triggered execution mechanisms to escalate their privileges. 

## Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

## Related Procedures (16)

- [[Abuse Group Policy Objects with pyGPOAbuse]]
- [[Abusing Shadow Copies for Privilege Escalation]]
- [[AWS Lambda Function Policy Enumeration]]
- [[Cobalt Strike Elevate Kit with Beacon Command Elevators]]
- [[Dart Reverse PowerShell Shell]]
- [[DCOM Shell Command Execution via MMC Application Class]]
- [[LAPS Password Expiration Time Persistence]]
- [[Linux - Docker Privilege Escalation]]
- [[Linux Password Looting via Recently Modified Files]]
- [[Linux Privilege Escalation via Capabilities Edit]]
- [[Linux - TMUX Session Hijacking]]
- [[Patching amsi.dll AmsiScanBuffer to bypass AMSI by rasta-mouse]]
- [[PrinterNightmare Privilege Escalation]]
- [[Printer Spooler Service Elevation of Privilege]]
- [[Windows Privilege Escalation using PowerUp, PrivescCheck, and WES-NG]]
- [[Windows - Privilege Escalation via Universal Printer Driver]]

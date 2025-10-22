---
id: 7d5e8fad-1cbb-4bbf-9a71-ebd8583b439a
name: CMSTP
type: technique
mitre_id: T1191
mitre_url: null
created_at: '2019-08-28T21:17:45.062161+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
procedures:
- '[[AWS RCE for Credential Access]]'
- '[[Bypassing Constrained Language Mode using Powershell DLL Runner]]'
- '[[Cassandra Login Bypass using Injection]]'
- '[[Gitlab/Github CI Command Execution]]'
- '[[Race Condition Turbo Intruder Attack]]'
- '[[Windows AppLocker Whitelist Bypass (cmstp.exe)]]'
---

# CMSTP

**MITRE ID**: T1191

## Description

The Microsoft Connection Manager Profile Installer (CMSTP.exe) is a command-line program used to install Connection Manager service profiles. [1] CMSTP.exe accepts an installation information file (INF) as a parameter and installs a service profile leveraged for remote access connections.Adversaries may supply CMSTP.exe with INF files infected with malicious commands. [2] Similar to Regsvr32 / "Squiblydoo", CMSTP.exe may be abused to load and execute DLLs [3]  and/or COM scriptlets (SCT) from remote servers. [4] [5] [6] This execution may also bypass AppLocker and other whitelisting defenses since CMSTP.exe is a legitimate, signed Microsoft application.CMSTP.exe can also be abused to Bypass User Account Control and execute arbitrary commands from a malicious INF through an auto-elevated COM interface. [3] [5] [6]

# Detection

Use process monitoring to detect and analyze the execution and arguments of CMSTP.exe. Compare recent invocations of CMSTP.exe with prior history of known good arguments and loaded files to determine anomalous and potentially adversarial activity.

Sysmon events can also be used to identify potential abuses of CMSTP.exe. Detection strategy may depend on the specific adversary procedure, but potential rules include: [6]

To detect loading and execution of local/remote payloads - Event 1 (Process creation) where ParentImage contains CMSTP.exe and/or Event 3 (Network connection) where Image contains CMSTP.exe and DestinationIP is external.To detect Bypass User Account Control via an auto-elevated COM interface - Event 10 (ProcessAccess) where CallTrace contains CMLUA.dll and/or Event 12 or 13 (RegistryEvent) where TargetObject contains CMMGR32.exe. Also monitor for events, such as the creation of processes (Sysmon Event 1), that involve auto-elevated CMSTP COM interfaces such as CMSTPLUA (3E5FC7F9-9A51-4367-9063-A120244FBEC7) and CMLUAUTIL (3E000D72-A845-4CD9-BD83-80C07C3B881F).

# Mitigation

CMSTP.exe may not be necessary within a given environment (unless using it for VPN connection installation). Consider using application whitelisting configured to block execution of CMSTP.exe if it is not required for a given system or network to prevent potential misuse by adversaries. [3]

# Footnotes

[1] Microsoft. (2009, October 8). How Connection Manager Works. Retrieved April 11, 2018.

[2] Carr, N. (2018, January 31). Here is some early bad cmstp.exe... Retrieved April 11, 2018.

[3] Moe, O. (2017, August 15). Research on CMSTP.exe. Retrieved April 11, 2018.

[4] Tyrer, N. (2018, January 30). CMSTP.exe - remote .sct execution applocker bypass. Retrieved April 11, 2018.

[5] Moe, O. (2018, March 1). Ultimate AppLocker Bypass List. Retrieved April 10, 2018.

[6] Seetharaman, N. (2018, July 7). Detecting CMSTP-Enabled Code Execution and UAC Bypass With Sysmon.. Retrieved August 6, 2018.

[7] Svajcer, V. (2018, July 31). Multiple Cobalt Personality Disorder. Retrieved September 5, 2018.

[8] Gorelik, M. (2018, October 08). Cobalt Group 2.0. Retrieved November 5, 2018.

[9] Unit 42. (2018, October 25). New Techniques to Uncover and Attribute Financial actors Commodity Builders and Infrastructure Revealed. Retrieved December 11, 2018.

[10] Singh, S. et al.. (2018, March 13). Iranian Threat Group Updates Tactics, Techniques and Procedures in Spear Phishing Campaign. Retrieved April 11, 2018.

## Defense

CMSTP.exe may not be necessary within a given environment (unless using it for VPN connection installation). Consider using application whitelisting configured to block execution of CMSTP.exe if it is not required for a given system or network to prevent 

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

## Related Procedures (6)

- [[AWS RCE for Credential Access]]
- [[Bypassing Constrained Language Mode using Powershell DLL Runner]]
- [[Cassandra Login Bypass using Injection]]
- [[Gitlab/Github CI Command Execution]]
- [[Race Condition Turbo Intruder Attack]]
- [[Windows AppLocker Whitelist Bypass (cmstp.exe)]]

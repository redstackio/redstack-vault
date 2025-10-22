---
id: 513296d3-251d-43fb-91d9-67921aeced9d
name: Service Execution
type: technique
mitre_id: T1035
mitre_url: null
created_at: '2019-08-28T21:17:40.794148+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
procedures:
- '[[Abusing DNSAdmins Group to Change DNS Service DLL]]'
- '[[DC PrintSpooler Service Check and ntlmrelayx with printerbug.py]]'
- '[[Escalate from an Administrator Session to SYSTEM (Windows)]]'
- '[[Pass the Hash with Meterpreter]]'
- '[[Perl Bind Shell]]'
- '[[PrintNightmare - Exploiting CVE to gain SYSTEM shell on DC via Anonymous SMB
  Server]]'
- '[[PrintNightmare WebDAV Attack]]'
- '[[UsoSvc Service Account Remote Command Execution]]'
- '[[Windows - Elevated Services Backdoor Persistence]]'
- '[[Windows Privilege Escalation - Processes and Tasks Enumeration]]'
- '[[Windows - Restore Service Account Privileges via Impersonation]]'
- '[[Windows Service Persistence with Calculator]]'
- '[[Windows - Using Impacket and PSExec with Credentials]]'
---

# Service Execution

**MITRE ID**: T1035

## Description

Adversaries may execute a binary, command, or script via a method that interacts with Windows services, such as the Service Control Manager. This can be done by either creating a new service or modifying an existing service. This technique is the execution used in conjunction with New Service and Modify Existing Service during service persistence or privilege escalation.

# Detection

Changes to service Registry entries and command-line invocation of tools capable of modifying services that do not correlate with known software, patch cycles, etc., may be suspicious. If a service is used only to execute a binary or script and not to persist, then it will likely be changed back to its original form shortly after the service is restarted so the service is not left broken, as is the case with the common administrator tool PsExec.

# Mitigation

Ensure that permissions disallow services that run at a higher permissions level from being created or interacted with by a user with a lower permission level. Also ensure that high permission level service binaries cannot be replaced or modified by users with a lower permission level.

Identify unnecessary system utilities or potentially malicious software that may be used to interact with Windows services, and audit and/or block them by using whitelisting [28] tools, like AppLocker, [29] [30] or Software Restriction Policies [31] where appropriate. [32]

# Footnotes

[1] Dumont, R. (2019, March 20). Fake or Fake: Keeping up with OceanLotus decoys. Retrieved April 1, 2019.

[2] Lee, B. Grunzweig, J. (2015, December 22). BBSRAT Attacks Targeting Russian Organizations Linked to Roaming Tiger. Retrieved August 19, 2016.

[3] Strategic Cyber LLC. (2017, March 14). Cobalt Strike Manual. Retrieved May 24, 2017.

[4] Cobalt Strike. (2017, December 8). Tactics, Techniques, and Procedures. Retrieved December 20, 2017.

[5] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[6] McKeague, B. et al. (2019, April 5). Pick-Six: Intercepting a FIN6 Intrusion, an Actor Recently Tied to Ryuk and LockerGoga Ransomware. Retrieved April 17, 2019.

[7] Sherstobitoff, R. (2018, March 02). McAfee Uncovers Operation Honeybee, a Malicious Document Campaign Targeting Humanitarian Aid Groups. Retrieved May 16, 2018.

[8] US-CERT. (2019, April 10). MAR-10135536-8 – North Korean Trojan: HOPLIGHT. Retrieved April 19, 2019.

[9] Fitzgerald, P. (2010, January 26). How Trojan.Hydraq Stays On Your Computer. Retrieved February 22, 2018.

[10] SecureAuth. (n.d.).  Retrieved January 15, 2019.

[11] Smallridge, R. (2018, March 10). APT15 is alive and strong: An analysis of RoyalCli and RoyalDNS. Retrieved April 4, 2018.

[12] Magius, J., et al. (2017, July 19). Koadic. Retrieved June 18, 2018.

[13] Savill, J. (1999, March 4). Net.exe reference. Retrieved September 22, 2015.

[14] Cylance. (2014, December). Operation Cleaver. Retrieved September 14, 2017.

[15] Chiu, A. (2016, June 27). New Ransomware Variant "Nyetya" Compromises Systems Worldwide. Retrieved March 26, 2019.

[16] US-CERT. (2017, July 1). Alert (TA17-181A): Petya Ransomware. Retrieved March 15, 2019.

[17] Mercer, W. and Rascagneres, P. (2018, February 12). Olympic Destroyer Takes Aim At Winter Olympics. Retrieved March 14, 2019.

[18] Nettitude. (2016, June 8). PoshC2: Powershell C2 Server and Implants. Retrieved April 23, 2019.

[19] Sherstobitoff, R., Malhotra, A. (2018, April 24). Analyzing Operation GhostSecret: Attack Seeks to Steal Data Worldwide. Retrieved May 16, 2018.

[20] Russinovich, M. (2014, May 2). Windows Sysinternals PsExec v2.11. Retrieved May 13, 2015.

[21] Nicolas Verdier. (n.d.). Retrieved January 29, 2018.

[22] Symantec Security Response. (2016, September 6). Buckeye cyberespionage group shifts gaze from US to Hong Kong. Retrieved September 26, 2016.

[23] Falcone, R.. (2016, November 30). Shamoon 2: Return of the Disttrack Wiper. Retrieved January 11, 2017.

[24] Prakash, T. (2017, June 21). Run commands on Windows system remotely using Winexe. Retrieved January 22, 2018.

[25] Anthe, C. et al. (2016, December 14). Microsoft Security Intelligence Report Volume 21. Retrieved November 27, 2017.

[26] Microsoft. (2017, November 9). Backdoor:Win32/Wingbird.A!dha. Retrieved November 27, 2017.

[27] Rayaprolu, A.. (2011, April 12). xCmd an Alternative to PsExec. Retrieved August 10, 2016.

[28] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[29] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[30] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[31] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[32] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Defense

Ensure that permissions disallow services that run at a higher permissions level from being created or interacted with by a user with a lower permission level. Also ensure that high permission level service binaries cannot be replaced or modified by users

## Tactics

- [[Execution|TA0002 - Execution]]

## Related Procedures (13)

- [[Abusing DNSAdmins Group to Change DNS Service DLL]]
- [[DC PrintSpooler Service Check and ntlmrelayx with printerbug.py]]
- [[Escalate from an Administrator Session to SYSTEM (Windows)]]
- [[Pass the Hash with Meterpreter]]
- [[Perl Bind Shell]]
- [[PrintNightmare - Exploiting CVE to gain SYSTEM shell on DC via Anonymous SMB Server]]
- [[PrintNightmare WebDAV Attack]]
- [[UsoSvc Service Account Remote Command Execution]]
- [[Windows - Elevated Services Backdoor Persistence]]
- [[Windows Privilege Escalation - Processes and Tasks Enumeration]]
- [[Windows - Restore Service Account Privileges via Impersonation]]
- [[Windows Service Persistence with Calculator]]
- [[Windows - Using Impacket and PSExec with Credentials]]

---
id: e80a2519-0cdb-4cca-9485-c0d19d1203b8
name: Windows Management Instrumentation Event Subscription
type: technique
mitre_id: T1084
mitre_url: null
created_at: '2019-08-28T21:17:41.478194+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
procedures:
- '[[Windows 10+ Binary Replacement via HID.dll]]'
---

# Windows Management Instrumentation Event Subscription

**MITRE ID**: T1084

## Description

Windows Management Instrumentation (WMI) can be used to install event filters, providers, consumers, and bindings that execute code when a defined event occurs. Adversaries may use the capabilities of WMI to subscribe to an event and execute arbitrary code when that event occurs, providing persistence on a system. Adversaries may attempt to evade detection of this technique by compiling WMI scripts. [1] Examples of events that may be subscribed to are the wall clock time or the computer's uptime. [2] Several threat groups have reportedly used this technique to maintain persistence. [3]

# Detection

Monitor WMI event subscription entries, comparing current WMI event subscriptions to known good subscriptions for each host. Tools such as Sysinternals Autoruns may also be used to detect WMI changes that could be attempts at persistence. [11]

# Mitigation

Disabling WMI services may cause system instability and should be evaluated to assess the impact to a network. By default, only administrators are allowed to connect remotely using WMI; restrict other users that are allowed to connect, or disallow all users from connecting remotely to WMI. Prevent credential overlap across systems of administrator and privileged accounts. [10]

# Footnotes

[1] Dell SecureWorks Counter Threat Unit™ (CTU) Research Team. (2016, March 28). A Novel WMI Persistence Implementation. Retrieved March 30, 2016.

[2] Kazanciyan, R. & Hastings, M. (2014). Defcon 22 Presentation. Investigating PowerShell Attacks [slides]. Retrieved November 3, 2014.

[3] Mandiant. (2015, February 24). M-Trends 2015: A View from the Front Lines. Retrieved May 18, 2016.

[4] Windows Defender Advanced Threat Hunting Team. (2016, April 29). PLATINUM: Targeted attacks in South and Southeast Asia. Retrieved February 15, 2018.

[5] Dunwoody, M. and Carr, N.. (2016, September 27). No Easy Breach DerbyCon 2016. Retrieved October 4, 2016.

[6] FireEye. (2018, March 16). Suspected Chinese Cyber Espionage Group (TEMP.Periscope) Targeting U.S. Engineering and Maritime Industries. Retrieved April 11, 2018.

[7] Nettitude. (2016, June 8). PoshC2: Powershell C2 Server and Implants. Retrieved April 23, 2019.

[8] Dunwoody, M.. (2017, April 3). Dissecting One of APT29’s Fileless WMI and PowerShell Backdoors (POSHSPY). Retrieved April 5, 2017.

[9] Ackerman, G., et al. (2018, December 21). OVERRULED: Containing a Potentially Destructive Adversary. Retrieved January 17, 2019.

[10] Ballenthin, W., et al. (2015). Windows Management Instrumentation (WMI) Offense, Defense, and Forensics. Retrieved March 30, 2016.

[11] Russinovich, M. (2016, January 4). Autoruns for Windows v13.51. Retrieved June 6, 2016.

## Defense

Disabling WMI services may cause system instability and should be evaluated to assess the impact to a network. By default, only administrators are allowed to connect remotely using WMI; restrict other users that are allowed to connect, or disallow all use

## Tactics

- [[Persistence|TA0003 - Persistence]]

## Related Procedures (1)

- [[Windows 10+ Binary Replacement via HID.dll]]

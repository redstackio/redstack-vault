---
id: 183aca88-8bec-4d8c-b508-800bf9fe33eb
name: Component Firmware
type: technique
mitre_id: T1109
mitre_url: null
created_at: '2019-08-28T21:17:45.736751+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
procedures:
- '[[Linux Privilege Escalation - Writable Files Escalation]]'
---

# Component Firmware

**MITRE ID**: T1109

## Description

Some adversaries may employ sophisticated means to compromise computer components and install malicious firmware that will execute adversary code outside of the operating system and main system firmware or BIOS. This technique may be similar to System Firmware but conducted upon other system components that may not have the same capability or level of integrity checking. Malicious device firmware could provide both a persistent level of access to systems despite potential typical failures to maintain access and hard disk re-images, as well as a way to evade host software-based defenses and integrity checks.

# Detection

Data and telemetry from use of device drivers (i.e. processes and API calls) and/or provided by SMART (Self-Monitoring, Analysis and Reporting Technology) [2] [3] disk monitoring may reveal malicious manipulations of components. Otherwise, this technique may be difficult to detect since malicious activity is taking place on system components possibly outside the purview of OS security and integrity mechanisms.

Disk check and forensic utilities [4] may reveal indicators of malicious firmware such as strings, unexpected disk partition table entries, or blocks of otherwise unusual memory that warrant deeper investigation. Also consider comparing components, including hashes of component firmware and behavior, against known good images.

# Mitigation

Prevent adversary access to privileged accounts or access necessary to perform this technique.

Consider removing and replacing system components suspected of being compromised.

# Footnotes

[1] Kaspersky Lab's Global Research and Analysis Team. (2015, February). Equation Group: Questions and Answers. Retrieved December 21, 2015.

[2] SanDisk. (n.d.). Self-Monitoring, Analysis and Reporting Technology (S.M.A.R.T.). Retrieved October 2, 2018.

[3] smartmontools. (n.d.). smartmontools. Retrieved October 2, 2018.

[4] Pinola, M. (2014, December 14). 3 tools to check your hard drive's health and make sure it's not already dying on you. Retrieved October 2, 2018.

## Defense

Prevent adversary access to privileged accounts or access necessary to perform this technique.

Consider removing and replacing system components suspected of being compromised.

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]

## Related Procedures (1)

- [[Linux Privilege Escalation - Writable Files Escalation]]

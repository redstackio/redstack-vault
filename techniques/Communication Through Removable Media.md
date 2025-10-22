---
id: 0286a3a7-ae05-4ca2-aa5e-b382abb0b6d3
name: Communication Through Removable Media
type: technique
mitre_id: T1092
mitre_url: null
created_at: '2019-08-28T21:17:35.304040+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
---

# Communication Through Removable Media

**MITRE ID**: T1092

## Description

Adversaries can perform command and control between compromised hosts on potentially disconnected networks using removable media to transfer commands from system to system. Both systems would need to be compromised, with the likelihood that an Internet-connected system was compromised first and the second through lateral movement by Replication Through Removable Media. Commands and files would be relayed from the disconnected system to the Internet-connected system to which the adversary has direct access.

# Detection

Monitor file access on removable media. Detect processes that execute when removable media is mounted.

# Mitigation

Disable Autorun if it is unnecessary. [5] Disallow or restrict removable media at an organizational policy level if they are not required for business operations. [6]

# Footnotes

[1] Anthe, C. et al. (2015, October 19). Microsoft Security Intelligence Report Volume 19. Retrieved December 23, 2015.

[2] FireEye. (2015). APT28: A WINDOW INTO RUSSIA’S CYBER ESPIONAGE OPERATIONS?. Retrieved August 19, 2015.

[3] ESET. (2016, October). En Route with Sednit - Part 2: Observing the Comings and Goings. Retrieved November 21, 2016.

[4] Calvet, J. (2014, November 11). Sednit Espionage Group Attacking Air-Gapped Networks. Retrieved January 4, 2017.

[5] Microsoft. (n.d.). How to disable the Autorun functionality in Windows. Retrieved April 20, 2016.

[6] Microsoft. (2007, August 31). https://technet.microsoft.com/en-us/library/cc771759(v=ws.10).aspx. Retrieved April 20, 2016.

## Defense

Disable Autorun if it is unnecessary. (Citation: Microsoft Disable Autorun) Disallow or restrict removable media at an organizational policy level if they are not required for business operations. (Citation: TechNet Removable Media Control)

## Tactics

- [[Command and Control|TA0011 - Command and Control]]

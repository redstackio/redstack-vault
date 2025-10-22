---
id: ef4d21de-aff7-4121-92d1-b8921fcd097c
name: Exfiltration Over Physical Medium
type: technique
mitre_id: T1052
mitre_url: null
created_at: '2019-08-28T21:17:31.500552+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
procedures:
- '[[PostgreSQL Time Based Table Dump]]'
---

# Exfiltration Over Physical Medium

**MITRE ID**: T1052

## Description

In certain circumstances, such as an air-gapped network compromise, exfiltration could occur via a physical medium or device introduced by a user. Such media could be an external hard drive, USB drive, cellular phone, MP3 player, or other removable storage and processing device. The physical medium or device could be used as the final exfiltration point or to hop between otherwise disconnected systems.

# Detection

Monitor file access on removable media. Detect processes that execute when removable media are mounted.

# Mitigation

Disable Autorun if it is unnecessary. [5] Disallow or restrict removable media at an organizational policy level if they are not required for business operations. [6]

# Footnotes

[1] Gostev, A.. (2014, March 12). Agent.btz: a Source of Inspiration?. Retrieved April 8, 2016.

[2] Kaspersky Lab's Global Research & Analysis Team. (2016, August 9). The ProjectSauron APT. Retrieved August 17, 2016.

[3] FireEye Labs. (2015, April). APT30 AND THE MECHANICS OF A LONG-RUNNING CYBER ESPIONAGE OPERATION. Retrieved May 1, 2015.

[4] Calvet, J. (2014, November 11). Sednit Espionage Group Attacking Air-Gapped Networks. Retrieved January 4, 2017.

[5] Microsoft. (n.d.). How to disable the Autorun functionality in Windows. Retrieved April 20, 2016.

[6] Microsoft. (2007, August 31). https://technet.microsoft.com/en-us/library/cc771759(v=ws.10).aspx. Retrieved April 20, 2016.

## Defense

Disable Autorun if it is unnecessary. (Citation: Microsoft Disable Autorun) Disallow or restrict removable media at an organizational policy level if they are not required for business operations. (Citation: TechNet Removable Media Control)

## Tactics

- [[Exfiltration|TA0010 - Exfiltration]]

## Related Procedures (1)

- [[PostgreSQL Time Based Table Dump]]

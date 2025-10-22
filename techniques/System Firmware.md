---
id: 72793eb6-4ba3-4c7f-97c4-6984aecc842b
name: System Firmware
type: technique
mitre_id: T1019
mitre_url: null
created_at: '2019-08-28T21:17:19.041917+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
---

# System Firmware

**MITRE ID**: T1019

## Description

The BIOS (Basic Input/Output System) and The Unified Extensible Firmware Interface (UEFI) or Extensible Firmware Interface (EFI) are examples of system firmware that operate as the software interface between the operating system and hardware of a computer. [1] [2] [3]System firmware like BIOS and (U)EFI underly the functionality of a computer and may be modified by an adversary to perform or assist in malicious activity. Capabilities exist to overwrite the system firmware, which may give sophisticated adversaries a means to install malicious firmware updates as a means of persistence on a system that may be difficult to detect.

# Detection

System firmware manipulation may be detected. [7] Dump and inspect BIOS images on vulnerable systems and compare against known good images. [8] Analyze differences to determine if malicious changes have occurred. Log attempts to read/write to BIOS and compare against known patching behavior.

Likewise, EFI modules can be collected and compared against a known-clean list of EFI executable binaries to detect potentially malicious modules. The CHIPSEC framework can be used for analysis to determine if firmware modifications have been performed. [9] [10] [11]

# Mitigation

Prevent adversary access to privileged accounts or access necessary to perform this technique. Check the integrity of the existing BIOS or EFI to determine if it is vulnerable to modification. Patch the BIOS and EFI as necessary. Use Trusted Platform Module technology. [6]

# Footnotes

[1] Wikipedia. (n.d.). BIOS. Retrieved January 5, 2016.

[2] Wikipedia. (2017, July 10). Unified Extensible Firmware Interface. Retrieved July 11, 2017.

[3] UEFI Forum. (n.d.). About UEFI Forum. Retrieved January 5, 2016.

[4] Lin, P. (2015, July 13). Hacking Team Uses UEFI BIOS Rootkit to Keep RCS 9 Agent in Target Systems. Retrieved December 11, 2015.

[5] Ge, L. (2011, September 9). BIOS Threat is Showing up Again!. Retrieved November 14, 2014.

[6] Trusted Computing Group. (2008, April 29). Trusted Platform Module (TPM) Summary. Retrieved June 8, 2016.

[7] Upham, K. (2014, March). Going Deep into the BIOS with MITRE Firmware Security Research. Retrieved January 5, 2016.

[8] Butterworth, J. (2013, July 30). Copernicus: Question Your Assumptions about BIOS Security. Retrieved December 11, 2015.

[9] Beek, C., Samani, R. (2017, March 8). CHIPSEC Support Against Vault 7 Disclosure Scanning. Retrieved March 13, 2017.

[10] Intel. (2017, March 18). CHIPSEC Platform Security Assessment Framework. Retrieved March 20, 2017.

[11] Intel Security. (2005, July 16). HackingTeam's UEFI Rootkit Details. Retrieved March 20, 2017.

## Defense

Prevent adversary access to privileged accounts or access necessary to perform this technique. Check the integrity of the existing BIOS or EFI to determine if it is vulnerable to modification. Patch the BIOS and EFI as necessary. Use Trusted Platform Modu

## Tactics

- [[Persistence|TA0003 - Persistence]]

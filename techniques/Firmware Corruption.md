---
id: e7d9433f-98f5-47e7-9b68-b9198e0e2400
name: Firmware Corruption
type: technique
mitre_id: T1495
mitre_url: null
created_at: '2019-08-28T21:17:31.836724+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Impact|TA0040 - Impact]]'
---

# Firmware Corruption

**MITRE ID**: T1495

## Description

Adversaries may overwrite or corrupt the flash memory contents of system BIOS or other firmware in devices attached to a system in order to render them inoperable or unable to boot.[1] Firmware is software that is loaded and executed from non-volatile memory on hardware devices in order to initialize and manage device functionality. These devices could include the motherboard, hard drive, or video cards.

# Detection

System firmware manipulation may be detected.[2] Log attempts to read/write to BIOS and compare against known patching behavior.

# Mitigation

Prevent adversary access to privileged accounts or access necessary to perform this technique. Check the integrity of the existing BIOS and device firmware to determine if it is vulnerable to modification. Patch the BIOS and other firmware as necessary to prevent successful use of known vulnerabilities. 

# Footnotes

[1] Yamamura, M. (2002, April 25). W95.CIH. Retrieved April 12, 2019.

[2] Upham, K. (2014, March). Going Deep into the BIOS with MITRE Firmware Security Research. Retrieved January 5, 2016.

## Defense

Prevent adversary access to privileged accounts or access necessary to perform this technique. Check the integrity of the existing BIOS and device firmware to determine if it is vulnerable to modification. Patch the BIOS and other firmware as necessary to

## Tactics

- [[Impact|TA0040 - Impact]]

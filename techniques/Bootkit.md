---
id: 70586765-27aa-4d04-929e-4186debb2667
name: Bootkit
type: technique
mitre_id: T1067
mitre_url: null
created_at: '2019-08-28T21:17:40.594129+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
procedures:
- '[[Bypassing Quotes in Script Tag for XSS Injection]]'
- '[[Filter Bypass with Incomplete HTML Tag for XSS Attacks]]'
---

# Bootkit

**MITRE ID**: T1067

## Description

A bootkit is a malware variant that modifies the boot sectors of a hard drive, including the Master Boot Record (MBR) and Volume Boot Record (VBR). [1]Adversaries may use bootkits to persist on systems at a layer below the operating system, which may make it difficult to perform full remediation unless an organization suspects one was used and can act accordingly.Master Boot RecordThe MBR is the section of disk that is first loaded after completing hardware initialization by the BIOS. It is the location of the boot loader. An adversary who has raw access to the boot drive may overwrite this area, diverting execution during startup from the normal boot loader to adversary code. [2]Volume Boot RecordThe MBR passes control of the boot process to the VBR. Similar to the case of MBR, an adversary who has raw access to the boot drive may overwrite the VBR to divert execution during startup to adversary code.

# Detection

Perform integrity checking on MBR and VBR. Take snapshots of MBR and VBR and compare against known good samples. Report changes to MBR and VBR as they occur for indicators of suspicious activity and further analysis.

# Mitigation

Ensure proper permissions are in place to help prevent adversary access to privileged accounts necessary to perform this action. Use Trusted Platform Module technology and a secure or trusted boot process to prevent system integrity from being compromised. [9] [10]

# Footnotes

[1] Mandiant. (2016, February). M-Trends 2016. Retrieved January 4, 2017.

[2] Lau, H. (2011, August 8). Are MBR Infections Back in Fashion? (Infographic). Retrieved November 13, 2014.

[3] ESET. (2016, October). En Route with Sednit - Part 3: A Mysterious Downloader. Retrieved November 21, 2016.

[4] FinFisher. (n.d.). Retrieved December 20, 2017.

[5] Allievi, A.,Flori, E. (2018, March 01). FinFisher exposed: A researcher’s tale of defeating traps, tricks, and complex virtual machines. Retrieved July 9, 2018.

[6] Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Unraveling the Long Thread of the Sony Attack. Retrieved February 25, 2016.

[7] Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Destructive Malware Report. Retrieved March 2, 2016.

[8] Andonov, D., et al. (2015, December 7). Thriving Beyond The Operating System: Financial Threat Group Targets Volume Boot Record. Retrieved May 13, 2016.

[9] Trusted Computing Group. (2008, April 29). Trusted Platform Module (TPM) Summary. Retrieved June 8, 2016.

[10] Microsoft. (n.d.). Secure the Windows 8.1 boot process. Retrieved June 11, 2016.

## Defense

Ensure proper permissions are in place to help prevent adversary access to privileged accounts necessary to perform this action. Use Trusted Platform Module technology and a secure or trusted boot process to prevent system integrity from being compromised

## Tactics

- [[Persistence|TA0003 - Persistence]]

## Related Procedures (2)

- [[Bypassing Quotes in Script Tag for XSS Injection]]
- [[Filter Bypass with Incomplete HTML Tag for XSS Attacks]]

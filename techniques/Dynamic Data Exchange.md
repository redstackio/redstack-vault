---
id: 9dc9bc51-cd67-459f-9478-bdfd1f2dd07d
name: Dynamic Data Exchange
type: technique
mitre_id: T1173
mitre_url: null
created_at: '2019-08-28T21:17:27.486068+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
procedures:
- '[[XLM Excel 4.0 GruntHttp Payload Generation]]'
---

# Dynamic Data Exchange

**MITRE ID**: T1173

## Description

Windows Dynamic Data Exchange (DDE) is a client-server protocol for one-time and/or continuous inter-process communication (IPC) between applications. Once a link is established, applications can autonomously exchange transactions consisting of strings, warm data links (notifications when a data item changes), hot data links (duplications of changes to a data item), and requests for command execution.Object Linking and Embedding (OLE), or the ability to link data between documents, was originally implemented through DDE. Despite being superseded by COM, DDE may be enabled in Windows 10 and most of Microsoft Office 2016 via Registry keys. [1] [2] [3]Adversaries may use DDE to execute arbitrary commands. Microsoft Office documents can be poisoned with DDE commands [4] [5], directly or through embedded files [6], and used to deliver execution via phishing campaigns or hosted Web content, avoiding the use of Visual Basic for Applications (VBA) macros. [7] DDE could also be leveraged by an adversary operating on a compromised machine who does not have direct access to command line execution.

# Detection

OLE and Office Open XML files can be scanned for ‘DDEAUTO', ‘DDE’, and other strings indicative of DDE execution. [22]

Monitor for Microsoft Office applications loading DLLs and other modules not typically associated with the application.

Monitor for spawning of unusual processes (such as cmd.exe) from Microsoft Office applications.

# Mitigation

Registry keys specific to Microsoft Office feature control security can be set to disable automatic DDE/OLE execution. [3] [1] [19] Microsoft also created, and enabled by default, Registry keys to completely disable DDE execution in Word and Excel. [2]

Ensure Protected View is enabled [20] and consider disabling embedded files in Office programs, such as OneNote, not enrolled in Protected View. [6] [19]

On Windows 10, enable Attack Surface Reduction (ASR) rules to prevent DDE attacks and spawning of child processes from Office programs. [21] [6]

# Footnotes

[1] Cimpanu, C. (2017, December 15). Microsoft Disables DDE Feature in Word to Prevent Further Malware Attacks. Retrieved December 19, 2017.

[2] Microsoft. (2017, December 12). ADV170021 - Microsoft Office Defense in Depth Update. Retrieved February 3, 2018.

[3] Microsoft. (2017, November 8). Microsoft Security Advisory 4053440 - Securely opening Microsoft Office documents that contain Dynamic Data Exchange (DDE) fields. Retrieved November 21, 2017.

[4] El-Sherei, S. (2016, May 20). PowerShell, C-Sharp and DDE The Power Within. Retrieved November 22, 2017.

[5] Kettle, J. (2014, August 29). Comma Separated Vulnerabilities. Retrieved November 22, 2017.

[6] Nelson, M. (2018, January 29). Reviving DDE: Using OneNote and Excel for Code Execution. Retrieved February 3, 2018.

[7] Stalmans, E., El-Sherei, S. (2017, October 9). Macro-less Code Exec in MSWord. Retrieved November 21, 2017.

[8] Sherstobitoff, R., Rea, M. (2017, November 7). Threat Group APT28 Slips Office Malware into Doc Citing NYC Terror Attack. Retrieved November 21, 2017.

[9] Paganini, P. (2017, November 9). Russia-Linked APT28 group observed using DDE attack to deliver malware. Retrieved November 21, 2017.

[10] Lee, B., Falcone, R. (2018, June 06). Sofacy Group’s Parallel Attacks. Retrieved June 18, 2018.

[11] Raiu, C., and Ivanov, A. (2016, June 17). Operation Daybreak. Retrieved February 15, 2018.

[12] Svajcer, V. (2018, July 31). Multiple Cobalt Personality Disorder. Retrieved September 5, 2018.

[13] Waterman, S. (2017, October 16). Fin7 weaponization of DDE is just their latest slick move, say researchers. Retrieved November 21, 2017.

[14] Symantec Security Response. (2018, October 10). Gallmaker: New Attack Group Eschews Malware to Live off the Land. Retrieved November 27, 2018.

[15] Mercer, W., Rascagneres, P. (2018, April 26). GravityRAT - The Two-Year Evolution Of An APT Targeting India. Retrieved May 16, 2018.

[16] Kaspersky Lab's Global Research & Analysis Team. (2018, October 10). MuddyWater expands operations. Retrieved November 2, 2018.

[17] Lunghi, D., et al. (2017, December). Untangling the Patchwork Cyberespionage Group. Retrieved July 10, 2018.

[18] Singh, S. et al.. (2018, March 13). Iranian Threat Group Updates Tactics, Techniques and Procedures in Spear Phishing Campaign. Retrieved April 11, 2018.

[19] Dormann, W. (2017, October 20). Disable DDEAUTO for Outlook, Word, OneNote, and Excel versions 2010, 2013, 2016. Retrieved February 3, 2018.

[20] Microsoft. (n.d.). What is Protected View?. Retrieved November 22, 2017.

[21] Brower, N. & D'Souza-Wiltshire, I. (2017, November 9). Enable Attack surface reduction. Retrieved February 3, 2018.

[22] NVISO Labs. (2017, October 11). Detecting DDE in MS Office documents. Retrieved November 21, 2017.

## Defense

Registry keys specific to Microsoft Office feature control security can be set to disable automatic DDE/OLE execution. (Citation: Microsoft DDE Advisory Nov 2017) (Citation: BleepingComputer DDE Disabled in Word Dec 2017) (Citation: GitHub Disable DDEAUTO

## Tactics

- [[Execution|TA0002 - Execution]]

## Related Procedures (1)

- [[XLM Excel 4.0 GruntHttp Payload Generation]]

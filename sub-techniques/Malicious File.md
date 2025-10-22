---
id: 64f0d650-4aed-47e4-a9b6-82d0bd619722
name: Malicious File
type: sub-technique
mitre_id: T1204.002
mitre_url: null
created_at: '2023-04-06T00:31:25.736532+00:00'
updated_at: '2023-04-06T00:31:25.736532+00:00'
parent_technique: '[[User Execution|T1204 - User Execution]]'
tactics:
- '[[Execution|TA0002 - Execution]]'
procedures:
- '[[Certutil Download and Execute]]'
- '[[LFI to RCE via uploaded file]]'
- '[[VBA Shell Execute Comment]]'
- '[[Windows - Cscript / Wscript JScript Payload Execution]]'
- '[[Windows Defender Application Control Enforcement Mode]]'
---

# Malicious File

**MITRE ID**: T1204.002

**Parent Technique**: [[User Execution|T1204 - User Execution]]

This is a sub-technique of T1204 - User Execution.

## Summary

An adversary may rely upon a user opening a malicious file in order to gain execution. Users may be subjected to social engineering to get them to open a file that will lead to code execution. This user action will typically be observed as follow-on behavior from [Spearphishing Attachment](https://a

## Description

An adversary may rely upon a user opening a malicious file in order to gain execution. Users may be subjected to social engineering to get them to open a file that will lead to code execution. This user action will typically be observed as follow-on behavior from [Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001). Adversaries may use several types of files that require a user to execute them, including .doc, .pdf, .xls, .rtf, .scr, .exe, .lnk, .pif, and .cpl.

Adversaries may employ various forms of [Masquerading](https://attack.mitre.org/techniques/T1036) and [Obfuscated Files or Information](https://attack.mitre.org/techniques/T1027) to increase the likelihood that a user will open and successfully execute a malicious file. These methods may include using a familiar naming convention and/or password protecting the file and supplying instructions to a user on how to open it.(Citation: Password Protected Word Docs) 

While [Malicious File](https://attack.mitre.org/techniques/T1204/002) frequently occurs shortly after Initial Access it may occur at other phases of an intrusion, such as when an adversary places a file in a shared directory or on a user's desktop hoping that a user will click on it. This activity may also be seen shortly after [Internal Spearphishing](https://attack.mitre.org/techniques/T1534).

## Tactics

This sub-technique is used in the following tactics:

- [[Execution|TA0002 - Execution]]

## Related Procedures

There are 5 procedures using this sub-technique:

- [[Certutil Download and Execute]]
- [[LFI to RCE via uploaded file]]
- [[VBA Shell Execute Comment]]
- [[Windows - Cscript / Wscript JScript Payload Execution]]
- [[Windows Defender Application Control Enforcement Mode]]

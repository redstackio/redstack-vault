---
id: ce8276a5-9c6e-47e6-b581-1c4b5d74579f
name: Execution through Module Load
type: technique
mitre_id: T1129
mitre_url: null
created_at: '2019-08-28T21:17:47.567611+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
---

# Execution through Module Load

**MITRE ID**: T1129

## Description

The Windows module loader can be instructed to load DLLs from arbitrary local paths and arbitrary Universal Naming Convention (UNC) network paths. This functionality resides in NTDLL.dll and is part of the Windows Native API which is called from functions like CreateProcess(), LoadLibrary(), etc. of the Win32 API. [1]The module loader can load DLLs:via specification of the (fully-qualified or relative) DLL pathname in the IMPORT directory;via EXPORT forwarded to another DLL, specified with (fully-qualified or relative) pathname (but without extension);via an NTFS junction or symlink program.exe.local with the fully-qualified or relative pathname of a directory containing the DLLs specified in the IMPORT directory or forwarded EXPORTs;via <file name="filename.extension" loadFrom="fully-qualified or relative pathname"> in an embedded or external "application manifest". The file name refers to an entry in the IMPORT directory or a forwarded EXPORT.Adversaries can use this functionality as a way to execute arbitrary code on a system.

# Detection

Monitoring DLL module loads may generate a significant amount of data and may not be directly useful for defense unless collected under specific circumstances, since benign use of Windows modules load functions are common and may be difficult to distinguish from malicious behavior. Legitimate software will likely only need to load routine, bundled DLL modules or Windows system DLLs such that deviation from known module loads may be suspicious. Limiting DLL module loads to %SystemRoot% and %ProgramFiles% directories will protect against module loads from unsafe paths. 

Correlation of other events with behavior surrounding module loads using API monitoring and suspicious DLLs written to disk will provide additional context to an event that may assist in determining if it is due to malicious behavior.

# Mitigation

Directly mitigating module loads and API calls related to module loads will likely have unintended side effects, such as preventing legitimate software from operating properly. Efforts should be focused on preventing adversary tools from running earlier in the chain of activity and on identifying and correlated subsequent behavior to determine if it is the result of malicious activity.

# Footnotes

[1] Wikipedia. (2017, January 31). Microsoft Windows library files. Retrieved February 13, 2017.

[2] Salem, E. (2019, February 13). ASTAROTH MALWARE USES LEGITIMATE OS AND ANTIVIRUS PROCESSES TO STEAL PASSWORDS AND PERSONAL DATA. Retrieved April 17, 2019.

[3] Symantec Security Response. (2010, January 18). The Trojan.Hydraq Incident. Retrieved February 20, 2018.

[4] Lelli, A. (2010, January 11). Trojan.Hydraq. Retrieved February 20, 2018.

[5] Elovitz, S. & Ahl, I. (2016, August 18). Know Your Enemy:  New Financially-Motivated & Spear-Phishing Group. Retrieved February 26, 2018.

## Defense

Directly mitigating module loads and API calls related to module loads will likely have unintended side effects, such as preventing legitimate software from operating properly. Efforts should be focused on preventing adversary tools from running earlier i

## Tactics

- [[Execution|TA0002 - Execution]]

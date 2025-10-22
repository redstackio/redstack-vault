---
id: 73113786-d698-4594-9d80-2b993b270b7c
name: Process Doppelgänging
type: technique
mitre_id: T1186
mitre_url: null
created_at: '2019-08-28T21:17:43.330598+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Process Doppelgänging

**MITRE ID**: T1186

## Description

Windows Transactional NTFS (TxF) was introduced in Vista as a method to perform safe file operations. [1] To ensure data integrity, TxF enables only one transacted handle to write to a file at a given time. Until the write handle transaction is terminated, all other handles are isolated from the writer and may only read the committed version of the file that existed at the time the handle was opened. [2] To avoid corruption, TxF performs an automatic rollback if the system or application fails during a write transaction. [3]Although deprecated, the TxF application programming interface (API) is still enabled as of Windows 10. [4]Adversaries may leverage TxF to a perform a file-less variation of Process Injection called Process Doppelgänging. Similar to Process Hollowing, Process Doppelgänging involves replacing the memory of a legitimate process, enabling the veiled execution of malicious code that may evade defenses and detection. Process Doppelgänging's use of TxF also avoids the use of highly-monitored API functions such as NtUnmapViewOfSection, VirtualProtectEx, and SetThreadContext. [4]Process Doppelgänging is implemented in 4 steps [4]:Transact – Create a TxF transaction using a legitimate executable then overwrite the file with malicious code. These changes will be isolated and only visible within the context of the transaction.Load – Create a shared section of memory and load the malicious executable.Rollback – Undo changes to original executable, effectively removing malicious code from the file system.Animate – Create a process from the tainted section of memory and initiate execution.

# Detection

Monitor and analyze calls to CreateTranscation, CreateFileTransacted, RollbackTransaction, and other rarely used functions indicative of TxF activity. Process Doppelgänging also invokes an outdated and undocumented implementation of the Windows process loader via calls to NtCreateProcessEx and NtCreateThreadEx as well as API calls used to modify memory within another process, such as WriteProcessMemory. [4] [12]

Scan file objects reported during the PsSetCreateProcessNotifyRoutine, [13] which triggers a callback whenever a process is created or deleted, specifically looking for file objects with enabled write access. [4] Also consider comparing file objects loaded in memory to the corresponding file on disk. [12]

Analyze process behavior to determine if a process is performing actions it usually does not, such as opening network connections, reading files, or other suspicious actions that could relate to post-compromise behavior.

# Mitigation

This type of attack technique cannot be easily mitigated with preventive controls or patched since it is based on the abuse of operating system design features. For example, mitigating specific API calls will likely have unintended side effects, such as preventing legitimate process-loading mechanisms from operating properly. Efforts should be focused on preventing adversary tools from running earlier in the chain of activity and on identifying subsequent malicious behavior.

Although Process Doppelgänging may be used to evade certain types of defenses, it is still good practice to identify potentially malicious software that may be used to perform adversarial actions and audit and/or block it by using whitelisting [7] tools, like AppLocker, [8] [9] or Software Restriction Policies [10] where appropriate. [11]

# Footnotes

[1] Microsoft. (n.d.). Transactional NTFS (TxF). Retrieved December 20, 2017.

[2] Microsoft. (n.d.). Basic TxF Concepts. Retrieved December 20, 2017.

[3] Microsoft. (n.d.). When to Use Transactional NTFS. Retrieved December 20, 2017.

[4] Liberman, T. & Kogan, E. (2017, December 7). Lost in Transaction: Process Doppelgänging. Retrieved December 20, 2017.

[5] Ivanov, A. et al.. (2018, May 7). SynAck targeted ransomware uses the Doppelgänging technique. Retrieved May 22, 2018.

[6] Bettencourt, J. (2018, May 7). Kaspersky Lab finds new variant of SynAck ransomware using sophisticated Doppelgänging technique. Retrieved May 24, 2018.

[7] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[8] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[9] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[10] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[11] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

[12] hasherezade. (2017, December 18). Process Doppelgänging – a new way to impersonate a process. Retrieved December 20, 2017.

[13] Microsoft. (n.d.). PsSetCreateProcessNotifyRoutine routine. Retrieved December 20, 2017.

## Defense

This type of attack technique cannot be easily mitigated with preventive controls or patched since it is based on the abuse of operating system design features. For example, mitigating specific API calls will likely have unintended side effects, such as p

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

---
id: 3137bcd6-ed85-45dc-ad7a-667e701e5c80
name: Hooking
type: technique
mitre_id: T1179
mitre_url: null
created_at: '2019-08-28T21:17:18.661102+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
procedures:
- '[[Patching AmsiScanBuffer to Bypass AMSI Scanning]]'
---

# Hooking

**MITRE ID**: T1179

## Description

Windows processes often leverage application programming interface (API) functions to perform tasks that require reusable system resources. Windows API functions are typically stored in dynamic-link libraries (DLLs) as exported functions. Hooking involves redirecting calls to these functions and can be implemented via:Hooks procedures, which intercept and execute designated code in response to events such as messages, keystrokes, and mouse inputs. [1] [2]Import address table (IAT) hooking, which use modifications to a process’s IAT, where pointers to imported API functions are stored. [2] [3] [4]Inline hooking, which overwrites the first bytes in an API function to redirect code flow. [2] [5] [4]Similar to Process Injection, adversaries may use hooking to load and execute malicious code within the context of another process, masking the execution while also allowing access to the process's memory and possibly elevated privileges. Installing hooking mechanisms may also provide Persistence via continuous invocation when the functions are called through normal use.Malicious hooking mechanisms may also capture API calls that include parameters that reveal user authentication credentials for Credential Access. [6]Hooking is commonly utilized by Rootkits to conceal files, processes, Registry keys, and other objects in order to hide malware and associated behaviors. [7]

# Detection

Monitor for calls to the SetWindowsHookEx and SetWinEventHook functions, which install a hook procedure. [1] [14] Also consider analyzing hook chains (which hold pointers to hook procedures for each type of hook) using tools  [14] [15] [16] or by programmatically examining internal kernel structures. [17] [18]

Rootkits detectors  [19] can also be used to monitor for various flavors of hooking activity.

Verify integrity of live processes by comparing code in memory to that of corresponding static binaries, specifically checking for jumps and other instructions that redirect code flow. Also consider taking snapshots of newly started processes  [20] to compare the in-memory IAT to the real addresses of the referenced functions. [21] [3]

Analyze process behavior to determine if a process is performing actions it usually does not, such as opening network connections, reading files, or other suspicious actions that could relate to post-compromise behavior.

# Mitigation

This type of attack technique cannot be easily mitigated with preventive controls since it is based on the abuse of operating system design features. For example, mitigating all hooking will likely have unintended side effects, such as preventing legitimate software (i.e., security products) from operating properly. Efforts should be focused on preventing adversary tools from running earlier in the chain of activity and on identifying subsequent malicious behavior.

# Footnotes

[1] Microsoft. (n.d.). Hooks Overview. Retrieved December 12, 2017.

[2] Hosseini, A. (2017, July 18). Ten Process Injection Techniques: A Technical Survey Of Common And Trending Process Injection Techniques. Retrieved December 7, 2017.

[3] Tigzy. (2014, October 15). Userland Rootkits: Part 1, IAT hooks. Retrieved December 12, 2017.

[4] Hillman, M. (2015, August 8). Dynamic Hooking Techniques: User Mode. Retrieved December 20, 2017.

[5] Mariani, B. (2011, September 6). Inline Hooking in Windows. Retrieved December 12, 2017.

[6] Microsoft. (2017, September 15). TrojanSpy:Win32/Ursnif.gen!I. Retrieved December 18, 2017.

[7] Symantec. (n.d.). Windows Rootkit Overview. Retrieved December 21, 2017.

[8] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[9] FinFisher. (n.d.). Retrieved December 20, 2017.

[10] Grunzweig, J., Lee, B. (2018, September 27). New KONNI Malware attacking Eurasia and Southeast Asia. Retrieved November 5, 2018.

[11] Llimos, N., Pascual, C.. (2019, February 12). Trickbot Adds Remote Application Credential-Grabbing Capabilities to Its Repertoire. Retrieved March 12, 2019.

[12] Kaspersky Lab's Global Research & Analysis Team. (2018, February 20). A Slice of 2017 Sofacy Activity. Retrieved November 27, 2018.

[13] Ebach, L. (2017, June 22). Analysis Results of Zeus.Variant.Panda. Retrieved November 5, 2018.

[14] Volatility Labs. (2012, September 24). MoVP 3.1 Detecting Malware Hooks in the Windows GUI Subsystem. Retrieved December 12, 2017.

[15] Prekas, G. (2011, July 11). Winhook. Retrieved December 12, 2017.

[16] Satiro, J. (2011, September 14). GetHooks. Retrieved December 12, 2017.

[17] Felici, M. (2006, December 6). Any application-defined hook procedure on my machine?. Retrieved December 12, 2017.

[18] Eye of Ra. (2017, June 27). Windows Keylogger Part 2: Defense against user-land. Retrieved December 12, 2017.

[19] GMER. (n.d.). GMER. Retrieved December 12, 2017.

[20] Microsoft. (n.d.). Taking a Snapshot and Viewing Processes. Retrieved December 12, 2017.

[21] Stack Exchange - Security. (2012, July 31). What are the methods to find hooked functions and APIs?. Retrieved December 12, 2017.

## Defense

This type of attack technique cannot be easily mitigated with preventive controls since it is based on the abuse of operating system design features. For example, mitigating all hooking will likely have unintended side effects, such as preventing legitima

## Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

## Related Procedures (1)

- [[Patching AmsiScanBuffer to Bypass AMSI Scanning]]

---
id: c00879f8-f4cf-42cb-a8c3-36202c8140a9
name: File Permissions Modification
type: technique
mitre_id: T1222
mitre_url: null
created_at: '2019-08-28T21:17:22.160970+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
procedures:
- '[[Application Escape and Breakout via Context Menus and File Search Command]]'
- '[[AWS CLI Profile Configuration for Persistence and Backdooring]]'
- '[[Image-Based .htaccess Upload]]'
- '[[PostgreSQL File Read Procedure]]'
- '[[PostgreSQL File Write with Reverse Shell Payload]]'
- '[[Preventing Cross Site Scripting (XSS) in XML and files]]'
- '[[Server Side Template Injection - Groovy File Manipulation]]'
- '[[Windows - Default Writeable Folders Privilege Escalation]]'
- '[[Windows - Password Looting via Alternate Data Stream]]'
- '[[Windows - Privileged File Write via UsoDLLLoader]]'
---

# File Permissions Modification

**MITRE ID**: T1222

## Description

File permissions are commonly managed by discretionary access control lists (DACLs) specified by the file owner. File DACL implementation may vary by platform, but generally explicitly designate which users/groups can perform which actions (ex: read, write, execute, etc.). [1] [2] [3]Adversaries may modify file permissions/attributes to evade intended DACLs. [4] [5] Modifications may include changing specific access rights, which may require taking ownership of a file and/or elevated permissions such as Administrator/root depending on the file's existing permissions to enable malicious activity such as modifying, replacing, or deleting specific files. Specific file modifications may be a required step for many techniques, such as establishing Persistence via Accessibility Features, Logon Scripts, or tainting/hijacking other instrumental binary/configuration files.

# Detection

Monitor and investigate attempts to modify DACLs and file ownership, such as use of icacls [9], takeown [10], attrib [11], and PowerShell Set-Acl [12] in Windows and chmod [13]/chown [14] in macOS/Linux. Many of these are built-in system utilities and may generate high false positive alerts, so compare against baseline knowledge for how systems are typically used and correlate modification events with other indications of malicious activity where possible.

Consider enabling file permission change auditing on folders containing key binary/configuration files. Windows Security Log events (Event ID 4670) are used when DACLs are modified. [15]

# Mitigation

This type of technique cannot be easily mitigated with preventive controls since it is based on the abuse of operating system design features. Efforts should be focused on preventing adversary tools from running earlier in the chain of activity and on identification of subsequent malicious behavior.

# Footnotes

[1] Microsoft. (2018, May 30). DACLs and ACEs. Retrieved August 19, 2018.

[2] Microsoft. (2018, May 30). File Security and Access Rights. Retrieved August 19, 2018.

[3] Tutorials Point. (n.d.). Unix / Linux - File Permission / Access Modes. Retrieved August 19, 2018.

[4] Hybrid Analysis. (2018, June 12). c9b65b764985dfd7a11d3faf599c56b8.exe. Retrieved August 19, 2018.

[5] Hybrid Analysis. (2018, May 30). 2a8efbfadd798f6111340f7c1c956bee.dll. Retrieved August 19, 2018.

[6] Dumont, R.. (2019, April 9). OceanLotus: macOS malware update. Retrieved April 15, 2019.

[7] Windows Defender Advanced Threat Hunting Team. (2016, April 29). PLATINUM: Targeted attacks in South and Southeast Asia. Retrieved February 15, 2018.

[8] Noerenberg, E., Costis, A., and Quist, N. (2017, May 16). A Technical Analysis of WannaCry Ransomware. Retrieved March 25, 2019.

[9] Plett, C. et al.. (2017, October 17). icacls. Retrieved August 19, 2018.

[10] Plett, C. et al.. (2017, October 15). takeown. Retrieved August 19, 2018.

[11] Plett, C. et al.. (2017, October 15). attrib. Retrieved August 19, 2018.

[12] Microsoft. (n.d.). Set-Acl. Retrieved August 19, 2018.

[13] MacKenzie, D. & Meyering, J. (n.d.). chmod(1) - Linux man page. Retrieved August 19, 2018.

[14] MacKenzie, D. & Meyering, J. (n.d.). chown(1) - Linux man page. Retrieved August 19, 2018.

[15] Netsurion. (2014, February 19). Monitoring File Permission Changes with the Windows Security Log. Retrieved August 19, 2018.

## Defense

This type of technique cannot be easily mitigated with preventive controls since it is based on the abuse of operating system design features. Efforts should be focused on preventing adversary tools from running earlier in the chain of activity and on ide

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

## Related Procedures (10)

- [[Application Escape and Breakout via Context Menus and File Search Command]]
- [[AWS CLI Profile Configuration for Persistence and Backdooring]]
- [[Image-Based .htaccess Upload]]
- [[PostgreSQL File Read Procedure]]
- [[PostgreSQL File Write with Reverse Shell Payload]]
- [[Preventing Cross Site Scripting (XSS) in XML and files]]
- [[Server Side Template Injection - Groovy File Manipulation]]
- [[Windows - Default Writeable Folders Privilege Escalation]]
- [[Windows - Password Looting via Alternate Data Stream]]
- [[Windows - Privileged File Write via UsoDLLLoader]]

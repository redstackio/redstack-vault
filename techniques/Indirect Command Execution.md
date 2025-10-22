---
id: 03c69665-4f22-44ab-8e4d-c4d642c9a043
name: Indirect Command Execution
type: technique
mitre_id: T1202
mitre_url: null
created_at: '2019-08-28T21:17:39.628200+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
procedures:
- '[[Akamai WAF Bypass via Prompt User Input]]'
- '[[Alternative Name Certificate Request]]'
- '[[Forest to Forest Compromise - Trust Ticket TGS Retrieval and LDAP Authentication]]'
- '[[Unicode Character Injection for XSS Filter Bypass]]'
- '[[Windows - EoP with Living Off The Land Binaries and Scripts]]'
---

# Indirect Command Execution

**MITRE ID**: T1202

## Description

Various Windows utilities may be used to execute commands, possibly without invoking cmd. For example, Forfiles, the Program Compatibility Assistant (pcalua.exe), components of the Windows Subsystem for Linux (WSL), as well as other utilities may invoke the execution of programs and commands from a Command-Line Interface, Run window, or via scripts. [1] [2]Adversaries may abuse these features for Defense Evasion, specifically to perform arbitrary execution while subverting detections and/or mitigation controls (such as Group Policy) that limit/prevent the usage of cmd or file extensions more commonly associated with malicious payloads.

# Detection

Monitor and analyze logs from host-based detection mechanisms, such as Sysmon, for events such as process creations that include or are resulting from parameters associated with invoking programs/commands/files and/or spawning child processes/network connections. [9]

# Mitigation

Identify or block potentially malicious software that may contain abusive functionality by using whitelisting [3] tools, like AppLocker, [4] [5] or Software Restriction Policies [6] where appropriate. [7]. These mechanisms can also be used to disable and/or limit user access to Windows utilities and file types/locations used to invoke malicious execution.[8]

# Footnotes

[1] vector_sec. (2017, August 11). Defenders watching launches of cmd? What about forfiles?. Retrieved January 22, 2018.

[2] Evi1cg. (2017, November 26). block cmd.exe ? try this :. Retrieved January 22, 2018.

[3] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[4] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[5] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[6] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[7] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

[8] Nelson, M. (2018, June 11). The Tale of SettingContent-ms Files. Retrieved April 18, 2019.

[9] Partington, E. (2017, August 14). Are you looking out for forfiles.exe (if you are watching for cmd.exe). Retrieved January 22, 2018.

## Defense

Identify or block potentially malicious software that may contain abusive functionality by using whitelisting (Citation: Beechey 2010) tools, like AppLocker, (Citation: Windows Commands JPCERT) (Citation: NSA MS AppLocker) or Software Restriction Policies

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

## Related Procedures (5)

- [[Akamai WAF Bypass via Prompt User Input]]
- [[Alternative Name Certificate Request]]
- [[Forest to Forest Compromise - Trust Ticket TGS Retrieval and LDAP Authentication]]
- [[Unicode Character Injection for XSS Filter Bypass]]
- [[Windows - EoP with Living Off The Land Binaries and Scripts]]

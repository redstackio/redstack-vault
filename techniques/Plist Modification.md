---
id: 80223095-02d3-49da-b3e7-faaa59a6270e
name: Plist Modification
type: technique
mitre_id: T1150
mitre_url: null
created_at: '2019-08-28T21:17:29.741896+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
---

# Plist Modification

**MITRE ID**: T1150

## Description

Property list (plist) files contain all of the information that macOS and OS X uses to configure applications and services. These files are UTF-8 encoded and formatted like XML documents via a series of keys surrounded by < >. They detail when programs should execute, file paths to the executables, program arguments, required OS permissions, and many others. plists are located in certain locations depending on their purpose such as /Library/Preferences (which execute with elevated privileges) and ~/Library/Preferences (which execute with a user's privileges). Adversaries can modify these plist files to point to their own code, can use them to execute their code in the context of another user, bypass whitelisting procedures, or even use them as a persistence mechanism. [1]

# Detection

File system monitoring can determine if plist files are being modified. Users should not have permission to modify these in most cases. Some software tools like "Knock Knock" can detect persistence mechanisms and point to the specific files that are being referenced. This can be helpful to see what is actually being executed.

Monitor process execution for abnormal process execution resulting from modified plist files. Monitor utilities used to modify plist files or that take a plist file as an argument, which may indicate suspicious activity.

# Mitigation

Prevent plist files from being modified by users by making them read-only.

# Footnotes

[1] Dani Creus, Tyler Halfpop, Robert Falcone. (2016, September 26). Sofacy's 'Komplex' OS X Trojan. Retrieved July 8, 2017.

## Defense

Prevent plist files from being modified by users by making them read-only.

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

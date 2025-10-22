---
id: db85511e-1fd2-4eb5-b2f2-f8767c2d83d9
name: Screensaver
type: technique
mitre_id: T1180
mitre_url: null
created_at: '2019-08-28T21:17:32.298378+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
---

# Screensaver

**MITRE ID**: T1180

## Description

Screensavers are programs that execute after a configurable time of user inactivity and consist of Portable Executable (PE) files with a .scr file extension.[1] The Windows screensaver application scrnsave.scr is located in C:\Windows\System32\, and C:\Windows\sysWOW64\ on 64-bit Windows systems, along with screensavers included with base Windows installations. The following screensaver settings are stored in the Registry (HKCU\Control Panel\Desktop\) and could be manipulated to achieve persistence:SCRNSAVE.exe - set to malicious PE pathScreenSaveActive - set to '1' to enable the screensaverScreenSaverIsSecure - set to '0' to not require a password to unlockScreenSaverTimeout - sets user inactivity timeout before screensaver is executedAdversaries can use screensaver settings to maintain persistence by setting the screensaver to run malware after a certain timeframe of user inactivity. [2]

# Detection

Monitor process execution and command-line parameters of .scr files. Monitor changes to screensaver configuration changes in the Registry that may not correlate with typical user behavior.

Tools such as Sysinternals Autoruns can be used to detect changes to the screensaver binary path in the Registry. Suspicious paths and PE files may indicate outliers among legitimate screensavers in a network and should be investigated.

# Mitigation

Block .scr files from being executed from non-standard locations. Set Group Policy to force users to have a dedicated screensaver where local changes should not override the settings to prevent changes. Use Group Policy to disable screensavers if they are unnecessary. [3]

# Footnotes

[1] Wikipedia. (2017, November 22). Screensaver. Retrieved December 5, 2017.

[2] ESET. (2017, August). Gazing at Gazer: Turla’s new second stage backdoor. Retrieved September 14, 2017.

[3] Microsoft. (n.d.). Customizing the Desktop. Retrieved December 5, 2017.

## Defense

Block .scr files from being executed from non-standard locations. Set Group Policy to force users to have a dedicated screensaver where local changes should not override the settings to prevent changes. Use Group Policy to disable screensavers if they are

## Tactics

- [[Persistence|TA0003 - Persistence]]

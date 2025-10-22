---
id: 1848098c-0ddf-42fa-9d85-558da6f0ea7f
name: Port Monitors
type: technique
mitre_id: T1013
mitre_url: null
created_at: '2019-08-28T21:17:44.758976+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
---

# Port Monitors

**MITRE ID**: T1013

## Description

A port monitor can be set through the  [1] API call to set a DLL to be loaded at startup. [1] This DLL can be located in C:\Windows\System32 and will be loaded by the print spooler service, spoolsv.exe, on boot. The spoolsv.exe process also runs under SYSTEM level permissions. [2] Alternatively, an arbitrary DLL can be loaded if permissions allow writing a fully-qualified pathname for that DLL to HKLM\SYSTEM\CurrentControlSet\Control\Print\Monitors. The Registry key contains entries for the following:Local PortStandard TCP/IP PortUSB MonitorWSD PortAdversaries can use this technique to load malicious code at startup that will persist on system reboot and execute as SYSTEM.

# Detection

Monitor process API calls to  [1].Monitor DLLs that are loaded by spoolsv.exe for DLLs that are abnormal.New DLLs written to the System32 directory that do not correlate with known good software or patching may be suspicious.Monitor Registry writes to HKLM\SYSTEM\CurrentControlSet\Control\Print\Monitors.Run the Autoruns utility, which checks for this Registry key as a persistence mechanism [5]

# Mitigation

Identify and block potentially malicious software that may persist in this manner by using whitelisting [4] tools capable of monitoring DLL loads by processes running under SYSTEM permissions.

# Footnotes

[1] Microsoft. (n.d.). AddMonitor function. Retrieved November 12, 2014.

[2] Bloxham, B. (n.d.). Getting Windows to Play with Itself [PowerPoint slides]. Retrieved November 12, 2014.

[3] FireEye. (2018, October 03). APT38: Un-usual Suspects. Retrieved November 6, 2018.

[4] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[5] Russinovich, M. (2016, January 4). Autoruns for Windows v13.51. Retrieved June 6, 2016.

## Defense

Identify and block potentially malicious software that may persist in this manner by using whitelisting (Citation: Beechey 2010) tools capable of monitoring DLL loads by processes running under SYSTEM permissions.

## Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

---
id: e7fa7ff8-214a-491b-a504-62a1fcd50132
name: Netsh Helper DLL
type: technique
mitre_id: T1128
mitre_url: null
created_at: '2019-08-28T21:17:20.095467+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
---

# Netsh Helper DLL

**MITRE ID**: T1128

## Description

Netsh.exe (also referred to as Netshell) is a command-line scripting utility used to interact with the network configuration of a system. It contains functionality to add helper DLLs for extending functionality of the utility. [1] The paths to registered netsh.exe helper DLLs are entered into the Windows Registry at HKLM\SOFTWARE\Microsoft\Netsh.Adversaries can use netsh.exe with helper DLLs to proxy execution of arbitrary code in a persistent manner when netsh.exe is executed automatically with another Persistence technique or if other persistent software is present on the system that executes netsh.exe as part of its normal functionality. Examples include some VPN software that invoke netsh.exe. [2]Proof of concept code exists to load Cobalt Strike's payload using netsh.exe helper DLLs. [3]

# Detection

It is likely unusual for netsh.exe to have any child processes in most environments. Monitor process executions and investigate any child processes spawned by netsh.exe for malicious behavior. Monitor the HKLM\SOFTWARE\Microsoft\Netsh registry key for any new or suspicious entries that do not correlate with known system files or benign software. [2]

# Mitigation

Identify and block potentially malicious software that may persist in this manner by using whitelisting [4] tools capable of monitoring DLL loads by Windows utilities like AppLocker. [5] [6]

# Footnotes

[1] Microsoft. (n.d.). Using Netsh. Retrieved February 13, 2017.

[2] Demaske, M. (2016, September 23). USING NETSHELL TO EXECUTE EVIL DLLS AND PERSIST ON A HOST. Retrieved April 8, 2017.

[3] Smeets, M. (2016, September 26). NetshHelperBeacon. Retrieved February 13, 2017.

[4] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[5] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[6] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

## Defense

Identify and block potentially malicious software that may persist in this manner by using whitelisting (Citation: Beechey 2010) tools capable of monitoring DLL loads by Windows utilities like AppLocker. (Citation: Windows Commands JPCERT) (Citation: NSA 

## Tactics

- [[Persistence|TA0003 - Persistence]]

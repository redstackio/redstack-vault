---
id: d0697084-b6cb-49f1-967b-1bd9111c47e4
name: Service Registry Permissions Weakness
type: technique
mitre_id: T1058
mitre_url: null
created_at: '2019-08-28T21:17:38.138485+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
procedures:
- '[[CORS Misconfiguration Exploitation: Origin Reflection]]'
- '[[CORS Misconfiguration Exploitation: Origin Reflection]]'
- '[[CORS Misconfiguration Exploitation: Origin Reflection]]'
- '[[CORS Misconfiguration Exploitation: Origin Reflection]]'
- '[[Windows - Elevated Services Backdoor Persistence]]'
- '[[Windows Local Service Permissions Escalation]]'
- '[[Windows Service Persistence with Calculator]]'
- '[[Windows XP SP1 - UPnP Host Exploit]]'
---

# Service Registry Permissions Weakness

**MITRE ID**: T1058

## Description

Windows stores local service configuration information in the Registry under HKLM\SYSTEM\CurrentControlSet\Services. The information stored under a service's Registry keys can be manipulated to modify a service's execution parameters through tools such as the service controller, sc.exe, PowerShell, or Reg. Access to Registry keys is controlled through Access Control Lists and permissions. [1]If the permissions for users and groups are not properly set and allow access to the Registry keys for a service, then adversaries can change the service binPath/ImagePath to point to a different executable under their control. When the service starts or is restarted, then the adversary-controlled program will execute, allowing the adversary to gain persistence and/or privilege escalation to the account context the service is set to execute under (local/domain account, SYSTEM, LocalService, or NetworkService).Adversaries may also alter Registry keys associated with service failure parameters (such as FailureCommand) that may be executed in an elevated context anytime the service fails or is intentionally corrupted. [2]

# Detection

Service changes are reflected in the Registry. Modification to existing services should not occur frequently. If a service binary path or failure parameters are changed to values that are not typical for that service and does not correlate with software updates, then it may be due to malicious activity. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as network connections made for Command and Control, learning details about the environment through Discovery, and Lateral Movement.

Tools such as Sysinternals Autoruns may also be used to detect system changes that could be attempts at persistence, including listing current service information. [6] Look for changes to services that do not correlate with known software, patch cycles, etc. Suspicious program execution through services may show up as outlier processes that have not been seen before when compared against historical data.

Monitor processes and command-line arguments for actions that could be done to modify services. Remote access tools with built-in features may interact directly with the Windows API to perform these functions outside of typical system utilities. Services may also be changed through Windows system management tools such as Windows Management Instrumentation and PowerShell, so additional logging may need to be configured to gather the appropriate data.

# Mitigation

Ensure proper permissions are set for Registry hives to prevent users from modifying keys for system components that may lead to privilege escalation.

Identify and block potentially malicious software that may be executed through service abuse by using whitelisting [3] tools like AppLocker [4] [5] that are capable of auditing and/or blocking unknown programs.

# Footnotes

[1] Microsoft. (n.d.). Registry Key Security and Access Rights. Retrieved March 16, 2017.

[2] The Cyber (@r0wdy_). (2017, November 30). Service Recovery Parameters. Retrieved April 9, 2018.

[3] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[4] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[5] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[6] Russinovich, M. (2016, January 4). Autoruns for Windows v13.51. Retrieved June 6, 2016.

## Defense

Ensure proper permissions are set for Registry hives to prevent users from modifying keys for system components that may lead to privilege escalation.

Identify and block potentially malicious software that may be executed through service abuse by using w

## Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

## Related Procedures (8)

- [[CORS Misconfiguration Exploitation: Origin Reflection]]
- [[CORS Misconfiguration Exploitation: Origin Reflection]]
- [[CORS Misconfiguration Exploitation: Origin Reflection]]
- [[CORS Misconfiguration Exploitation: Origin Reflection]]
- [[Windows - Elevated Services Backdoor Persistence]]
- [[Windows Local Service Permissions Escalation]]
- [[Windows Service Persistence with Calculator]]
- [[Windows XP SP1 - UPnP Host Exploit]]

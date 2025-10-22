---
id: a7c32cc7-84a4-4dbf-8db7-9b9921958e8f
name: Time Providers
type: technique
mitre_id: T1209
mitre_url: null
created_at: '2019-08-28T21:17:19.537581+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
---

# Time Providers

**MITRE ID**: T1209

## Description

The Windows Time service (W32Time) enables time synchronization across and within domains. [1] W32Time time providers are responsible for retrieving time stamps from hardware/network resources and outputting these values to other network clients. [2]Time providers are implemented as dynamic-link libraries (DLLs) that are registered in the subkeys of  HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\W32Time\TimeProviders\. [2] The time provider manager, directed by the service control manager, loads and starts time providers listed and enabled under this key at system startup and/or whenever parameters are changed. [2]Adversaries may abuse this architecture to establish Persistence, specifically by registering and enabling a malicious DLL as a time provider. Administrator privileges are required for time provider registration, though execution will run in context of the Local Service account. [3]

# Detection

Baseline values and monitor/analyze activity related to modifying W32Time information in the Registry, including application programming interface (API) calls such as RegCreateKeyEx and RegSetValueEx as well as execution of the W32tm.exe utility. [7] There is no restriction on the number of custom time providers registrations, though each may require a DLL payload written to disk. [3]

The Sysinternals Autoruns tool may also be used to analyze auto-starting locations, including DLLs listed as time providers. [8]

# Mitigation

Identify and block potentially malicious software that may be executed as a time provider by using whitelisting [4] tools, like AppLocker, [5] [6] that are capable of auditing and/or blocking unknown DLLs.

Consider using Group Policy to configure and block subsequent modifications to W32Time parameters. [7]

# Footnotes

[1] Microsoft. (2018, February 1). Windows Time Service (W32Time). Retrieved March 26, 2018.

[2] Microsoft. (n.d.). Time Provider. Retrieved March 26, 2018.

[3] Lundgren, S. (2017, October 28). w32time. Retrieved March 26, 2018.

[4] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[5] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[6] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[7] Mathers, B. (2017, May 31). Windows Time Service Tools and Settings. Retrieved March 26, 2018.

[8] Russinovich, M. (2016, January 4). Autoruns for Windows v13.51. Retrieved June 6, 2016.

## Defense

Identify and block potentially malicious software that may be executed as a time provider by using whitelisting (Citation: Beechey 2010) tools, like AppLocker, (Citation: Windows Commands JPCERT) (Citation: NSA MS AppLocker) that are capable of auditing a

## Tactics

- [[Persistence|TA0003 - Persistence]]

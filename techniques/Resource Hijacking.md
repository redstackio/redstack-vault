---
id: d21e8aba-7a0f-4003-9d01-074c7cbd83f5
name: Resource Hijacking
type: technique
mitre_id: T1496
mitre_url: null
created_at: '2019-08-28T21:17:19.151211+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Impact|TA0040 - Impact]]'
procedures:
- '[[Race Condition Turbo Intruder Attack]]'
- '[[SQL Injection WAF Bypass]]'
---

# Resource Hijacking

**MITRE ID**: T1496

## Description

Adversaries may leverage the resources of co-opted systems in order to solve resource intensive problems which may impact system and/or hosted service availability. One common purpose for Resource Hijacking is to validate transactions of cryptocurrency networks and earn virtual currency. Adversaries may consume enough system resources to negatively impact and/or cause affected machines to become unresponsive.[1] Servers and cloud-based systems are common targets because of the high potential for available resources, but user endpoint systems may also be compromised and used for Resource Hijacking and cryptocurrency mining.

# Detection

Consider monitoring process resource usage to determine anomalous activity associated with malicious hijacking of computer resources such as CPU, memory, and graphics processing resources. Monitor for suspicious use of network resources associated with cryptocurrency mining software. Monitor for common cryptomining software process names and files on local systems that may indicate compromise and resource usage.

# Mitigation

Identify potentially malicious software and audit and/or block it by using whitelisting[2] tools, like AppLocker,[3][4] or Software Restriction Policies[5] where appropriate.[6]

# Footnotes

[1] GReAT. (2017, April 3). Lazarus Under the Hood. Retrieved April 17, 2019.

[2] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[3] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[4] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[5] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[6] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Defense

Identify potentially malicious software and audit and/or block it by using whitelisting(Citation: Beechey 2010) tools, like AppLocker,(Citation: Windows Commands JPCERT)(Citation: NSA MS AppLocker) or Software Restriction Policies(Citation: Corio 2008) wh

## Tactics

- [[Impact|TA0040 - Impact]]

## Related Procedures (2)

- [[Race Condition Turbo Intruder Attack]]
- [[SQL Injection WAF Bypass]]

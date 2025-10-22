---
id: 292ca697-fde7-4e54-9ed6-36c5f1a17320
name: Runtime Data Manipulation
type: technique
mitre_id: T1494
mitre_url: null
created_at: '2019-08-28T21:17:32.443852+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Impact|TA0040 - Impact]]'
---

# Runtime Data Manipulation

**MITRE ID**: T1494

## Description

Adversaries may modify systems in order to manipulate the data as it is accessed and displayed to an end user.[1][2] By manipulating runtime data, adversaries may attempt to affect a business process, organizational understanding, and decision making. Adversaries may alter application binaries used to display data in order to cause runtime manipulations. Adversaries may also conduct Change Default File Association and Masquerading to cause a similar effect. The type of modification and the impact it will have depends on the target application and process as well as the goals and objectives of the adversary. For complex systems, an adversary would likely need special expertise and possibly access to specialized software related to the system that would typically be gained through a prolonged information gathering campaign in order to have the desired impact.

# Detection

Inspect important application binary file hashes, locations, and modifications for suspicious/unexpected values.

# Mitigation

Identify critical business and system processes that may be targeted by adversaries and work to secure those systems against tampering. Prevent critical business and system processes from being replaced, overwritten, or reconfigured to load potentially malicious code. Identify potentially malicious software and audit and/or block it by using whitelisting[3] tools, like AppLocker,[4][5] or Software Restriction Policies[6] where appropriate.[7]

# Footnotes

[1] FireEye. (2018, October 03). APT38: Un-usual Suspects. Retrieved November 6, 2018.

[2] Department of Justice. (2018, September 6). Criminal Complaint - United States of America v. PARK JIN HYOK. Retrieved March 29, 2019.

[3] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[4] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[5] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[6] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[7] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Defense

Identify critical business and system processes that may be targeted by adversaries and work to secure those systems against tampering. Prevent critical business and system processes from being replaced, overwritten, or reconfigured to load potentially ma

## Tactics

- [[Impact|TA0040 - Impact]]

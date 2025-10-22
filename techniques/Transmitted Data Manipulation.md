---
id: be3098bc-13ad-4c2d-b0ec-6d8f4a7e684b
name: Transmitted Data Manipulation
type: technique
mitre_id: T1493
mitre_url: null
created_at: '2019-08-28T21:17:42.520349+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Impact|TA0040 - Impact]]'
---

# Transmitted Data Manipulation

**MITRE ID**: T1493

## Description

Adversaries may alter data en route to storage or other systems in order to manipulate external outcomes or hide activity.[1][2] By manipulating transmitted data, adversaries may attempt to affect a business process, organizational understanding, and decision making. Manipulation may be possible over a network connection or between system processes where there is an opportunity deploy a tool that will intercept and change information. The type of modification and the impact it will have depends on the target transmission mechanism as well as the goals and objectives of the adversary. For complex systems, an adversary would likely need special expertise and possibly access to specialized software related to the system that would typically be gained through a prolonged information gathering campaign in order to have the desired impact.

# Detection

Detecting the manipulation of data as at passes over a network can be difficult without the appropriate tools. In some cases integrity verification checks, such as file hashing, may be used on critical files as they transit a network. With some critical processes involving transmission of data, manual or out-of-band integrity checking may be useful for identifying manipulated data.

# Mitigation

Identify critical business and system processes that may be targeted by adversaries and work to secure communications related to those processes against tampering. Encrypt all important data flows to reduce the impact of tailored modifications on data in transit.

# Footnotes

[1] FireEye. (2018, October 03). APT38: Un-usual Suspects. Retrieved November 6, 2018.

[2] Department of Justice. (2018, September 6). Criminal Complaint - United States of America v. PARK JIN HYOK. Retrieved March 29, 2019.

## Defense

Identify critical business and system processes that may be targeted by adversaries and work to secure communications related to those processes against tampering. Encrypt all important data flows to reduce the impact of tailored modifications on data in 

## Tactics

- [[Impact|TA0040 - Impact]]

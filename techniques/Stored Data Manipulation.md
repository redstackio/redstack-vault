---
id: bb00aa79-3ef2-4531-9bb2-7c9edac7f1cd
name: Stored Data Manipulation
type: technique
mitre_id: T1492
mitre_url: null
created_at: '2019-08-28T21:17:44.930271+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Impact|TA0040 - Impact]]'
---

# Stored Data Manipulation

**MITRE ID**: T1492

## Description

Adversaries may insert, delete, or manipulate data at rest in order to manipulate external outcomes or hide activity.[1][2] By manipulating stored data, adversaries may attempt to affect a business process, organizational understanding, and decision making. Stored data could include a variety of file formats, such as Office files, databases, stored emails, and custom file formats. The type of modification and the impact it will have depends on the type of data as well as the goals and objectives of the adversary. For complex systems, an adversary would likely need special expertise and possibly access to specialized software related to the system that would typically be gained through a prolonged information gathering campaign in order to have the desired impact.

# Detection

Where applicable, inspect important file hashes, locations, and modifications for suspicious/unexpected values.

# Mitigation

Identify critical business and system processes that may be targeted by adversaries and work to secure the data related to those processes against tampering. least privilege principles are applied to important information resources to reduce exposure to data manipulation risk. Consider encrypting important information to reduce an adversaries ability to perform tailor data modifications. Where applicable, examine using file monitoring software to check integrity on important files and directories as well as take corrective actions when unauthorized changes are detected. 

Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data.[4] Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and manipulate backups.

# Footnotes

[1] FireEye. (2018, October 03). APT38: Un-usual Suspects. Retrieved November 6, 2018.

[2] Department of Justice. (2018, September 6). Criminal Complaint - United States of America v. PARK JIN HYOK. Retrieved March 29, 2019.

[3] Vengerik, B. et al.. (2014, December 5). Hacking the Street? FIN4 Likely Playing the Market. Retrieved December 17, 2018.

[4] Ready.gov. (n.d.). IT Disaster Recovery Plan. Retrieved March 15, 2019.

## Defense

Identify critical business and system processes that may be targeted by adversaries and work to secure the data related to those processes against tampering. Ensure least privilege principles are applied to important information resources to reduce exposu

## Tactics

- [[Impact|TA0040 - Impact]]

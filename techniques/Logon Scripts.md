---
id: df1e841f-2efa-44ce-830c-140c307f7afd
name: Logon Scripts
type: technique
mitre_id: T1037
mitre_url: null
created_at: '2019-08-28T21:17:33.277698+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
---

# Logon Scripts

**MITRE ID**: T1037

## Description

WindowsWindows allows logon scripts to be run whenever a specific user or group of users log into a system. [1] The scripts can be used to perform administrative functions, which may often execute other programs or send information to an internal logging server.If adversaries can access these scripts, they may insert additional code into the logon script to execute their tools when a user logs in. This code can allow them to maintain persistence on a single system, if it is a local script, or to move laterally within a network, if the script is stored on a central server and pushed to many systems. Depending on the access configuration of the logon scripts, either local credentials or an administrator account may be necessary.MacMac allows login and logoff hooks to be run as root whenever a specific user logs into or out of a system. A login hook tells Mac OS X to execute a certain script when a user logs in, but unlike startup items, a login hook executes as root [2]. There can only be one login hook at a time though. If adversaries can access these scripts, they can insert additional code to the script to execute their tools when a user logs in.

# Detection

Monitor logon scripts for unusual access by abnormal users or at abnormal times. Look for files added or modified by unusual accounts outside of normal administration duties.

# Mitigation

Restrict write access to logon scripts to specific administrators. Prevent access to administrator accounts by mitigating Credential Access techniques and limiting account access and permissions of Valid Accounts.

Identify and block potentially malicious software that may be executed through logon script modification by using whitelisting [8] tools like AppLocker [9] [10] that are capable of auditing and/or blocking unknown programs.

# Footnotes

[1] Microsoft. (2005, January 21). Creating logon scripts. Retrieved April 27, 2016.

[2] Apple. (2011, June 1). Mac OS X: Creating a login hook. Retrieved July 17, 2017.

[3] Unit 42. (2017, December 15). Unit 42 Playbook Viewer. Retrieved December 20, 2017.

[4] Gorelik, M. (2018, October 08). Cobalt Group 2.0. Retrieved November 5, 2018.

[5] ESET. (2016, October). En Route with Sednit - Part 1: Approaching the Target. Retrieved November 8, 2016.

[6] Mercer, W., et al. (2017, October 22). "Cyber Conflict" Decoy Document Used in Real Cyber Conflict. Retrieved November 2, 2018.

[7] ESET. (2018, November 20). Sednit: What’s going on with Zebrocy?. Retrieved February 12, 2019.

[8] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[9] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[10] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

## Defense

Restrict write access to logon scripts to specific administrators. Prevent access to administrator accounts by mitigating Credential Access techniques and limiting account access and permissions of [Valid Accounts](https://attack.mitre.org/techniques/T107

## Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

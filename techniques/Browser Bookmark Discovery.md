---
id: dc9cdc70-404d-4575-80df-fe91d63be833
name: Browser Bookmark Discovery
type: technique
mitre_id: T1217
mitre_url: null
created_at: '2019-08-28T21:17:36.770695+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
procedures:
- '[[Enumerate MSSQL Server Agent Jobs]]'
- '[[Enumerate MSSQL Server Logins]]'
- '[[Linux Privilege Escalation Enumeration]]'
- '[[SAMAccountName Spoofing via SMB Credential Enumeration]]'
---

# Browser Bookmark Discovery

**MITRE ID**: T1217

## Description

Adversaries may enumerate browser bookmarks to learn more about compromised hosts. Browser bookmarks may reveal personal information about users (ex: banking sites, interests, social media, etc.) as well as details about internal network resources such as servers, tools/dashboards, or other related infrastructure.Browser bookmarks may also highlight additional targets after an adversary has access to valid credentials, especially Credentials in Files associated with logins cached by a browser.Specific storage locations vary based on platform and/or application, but browser bookmarks are typically stored in local files/databases.

# Detection

Monitor processes and command-line arguments for actions that could be taken to gather browser bookmark information. Remote access tools with built-in features may interact directly using APIs to gather information. Information may also be acquired through system management tools such as Windows Management Instrumentation and PowerShell.

System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as Collection and Exfiltration, based on the information obtained.

# Mitigation

File system activity is a common part of an operating system, so it is unlikely that mitigation would be appropriate for this technique. For example, mitigating accesses to browser bookmark files will likely have unintended side effects such as preventing legitimate software from operating properly. Efforts should be focused on preventing adversary tools from running earlier in the chain of activity and on identification of subsequent malicious behavior. It may still be beneficial to identify and block unnecessary system utilities or potentially malicious software by using whitelisting [4] tools, like AppLocker, [5] [6] or Software Restriction Policies [7] where appropriate. [8]

# Footnotes

[1] Kuzin, M., Zelensky S. (2018, July 20). Calisto Trojan for macOS. Retrieved September 7, 2018.

[2] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[3] Falcone, R. and Miller-Osborn, J.. (2016, January 24). Scarlet Mimic: Years-Long Espionage Campaign Targets Minority Activists. Retrieved February 10, 2016.

[4] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[5] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[6] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[7] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[8] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Defense

File system activity is a common part of an operating system, so it is unlikely that mitigation would be appropriate for this technique. For example, mitigating accesses to browser bookmark files will likely have unintended side effects such as preventing

## Tactics

- [[Discovery|TA0007 - Discovery]]

## Related Procedures (4)

- [[Enumerate MSSQL Server Agent Jobs]]
- [[Enumerate MSSQL Server Logins]]
- [[Linux Privilege Escalation Enumeration]]
- [[SAMAccountName Spoofing via SMB Credential Enumeration]]

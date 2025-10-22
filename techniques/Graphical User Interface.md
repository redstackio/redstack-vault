---
id: fc42c66f-446c-4889-af13-66e8b868f9f2
name: Graphical User Interface
type: technique
mitre_id: T1061
mitre_url: null
created_at: '2019-08-28T21:17:38.646930+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
---

# Graphical User Interface

**MITRE ID**: T1061

## Description

The Graphical User Interfaces (GUI) is a common way to interact with an operating system. Adversaries may use a system's GUI during an operation, commonly through a remote interactive session such as Remote Desktop Protocol, instead of through a Command-Line Interface, to search for information and execute files via mouse double-click events, the Windows Run command [1], or other potentially difficult to monitor interactions.

# Detection

Detection of execution through the GUI will likely lead to significant false positives. Other factors should be considered to detect misuse of services that can lead to adversaries gaining access to systems through interactive remote sessions. 

Unknown or unusual process launches outside of normal behavior on a particular system occurring through remote interactive sessions are suspicious. Collect and audit security logs that may indicate access to and use of Legitimate Credentials to access remote systems within the network.

# Mitigation

Prevent adversaries from gaining access to credentials through Credential Access that can be used to log into remote desktop sessions on systems.

Identify unnecessary system utilities, third-party tools, or potentially malicious software that may be used to log into remote interactive sessions, and audit and/or block them by using whitelisting [3] tools, like AppLocker [4] [5] and Software Restriction Policies [6] where appropriate. [7]

# Footnotes

[1] Wikipedia. (2018, August 3). Run Command. Retrieved October 12, 2018.

[2] Glyer, C. (2018, April 14). @cglyer Status Update. Retrieved October 11, 2018.

[3] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[4] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[5] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[6] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[7] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Defense

Prevent adversaries from gaining access to credentials through Credential Access that can be used to log into remote desktop sessions on systems.

Identify unnecessary system utilities, third-party tools, or potentially malicious software that may be used

## Tactics

- [[Execution|TA0002 - Execution]]

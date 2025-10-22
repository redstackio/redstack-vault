---
id: c7aeb8a5-e2b3-4dd0-bb3c-055dafa1506e
name: Shared Webroot
type: technique
mitre_id: T1051
mitre_url: null
created_at: '2019-08-28T21:17:20.664076+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
procedures:
- '[[Reverse Shell Cheat Sheet - Spawn TTY Shell]]'
- '[[Reverse Shell: Spawn TTY Shell]]'
---

# Shared Webroot

**MITRE ID**: T1051

## Description

Adversaries may add malicious content to an internally accessible website through an open network file share that contains the website's webroot or Web content directory [1] [2] and then browse to that content with a Web browser to cause the server to execute the malicious content. The malicious content will typically run under the context and permissions of the Web server process, often resulting in local system or administrative privileges, depending on how the Web server is configured.This mechanism of shared access and remote execution could be used for lateral movement to the system running the Web server. For example, a Web server running PHP with an open network share could allow an adversary to upload a remote access tool and PHP script to execute the RAT on the system running the Web server when a specific page is visited. [3]

# Detection

Use file and process monitoring to detect when files are written to a Web server by a process that is not the normal Web server process or when files are written outside of normal administrative time periods. Use process monitoring to identify normal processes that run on the Web server and detect processes that are not typically executed.

# Mitigation

Networks that allow for open development and testing of Web content and allow users to set up their own Web servers on the enterprise network may be particularly vulnerable if the systems and Web servers are not properly secured to limit privileged account use, unauthenticated network share access, and network/system isolation.

Ensure proper permissions on directories that are accessible through a Web server. Disallow remote access to the webroot or other directories used to serve Web content. Disable execution on directories within the webroot. Ensure that permissions of the Web server process are only what is required by not using built-in accounts; instead, create specific accounts to limit unnecessary access or permissions overlap across multiple systems. [4] [5]

# Footnotes

[1] Microsoft. (2016, October 20). How to: Find the Web Application Root. Retrieved July 27, 2018.

[2] Apache. (n.d.). Apache HTTP Server Version 2.4 Documentation - Web Site Content. Retrieved July 27, 2018.

[3] Brandt, Andrew. (2011, February 22). Malicious PHP Scripts on the Rise. Retrieved October 3, 2018.

[4] Acunetix. (n.d.). Web Server Security and Database Server Security. Retrieved July 26, 2018.

[5] Scarfone, K. et al.. (2008, July). NIST Special Publication 800-123 - Guide to General Server Security. Retrieved July 26, 2018.

## Defense

Networks that allow for open development and testing of Web content and allow users to set up their own Web servers on the enterprise network may be particularly vulnerable if the systems and Web servers are not properly secured to limit privileged accoun

## Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

## Related Procedures (2)

- [[Reverse Shell Cheat Sheet - Spawn TTY Shell]]
- [[Reverse Shell: Spawn TTY Shell]]

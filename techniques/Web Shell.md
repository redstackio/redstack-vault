---
id: 1ceb824f-8146-44fb-9ef1-1b799ec511b0
name: Web Shell
type: technique
mitre_id: T1100
mitre_url: null
created_at: '2019-08-28T21:17:26.294425+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
procedures:
- '[[Add and Execute Code on a WordPress Site (Authenticated)]]'
- '[[AWS EC2 Instance Connect with SSH Key Push]]'
- '[[HTAccess and PHP Shell Upload]]'
- '[[Insecure File Upload Exploit via Picture Compression]]'
- '[[Upgrade from a Website RCE to Reverse Shell (Linux)]]'
- '[[Upload Insecure Configuration Files]]'
---

# Web Shell

**MITRE ID**: T1100

## Description

A Web shell is a Web script that is placed on an openly accessible Web server to allow an adversary to use the Web server as a gateway into a network. A Web shell may provide a set of functions to execute or a command-line interface on the system that hosts the Web server. In addition to a server-side script, a Web shell may have a client interface program that is used to talk to the Web server (see, for example, China Chopper Web shell client). [1]Web shells may serve as Redundant Access or as a persistence mechanism in case an adversary's primary access methods are detected and removed.

# Detection

Web shells can be difficult to detect. Unlike other forms of persistent remote access, they do not initiate connections. The portion of the Web shell that is on the server may be small and innocuous looking. The PHP version of the China Chopper Web shell, for example, is the following short payload: [1]

<?php @eval($_POST['password']);>

Nevertheless, detection mechanisms exist. Process monitoring may be used to detect Web servers that perform suspicious actions such as running cmd or accessing files that are not in the Web directory. File monitoring may be used to detect changes to files in the Web directory of a Web server that do not match with updates to the Web server's content and may indicate implantation of a Web shell script. Log authentication attempts to the server and any unusual traffic patterns to or from the server and internal network. [12]

# Mitigation

Ensure that externally facing Web servers are patched regularly to prevent adversary access through Exploitation for Privilege Escalation to gain remote code access or through file inclusion weaknesses that may allow adversaries to upload files or scripts that are automatically served as Web pages. 

Audit account and group permissions to ensure that accounts used to manage servers do not overlap with accounts and permissions of users in the internal network that could be acquired through Credential Access and used to log into the Web server and plant a Web shell or pivot from the Web server into the internal network. [12]

# Footnotes

[1] Lee, T., Hanzlik, D., Ahl, I. (2013, August 7). Breaking Down the China Chopper Web Shell - Part I. Retrieved March 27, 2015.

[2] Lassalle, D., et al. (2017, November 6). OceanLotus Blossoms: Mass Digital Surveillance and Attacks Targeting ASEAN, Asian Nations, the Media, Human Rights Groups, and Civil Society. Retrieved November 6, 2017.

[3] Hawley et al. (2019, January 29). APT39: An Iranian Cyber Espionage Group Focused on Personal Information. Retrieved February 19, 2019.

[4] Dell SecureWorks Counter Threat Unit Threat Intelligence. (2015, August 5). Threat Group-3390 Targets Organizations for Cyberespionage. Retrieved August 18, 2018.

[5] RYANJ. (2014, February 20). Mo’ Shells Mo’ Problems – Deep Panda Web Shells. Retrieved September 16, 2015.

[6] US-CERT. (2018, March 16). Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved June 6, 2018.

[7] US-CERT. (2017, October 20). Alert (TA17-293A): Advanced Persistent Threat Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved November 2, 2017.

[8] Plan, F., et all. (2019, March 4). APT40: Examining a China-Nexus Espionage Actor. Retrieved March 18, 2019.

[9] Unit 42. (2017, December 15). Unit 42 Playbook Viewer. Retrieved December 20, 2017.

[10] Davis, S. and Caban, D. (2017, December 19). APT34 - New Targeted Attack in the Middle East. Retrieved December 20, 2017.

[11] Miller, S, et al. (2019, April 10). TRITON Actor TTP Profile, Custom Attack Tools, Detections, and ATT&CK Mapping. Retrieved April 16, 2019.

[12] US-CERT. (2015, November 13). Compromised Web Servers and Web Shells - Threat Awareness and Guidance. Retrieved June 8, 2016.

## Defense

Ensure that externally facing Web servers are patched regularly to prevent adversary access through [Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1068) to gain remote code access or through file inclusion weaknesses that may

## Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

## Related Procedures (6)

- [[Add and Execute Code on a WordPress Site (Authenticated)]]
- [[AWS EC2 Instance Connect with SSH Key Push]]
- [[HTAccess and PHP Shell Upload]]
- [[Insecure File Upload Exploit via Picture Compression]]
- [[Upgrade from a Website RCE to Reverse Shell (Linux)]]
- [[Upload Insecure Configuration Files]]

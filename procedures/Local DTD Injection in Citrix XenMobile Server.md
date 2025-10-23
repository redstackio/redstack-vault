---
id: 53a7ffa3-49bf-4885-a4aa-9ad3d6388f46
name: Local DTD Injection in Citrix XenMobile Server
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:44.497123+00:00'
updated_at: '2023-04-10T20:24:42.317329+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Exfiltration|TA0010 - Exfiltration]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Create Account|T1136 - Create Account]]'
- '[[Distributed Component Object Model|T1175 - Distributed Component Object Model]]'
- '[[Scheduled Transfer|T1029 - Scheduled Transfer]]'
- '[[User Execution|T1204 - User Execution]]'
tags:
- '[[Citrix XenMobile Server]]'
- '[[XML External Entity]]'
- '[[XXE with local DTD]]'
---

# Local DTD Injection in Citrix XenMobile Server

## Summary

Local DTD Injection in Citrix XenMobile Server allows an attacker to read files on the server and execute system commands. The attacker can modify the DTD to include an external entity that points to a file on the server. When the XML is parsed, the contents of the file will be included in the outp

## Description

# Description

Local DTD Injection in Citrix XenMobile Server allows an attacker to read files on the server and execute system commands. The attacker can modify the DTD to include an external entity that points to a file on the server. When the XML is parsed, the contents of the file will be included in the output. This vulnerability can be used to read sensitive files, such as the configuration file, which contains the database credentials. An attacker can also execute system commands by modifying the DTD to include a system entity that executes the command. This can lead to a complete compromise of the server.

 

## Requirements

1. Access to the Citrix XenMobile Server.

1. Ability to modify the DTD in the XML input.

 

## Defense

1. Disable external entity processing in XML parsers.

1. Use input validation to prevent untrusted XML input from being processed.

1. Implement least privilege access controls to limit the impact of a successful attack.

 

## Objectives

1. Read sensitive files on the Citrix XenMobile Server.

1. Execute system commands on the Citrix XenMobile Server.

 

# Instructions

1. The DTD Injection attack is an attack technique used to exploit web applications that parse XML input containing a reference to an external entity. An attacker can leverage the vulnerable XML parser to include a reference to an external DTD, which can be abused to read arbitrary files and in some cases execute arbitrary code on the target system.

 

The 'data' field contains the payload for the DTD Injection attack. In this example, the payload injects a reference to an external DTD file located in a JAR file on the target system. The 'instruction' field provides an overview of the DTD Injection attack and how it can be used to exploit vulnerable web applications. The 'explain' field provides additional information about the attack and its potential impact on the target system.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Exfiltration|TA0010 - Exfiltration]]
- [[Lateral Movement|TA0008 - Lateral Movement]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Create Account|T1136 - Create Account]]
- [[Distributed Component Object Model|T1175 - Distributed Component Object Model]]
- [[Scheduled Transfer|T1029 - Scheduled Transfer]]
- [[User Execution|T1204 - User Execution]]

## Tags

- [[Citrix XenMobile Server]]
- [[XML External Entity]]
- [[XXE with local DTD]]



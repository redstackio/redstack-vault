---
id: b1cdb361-981a-428f-aa67-57c7d7e69e26
name: XSLT Injection - Remote Code Execution with Java
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:41.584235+00:00'
updated_at: '2023-04-10T20:24:51.113173+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
- '[[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]'
tags:
- '[[Exploit]]'
- '[[Remote Code Execution with Java]]'
- '[[XSLT Injection]]'
---

# XSLT Injection - Remote Code Execution with Java

## Summary

XSLT Injection is a type of attack that targets web applications by injecting malicious code into XSLT (eXtensible Stylesheet Language Transformations) files. This can result in remote code execution on the server-side, which can be exploited by attackers to gain unauthorized access to sensitive da

## Description

# Description

XSLT Injection is a type of attack that targets web applications by injecting malicious code into XSLT (eXtensible Stylesheet Language Transformations) files. This can result in remote code execution on the server-side, which can be exploited by attackers to gain unauthorized access to sensitive data or systems. In the case of this specific procedure, the attacker can use the XSLT Injection vulnerability to execute Java code remotely. This can allow them to take control of the server and perform various malicious activities, such as stealing data, installing malware, or launching further attacks.

From a technical perspective, XSLT Injection works by exploiting the trust relationship between the web application and the XSLT processor. By injecting malicious code into the XSLT file, the attacker can manipulate the output of the transformation and execute arbitrary code on the server. This procedure specifically uses the List Files and Ping commands to achieve remote code execution with Java.

The business value of this attack lies in the potential for attackers to gain access to sensitive data or systems, which can lead to financial loss, reputational damage, and legal consequences for the affected organization. It is therefore important for organizations to be aware of this attack vector and take appropriate measures to protect their web applications and servers.

 

## Requirements

1. Access to a vulnerable web application with XSLT Injection vulnerability

1. Knowledge of the List Files and Ping commands

1. Access to the target network

 

## Defense

1. Implement input validation and output encoding to prevent XSLT Injection

1. Use a web application firewall (WAF) to detect and block XSLT Injection attacks

1. Regularly update and patch web applications and servers to address known vulnerabilities

 

## Objectives

1. Execute Java code remotely

1. Take control of the server

1. Steal sensitive data

1. Install malware

1. Launch further attacks

 

# Instructions

1. This command is used to list all the files in a directory.

 



**Code**: [[  <xsl:stylesheet version="1.0" xmlns:xsl="http://]]



> The 'ls' command is executed using the 'Runtime' class of Java. The output of the command is then converted to a string using the 'Object' class of Java. The list of files is then returned as a string.

2. This command is used to check the connectivity between two devices over a network using the ping utility.

 



**Code**: [[<xml version="1.0"?>
<xsl:stylesheet version="2.0"]]



> The ping command sends an ICMP (Internet Control Message Protocol) echo request to the destination IP address and waits for a response. If the destination device is reachable, it responds with an ICMP echo reply. The arguments of the command are:
1. IP: The IP address or hostname of the device to which the ping request is to be sent. It can be IPv4 or IPv6 address.

Example: ping 192.168.1.1

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]
- [[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]

## Tags

- [[Exploit]]
- [[Remote Code Execution with Java]]
- [[XSLT Injection]]



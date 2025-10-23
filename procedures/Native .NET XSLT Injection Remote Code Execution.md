---
id: dadae9c9-4ed9-4465-86f5-e095ad1cb528
name: Native .NET XSLT Injection Remote Code Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:41.609783+00:00'
updated_at: '2023-04-10T20:24:49.991979+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[XSL Script Processing|T1220 - XSL Script Processing]]'
tags:
- '[[Exploit]]'
- '[[Remote Code Execution with Native .NET]]'
- '[[XSLT Injection]]'
---

# Native .NET XSLT Injection Remote Code Execution

## Summary

XSLT Injection is a type of injection attack that targets web applications utilizing XML and XSLT to transform XML data into HTML. This exploit utilizes XSLT Injection to execute arbitrary code on the server using Native .NET libraries. The attacker can use this technique to bypass security control

## Description

# Description

XSLT Injection is a type of injection attack that targets web applications utilizing XML and XSLT to transform XML data into HTML. This exploit utilizes XSLT Injection to execute arbitrary code on the server using Native .NET libraries. The attacker can use this technique to bypass security controls and gain remote access to the targeted system. By injecting malicious code into the XSLT stylesheet, the attacker can execute arbitrary code on the server, allowing them to take control of the system, steal sensitive data, or move laterally within the network.

Technical Explanation: An attacker can use XSLT Injection to modify the XSLT stylesheet to include arbitrary code. When the XML data is transformed using the malicious XSLT stylesheet, the code is executed on the server. This technique can be used to gain remote code execution on the server using Native .NET libraries.

Business Value: This attack can lead to a complete compromise of the targeted system, resulting in data theft, system downtime, and loss of business reputation. By gaining remote access to the system, the attacker can also move laterally within the network, potentially compromising other systems and data.

 

## Requirements

1. Access to the targeted web application

1. Knowledge of XSLT Injection techniques

1. Access to Native .NET libraries

 

## Defense

1. Implement input validation and sanitization to prevent XSLT Injection attacks

1. Implement least privilege access controls to limit the impact of a successful attack

1. Regularly monitor and audit system logs for suspicious activity

 

## Objectives

1. Execute arbitrary code on the targeted system

1. Gain remote access to the targeted system

1. Steal sensitive data

1. Move laterally within the network

 

# Instructions

1. Transforms an XML document into an HTML table using XSLT.

 



**Code**: [[<xsl:stylesheet version="1.0" xmlns:xsl="http://ww]]



> This command takes an XML document and applies an XSLT stylesheet to it to transform the data into an HTML table. The stylesheet is defined in the 'data' field of the JSON object. The resulting HTML table can be used to display the data in a more user-friendly format. The 'lang' field specifies the language of the data and the 'text' field can be used to provide additional information about the data being transformed. The 'instruction' field can be used to provide additional instructions on how to use this command. The 'explain' field can be used to explain the arguments of the command in detail.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[XSL Script Processing|T1220 - XSL Script Processing]]

## Tags

- [[Exploit]]
- [[Remote Code Execution with Native .NET]]
- [[XSLT Injection]]



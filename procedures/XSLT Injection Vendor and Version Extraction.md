---
id: 38d65acf-8234-4ffc-b4bd-6ee6dcd11626
name: XSLT Injection Vendor and Version Extraction
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:41.460340+00:00'
updated_at: '2023-04-10T20:24:48.976986+00:00'
tags:
- '[[Determine the vendor and version]]'
- '[[Exploit]]'
- '[[XSLT Injection]]'
---

# XSLT Injection Vendor and Version Extraction

## Summary

XSLT Injection is a type of web vulnerability that allows an attacker to inject malicious code into an XSLT stylesheet. By doing so, the attacker can execute arbitrary code on the server or manipulate the output of the application. The 'Extract Vendor Information from XML' and 'XSL Version Informat

## Description

# Description

XSLT Injection is a type of web vulnerability that allows an attacker to inject malicious code into an XSLT stylesheet. By doing so, the attacker can execute arbitrary code on the server or manipulate the output of the application. The 'Extract Vendor Information from XML' and 'XSL Version Information' commands can be used to determine the vendor and version of the XSLT processor in use. This information can be used to tailor subsequent attacks or to determine if a known vulnerability can be exploited. 

Technical Explanation: XSLT Injection occurs when an attacker is able to inject malicious code into an XSLT stylesheet. This can be done through user input or by modifying the application's request parameters. Once the malicious code is executed, the attacker can manipulate the output of the application or execute arbitrary code on the server. The 'Extract Vendor Information from XML' and 'XSL Version Information' commands can be used to determine the vendor and version of the XSLT processor in use. 

Business Value: By exploiting XSLT Injection vulnerabilities, an attacker can access sensitive data or execute arbitrary code on the server. This can result in data theft, system compromise, and reputational damage to the organization.

## Requirements

1. Access to the application

1. Knowledge of XSLT Injection

## Defense

1. Input validation and sanitization should be implemented to prevent XSLT Injection vulnerabilities

1. Regular patching and updates of the XSLT processor should be performed to mitigate known vulnerabilities

1. Web application firewalls (WAFs) can be used to detect and block XSLT Injection attacks

## Objectives

1. Determine the vendor and version of the XSLT processor in use

1. Tailor subsequent attacks based on the vendor and version information

1. Determine if a known vulnerability can be exploited

# Instructions

1. This command extracts vendor information from an XML file using XSLT.

**Code**: [[<?xml version="1.0" encoding="utf-8"?>
<xsl:styles]]

> The XSLT stylesheet in the 'data' field is used to transform an input XML file. The 'system-property' function is used to extract the vendor information of the XSLT processor being used. The 'match' attribute in the 'xsl:template' element specifies the root element of the input XML file. The 'select' attribute in the 'xsl:value-of' element specifies the function to extract the vendor information. This command requires an input XML file and an XSLT processor that supports the 'system-property' function.

2. system-property

**Code**: [[<?xml version="1.0" encoding="UTF-8"?>
<html xsl:v]]

> This command is used to retrieve the version information of the XSLT processor. The 'system-property' function is used to retrieve the specified system property value. In this case, 'xsl:version', 'xsl:vendor' and 'xsl:vendor-url' are retrieved to display the version, vendor and vendor URL of the XSLT processor respectively.

## Tags

- [[Determine the vendor and version]]
- [[Exploit]]
- [[XSLT Injection]]

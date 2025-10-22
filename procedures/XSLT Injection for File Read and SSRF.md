---
id: 8ad33483-e45a-4ead-8d27-9346f3b97c86
name: XSLT Injection for File Read and SSRF
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:41.497456+00:00'
updated_at: '2023-04-10T20:24:50.379204+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Data from Information Repositories|T1213 - Data from Information Repositories]]'
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Exploit]]'
- '[[Read files and SSRF using document]]'
- '[[XSLT Injection]]'
---

# XSLT Injection for File Read and SSRF

## Summary

XSLT Injection is an attack technique used to inject malicious code into XSLT (Extensible Stylesheet Language Transformations) files, which are used to transform XML data into other formats such as HTML, PDF, or plain text. This specific procedure focuses on using XSLT Injection to read files and p

## Description

# Description

XSLT Injection is an attack technique used to inject malicious code into XSLT (Extensible Stylesheet Language Transformations) files, which are used to transform XML data into other formats such as HTML, PDF, or plain text. This specific procedure focuses on using XSLT Injection to read files and perform Server Side Request Forgery (SSRF) attacks. An attacker can use this technique to read sensitive files on the server or perform actions on behalf of the server. This attack can be carried out by sending specially crafted XML data to the server, which gets processed by the XSLT file. By injecting malicious code into the XSLT file, an attacker can control the output and perform unauthorized actions.

## Requirements

1. Access to a vulnerable application that uses XSLT files

1. Knowledge of XSLT Injection techniques

## Defense

1. Validate and sanitize all user input to prevent injection attacks

1. Implement access controls to limit the actions that can be performed by the XSLT file

1. Monitor server logs for any suspicious activity related to XSLT files

## Objectives

1. Read sensitive files on the server

1. Perform actions on behalf of the server

1. Perform Server Side Request Forgery (SSRF) attacks

# Instructions

1. This command extracts the details of fruits using XSLT.

**Code**: [[<?xml version="1.0" encoding="utf-8"?>
<xsl:styles]]

> The command uses XSLT to extract the details of fruits from an XML file. The extracted details include the name and description of each fruit. The command also includes the details of documents from remote and local locations using the 'document()' function in XSLT. The extracted details are then printed in a formatted manner using the 'for-each' loop in XSLT.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Data from Information Repositories|T1213 - Data from Information Repositories]]
- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Tags

- [[Exploit]]
- [[Read files and SSRF using document]]
- [[XSLT Injection]]

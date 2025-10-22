---
id: d9531e80-acb1-4738-aa5d-55eab48e7e84
name: Lessjs Server Side Template Injection via Inline Import
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.992451+00:00'
updated_at: '2023-04-10T20:23:52.636123+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Impact|TA0040 - Impact]]'
techniques:
- '[[Data from Information Repositories|T1213 - Data from Information Repositories]]'
- '[[Password Policy Discovery|T1201 - Password Policy Discovery]]'
- '[[System Shutdown/Reboot|T1529 - System Shutdown/Reboot]]'
sub_techniques:
- '[[Confluence|T1213.001 - Confluence]]'
tags:
- '[[Lessjs]]'
- '[[Lessjs - SSRF / LFI]]'
- '[[Server Side Template Injection]]'
---

# Lessjs Server Side Template Injection via Inline Import

## Summary

Lessjs is a popular CSS pre-processor that allows developers to write CSS in a more efficient and modular way. It supports inline import of external files which can be used to import templates. However, this functionality can be abused to perform Server Side Template Injection (SSTI) attacks. This 

## Description

# Description

Lessjs is a popular CSS pre-processor that allows developers to write CSS in a more efficient and modular way. It supports inline import of external files which can be used to import templates. However, this functionality can be abused to perform Server Side Template Injection (SSTI) attacks. This can lead to the execution of arbitrary code on the server and can result in sensitive data leakage.

An attacker can exploit the SSTI vulnerability in Lessjs by injecting malicious code into the imported template. This can be done by using a combination of Server Side Request Forgery (SSRF) and Local File Inclusion (LFI) attacks. By exploiting these vulnerabilities, an attacker can gain access to sensitive data and take control of the server.

The business value of this attack is that it allows an attacker to gain unauthorized access to sensitive data and take control of the server, which can lead to a loss of reputation, financial loss, and legal repercussions.

## Requirements

1. Access to a server running Lessjs

1. Knowledge of Server Side Request Forgery (SSRF) and Local File Inclusion (LFI) attacks

1. Knowledge of Lessjs inline import functionality

## Defense

1. Disable inline import functionality in Lessjs

1. Implement input validation and sanitization to prevent injection attacks

1. Monitor server logs for suspicious activity

## Objectives

1. Perform Server Side Template Injection (SSTI) attacks on a server running Lessjs

1. Gain unauthorized access to sensitive data

1. Take control of the server

# Instructions

1. Use the @import (inline) command to import a file directly into your Less file.

**Code**: [[@import (inline) "http://localhost";
// or
@import]]

> This command allows you to import a file directly into your Less file. The imported file will be included in the compiled CSS output. The 'inline' keyword specifies that the file should be included in the compiled CSS rather than being imported as a separate file. The argument to the command should be a valid URL or file path. This command is useful when you need to include small snippets of code from other files in your Less file.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Discovery|TA0007 - Discovery]]
- [[Impact|TA0040 - Impact]]

### Techniques

- [[Data from Information Repositories|T1213 - Data from Information Repositories]]
- [[Password Policy Discovery|T1201 - Password Policy Discovery]]
- [[System Shutdown/Reboot|T1529 - System Shutdown/Reboot]]

### Sub-Techniques

- [[Confluence|T1213.001 - Confluence]]

## Tags

- [[Lessjs]]
- [[Lessjs - SSRF / LFI]]
- [[Server Side Template Injection]]

---
id: 1a33bd28-c386-4065-8454-0bf59d529f37
name: Msbuild Preprocessing Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:26.997407+00:00'
updated_at: '2023-04-10T20:37:08.901686+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Trusted Developer Utilities|T1127 - Trusted Developer Utilities]]'
sub_techniques:
- '[[MSBuild|T1127.001 - MSBuild]]'
tags:
- '[[Msbuild]]'
- '[[Windows - Download and execute methods]]'
---

# Msbuild Preprocessing Execution

## Summary

Msbuild is a trusted developer utility that can be used to download and execute files. An attacker can use Msbuild to bypass application whitelisting solutions and execute malicious payloads. This technique involves preprocessing the Msbuild XML file to include the payload in base64 format. When Ms

## Description

# Description

Msbuild is a trusted developer utility that can be used to download and execute files. An attacker can use Msbuild to bypass application whitelisting solutions and execute malicious payloads. This technique involves preprocessing the Msbuild XML file to include the payload in base64 format. When Msbuild runs, it decodes the payload and executes it. This technique is commonly used in targeted attacks to gain initial access to a network.

Technical Description: An attacker can use Msbuild to download and execute files by preprocessing the XML file to include the payload in base64 format. The payload is then decoded and executed when Msbuild runs. This technique can bypass application whitelisting solutions and is commonly used in targeted attacks.

Business Value: This technique can be used to gain initial access to a network and bypass application whitelisting solutions. This can allow an attacker to steal sensitive data, install malware or ransomware, and cause significant damage to the target organization.

## Requirements

1. Access to a target system with Msbuild installed

1. Permissions to execute Msbuild

1. A payload to download and execute

## Defense

1. Implement application whitelisting solutions to prevent unauthorized applications from running

1. Monitor Msbuild for suspicious activity

1. Use anti-malware and endpoint detection and response (EDR) solutions to detect and respond to attacks

## Objectives

1. Download and execute a payload on a target system

1. Bypass application whitelisting solutions

1. Gain initial access to a network

# Instructions

1. This command executes MSBuild.exe to preprocess a specified XML file and outputs the result to a new file named payload.xml.

**Code**: [[cmd /V /c "set MB="C:\Windows\Microsoft.NET\Framew]]

> The argument /noautoresponse disables automatic responses to prompts during the build process. The argument /preprocess specifies that the XML file should be preprocessed. The argument \\webdavserver\folder\payload.xml specifies the location of the input XML file. The output is redirected to a new file named payload.xml. The final argument !MB! payload.xml specifies that the preprocessed XML file should be built using MSBuild.exe.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Trusted Developer Utilities|T1127 - Trusted Developer Utilities]]

### Sub-Techniques

- [[MSBuild|T1127.001 - MSBuild]]

## Tags

- [[Msbuild]]
- [[Windows - Download and execute methods]]

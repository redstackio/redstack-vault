---
id: b4f853ce-5e18-42ad-bbc2-3d8dc90232d4
name: Gitrob Secret Harvesting
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:00.178891+00:00'
updated_at: '2023-04-10T20:33:53.849246+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
- '[[Credentials In Files|T1552.001 - Credentials In Files]]'
tags:
- '[[Git]]'
- '[[Gitrob]]'
- '[[Harvesting secrets]]'
- '[[Insecure Source Code Management]]'
- '[[Tools]]'
---

# Gitrob Secret Harvesting

## Summary

Gitrob is a tool used to find sensitive information such as passwords, API keys, and other secrets in a target organization's public and private GitHub repositories. The tool can be used to identify and help remediate insecure source code management practices. By harvesting secrets from public and 

## Description

# Description

Gitrob is a tool used to find sensitive information such as passwords, API keys, and other secrets in a target organization's public and private GitHub repositories. The tool can be used to identify and help remediate insecure source code management practices. By harvesting secrets from public and private repositories, attackers can gain access to sensitive data and systems that rely on that data. Gitrob can also be used by defenders to identify and remediate these issues before attackers can exploit them.

## Requirements

1. Access to the target organization's GitHub repositories.

1. Gitrob tool installed on the attacker's system.

## Defense

1. Ensure that sensitive information is not stored in public GitHub repositories.

1. Implement access controls and monitoring to detect and prevent unauthorized access to GitHub repositories.

1. Regularly scan GitHub repositories for sensitive information and remediate any issues found.

## Objectives

1. Identify sensitive information in public and private GitHub repositories.

1. Remediate insecure source code management practices.

# Instructions

1. To use Gitrob, first install the tool using the command 'go get github.com/michenriksen/gitrob'. Then, set the GITROB_ACCESS_TOKEN environment variable to a valid GitHub access token. Finally, run the command 'gitrob' followed by the target organization's GitHub repositories.

**Code**: [[go get github.com/michenriksen/gitrob # https://gi]]

> The 'gitrob' command will scan the specified GitHub repositories for sensitive information such as passwords, API keys, and other secrets. The tool will output a report of any findings and provide guidance on how to remediate any issues found.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Unsecured Credentials|T1552 - Unsecured Credentials]]

### Sub-Techniques

- [[Credentials In Files|T1552.001 - Credentials In Files]]

## Tags

- [[Git]]
- [[Gitrob]]
- [[Harvesting secrets]]
- [[Insecure Source Code Management]]
- [[Tools]]

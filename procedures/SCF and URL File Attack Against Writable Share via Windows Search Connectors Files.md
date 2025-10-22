---
id: f38f7724-0f30-46e6-892a-305cdc3946db
name: SCF and URL File Attack Against Writable Share via Windows Search Connectors
  Files
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:03.478611+00:00'
updated_at: '2023-04-10T20:26:08.872977+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Drive-by Compromise|T1189 - Drive-by Compromise]]'
- '[[User Execution|T1204 - User Execution]]'
tags:
- '[[Active Directory Attacks]]'
- '[[SCF and URL file attack against writeable share]]'
- '[[Windows Search Connectors Files]]'
---

# SCF and URL File Attack Against Writable Share via Windows Search Connectors Files

## Summary

This procedure involves creating a Windows Search Connector file (.searchconnector-ms) that points to a malicious SCF or URL file hosted on a writable share. When a user clicks on the search connector file, it will automatically execute the SCF or URL file, which can lead to code execution or the t

## Description

# Description

This procedure involves creating a Windows Search Connector file (.searchconnector-ms) that points to a malicious SCF or URL file hosted on a writable share. When a user clicks on the search connector file, it will automatically execute the SCF or URL file, which can lead to code execution or the theft of sensitive information. This attack can be used as a phishing technique to trick users into executing the malicious file or as a way to escalate privileges on a compromised system.

Technical Explanation: Windows Search Connectors are XML files that allow users to search for specific types of content on the internet or on their local machine. These files can be created with a simple text editor and can be pointed to any URL or file on the web or on a local network share. SCF and URL files are special file types in Windows that can execute commands when opened.

Business Value: This attack can be used to gain access to sensitive information or to escalate privileges on a compromised system. It can also be used as a way to deliver malware to a target system.

## Requirements

1. Access to a writable share

1. Ability to create a Windows Search Connector file

1. Ability to host a malicious SCF or URL file

## Defense

1. Disable Windows Search Connectors on all systems

1. Monitor network traffic for suspicious activity

1. Educate users on the dangers of opening files from untrusted sources

## Objectives

1. Gain access to sensitive information

1. Escalate privileges on a compromised system

1. Deliver malware to a target system

# Instructions

1. This command creates a search connector for Microsoft Outlook

**Code**: [[<?xml version="1.0" encoding="UTF-8"?>
<searchConn]]

> The 'data' field contains the XML code necessary to create the search connector for Microsoft Outlook. The 'lang' field specifies the language used in the XML code. The 'instruction' field provides instructions on how to use this command. The 'explain' field provides additional details on what this command does.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Drive-by Compromise|T1189 - Drive-by Compromise]]
- [[User Execution|T1204 - User Execution]]

## Tags

- [[Active Directory Attacks]]
- [[SCF and URL file attack against writeable share]]
- [[Windows Search Connectors Files]]

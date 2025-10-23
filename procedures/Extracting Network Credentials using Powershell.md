---
id: 8e7c2cf7-d471-4d6a-b7af-605068e4fb9a
name: Extracting Network Credentials using Powershell
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:24.121898+00:00'
updated_at: '2023-04-10T20:37:01.443059+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credentials from Password Stores|T1555 - Credentials from Password Stores]]'
- '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
- '[[Credentials In Files|T1552.001 - Credentials In Files]]'
tags:
- '[[Powershell]]'
- '[[Secure String to Plaintext]]'
---

# Extracting Network Credentials using Powershell

## Summary

This procedure uses Powershell to extract network credentials from a secure string to plaintext. The attacker can then use these credentials to gain unauthorized access to the network. This technique is commonly used in post-exploitation scenarios where the attacker has already gained a foothold on

## Description

# Description

This procedure uses Powershell to extract network credentials from a secure string to plaintext. The attacker can then use these credentials to gain unauthorized access to the network. This technique is commonly used in post-exploitation scenarios where the attacker has already gained a foothold on the network.

To extract the credentials, the attacker first needs to obtain the secure string. This can be done by using various techniques such as keylogging, phishing, or using a tool like Mimikatz. Once the secure string is obtained, the attacker can use Powershell to convert it to plaintext. This can then be used to authenticate to various network resources.

The business value of this procedure is that it allows an attacker to gain access to sensitive information and resources on the network, potentially leading to data theft or other malicious activities.

 

## Requirements

1. Access to a system with Powershell installed

1. Access to a secure string containing network credentials

 

## Defense

1. Use strong and unique passwords to make it harder for attackers to obtain network credentials

1. Implement two-factor authentication to make it harder for attackers to use stolen credentials

1. Monitor network traffic for suspicious activity, such as multiple failed login attempts

 

## Objectives

1. Extract network credentials from a secure string

1. Convert the secure string to plaintext

1. Use the extracted credentials to gain unauthorized access to the network

 

# Instructions

1. This command retrieves the network credentials of the user 'Tom' using PowerShell. 

To use this command, replace 'Tom' with the appropriate username and the encrypted password string in the $pass variable with the actual password. Then run the command in a PowerShell window.

 



**Code**: [[$pass = "01000000d08c9ddf0115d1118c7a00c04fc297eb0]]



> - $pass: This variable contains the encrypted password string of the user.
- $user: This variable contains the username of the user.
- $cred: This variable creates a new PSCredential object that stores the username and password.
- $cred.GetNetworkCredential(): This command retrieves the network credentials of the user and returns a formatted list of the user's username, password, secure password, and domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credentials from Password Stores|T1555 - Credentials from Password Stores]]
- [[Unsecured Credentials|T1552 - Unsecured Credentials]]

### Sub-Techniques

- [[Credentials In Files|T1552.001 - Credentials In Files]]

## Tags

- [[Powershell]]
- [[Secure String to Plaintext]]



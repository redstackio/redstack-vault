---
id: 85d70eef-9f15-4d84-9c77-5f8bbb817826
name: Windows Privilege Escalation via IIS Web Config Looting
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:29.125084+00:00'
updated_at: '2023-04-10T20:37:44.551157+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Access Token Manipulation|T1134 - Access Token Manipulation]]'
- '[[Password Filter DLL|T1174 - Password Filter DLL]]'
tags:
- '[[EoP - Looting for passwords]]'
- '[[IIS Web config]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[Find Web.Config files in the C:\inetpub\ directory]]'
---

# Windows Privilege Escalation via IIS Web Config Looting

## Summary

This procedure involves looting the IIS web configuration files to find stored passwords that can be used to escalate privileges on a Windows system. This technique is commonly used by attackers who have already gained a foothold on a system and are looking to expand their access. By accessing the 

## Description

# Description

This procedure involves looting the IIS web configuration files to find stored passwords that can be used to escalate privileges on a Windows system. This technique is commonly used by attackers who have already gained a foothold on a system and are looking to expand their access. By accessing the web configuration files, an attacker can find stored passwords for various services and applications, including the Windows operating system itself.

Technical Explanation: IIS web configuration files are XML files that contain settings and configuration information for web applications. These files can also contain plaintext passwords for various services and applications. By accessing these files, an attacker can obtain passwords that can be used to escalate privileges on the system.

Business Value: This technique is valuable for attackers as it allows them to gain higher levels of access and control over a compromised system. By escalating privileges, an attacker can gain access to sensitive data, install malware, or perform other malicious activities.

## Requirements

1. Access to a Windows system running IIS

1. Ability to read and modify web configuration files

1. Knowledge of the location of web configuration files on the system

## Defense

1. Regularly review and update web configuration files to remove any stored passwords

1. Implement strong password policies and use password managers to prevent the storage of plaintext passwords

1. Monitor system logs for any suspicious activity related to web configuration files or privilege escalation

## Objectives

1. Find and loot IIS web configuration files

1. Identify stored passwords for various services and applications

1. Use looted passwords to escalate privileges on a Windows system

# Instructions

1. To retrieve all web configuration files in the C:\inetpub\ directory and its subdirectories, run the following command:

**Code**: [[Get-Childitem –Path C:\inetpub\ -Include web.confi]]

> This command uses the Get-Childitem cmdlet to search for all files named web.config in the C:\inetpub\ directory and its subdirectories. The -File parameter ensures that only files are returned, and the -Recurse parameter ensures that the search is performed recursively. The -ErrorAction parameter with the value SilentlyContinue suppresses any errors that may occur during the search.

**Command** ([[Find Web.Config files in the C:\inetpub\ directory]]):

```bash
Get-Childitem –Path C:\inetpub\ -Include web.config -File -Recurse -ErrorAction SilentlyContinue
```

2. To view or edit web.config files, use the following commands:
- View: Get-Content <file_path>
- Edit: Set-Content <file_path> <new_content>

**Code**: [[C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Co]]

> The web.config file is an XML file used by ASP.NET applications to store configuration settings. It contains settings such as database connection strings, authentication settings, and application-specific settings. To view the contents of a web.config file, use the Get-Content command followed by the file path. To edit the contents of a web.config file, use the Set-Content command followed by the file path and the new content to be added.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Access Token Manipulation|T1134 - Access Token Manipulation]]
- [[Password Filter DLL|T1174 - Password Filter DLL]]

## Commands Used

- [[Find Web.Config files in the C:\inetpub\ directory]]

## Tags

- [[EoP - Looting for passwords]]
- [[IIS Web config]]
- [[Windows - Privilege Escalation]]

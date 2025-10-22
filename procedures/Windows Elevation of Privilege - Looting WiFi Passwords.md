---
id: 8f5b70fa-da75-4d81-b342-b136fd6183db
name: Windows Elevation of Privilege - Looting WiFi Passwords
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:29.178716+00:00'
updated_at: '2023-04-10T20:37:43.111762+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Credentials in Files|T1081 - Credentials in Files]]'
- '[[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]'
tags:
- '[[EoP - Looting for passwords]]'
- '[[Wifi passwords]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[List all Wi-Fi profiles]]'
- '[[Show Wi-Fi Profile Key]]'
---

# Windows Elevation of Privilege - Looting WiFi Passwords

## Summary

This procedure aims to escalate privileges on a Windows machine in order to loot Wi-Fi passwords. By exploiting a privilege escalation vulnerability or retrieving credentials stored in files, an attacker can gain access to the Wi-Fi passwords in clear text. This can be useful for lateral movement a

## Description

# Description

This procedure aims to escalate privileges on a Windows machine in order to loot Wi-Fi passwords. By exploiting a privilege escalation vulnerability or retrieving credentials stored in files, an attacker can gain access to the Wi-Fi passwords in clear text. This can be useful for lateral movement and persistence on the network. From a technical perspective, this procedure involves identifying and exploiting a vulnerability or misconfiguration in the Windows system to gain elevated privileges. Once elevated, the attacker can retrieve the Wi-Fi passwords from the system files. The business value of this procedure is that it can be used to gain access to sensitive information, move laterally through the network, and maintain persistence.

## Requirements

1. Access to a Windows machine

1. Privilege escalation vulnerability or credentials stored in files

## Defense

1. Regularly apply security patches and updates to Windows systems

1. Use strong passwords and avoid storing them in files

1. Monitor network traffic for signs of privilege escalation and credential theft

## Objectives

1. Escalate privileges on a Windows machine

1. Retrieve Wi-Fi passwords in clear text

# Instructions

1. This command lists all the wireless network names (SSIDs) that the computer has connected to in the past.

**Code**: [[netsh wlan show profile]]

> The 'netsh wlan show profile' command is used to display a list of all the wireless network profiles that have been saved on a Windows computer. These profiles include the SSID (network name), authentication and encryption methods, and other settings that were used to connect to the network. This command can be useful for troubleshooting wireless connectivity issues or for identifying networks that the computer has connected to in the past.

**Command** ([[List all Wi-Fi profiles]]):

```bash
netsh wlan show profile
```

2. To retrieve the Wi-Fi password in clear text, run the following command in Command Prompt:

netsh wlan show profile <SSID> key=clear

Replace <SSID> with the name of the Wi-Fi network you want to retrieve the password for.

**Code**: [[netsh wlan show profile <SSID> key=clear]]

> This command will show you the Wi-Fi password in clear text for the specified network. It is useful if you need to connect to the Wi-Fi network on another device or if you need to troubleshoot issues with the network. Note that this command requires administrative privileges to run.

**Command** ([[Show Wi-Fi Profile Key]]):

```bash
netsh wlan show profile <SSID> key=clear
```

3. This command extracts WiFi passwords from all the access points on your device using a one-liner method.

**Code**: [[cls & echo. & for /f "tokens=4 delims=: " %a in (']]

> The command first clears the command prompt screen using the 'cls' command. It then uses the 'for' loop to iterate over all the WiFi profiles on the device. The 'netsh wlan show profiles' command is used to show all the WiFi profiles on the device. The 'find' command is used to filter out the relevant profiles. The 'netsh wlan show profiles name=%a key=clear' command is then used to show the details of each profile. The 'findstr' command is used to filter out the relevant details, which include the SSID, cipher, and content. The 'find' command is used to remove any lines with the word 'Number'. Finally, the 'echo' command is used to display the details of each profile, including the password.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Credentials in Files|T1081 - Credentials in Files]]
- [[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]

## Commands Used

- [[List all Wi-Fi profiles]]
- [[Show Wi-Fi Profile Key]]

## Tags

- [[EoP - Looting for passwords]]
- [[Wifi passwords]]
- [[Windows - Privilege Escalation]]

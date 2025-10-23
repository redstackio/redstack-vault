---
id: 8591115a-e5d6-44fc-86b5-8517110cd6a9
name: PrintNightmare Remote Code Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:02.835028+00:00'
updated_at: '2023-04-10T20:25:51.521195+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Remote Services|T1021 - Remote Services]]'
tags:
- '[[Active Directory Attacks]]'
- '[[From CVE to SYSTEM shell on DC]]'
- '[[PrintNightmare]]'
commands:
- '[[Clone ItWasAllADream Repository]]'
- '[[Install Dependencies and Activate Virtual Environment]]'
- '[[RPCDump with egrep filter on MS-RPRN and MS-PAR]]'
- '[[Run ItWasAllADream Tool in Docker Container]]'
- '[[Run ItWasAllADream Tool Locally]]'
---

# PrintNightmare Remote Code Execution

## Summary

This procedure details the exploitation of a vulnerability in the Windows Print Spooler service, known as PrintNightmare, to achieve remote code execution on a target system. By sending specially crafted print jobs to a vulnerable print spooler service, an attacker can execute arbitrary code with S

## Description

# Description

This procedure details the exploitation of a vulnerability in the Windows Print Spooler service, known as PrintNightmare, to achieve remote code execution on a target system. By sending specially crafted print jobs to a vulnerable print spooler service, an attacker can execute arbitrary code with SYSTEM privileges. This technique can be used to gain access to sensitive data, move laterally through a network, or establish persistent access to a compromised system. 

Technical Explanation: The PrintNightmare vulnerability allows an attacker to execute arbitrary code with SYSTEM privileges by sending specially crafted print jobs to a vulnerable print spooler service. This vulnerability is caused by the mishandling of RPC calls by the Windows Print Spooler service. An attacker can exploit this vulnerability by sending a malicious print job to a vulnerable print spooler service, which will execute the code with SYSTEM privileges. 

Business Value: This technique can be used to gain access to sensitive data, move laterally through a network, or establish persistent access to a compromised system. By gaining SYSTEM privileges, an attacker can take complete control of a compromised system and perform any action they desire.

 

## Requirements

1. Access to the target system

1. Vulnerable Print Spooler service

 

## Defense

1. Ensure that all systems are patched with the latest security updates

1. Disable the Windows Print Spooler service if it is not needed

1. Monitor network traffic for suspicious activity related to print jobs

 

## Objectives

1. Gain remote code execution on a target system

1. Execute arbitrary code with SYSTEM privileges

 

# Instructions

1. To use the Remote Print System Protocol, run the 'rpcdump.py' script with the IP address of the remote system as an argument. Use the 'egrep' command to filter the output for the 'MS-RPRN' and 'MS-PAR' protocols.

 



**Code**: [[python3 ./rpcdump.py @10.0.2.10 | egrep 'MS-RPRN|M]]



> The 'rpcdump.py' script is part of the Impacket toolkit and is used to dump the remote procedure call (RPC) interface information for a specified host. The 'MS-RPRN' protocol is used for managing printer resources, while the 'MS-PAR' protocol is used for managing parallel ports. By using the 'egrep' command, we can filter the output to show only the information related to these protocols.



**Command** ([[RPCDump with egrep filter on MS-RPRN and MS-PAR]]):

```bash
python3 ./rpcdump.py @10.0.2.10 | egrep 'MS-RPRN|MS-PAR'
```



2. This command is used to run the `It Was All A Dream` tool, which is a network enumeration and attack tool. The `git clone` command is used to download the tool from the GitHub repository. The `cd` command is used to navigate to the tool's directory, followed by `poetry install` and `poetry shell` commands to install and activate the tool's dependencies. The `itwasalladream` command is used to run the tool with the specified arguments. Finally, the `docker run` command is used to run the tool in a Docker container.

 



**Code**: [[git clone https://github.com/byt3bl33d3r/ItWasAllA]]



> The `itwasalladream` command has the following arguments:
- `-u user`: Specifies the username to use for authentication
- `-p Password123`: Specifies the password to use for authentication
- `-d domain`: Specifies the domain to target
- `10.10.10.10/24`: Specifies the IP address range to scan

The tool is used for network enumeration and attack, and can be used to perform tasks such as port scanning, DNS enumeration, and password spraying.



**Command** ([[Clone ItWasAllADream Repository]]):

```bash
git clone https://github.com/byt3bl33d3r/ItWasAllADream
```





**Command** ([[Install Dependencies and Activate Virtual Environment]]):

```bash
cd ItWasAllADream && poetry install && poetry shell
```





**Command** ([[Run ItWasAllADream Tool Locally]]):

```bash
itwasalladream -u user -p Password123 -d domain 10.10.10.10/24
```





**Command** ([[Run ItWasAllADream Tool in Docker Container]]):

```bash
docker run -it itwasalladream -u username -p Password123 -d domain 10.10.10.10
```



## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Remote Services|T1021 - Remote Services]]

## Commands Used

- [[Clone ItWasAllADream Repository]]
- [[Install Dependencies and Activate Virtual Environment]]
- [[RPCDump with egrep filter on MS-RPRN and MS-PAR]]
- [[Run ItWasAllADream Tool in Docker Container]]
- [[Run ItWasAllADream Tool Locally]]

## Tags

- [[Active Directory Attacks]]
- [[From CVE to SYSTEM shell on DC]]
- [[PrintNightmare]]



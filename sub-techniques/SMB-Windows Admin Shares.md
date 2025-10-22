---
id: 26a496d9-be0d-48c1-90f4-8ff2618c1da8
name: SMB/Windows Admin Shares
type: sub-technique
mitre_id: T1021.002
mitre_url: null
created_at: '2023-04-06T00:31:26.076825+00:00'
updated_at: '2023-04-06T00:31:26.076825+00:00'
parent_technique: '[[Remote Services|T1021 - Remote Services]]'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
procedures:
- '[[DCOM Lateral Movement]]'
- '[[DCOM Office Remote Code Execution]]'
- '[[DCOM ShellBrowserWindow Calculator Execution]]'
- '[[DCOM ShellExecute Calculator Execution]]'
- '[[Go Application Proxification with Graftcp]]'
- '[[Inter-User Messaging]]'
- '[[Linked Database Column Extraction]]'
- '[[Linux Reverse Shell Persistence with Ncat]]'
- '[[Network Pivoting with plink Port Forwarding]]'
- '[[Ruby Bind Shell]]'
- '[[Subversion Source Code Disclosure]]'
- '[[WebDAV Relay Attack]]'
- '[[Windows - Impacket Psexec Remote Command Execution]]'
- '[[Windows Remote Share Connection]]'
- '[[Windows - SMBExec with Impacket for Command Execution]]'
---

# SMB/Windows Admin Shares

**MITRE ID**: T1021.002

**Parent Technique**: [[Remote Services|T1021 - Remote Services]]

This is a sub-technique of T1021 - Remote Services.

## Summary

Adversaries may use [Valid Accounts](https://attack.mitre.org/techniques/T1078) to interact with a remote network share using Server Message Block (SMB). The adversary may then perform actions as the logged-on user.

SMB is a file, printer, and serial port sharing protocol for Windows machines on th

## Description

Adversaries may use [Valid Accounts](https://attack.mitre.org/techniques/T1078) to interact with a remote network share using Server Message Block (SMB). The adversary may then perform actions as the logged-on user.

SMB is a file, printer, and serial port sharing protocol for Windows machines on the same network or domain. Adversaries may use SMB to interact with file shares, allowing them to move laterally throughout a network. Linux and macOS implementations of SMB typically use Samba.

Windows systems have hidden network shares that are accessible only to administrators and provide the ability for remote file copy and other administrative functions. Example network shares include `C$`, `ADMIN$`, and `IPC$`. Adversaries may use this technique in conjunction with administrator-level [Valid Accounts](https://attack.mitre.org/techniques/T1078) to remotely access a networked system over SMB,(Citation: Wikipedia Server Message Block) to interact with systems using remote procedure calls (RPCs),(Citation: TechNet RPC) transfer files, and run transferred binaries through remote Execution. Example execution techniques that rely on authenticated sessions over SMB/RPC are [Scheduled Task/Job](https://attack.mitre.org/techniques/T1053), [Service Execution](https://attack.mitre.org/techniques/T1569/002), and [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047). Adversaries can also use NTLM hashes to access administrator shares on systems with [Pass the Hash](https://attack.mitre.org/techniques/T1550/002) and certain configuration and patch levels.(Citation: Microsoft Admin Shares)

## Tactics

This sub-technique is used in the following tactics:

- [[Lateral Movement|TA0008 - Lateral Movement]]

## Related Procedures

There are 15 procedures using this sub-technique:

- [[DCOM Lateral Movement]]
- [[DCOM Office Remote Code Execution]]
- [[DCOM ShellBrowserWindow Calculator Execution]]
- [[DCOM ShellExecute Calculator Execution]]
- [[Go Application Proxification with Graftcp]]
- [[Inter-User Messaging]]
- [[Linked Database Column Extraction]]
- [[Linux Reverse Shell Persistence with Ncat]]
- [[Network Pivoting with plink Port Forwarding]]
- [[Ruby Bind Shell]]
- [[Subversion Source Code Disclosure]]
- [[WebDAV Relay Attack]]
- [[Windows - Impacket Psexec Remote Command Execution]]
- [[Windows Remote Share Connection]]
- [[Windows - SMBExec with Impacket for Command Execution]]

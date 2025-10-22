---
id: 493356a9-6dcf-40a4-bf7b-4ce777fdbd5e
name: Ghost Potato NTLM Relay Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:05.590680+00:00'
updated_at: '2023-04-10T20:26:35.416554+00:00'
tags:
- '[[Active Directory Attacks]]'
- '[[Ghost Potato - CVE-2019-1384]]'
- '[[Man-in-the-Middle attacks & relaying]]'
---

# Ghost Potato NTLM Relay Attack

## Summary

The Ghost Potato NTLM Relay Attack is a technique that allows an attacker to gain elevated privileges on a Windows machine by relaying authentication requests to a target machine. This technique takes advantage of a vulnerability in the Windows operating system (CVE-2019-1384) that allows an attack

## Description

# Description

The Ghost Potato NTLM Relay Attack is a technique that allows an attacker to gain elevated privileges on a Windows machine by relaying authentication requests to a target machine. This technique takes advantage of a vulnerability in the Windows operating system (CVE-2019-1384) that allows an attacker to impersonate the NT Authority System account. By relaying authentication requests to a target machine, an attacker can execute code with elevated privileges, giving them complete control over the target machine. This attack is particularly dangerous because it can be executed over the network, without the need for any user interaction.

## Requirements

1. Access to a Windows network

1. NTLMRelayX tool

## Defense

1. Enforce SMB signing to prevent relaying attacks

1. Use strong passwords and two-factor authentication to prevent credential theft

1. Deploy host-based intrusion detection systems to detect and respond to attacks in real-time

## Objectives

1. Gain elevated privileges on a Windows machine

1. Execute code with elevated privileges

1. Take complete control over a target machine

# Instructions

1. This command allows you to relay NTLM authentication to a target host. The --smb2support flag enables the use of SMB2 protocol. The --no-smb-server flag disables the SMB server functionality of ntlmrelayx. The --gpotato-startup flag specifies the executable to be run on the target host upon successful authentication.

**Code**: [[ntlmrelayx -smb2support --no-smb-server --gpotato-]]

> The ntlmrelayx tool is used for performing NTLM relay attacks. This command specifically enables the use of SMB2 protocol, disables the SMB server functionality of ntlmrelayx, and specifies the executable to be run on the target host upon successful authentication. The target host must have SMB2 enabled and the specified executable must be present on the target host. This command can be used for various purposes such as gaining access to a target host or executing code on a target host.

## Tags

- [[Active Directory Attacks]]
- [[Ghost Potato - CVE-2019-1384]]
- [[Man-in-the-Middle attacks & relaying]]

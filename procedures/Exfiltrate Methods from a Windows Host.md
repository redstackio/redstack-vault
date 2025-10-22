---
id: 26e892b4-b999-465a-b162-c0dd93ccafd0
name: Exfiltrate Methods from a Windows Host
type: procedure
verified: false
submitted: false
created_at: '2023-02-19T05:51:16.045851+00:00'
updated_at: '2023-03-13T19:52:35.078857+00:00'
---

# Exfiltrate Methods from a Windows Host

## Summary

Exfiltrating the results of a SharpHound scan from a Windows host can be done in various ways, depending on the tools and techniques available to the attacker. Some methods that an attacker might use to exfiltrate the data include: File transfer tools: An attacker might use file transfer tools such

## Description

# Description

Exfiltrating the results of a SharpHound scan from a Windows host can be done in various ways, depending on the tools and techniques available to the attacker. Some methods that an attacker might use to exfiltrate the data include:

1. File transfer tools: An attacker might use file transfer tools such as FTP, SCP, or SMB to transfer the SharpHound results file to a remote system under their control. This can be done manually, or via a script or tool that automates the transfer process.

1. Covert channels: An attacker might use a covert channel, such as a hidden HTTP or DNS tunnel, to exfiltrate the SharpHound results file from the Windows host. This can be done using tools such as PowerSploit, Covenant, or Cobalt Strike, which provide various built-in options for exfiltration over covert channels.

1. Data encoding: An attacker might encode the SharpHound results file into a different format, such as base64 or hex, in order to evade detection by security controls. The encoded file can then be transferred via a file transfer tool or covert channel, and then decoded on the attacker's system.

1. Data exfiltration via command and control (C2) channel: If the attacker has already established a command and control channel with the compromised system, they might use this channel to exfiltrate the SharpHound results file. This can be done using various C2 frameworks, such as Metasploit, Empire, or Cobalt Strike.

For large exfiltrations consider the effects of hibernation, a logged out user, a closed laptop lid. Can it be setup as a scheduled task or resumed dependent on your tooling.

## Objectives

It is important to note that exfiltrating data from a compromised system is a critical step in the attack process, and one that is often detected by security controls. Therefore, it is important to use techniques that are tailored to the specific target environment and that are designed to evade detection by security controls. Additionally, it is important to implement effective security controls, such as intrusion detection and prevention systems (IDPS) and endpoint detection and response (EDR) solutions, to detect and prevent exfiltration attempts.

1. Model what level of stealth is required for the engagement

 - Over a C2 channel

 - Binaries or tools that could be alerted on when executed

 - Network alerts:

    - DNS / Domain names / IP address

    - Types of protocols

    - Target port being used / What type of service the exfiltration is mimicking

    - Type of encryption (TLS)

 - Transfer size limit

 - Network medium? (Bluetooth, wifi) to a dropped box

 - To the cloud

2. If you are not using C2, find a tool with the capability to exfiltrate the data off the network

 - Living off the Land

 - Script

3. Initiate the data exfiltration

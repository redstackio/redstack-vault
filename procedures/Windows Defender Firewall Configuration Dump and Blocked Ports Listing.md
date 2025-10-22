---
id: 321ebadc-49e4-459e-b99a-f31406b259ce
name: Windows Defender Firewall Configuration Dump and Blocked Ports Listing
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:26.717242+00:00'
updated_at: '2023-04-10T20:37:05.957220+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Security Software Discovery|T1063 - Security Software Discovery]]'
- '[[System Network Configuration Discovery|T1016 - System Network Configuration Discovery]]'
tags:
- '[[Windows Defender Firewall]]'
- '[[Windows - Defenses]]'
commands:
- '[[Get Firewall Rules]]'
---

# Windows Defender Firewall Configuration Dump and Blocked Ports Listing

## Summary

The Windows Defender Firewall Configuration Dump and Blocked Ports Listing procedure involves dumping the configuration of the Windows Defender Firewall and listing all the blocked ports on the firewall. This procedure is useful for an attacker to discover the network topology and identify potentia

## Description

# Description

The Windows Defender Firewall Configuration Dump and Blocked Ports Listing procedure involves dumping the configuration of the Windows Defender Firewall and listing all the blocked ports on the firewall. This procedure is useful for an attacker to discover the network topology and identify potential targets. By listing the blocked ports, an attacker can identify which ports are not blocked and can be used to launch an attack. From a technical perspective, this procedure involves using the 'Firewall Configuration Dump' and 'List Blocked Ports on Firewall' commands to gather information. From a business perspective, this procedure can help an attacker identify vulnerabilities in the network and take appropriate measures to secure the network.

## Requirements

1. Access to a Windows machine with Windows Defender Firewall enabled

## Defense

1. Ensure that the Windows Defender Firewall is properly configured and all unnecessary ports are blocked

1. Use network segmentation to limit the attack surface

1. Implement proper access controls and authentication mechanisms to prevent unauthorized access to the network

## Objectives

1. Discover network topology

1. Identify potential targets

1. Identify vulnerabilities in the network

# Instructions

1. To view the current state and configuration of the firewall, run either of the following commands:

netsh advfirewall firewall dump

or

netsh firewall show state
netsh firewall show config

**Code**: [[netsh advfirewall firewall dump
# or 
netsh firewa]]

> These commands allow you to view the current state and configuration of the Windows Firewall. The 'netsh advfirewall firewall dump' command will display the complete configuration of the firewall in a format that can be easily imported to another system if necessary. The 'netsh firewall show state' and 'netsh firewall show config' commands will display the current state and configuration of the firewall respectively. These commands can be useful for troubleshooting firewall issues or verifying that the firewall is configured correctly.

2. To list the blocked ports on the firewall, run the following command in PowerShell:

**Code**: [[$f=New-object -comObject HNetCfg.FwPolicy2;$f.rule]]

> This PowerShell command uses the HNetCfg.FwPolicy2 COM object to retrieve a list of firewall rules where the action is set to block (action -eq "0"). The command then selects the name, application name, and local ports for each rule and displays them in the output. This information can be useful for troubleshooting network connectivity issues and configuring firewall rules.

**Command** ([[Get Firewall Rules]]):

```bash
$f=New-object -comObject HNetCfg.FwPolicy2;$f.rules |  where {$_.action -eq "0"} | select name,applicationname,localports
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Security Software Discovery|T1063 - Security Software Discovery]]
- [[System Network Configuration Discovery|T1016 - System Network Configuration Discovery]]

## Commands Used

- [[Get Firewall Rules]]

## Tags

- [[Windows Defender Firewall]]
- [[Windows - Defenses]]

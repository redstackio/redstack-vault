---
id: 1c5af038-0269-4c41-80be-113a420a6092
name: Windows Firewall and Antivirus Disabling
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:27.703274+00:00'
updated_at: '2023-04-10T20:37:20.836710+00:00'
tags:
- '[[Disable Antivirus and Security]]'
- '[[Disable Windows Firewall]]'
- '[[Windows - Persistence]]'
---

# Windows Firewall and Antivirus Disabling

## Summary

This procedure is used to disable the Windows Firewall and Antivirus software on a target machine. By disabling these security measures, the attacker can gain persistent access to the target machine and avoid detection by security software. This is achieved by modifying the registry keys and settin

## Description

# Description

This procedure is used to disable the Windows Firewall and Antivirus software on a target machine. By disabling these security measures, the attacker can gain persistent access to the target machine and avoid detection by security software. This is achieved by modifying the registry keys and settings related to the Windows Firewall and Antivirus software. The business value of this procedure is that it allows the attacker to maintain access to the target machine and potentially move laterally within the target network.

 

## Requirements

1. Administrator-level access to the target machine

1. Knowledge of the registry keys and settings related to the Windows Firewall and Antivirus software

 

## Defense

1. Regularly update and patch the Windows Firewall and Antivirus software to prevent known vulnerabilities

1. Implement network segmentation to limit the impact of a compromised machine

1. Monitor network traffic for suspicious activity and behavior

 

## Objectives

1. Disable Windows Firewall and Antivirus software on the target machine

1. Gain persistent access to the target machine

1. Avoid detection by security software

 

# Instructions

1. To protect your system from unauthorized access, follow these steps:
1. Run 'Netsh Advfirewall show allprofiles' to view the current firewall settings.
2. Run 'NetSh Advfirewall set allprofiles state off' to turn off the firewall for all profiles.
3. Whitelist specific IP addresses by running 'New-NetFirewallRule' command with the appropriate arguments. Replace 'ATTACKER_IP' with the IP address you want to whitelist.

 



**Code**: [[Netsh Advfirewall show allprofiles
NetSh Advfirewa]]



> The 'Netsh Advfirewall show allprofiles' command displays the current firewall settings for all profiles. The 'NetSh Advfirewall set allprofiles state off' command turns off the firewall for all profiles. The 'New-NetFirewallRule' command creates a new firewall rule to whitelist specific IP addresses. The '-Name' argument specifies the name of the rule, the '-Enabled' argument specifies whether the rule is enabled, the '-Direction' argument specifies the direction of the traffic to be allowed, the '-Protocol' argument specifies the protocol to be allowed, the '-Action' argument specifies the action to be taken for the traffic, the '-Profile' argument specifies the profile to which the rule applies, and the '-RemoteAddress' argument specifies the IP address to be whitelisted.

## Tags

- [[Disable Antivirus and Security]]
- [[Disable Windows Firewall]]
- [[Windows - Persistence]]



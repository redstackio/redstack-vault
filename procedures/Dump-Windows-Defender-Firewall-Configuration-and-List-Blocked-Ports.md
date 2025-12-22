---
type: procedure
verified: true
submitted: false
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/Security Software Discovery|T1063 - Security Software
    Discovery]]
  - >-
    [[techniques/System Network Configuration Discovery|T1016 - System Network
    Configuration Discovery]]
tags:
  - '[[tags/Windows Defender Firewall]]'
  - '[[tags/Windows - Defenses]]'
commands:
  - '[[commands/powershell-enumerate-blocked-firewall-rules]]'
platforms:
  - Windows
validated: true
---

# Dump-Windows-Defender-Firewall-Configuration-and-List-Blocked-Ports

## Summary

This procedure dumps the full configuration of the Windows Defender Firewall using netsh commands and enumerates blocked ports via PowerShell to discover active security policies, network restrictions, and potential open paths for lateral movement or exfiltration in a compromised Windows environment.

## Description

During the discovery phase of an attack, understanding the target's firewall configuration is crucial for mapping network topology, identifying blocked services, and finding exploitable gaps. This procedure uses built-in Windows tools—netsh for exporting the complete firewall policy (which includes inbound/outbound rules, profiles, and exceptions) and PowerShell's HNetCfg.FwPolicy2 COM object to query specifically for blocking rules. It targets Windows 10 and later systems where Windows Defender Firewall is enabled by default. The output reveals application-specific blocks, port restrictions, and overall policy, helping attackers assess risks like unnecessary open ports or misconfigurations. No external tools are required, making it stealthy for early reconnaissance post-initial access.

## Requirements

1. Local access to a Windows 10+ machine with Windows Defender Firewall enabled.
2. Administrator privileges (required for full netsh dump and COM object access to firewall policies).
3. PowerShell execution policy allowing scripts (default on modern Windows).

## Defense

- Enable advanced auditing for process creation and command line arguments to log netsh and PowerShell executions.
- Implement application whitelisting (e.g., via AppLocker) to restrict unauthorized use of netsh or PowerShell for administrative tasks.
- Use network segmentation and least-privilege access to limit lateral discovery; regularly review and harden firewall rules to minimize information leakage.
- Monitor for anomalous firewall queries via Sysmon or EDR tools, focusing on HNetCfg.FwPolicy2 instantiations.

## Objectives

1. Export and analyze the complete Windows Defender Firewall policy to understand enforcement rules.
2. Identify blocked ports and associated applications to map restricted network paths.
3. Uncover potential vulnerabilities, such as overly permissive exceptions or discoverable service blocks.

## Instructions

### Step 1: Dump Firewall Configuration

**Context**: Begin by using netsh to capture the current firewall state and full configuration. This provides a comprehensive view of all rules, profiles (domain, private, public), and enabled features, allowing review for open avenues or misconfigurations. The dump output can be redirected to a file for offline analysis.

**Code** ([[codes/Netsh-Firewall-Discovery-Commands]]):

```powershell
netsh advfirewall firewall dump
# or 
netsh firewall show state
netsh firewall show config
```

> The primary command `netsh advfirewall firewall dump` exports the entire policy in a portable .wfw format, ideal for importing or parsing. Use `netsh firewall show state` to see active connections and `netsh firewall show config` for rule details (note: these are legacy for pre-Windows 8; prefer advfirewall on modern systems). Run in an elevated PowerShell or Command Prompt. Redirect output with `> firewall_dump.txt` to avoid console clutter. This step reveals global settings like logging and IPsec integration.

### Step 2: Enumerate Blocked Ports and Rules

**Context**: Query the firewall policy for rules set to block traffic (action code 0), focusing on local ports, applications, and rule names. This helps identify enforced restrictions, such as blocked RDP or SMB ports, to prioritize attack vectors on unblocked alternatives.

**Command** ([[commands/powershell-enumerate-blocked-firewall-rules]]):

```powershell
$f=New-object -comObject HNetCfg.FwPolicy2;$f.rules | where {$_.action -eq "0"} | select name,applicationname,localports
```

> This one-liner instantiates the FwPolicy2 COM object to access all rules, filters for blocks (action -eq "0"), and selects relevant properties. Execute in an elevated PowerShell session. If no output, it indicates no explicit block rules (common with default allow + exceptions model). Pipe to `| Export-Csv blocked_rules.csv` for structured analysis. Decision point: If results show specific app blocks (e.g., svchost.exe on port 445), investigate those services for bypass opportunities.

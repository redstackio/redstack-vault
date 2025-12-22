---
type: procedure
tactics:
  - '[[tactics/Defense-Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Privilege-Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Process-Injection|T1055 - Process Injection]]'
sub_techniques: []
tags:
  - '[[tags/Execute-from-Memory]]'
  - '[[tags/Metasploit]]'
  - '[[tags/Meterpreter-Basic]]'
commands:
  - '[[commands/meterpreter-execute-wce-via-calculator]]'
platforms:
  - Windows
tools:
  - '[[tools/Metasploit-Framework]]'
skill_level: intermediate
impact_level: high
detection_risk: high
verified: true
validated: true
---

# Memory Execution of Calculator and WCE with Meterpreter

## Summary

This procedure demonstrates how to use Meterpreter's execute command to run Calculator (calc.exe) and Windows Credential Editor (WCE) directly from memory on a compromised Windows system. By executing these binaries without writing to disk, attackers can evade file-based detection mechanisms in antivirus and EDR solutions, enabling credential theft for lateral movement.

## Description

In post-exploitation scenarios, attackers with an active Meterpreter session can leverage the 'execute' command to launch legitimate processes like calc.exe while injecting or running additional tools like WCE in memory. WCE is a tool for dumping and injecting Windows credentials, often used to pass-the-hash or escalate privileges. This technique maps to process injection by hijacking legitimate process contexts to run malicious code. It requires an established Meterpreter session via Metasploit and assumes the WCE binary is accessible (e.g., uploaded to the target or staged in memory). The target environment is a Windows system with administrative privileges or high integrity context. Success allows credential extraction without triggering disk-write alerts, facilitating network pivoting.

## Requirements

1. Active Meterpreter session on a compromised Windows target (established via exploit in Metasploit).
2. WCE binary available (e.g., uploaded to target via Meterpreter's upload command or staged from attacker machine).
3. High integrity level access (e.g., SYSTEM or admin privileges) for effective execution.
4. Metasploit Framework installed on the attacker's machine.

## Defense

Defensive measures and detection strategies:

- Implement application whitelisting and control (e.g., AppLocker or WDAC) to restrict unsigned binaries like WCE.
- Deploy EDR solutions with behavioral analytics to monitor process injection, unusual child processes from calc.exe, and memory execution patterns.
- Enable PowerShell and command-line logging to capture Meterpreter interactions; monitor for anomalous network callbacks to Metasploit handlers.
- Use integrity monitoring to detect credential dumping attempts and segment networks to limit lateral movement post-compromise.

## Objectives

1. Execute calc.exe in memory to establish a legitimate process context without disk writes.
2. Run WCE within the session to dump or inject Windows credentials.
3. Enable privilege escalation or lateral movement using stolen credentials.
4. Evade detection by avoiding persistent artifacts on disk.

## Instructions

### Step 1: Verify Meterpreter Session and Upload WCE if Needed

**Context**: Ensure the Meterpreter session is active and upload the WCE executable to the target if it's not already present. This step prepares the environment for memory execution, assuming the attacker has the WCE binary on their Kali machine.

**Commands**:
- Use Meterpreter's built-in upload command to transfer WCE to a temporary path on the target (e.g., C:\Windows\Temp\wce.exe).

> Upload the file first to ensure accessibility. Expected output: Confirmation of successful upload with file size and path.

### Step 2: Execute Calculator in High Integrity Context

**Context**: Launch calc.exe interactively in a new console with high integrity to create a visible, legitimate process that can serve as cover for further actions. This step tests the execution environment and confirms evasion capabilities.

**Command** ([[commands/meterpreter-execute-calculator]]):
```meterpreter
execute -H -i -c -f calc.exe -w
```

> This runs calc.exe with high integrity (-H), interactively (-i), in a new console (-c), and waits for completion (-w). No directory or arguments needed for basic execution. Expected output: Calculator window opens on the target without triggering file creation alerts; session remains active.

### Step 3: Execute WCE via Memory Injection into Legitimate Process

**Context**: Use the execute command to run WCE in the context of a legitimate process like calc.exe, injecting its functionality into memory to dump credentials. This combines execution with process hollowing-like behavior to steal hashes or passwords.

**Command** ([[commands/meterpreter-execute-wce-via-calculator]]):
```meterpreter
execute -H -i -c -m -d C:\Windows\System32 -f wce.exe -a "-w" -w
```

> Adjust the directory (-d) to a valid path like System32 for context, and pass arguments (-a) to WCE (e.g., -w for wordlist mode). The -m flag migrates the session if needed. Expected output: WCE runs silently, outputting captured credentials (e.g., NTLM hashes) to the Meterpreter console; no disk artifacts left behind.

### Step 4: Verify Credential Dump and Clean Up

**Context**: Confirm successful credential extraction and terminate processes to minimize footprint. Use the dumped credentials for further actions like psexec or pass-the-hash.

**Commands**:
- In Meterpreter, run 'ps' to list processes and 'kill' to terminate calc.exe and wce.exe if visible.

> Expected output: List of dumped credentials (e.g., administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::). Success confirmed by usable hashes for lateral movement.

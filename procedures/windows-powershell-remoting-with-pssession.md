---
id: 6d912fe3-7ec1-4dbd-b62b-d35757268034
name: windows-powershell-remoting-with-pssession
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:31.151347+00:00'
updated_at: '2023-04-10T20:37:59.117240+00:00'
tactics:
  - '[[Defense Evasion]]'
  - '[[Execution]]'
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
  - '[[Persistence]]'
  - '[[Privilege-Escalation-via-Direct-URL-Access]]'
techniques:
  - '[[Command-Line Interface]]'
  - '[[Remote Services]]'
  - '[[Valid Accounts]]'
sub_techniques:
  - '[[PowerShell]]'
  - '[[Windows Remote Management]]'
tags:
  - '[[tags/powershell-pssession]]'
  - '[[tags/powershell-remoting-protocol]]'
  - '[[tags/windows-using-credentials]]'
commands:
  - '[[commands/enable-powershell-remoting]]'
  - '[[commands/set-trusted-hosts]]'
  - '[[commands/new-pssession]]'
  - '[[commands/enter-pssession]]'
  - '[[commands/invoke-command-on-pssession]]'
platforms:
  - Windows
tools: []
validated: true
---

# windows-powershell-remoting-with-pssession

## Summary

This procedure demonstrates how to establish remote PowerShell execution on a Windows target using the PowerShell Remoting Protocol via PSSession, enabling persistent interactive or scripted access for reconnaissance, lateral movement, and other post-exploitation activities. It requires valid credentials and leverages Windows Remote Management (WinRM) for authenticated, encrypted connections, allowing attackers to blend in with legitimate administrative traffic.

## Description

PowerShell Remoting allows remote command execution over WinRM, using either direct Invoke-Command for one-off tasks or New-PSSession/Enter-PSSession for persistent sessions. This technique is useful in domain environments where attackers have stolen credentials, as it mimics admin tools like PowerShell ISE. The process involves enabling WinRM on the target (if not already), configuring trusted hosts on the attacker machine to allow connections without Kerberos, creating a session with credentials, and executing commands or entering an interactive shell. Success provides a foothold for further actions like data exfiltration or privilege escalation, while evading basic detection by using native Windows features. Target environment is Windows Server or Workstation with WinRM service; estimated time is 5-10 minutes assuming network access.

## Requirements

1. Valid domain or local credentials with remote access privileges on the target.
2. WinRM service enabled on the target (ports 5985 HTTP or 5986 HTTPS open in firewall).
3. Administrative access on the target to enable remoting if disabled.
4. PowerShell 3.0+ on both attacker and target machines.
5. Network connectivity from attacker to target (no proxy interference).

## Defense

1. Ensure that all remote PowerShell sessions are authenticated and encrypted using HTTPS (port 5986) with certificate-based auth.
2. Implement network segmentation to limit the scope of remote PowerShell sessions and block unnecessary WinRM traffic.
3. Monitor for anomalous PowerShell activity such as suspicious commands, large data transfers, unusual process spawning, or connections from untrusted hosts via Windows Event Logs (ID 4103/4104) or Sysmon.
4. Use constrained language mode or script block logging to restrict and audit PowerShell execution.
5. Apply least privilege: disable WinRM for non-admin users and use Just Enough Administration (JEA).

## Objectives

1. Remotely execute PowerShell commands on a target machine using valid credentials.
2. Establish a persistent PSSession for interactive or repeated command execution.
3. Perform reconnaissance, lateral movement, and data exfiltration while maintaining stealth.

## Instructions

### Step 1: Enable PowerShell Remoting on Target

**Context**: If WinRM is not already configured on the target, run this as administrator locally on the target or via initial access (e.g., RDP). This starts the service and sets basic remoting policies. Why: Without this, remote connections will fail.

**Code** ([[codes/enable-powershell-remoting-and-trusted-hosts-script]]):

```ps1
Enable-PSRemoting -Force
net start winrm
```

> The Enable-PSRemoting cmdlet configures the target for incoming remote sessions, suppressing prompts with -Force. net start winrm ensures the service is running. Expected: No errors; confirmation like "WinRM has been updated for remote management." Verify with Get-Service winrm (Status: Running).

### Step 2: Configure Trusted Hosts on Attacker Machine

**Context**: On the attacker side, add the target to trusted hosts to allow non-Kerberos authentication (useful for workgroup or cross-domain). Why: Prevents auth failures in non-domain setups; use specific IPs for security.

**Command** ([[commands/set-trusted-hosts]]):

```powershell
Set-Item WSMan:\localhost\Client\TrustedHosts -Value $_TRUSTED_HOSTS -Force
```

> This updates the WSMan client config to trust specified hosts. Restart PowerShell or run Restart-Service WinRM for changes to take effect. Expected: No output if successful; verify with Get-Item WSMan:\localhost\Client\TrustedHosts.

### Step 3: Create a New PSSession

**Context**: Establish a persistent session to the target using credentials. Why: Allows multiple commands without re-authenticating each time, reducing detection surface.

First, create a credential object:

```powershell
$cred = Get-Credential
```

**Command** ([[commands/new-pssession]]):

```powershell
$session = New-PSSession -ComputerName $_COMPUTER_NAME -Credential $cred
```

> New-PSSession creates a session object. Expected: $session variable populated; no errors. If fails, check firewall/WinRM. Success indicator: Get-PSSession shows active session.

### Step 4: Enter Interactive PSSession

**Context**: For interactive shell access, enter the session directly. Why: Provides a console-like experience for ad-hoc commands, similar to SSH.

**Command** ([[commands/enter-pssession]]):

```powershell
Enter-PSSession -ComputerName $_COMPUTER_NAME -Credential $cred
```

> This connects interactively; prompt changes to [TARGET]: PS>. Type commands as usual. Expected: Connected prompt. To exit: Exit-PSSession. Success: Run whoami to confirm context.

### Step 5: Execute Commands on PSSession

**Context**: Run scripted commands on the session without entering interactively. Why: Enables automation for reconnaissance (e.g., Get-Service) or exfiltration; can target multiple sessions.

**Command** ([[commands/invoke-command-on-pssession]]):

```powershell
Invoke-Command -Session $session -ScriptBlock { whoami }
```

> Invoke-Command executes the script block remotely. For multiple: Invoke-Command -Session $session1, $session2 -ScriptBlock { Get-Process }. Expected: Output from remote, e.g., "domain\user". If file: -FilePath C:\script.ps1. Success: Command results returned without errors; use Receive-Job for async.

### Step 6: Clean Up Sessions

**Context**: Disconnect and remove sessions to avoid leaving artifacts. Why: Prevents detection via active sessions in Get-PSSession.

```powershell
Exit-PSSession
Remove-PSSession $session
```

> Exit-PSSession leaves interactive mode; Remove-PSSession closes it. Expected: No active sessions in Get-PSSession.

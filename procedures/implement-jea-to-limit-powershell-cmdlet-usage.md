---
id: 25dba789-1058-4247-82b4-bf20671e0afb
name: Implement JEA to Limit PowerShell Cmdlet Usage
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:26.436581+00:00'
updated_at: '2023-04-10T20:37:06.712732+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Abuse Elevation Control Mechanism|T1548 - Abuse Elevation
    Control Mechanism]]
sub_techniques:
  - >-
    [[sub-techniques/Bypass User Account Control|T1548.002 - Bypass User Account
    Control]]
tags:
  - '[[tags/Just Enough Administration]]'
  - '[[tags/Powershell]]'
  - '[[tags/Windows - Defenses]]'
commands:
  - '[[commands/add-computer-to-domain]]'
  - '[[commands/create-new-windows-service]]'
  - '[[commands/create-new-powershell-session-configuration]]'
  - '[[commands/start-new-process]]'
platforms:
  - Windows
validated: true
---

# Implement JEA to Limit PowerShell Cmdlet Usage

## Summary

Just Enough Administration (JEA) is a PowerShell feature that enables administrators to delegate specific tasks to users by restricting access to only approved cmdlets and parameters, reducing the risk of misuse or attack. This procedure outlines how to configure a JEA endpoint that limits PowerShell sessions to a curated set of cmdlets (e.g., Add-Computer, New-Service, Start-Process, and session configuration commands), thereby minimizing the attack surface while allowing necessary administrative functions in a controlled environment.

## Description

JEA creates constrained PowerShell endpoints where users can only execute predefined cmdlets, parameters, and scripts, preventing access to dangerous or unnecessary functionality. This is particularly useful in enterprise environments to enforce least privilege for delegated administration, such as allowing domain joins or service creation without full PowerShell access. The setup involves defining role capabilities (what cmdlets are visible and executable), creating a session configuration, and registering the endpoint. Once implemented, users connecting to the endpoint operate in a sandboxed session, which helps mitigate risks from malicious scripts or unintended privilege escalation. This procedure assumes an administrative context for setup and targets Windows Server environments with PowerShell 5.0+.

## Requirements

1. Windows Server 2012 or later with PowerShell 5.0 or higher installed.
2. Administrative privileges on the target machine to register session configurations.
3. PowerShell remoting enabled (run Enable-PSRemoting if not already configured).
4. Basic familiarity with PowerShell scripting for creating configuration files.

## Defense

- Regularly audit JEA endpoint usage via PowerShell event logs (Event ID 4103/4104 for script block logging) and module logging to detect unauthorized attempts.
- Apply the principle of least privilege by reviewing and updating allowed cmdlets periodically to remove any unnecessary ones.
- Monitor for attempts to modify or unregister JEA configurations using tools like Windows Event Forwarding or SIEM integration.
- Combine with AppLocker or Constrained Language Mode to further restrict PowerShell execution outside JEA endpoints.

## Objectives

1. Configure a JEA endpoint that restricts PowerShell to only approved cmdlets like Add-Computer, New-Service, Start-Process, and session management commands.
2. Reduce the potential for attackers to leverage full PowerShell for evasion or escalation by limiting available functionality.
3. Enable safe delegation of administrative tasks while preventing accidental or malicious overuse of PowerShell capabilities.

## Instructions

### Step 1: Create the JEA Role Capabilities File

**Context**: Define the allowed and visible cmdlets in a role capabilities file (.psrc, saved as .psd1). This file specifies what users can see and execute in the constrained session, limiting to the target cmdlets to enforce restrictions.

Create a new directory for your JEA module (e.g., C:\Program Files\WindowsPowerShell\Modules\MyJEA\1.0.0.0), then create RoleCapabilities.psd1 with the following content:

```powershell
@{
    GUID = '12345678-1234-1234-1234-123456789abc'  # Replace with a new GUID from New-Guid
    Author = 'Admin'
    CompanyName = 'Organization'
    VisibleCmdlets = @(
        'Add-Computer',
        'New-Service',
        'Start-Process',
        'Microsoft.PowerShell.Core\*'
    )
    # For execution, use AllowedCommands if more granular control is needed
    # AllowedCommands = @('Add-Computer*', 'New-Service*', etc.)
}
```

Save the file in the module's RoleCapabilities subdirectory. This step ensures only the specified cmdlets are available, why: to prevent access to cmdlets like Invoke-Expression that could be abused.

**Expected Output**: A valid .psd1 file with no syntax errors (test with Import-PowerShellDataFile 'path\to\RoleCapabilities.psd1').

### Step 2: Create the JEA Session Configuration File

**Context**: The session configuration file (.pssc, saved as .ps1) defines the overall endpoint behavior, including the roles users assume upon connection. This links to the role capabilities file and sets the session type to restricted.

Create MyJEAConfiguration.pssc in the module directory with:

```powershell
# MyJEAConfiguration.pssc
@{
    SessionType = 'RestrictedRemoteServer'
    RoleDefinitions = @{
        'MyRole' = @{ RoleCapabilityFiles = 'RoleCapabilities.psd1' }
    }
    TranscriptDirectory = 'C:\JEA_Transcripts'  # For logging all sessions
    RunAsVirtualAccount = $true  # Run under a virtual account for isolation
}
```

This configuration applies the role to connecting users, why: to enforce the cmdlet restrictions across all sessions on this endpoint.

**Expected Output**: A script file that returns a hashtable (test by dot-sourcing the file and inspecting the output).

### Step 3: Register the JEA Session Configuration

**Context**: Register the configuration to make the JEA endpoint available for remote or local connections. This uses a PowerShell command to apply the .pssc file system-wide.

**Command** ([[commands/create-new-powershell-session-configuration]]):
```powershell
Register-PSSessionConfiguration -Name 'MyJEAEndpoint' -Path 'C:\Path\To\MyJEAConfiguration.pssc' -Force -TrustPipelineInput
```

> This command creates and enables the constrained endpoint named 'MyJEAEndpoint'. The -Force flag overwrites if it exists, and -TrustPipelineInput allows parameter passing. Run as administrator. Why: This activates the JEA restrictions for future sessions.

**Expected Output**: Confirmation message like "Directory: \RemoteRepository\PSSessionConfigurationFiles\MyJEAEndpoint\1.0.0.0" and the configuration is registered successfully.

### Step 4: Test the JEA Endpoint by Connecting and Running Allowed Commands

**Context**: Verify the setup by connecting to the endpoint as a non-admin user and executing the allowed cmdlets. This confirms the limitations are enforced (e.g., trying a disallowed cmdlet like Get-Process should fail).

First, grant a user access: Add-PSSessionConfigurationAccessRule -ConfigurationName 'MyJEAEndpoint' -UserName 'testuser' -AccessMode ReadWrite.

Then, connect as the user:
```powershell
Enter-PSSession -ComputerName localhost -ConfigurationName 'MyJEAEndpoint' -Credential (Get-Credential)
```

Within the session, test allowed commands:

**Command** ([[commands/create-new-windows-service]]):
```powershell
New-Service -Name 'TestService' -BinaryPathName 'C:\Windows\System32\notepad.exe' -StartupType Manual
```

> Creates a sample service to test. Expected: "The service 'TestService' was created successfully."

**Command** ([[commands/start-new-process]]):
```powershell
Start-Process notepad.exe
```

> Launches Notepad. Expected: Process starts without errors.

**Command** ([[commands/add-computer-to-domain]]):
```powershell
Add-Computer -DomainName 'example.com' -Credential (Get-Credential) -Restart
```

> Joins the machine to a domain (use in test env). Expected: "Computer successfully joined the domain."

Exit the session with Exit-PSSession. Why: Validates that only approved cmdlets work, confirming the limitation.

**Expected Output**: Successful execution of allowed commands; errors like "The term 'Get-Process' is not recognized" for disallowed ones.

### Step 5: Monitor and Maintain the JEA Endpoint

**Context**: After setup, enable logging and periodically review to ensure ongoing security.

Enable transcription in the .pssc file if not already, then restart the WinRM service: Restart-Service WinRM.

Use Get-PSSessionConfiguration to list endpoints and Update-PSSessionConfigurationFile for changes.

Why: Ongoing maintenance prevents drift and detects issues.

**Expected Output**: Logs in the transcript directory showing session activity.

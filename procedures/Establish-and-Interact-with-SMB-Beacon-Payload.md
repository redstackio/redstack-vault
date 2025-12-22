---
id: 07f2c348-a675-41ce-b82e-8f83942f9301
name: Establish-and-Interact-with-SMB-Beacon-Payload
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:16.340572+00:00'
updated_at: '2023-04-10T20:36:22.162395+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
techniques:
  - '[[techniques/Data Encoding|T1132 - Data Encoding]]'
  - '[[techniques/Remote Access Tools|T1219 - Remote Access Tools]]'
sub_techniques: []
tags:
  - '[[tags/Cobalt Strike]]'
  - '[[tags/Payloads]]'
  - '[[tags/SMB Beacon]]'
commands:
  - '[[commands/smb-beacon-link]]'
  - '[[commands/smb-beacon-connect]]'
  - '[[commands/smb-beacon-unlink]]'
  - '[[commands/smb-beacon-jump]]'
platforms:
  - Windows
tools:
  - '[[tools/Cobalt-Strike]]'
validated: true
---

# Establish-and-Interact-with-SMB-Beacon-Payload

## Summary

This procedure outlines how to deploy an SMB Beacon payload using Cobalt Strike to establish a covert command and control (C2) channel over SMB traffic, blending with normal network activity. Once implanted, attackers can interact with the beacon via command line to execute actions like connecting to pipes, ports, disconnecting processes, and injecting into new executables for lateral movement and persistence.

## Description

The SMB Beacon is a staged payload in Cobalt Strike that uses SMB for communication, making it stealthy in Windows environments where SMB is common. It is delivered via exploits or phishing and phones home to the C2 server. Interactions occur through the Cobalt Strike client console, allowing remote command execution, file transfer, and process manipulation without generating suspicious network patterns. This is ideal for post-exploitation in domain-joined networks, enabling lateral movement while evading detection by mimicking legitimate SMB sessions. Prerequisites include a Cobalt Strike license and target access for payload delivery.

## Requirements

1. Cobalt Strike software installed and licensed on the attacker's machine.
2. Network access to the target Windows system (e.g., via initial foothold or exploit).
3. Listener configured in Cobalt Strike for SMB protocol (port 445 typically).
4. Administrative privileges on the target for full beacon functionality.

## Defense

- Implement network segmentation to isolate SMB traffic and limit lateral movement.
- Deploy endpoint detection and response (EDR) tools to monitor for anomalous SMB connections and process injections.
- Enforce least privilege principles and monitor for unexpected named pipe or process creations.
- Use application whitelisting to prevent unauthorized executable launches.

## Objectives

1. Deploy the SMB Beacon payload to establish a persistent C2 channel.
2. Interact with the beacon to perform remote command execution and reconnaissance.
3. Enable lateral movement by connecting to remote pipes, ports, and injecting into processes.
4. Maintain stealth by leveraging SMB for all communications.

## Instructions

### Step 1: Configure SMB Listener and Generate Payload

**Context**: Set up the C2 infrastructure in Cobalt Strike to receive SMB Beacon connections and generate the payload for delivery.

Use the Cobalt Strike client to create an SMB listener:

- In the Cobalt Strike GUI, go to Listeners > Add > Select SMB as protocol.
- Configure host (attacker IP), port (445), and any stager settings.

Generate the payload using the Attacks menu or beacon generator, selecting SMB Beacon as the payload type. Deliver via your chosen vector (e.g., phishing executable or exploit).

**Expected Output**: A .exe or staged payload file ready for deployment. Upon execution on target, the beacon should appear in the Cobalt Strike team server console.

### Step 2: Establish Initial Beacon Connection

**Context**: Once the payload executes on the target, confirm the beacon is active and ready for interactions.

In the Cobalt Strike console, interact with the new beacon session. Verify connectivity by running basic tasks like `whoami` or `pwd`.

**Expected Output**: Beacon metadata displayed, including hostname, PID, and architecture. Successful task responses without errors.

### Step 3: Use Link Command for Named Pipe Connections

**Context**: Connect the beacon to a named pipe on a remote host for SMB-based lateral movement or data exfiltration.

**Command** ([[commands/smb-beacon-link]]):

Reference the interaction syntax from [[codes/SMB-Beacon-Command-Line-Interactions]]. In the beacon console:

```
link [host] [pipename]
```

Replace [host] with the target IP or hostname, and [pipename] with the pipe (e.g., \\pipe\foo).

**Expected Output**: Confirmation message like "Linked to pipe" or error if connection fails. Subsequent SMB traffic over the pipe.

### Step 4: Use Connect Command for Port Connections

**Context**: Establish a TCP connection from the beacon to a specified port on a remote host, useful for pivoting or external C2.

**Command** ([[commands/smb-beacon-connect]]):

In the beacon console:

```
connect [host] [port]
```

Specify [host] as IP/hostname and [port] as the target port (e.g., 4444 for a listener).

**Expected Output**: "Connected to port" message. Ability to send/receive data over the connection.

### Step 5: Use Unlink Command to Disconnect Processes

**Context**: Safely disconnect from a previously linked host or process to clean up or avoid detection.

**Command** ([[commands/smb-beacon-unlink]]):

In the beacon console:

```
unlink [host] [PID]
```

Provide [host] and [PID] of the target process.

**Expected Output**: "Unlinked" confirmation. No further traffic to the specified host/PID.

### Step 6: Use Jump Command for Process Injection

**Context**: Execute an executable on the target and connect it to a pipe for advanced persistence or evasion.

**Command** ([[commands/smb-beacon-jump]]):

In the beacon console:

```
jump [exec] [host] [pipe]
```

[exec] is the path to the executable (e.g., cmd.exe), [host] the target, [pipe] the pipe name.

**Expected Output**: New process spawned and linked, with interactive shell if applicable.

### Step 7: Verify and Maintain Persistence

**Context**: Run reconnaissance tasks and ensure the beacon remains operational.

Execute built-in beacon tasks like `ls`, `net use`, or `tasklist` to gather info. Use `exit` only when done to maintain the session.

**Expected Output**: Directory listings, network shares, and process lists without beacon termination.

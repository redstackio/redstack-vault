---
type: procedure
description: >-
  Exploit XSLT injection vulnerabilities to execute arbitrary C# code embedded
  in XSLT stylesheets, leading to remote code execution on Windows servers.
verified: true
submitted: false
created_at: '2023-04-06T03:56:41.521148+00:00'
updated_at: '2023-04-10T20:24:50.741101+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Scripting|T1064 - Scripting]]'
  - '[[techniques/XSL Script Processing|T1220 - XSL Script Processing]]'
sub_techniques: []
tags:
  - Exploit
  - Remote Code Execution with Embedded Script Blocks
  - XSLT Injection
commands: []
platforms:
  - Web
  - Windows
tools: []
validated: true
---

# XSLT-Injection-with-Embedded-C-Sharp-Script-for-RCE

## Summary

This procedure demonstrates how to exploit XSLT injection vulnerabilities in web applications that process XML with XSLT transformations, allowing the injection of malicious XSLT stylesheets containing embedded C# scripts to achieve remote code execution (RCE) on the server. By crafting a stylesheet that uses Microsoft's msxsl namespace to execute system commands, attackers can run arbitrary code, such as directory listings, on Windows-based servers processing the input.

## Description

XSLT Injection targets applications that dynamically apply user-supplied input to XSLT transformations without proper sanitization. In this technique, the attacker injects a malicious XSLT stylesheet into an XML processing pipeline, embedding C# code via the msxsl:script element. When the server applies the transformation (typically using .NET's XslCompiledTransform or similar), the C# code executes in the context of the web application, potentially with elevated privileges. This is particularly effective against legacy or misconfigured XML/XSLT parsers in ASP.NET applications. The procedure focuses on a Windows environment where cmd.exe can be invoked to run commands like 'dir' for reconnaissance, but it can be extended to more destructive actions. Success depends on the application reflecting the injected XSLT in its output, revealing the command results.

## Requirements

1. Access to a web application endpoint that accepts XML input and applies XSLT transformations without validation.
2. Knowledge of the XML structure expected by the application to craft a valid injection point.
3. A tool like Burp Suite or curl to intercept and modify HTTP requests containing XML payloads.
4. Target server running Microsoft .NET with XSLT processing enabled (common in Windows IIS environments).

## Defense

- Validate and sanitize all XML and XSLT inputs, disabling external entity processing and script extensions like msxsl:script.
- Use secure XML parsers (e.g., disable DTD processing and limit stylesheet namespaces to standard XSLT).
- Implement a Web Application Firewall (WAF) with rules to detect anomalous XSLT patterns, such as embedded scripting namespaces.
- Apply least privilege to the application pool identity to limit RCE impact.

## Objectives

1. Inject a malicious XSLT stylesheet to execute embedded C# code on the server.
2. Run system commands to enumerate files, directories, or other resources.
3. Achieve initial RCE for further post-exploitation, such as privilege escalation or data exfiltration.
4. Demonstrate control over the server process without direct authentication.

## Instructions

### Step 1: Identify the Injection Point

**Context**: Locate the vulnerable endpoint in the web application where user-controlled XML input is transformed using XSLT. This is often a search, import, or rendering feature that processes XML feeds.

Inspect the application's responses for XML/XSLT processing indicators, such as references to .xsl files or transformation errors. Use a proxy tool to capture requests and test for injection by appending malformed XML tags.

**Expected Output**: Confirmation of XSLT application, e.g., a response including transformed XML or error messages revealing stylesheet usage.

### Step 2: Craft the Malicious XSLT Payload

**Context**: Create an XSLT stylesheet that embeds C# code to execute a system command. Use the provided code snippet to define a function that spawns cmd.exe and captures its output.

Reference the payload code [[codes/XSLT-with-Embedded-C-Sharp-Script-to-Execute-Dir-Command]]. Customize the command in the Arguments property if needed (e.g., change '/c dir' to '/c whoami' for user enumeration).

**Expected Output**: A valid XML file containing the injected XSLT, ready for submission.

### Step 3: Inject and Submit the Payload

**Context**: Modify the HTTP request to include the malicious XML payload at the injection point, typically in a POST body or query parameter. Ensure the XML structure matches the application's expected format to trigger the transformation.

Submit the request using a tool like curl or Burp Repeater. For example, if the endpoint is /transform, send the XML as the body with Content-Type: application/xml.

**Expected Output**: Server response containing the transformed output, including the results of the executed command (e.g., directory listing).

### Step 4: Verify Execution and Iterate

**Context**: Analyze the response for signs of successful RCE, such as command output embedded in the XSLT result. If successful, iterate by modifying the embedded script for more advanced commands.

Check for errors indicating blocked execution (e.g., script disabled). If output is not reflected, adjust the xsl:template match to align with the input XML structure.

**Expected Output**: Command output like file listings confirming RCE; no transformation errors.

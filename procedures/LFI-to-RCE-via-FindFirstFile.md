---
id: d0bb4013-5469-455d-97f3-1c4eeedc3bb5
name: LFI-to-RCE-via-FindFirstFile
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:58.529690+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Scripting|T1064 - Scripting]]'
sub_techniques: []
tags:
  - '[[tags/File Inclusion]]'
  - '[[tags/LFI]]'
  - '[[tags/RCE]]'
commands:
  - '[[commands/curl-lfi-payload-test]]'
platforms:
  - Windows
  - Web
tools: []
validated: true
---

# LFI-to-RCE-via-FindFirstFile

## Summary

This procedure exploits a Local File Inclusion (LFI) vulnerability in a Windows-based application that insecurely uses the FindFirstFile API function for file searching and inclusion. By crafting user-controlled input with file masks and traversal sequences, an attacker can force the application to include and execute a malicious file, achieving remote code execution (RCE) without direct upload capabilities.

## Description

The vulnerability arises when an application uses the Windows FindFirstFile function with unsanitized user input for file paths or search patterns, allowing directory traversal and wildcard manipulation. FindFirstFile enumerates files matching a specified pattern, and if integrated into the application's inclusion logic (e.g., in a custom file loader), attackers can manipulate the search to include arbitrary local files or staged malicious payloads. This technique bypasses basic path restrictions by leveraging wildcard masks (e.g., '*.*') combined with '../' traversals to reach writable directories and execute scripts like ASP or PHP files if the application supports them. The target environment is typically a web application on Windows IIS or a similar setup where file inclusion occurs server-side. Success leads to RCE, enabling data exfiltration, persistence, or lateral movement. This maps to scenarios where developers fail to validate inputs against traversal patterns or wildcard expansions.

## Requirements

1. Validated LFI vulnerability in the target application, confirmed by including known files like /windows/system32/drivers/etc/hosts.
2. Knowledge of the file inclusion parameter (e.g., ?file= or ?include=) and the application's root directory structure.
3. Network access to the target web application, typically over HTTP/HTTPS on port 80/443.
4. Ability to stage a malicious file in a traversable directory (e.g., via another vuln or temporary web access).
5. Tools like curl for payload delivery; no elevated privileges required on the attacker side.

## Defense

- Implement strict input validation and sanitization for file paths, rejecting traversal sequences ('../') and wildcards ('*').
- Use whitelisting for allowed file inclusions, restricting to a safe directory without executable permissions.
- Monitor application logs and file system for anomalous FindFirstFile calls or unexpected file accesses via Windows Event Logs (Event ID 4663).
- Apply least privilege to the application process, preventing execution of included files in sensitive directories.
- Deploy WAF rules to block LFI patterns and enable server-side logging for API calls like FindFirstFile.

## Objectives

1. Confirm LFI by including and reading sensitive local files.
2. Craft a payload using file masks to include a staged malicious executable file.
3. Achieve RCE by executing the included malicious code on the server.
4. Verify execution through command output or reverse shell connection.

## Instructions

### Step 1: Confirm LFI Vulnerability

**Context**: Test the file inclusion endpoint to ensure traversal is possible, starting with reading a known system file. This verifies the parameter is vulnerable before attempting RCE.

**Command** ([[commands/curl-lfi-payload-test]]):
```bash
curl "http://target.com/vulnerable.php?file=../../../windows/system32/drivers/etc/hosts" -v
```

> This sends a GET request with a traversal payload to include the hosts file. The command uses curl's verbose flag (-v) to inspect headers and response. Expected output includes the contents of the hosts file if LFI works; errors like 404 or blank responses indicate filtering or non-vulnerable param.

If successful, proceed; otherwise, identify the correct parameter via source code review or fuzzing.

### Step 2: Stage Malicious File Using Traversal

**Context**: Use LFI to write or include a file in a traversable directory. Assuming a writable temp directory (e.g., /temp/), craft input to place a simple executable like a .asp webshell. This step leverages the application's inclusion to simulate upload via inclusion chaining.

**Instructions**: Identify a writable path via initial LFI tests (e.g., include /temp/ to list contents). Then, use a payload that exploits FindFirstFile's mask to match and include your staged file. For example, if the app uses FindFirstFile('userinput.*'), supply '../temp/malicious.asp'.

No specific command here; use browser or curl to submit the crafted path. Example payload: ?file=../../../temp/<<*>> where <<*>> mimics the wildcard mask to enumerate and include.

> WHY: FindFirstFile expands masks to find matching files, so if malicious.asp matches the pattern, it's included and parsed as code. Expected: No direct output, but file creation confirmed by subsequent inclusion tests.

Decision point: If temp is not writable, target session files or logs for injection (e.g., ?file=../../../windows/temp/php_error.log%00).

### Step 3: Execute RCE via Included File

**Context**: Once the malicious file is included via the crafted mask, trigger its execution to run arbitrary commands. The file could be a simple echo command or reverse shell payload.

**Command** ([[commands/curl-lfi-payload-test]]):
```bash
curl "http://target.com/vulnerable.php?file=../../../temp/malicious.asp&cmd=whoami" -v
```

> Append a command parameter if the app supports it post-inclusion. This executes 'whoami' via the included ASP. Expected output: Server response showing the current user (e.g., 'nt authority\iusr'), confirming RCE. If no param, the inclusion itself executes the file's code on load.

Verify by checking for side effects like a reverse connection if the payload includes a shell.

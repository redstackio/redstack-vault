---
tags:
  - lfr
  - php-object-injection
  - xxe
  - ssrf
  - pickle-deserialization
  - rce
type: attack_chain
tools:
  - '[[tools/Custom-PHP-Script]]'
  - '[[tools/Custom-Python-Script]]'
  - '[[tools/Netcat]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Discovery]]'
commands:
  - '[[commands/php-exploit-script]]'
  - '[[commands/python-reverse-shell]]'
platforms:
  - Web
  - Linux
complexity: high
procedures:
  - '[[procedures/Exploit-Local-File-Read-to-Access-Source-Code]]'
  - '[[procedures/Perform-PHP-Object-Injection]]'
  - '[[procedures/Trigger-XXE-for-SSRF]]'
  - '[[procedures/Exploit-Python-Pickle-Deserialization-for-RCE]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
  - '[[Server Software Component]]'
description: >-
  Chained exploit starting with local file read to expose source code, leading
  to PHP object injection, XXE-based SSRF to access internal service, and Python
  pickle deserialization for remote code execution.
skill_level: advanced
impact_level: high
id: 81c65544-d2b0-4ac0-b3c7-4b0e07ea6e3c
created_at: '2025-12-13T09:00:28.015Z'
updated_at: '2025-12-13T09:00:28.015Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
  - '[[Server Software Component]]'
---
# RCE via LFR to PHP Object Injection, XXE SSRF, and Python Pickle Deserialization

Multi-stage attack chain demonstrating a complete attack workflow exploiting a meme generation service to achieve remote code execution.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~30 minutes |
| Skill Level | Advanced |
| Complexity | High |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Local File Read] --> B[PHP Object Injection]
    B --> C[XXE SSRF]
    C --> D[Pickle Deserialization RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Custom-PHP-Script]]
- [[tools/Custom-Python-Script]]
- [[tools/Netcat]]

### Target Environment

- Linux-based web server
- PHP and Python services running
- Internal service on port 1337

### Initial Access Requirements

- Access to public web endpoints (/api/generate.php, /api/import_memes_2.0.php, /memes.php)
- Network access to target host
- No prior credentials needed

## Detailed Attack Procedures

### Step 1: Exploit Local File Read to Access Source Code
procedure: [[procedures/Exploit-Local-File-Read-to-Access-Source-Code]]

**Objective**: Access arbitrary server files including PHP source code to identify further vulnerabilities.

**Instructions**: Send a POST request to /api/generate.php with the template parameter set to a path like ../../../../../../../etc/passwd to include file contents in a generated meme. Retrieve the meme file from the returned path to view the contents.

Use a tool like curl to send the request:

```bash
curl -X POST http://target/api/generate.php -d "template=../../../../../../../etc/passwd"
```

Then, read key PHP files such as config.php, includes/classes.php, etc., by adjusting the template path accordingly.

**Expected Output**: File contents embedded in the generated meme image or text.

**Success Indicators**:
- Arbitrary files readable
- Source code of PHP files obtained

### Step 2: Perform PHP Object Injection
procedure: [[procedures/Perform-PHP-Object-Injection]]

**Objective**: Inject a crafted PHP object into the session via unserialization to set up for XXE exploitation.

**Instructions**: Use [[commands/php-exploit-script]] to generate a base64-encoded serialized object:

```bash
php exploit.php http://localhost
```

Upload the payload via multipart POST to /api/import_memes_2.0.php in the 'f' file parameter. This stores the object in the session.

**Expected Output**: Base64-encoded serialized array containing ConfigFile object.

**Success Indicators**:
- Object successfully injected into session
- No errors in upload response

### Step 3: Trigger XXE for SSRF
procedure: [[procedures/Trigger-XXE-for-SSRF]]

**Objective**: Invoke the injected object's magic method to trigger XXE and perform SSRF to access internal services.

**Instructions**: Visit /memes.php to echo the session array, which calls __toString() on the injected ConfigFile object, parsing malicious XML with an external entity pointing to http://localhost:1337/status.

Use SSRF to probe /status and /update-status endpoints on the internal service.

**Expected Output**: Response from internal service, such as status information or base64-encoded pickle objects.

**Success Indicators**:
- Internal service responses retrieved
- Confirmation of pickle deserialization vulnerability

### Step 4: Exploit Python Pickle Deserialization for RCE
procedure: [[procedures/Exploit-Python-Pickle-Deserialization-for-RCE]]

**Objective**: Achieve remote code execution by sending a malicious pickle object via SSRF to the internal service.

**Instructions**: Use [[commands/python-reverse-shell]] embedded in a custom pickle payload generated by a Python script. Base64-encode it and send via XXE SSRF to /update-status?status=<base64_pickle>&debug=1.

Listen for the reverse shell using netcat:

```bash
nc -lvnp 443
```

Once connected, read flag.txt from the server.

**Expected Output**: Reverse shell session allowing command execution and file access.

**Success Indicators**:
- Reverse shell established
- Access to flag.txt or other sensitive files

## Attack Chain Summary

### Key Achievements

1. Exposed server source code via LFR
2. Injected PHP object to trigger XXE
3. Accessed internal service via SSRF
4. Achieved RCE via pickle deserialization

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

*Last updated: 2023-10-01*

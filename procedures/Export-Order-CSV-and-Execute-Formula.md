---
id: 550e8400-e29b-41d4-a716-446655440003
tags:
  - csv-export
  - formula-execution
  - rce
  - excel
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/excel-formula-injection-cmd]]'
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:28:44.263Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Windows Command Shell]]'
---
---

# Export-Order-CSV-and-Execute-Formula

## Summary

This procedure exports the malicious order to CSV format and opens it in Excel, triggering the formula injection for command execution due to unfiltered variant data.

## Description

Shopify's CSV export for orders includes product titles and variant details in columns. Dangerous characters are filtered in the first occurrence (e.g., '=' to space), but not in subsequent rows for multi-variant line items. When opened in Excel, the preserved formula in later variants executes as `=cmd|' /C calc'!'D2'`, invoking cmd.exe to run calc.exe. This achieves RCE in the context of the user's Excel session on Windows, potentially allowing more dangerous payloads like file downloads or malware execution.

## Requirements

1. Completed order with malicious variants
2. Microsoft Excel on Windows
3. Shopify admin access for export

## Defense

Defensive measures and detection strategies:

- Apply uniform CSV escaping across all rows and fields; use quoted strings or HTML entities
- Disable automatic formula execution in Excel via Trust Center settings
- Log and alert on CSV exports containing unescaped special characters

## Objectives

1. Generate CSV export with preserved injection payload
2. Open in Excel to trigger execution
3. Verify arbitrary command runs (e.g., calc.exe launch)

## Instructions

### Step 1: Initiate CSV Export

**Context**: From the order details, export data to CSV.

**Instructions**:

Go to the specific order page. Click Export > All line items. Choose "Open in Excel" or download the CSV file.

> Expected: CSV file generated or Excel launches directly.

### Step 2: Open CSV in Excel and Observe Execution

**Context**: Load the file in Excel to activate the formula.

**Command** ([[commands/excel-formula-injection-cmd]]):

The payload executes automatically:

```text
=cmd|' /C calc'!'D2'
```

> In the CSV, the first variant row shows filtered title (e.g., ` cmd|' /C calc'!'D2'`), but subsequent rows retain `=cmd|' /C calc'!'D2'`. Upon opening, Excel interprets it as a formula, running cmd /C calc, which opens the calculator. For validation, replace 'calc' with other commands like 'notepad'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[Windows Command Shell]] Command and Scripting Interpreter: Windows Command Shell

### Sub-Techniques


## Commands Used

- [[commands/excel-formula-injection-cmd]]

## Tools Used


## Tags

- [[csv-export]]
- [[rce]]
- [[excel]]

---

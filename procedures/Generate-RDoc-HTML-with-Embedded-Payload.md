---
tags:
  - xss
  - generation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/rdoc-generate-docs]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:53.426Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 9e980a2a-5cb0-4181-8c71-a2d0ce702774
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Generate-RDoc-HTML-with-Embedded-Payload

## Summary

This procedure runs RDoc to generate HTML documentation, embedding the XSS payload from the malicious filename into files like index.html without escaping.

## Description

RDoc's darkfish generator (lib/rdoc/generator/darkfish.rb) inserts filenames into templates (e.g., _sidebar_pages.rhtml) without HTML escaping, allowing tags like <object> and onerror JS to render directly. This creates stored XSS in the output, exploitable by doc viewers.

## Requirements

1. Ruby and RDoc installed
2. Malicious file in project directory
3. Write access to output directory (e.g., doc/)

## Defense

Defensive measures and detection strategies:

- Patch RDoc to escape filenames (as in the reported fix)
- Review generated HTML for unescaped content
- Avoid generating docs from untrusted sources

## Objectives

1. Process files to inject payload into HTML
2. Create vulnerable documentation pages
3. Enable browser-based JS execution

## Instructions

### Step 1: Run RDoc Generation

**Context**: Execute rdoc to build all docs, forcing inclusion of the malicious file.

**Command** ([[commands/rdoc-generate-docs]]):
```bash
rdoc --all
```

> This generates HTML in doc/, with the payload in index.html as an unescaped <li><a> link. Check source for injection like '<object src=1 onerror="javascript:alert(1);">'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques

- None

## Commands Used

- [[commands/rdoc-generate-docs]]

## Tools Used

- None

## Tags

- [[xss]]
- [[generation]]

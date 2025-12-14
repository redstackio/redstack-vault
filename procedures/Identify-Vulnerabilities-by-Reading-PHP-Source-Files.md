---
tags:
  - source-code-review
  - vulnerability-discovery
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/exploit-lfr-read-etc-passwd]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:23:50.030Z'
sub_techniques: []
id: 0b596edc-aac1-401c-a02f-e22bb8a17f5f
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Identify-Vulnerabilities-by-Reading-PHP-Source-Files

## Summary

This procedure involves auditing PHP source code obtained via Local File Read to identify vulnerabilities such as unsafe unserialization for object injection and XXE in XML parsing.

## Description

By reading files like config.php, classes.php, export_memes_2.0.php, and import_memes_2.0.php, attackers can statically analyze code for insecure patterns. Key findings include unserialize on $_FILES['f'] in import functionality and DOMDocument with vulnerable flags in ConfigFile::parse(), enabling the next stages of the chain.

## Requirements

1. Access to PHP source via LFR
2. Basic PHP knowledge for code review
3. Text editor or grep for pattern searching

## Defense

Defensive measures and detection strategies:

- Obfuscate or remove sensitive code from web-readable paths
- Implement code access controls (e.g., .htaccess deny)
- Use static analysis tools to detect insecure patterns pre-deployment

## Objectives

1. Locate unserialize calls on user input
2. Identify XXE-prone XML parsing
3. Plan exploitation chain

## Instructions

### Step 1: Read and Review Config and Classes

**Context**: Extract includes and class definitions.

**Command** ([[commands/exploit-lfr-read-etc-passwd]] for config.php):
```bash
curl -X POST http://target.com/api/generate.php -d "template=../../../../../../../var/www/html/config.php&type=text&top-text=ad&bottom-text=asd"
```

> Review output for includes like header.php and classes.php.

### Step 2: Audit for Vulnerabilities

**Context**: Search for deserialization and XXE.

**Command** (Local analysis, e.g., grep):
```bash
grep -r "unserialize" downloaded_sources/
```

> Look for $_FILES['f'] unserialize and DOMDocument loadXML with LIBXML_NOENT | LIBXML_DTDLOAD.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used

- [[commands/exploit-lfr-read-etc-passwd]]

## Tools Used


## Tags

- source-code-review
- vulnerability-discovery

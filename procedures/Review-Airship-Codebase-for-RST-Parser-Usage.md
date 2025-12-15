---
tags:
  - code-review
  - rst-parser
  - airship-cms
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:26:17.113Z'
sub_techniques: []
id: 12f5d691-8c8d-4958-aec3-d4eeeb7d5b19
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Review-Airship-Codebase-for-RST-Parser-Usage

## Summary

This procedure involves auditing the Airship CMS source code to locate instances where the Gregwar/RST parser processes user-controlled input, identifying potential vectors for directive injection like the vulnerable include statement.

## Description

In the context of vulnerability research, reviewing the codebase of Airship CMS reveals that user-submitted RST content is parsed in key files without restrictions on directives. This step is crucial for understanding how custom pages and lens functions handle RST, setting the stage for LFI exploitation. The target environment is a PHP-based web application, and outcomes include pinpointing exact lines of code where parsing occurs, enabling subsequent payload crafting.

## Requirements

1. Access to Airship CMS GitHub repository or source code
2. Text editor or IDE for code searching (e.g., grep or VS Code)
3. Basic knowledge of PHP and RST syntax

## Defense

Defensive measures and detection strategies:

- Implement code reviews with static analysis tools like SonarQube to flag unsafe parsing
- Use web application firewalls (WAF) to detect anomalous RST uploads
- Monitor logs for RST parsing errors or unusual file access patterns

## Objectives

1. Locate all RST parsing entry points in the codebase
2. Confirm user control over RST input
3. Document vulnerable lines for exploitation planning

## Instructions

### Step 1: Clone and Search Codebase

**Context**: Obtain the source code and search for RST-related classes or functions to identify parsing locations.

No specific command; manually review or use grep:

```bash
git clone https://github.com/paragonie/airship.git
cd airship
 grep -r "RST" src/ --include="*.php"
```

> This command searches for RST references, revealing files like CustomPages.php and lens_functions.php. Expected output includes line numbers and code snippets showing parser instantiation.

### Step 2: Analyze Specific Files

**Context**: Dive into identified files to confirm user input flows into the parser.

Review src/Cabin/Hull/Landing/CustomPages.php around line 186 and src/lens_functions.php around line 714.

> Manually inspect for $parser->parse($userInput) patterns without directive whitelisting. Success confirms vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- code-review
- rst-parser
- airship-cms

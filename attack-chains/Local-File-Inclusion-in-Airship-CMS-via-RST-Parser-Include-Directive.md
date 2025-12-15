---
tags:
  - lfi
  - file-inclusion
  - rst-parser
  - php
  - information-disclosure
type: attack_chain
tools:
  - '[[tools/Gregwar-RST]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Review-Airship-Codebase-for-RST-Parser-Usage]]'
  - '[[procedures/Analyze-Gregwar-RST-Library-for-Vulnerabilities]]'
  - '[[procedures/Craft-Malicious-RST-Document-for-LFI]]'
  - '[[procedures/Execute-PHP-Script-to-Parse-RST-and-Disclose-Files]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:17.124Z'
description: >-
  Multi-stage attack chain exploiting a Local File Inclusion vulnerability in
  Airship CMS by leveraging the Gregwar/RST parser's unrestricted include
  directive to disclose arbitrary local files.
id: 7ea35078-c059-48a6-a65e-65ba2c3a42d1
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# Local File Inclusion in Airship CMS via RST Parser Include Directive

Multi-stage attack chain demonstrating the discovery and exploitation of a Local File Inclusion (LFI) vulnerability in Airship CMS. The attack begins with code review to identify RST parser usage, analyzes the underlying library for flaws, crafts malicious RST content using path traversal, and executes a PHP script to parse and disclose sensitive files like /etc/hosts.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Code Review] --> B[Library Analysis]
    B --> C[Craft Malicious RST]
    C --> D[Execute Parsing and Disclosure]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Gregwar-RST]]
- PHP environment (version 7+ recommended)

### Target Environment

- Airship CMS installation on a PHP-enabled web server
- Access to source code for review (e.g., GitHub repository)
- Linux-based server for file disclosure testing (/etc/hosts)

### Initial Access Requirements

- Read access to Airship CMS codebase
- Local PHP setup for demonstration
- No network credentials needed for local testing; assumes authenticated upload of RST content in production

## Detailed Attack Procedures

### Step 1: Code Review
procedure: [[procedures/Review-Airship-Codebase-for-RST-Parser-Usage]]

**Objective**: Identify points in the Airship CMS codebase where user-controlled RST content is parsed, revealing potential injection sites for the include directive.

**Instructions**: Clone the Airship CMS repository and search for RST parser instantiations. Focus on files handling custom pages and lens functions.

**Expected Output**: Locations such as src/Cabin/Hull/Landing/CustomPages.php at line 186 and src/lens_functions.php at line 714.

**Success Indicators**:
- RST parsing code found without path validation
- User-controlled input confirmed as RST source

### Step 2: Library Analysis
procedure: [[procedures/Analyze-Gregwar-RST-Library-for-Vulnerabilities]]

**Objective**: Examine the Gregwar/RST library to confirm the include directive allows arbitrary file paths via path traversal.

**Instructions**: Review the Parser.php file in the Gregwar/RST source, specifically line 762, to understand how includes are handled without restrictions.

**Expected Output**: Confirmation that directives like '.. include:: /./../../../../../../../../../../../../../../../../../../etc/hosts' resolve to arbitrary files.

**Success Indicators**:
- Include directive lacks path sanitization
- Path traversal possible to system files

### Step 3: Craft Malicious RST
procedure: [[procedures/Craft-Malicious-RST-Document-for-LFI]]

**Objective**: Create RST content that embeds a path traversal payload in the include directive to target sensitive files.

**Instructions**: Write an RST document with mixed content and include, e.g., '*Test* .. include:: /./../../../../../../../../../../../../../../../../../../etc/hosts ``test``'.

**Expected Output**: RST file ready for parsing, which will attempt to include and render the target file.

**Success Indicators**:
- RST syntax valid with include payload
- Payload uses sufficient '../' for traversal

### Step 4: Execute Parsing
procedure: [[procedures/Execute-PHP-Script-to-Parse-RST-and-Disclose-Files]]

**Objective**: Parse the malicious RST using a PHP script to demonstrate file disclosure in HTML output.

**Instructions**: Create and run a PHP script (rst.php) that loads the RST autoload, instantiates the parser, parses the RST, and outputs the result. Execute using [[commands/php-rst-parse]]:

```bash
php rst.php
```

**Expected Output**: HTML output embedding /etc/hosts contents, e.g., <p><em>Test</em></p><p>##\n# Host Database\n... 127.0.0.1\tlocalhost</p>.

**Success Indicators**:
- Arbitrary file contents rendered
- No parsing errors; successful inclusion

## Attack Chain Summary

### Key Achievements

1. Identified unvalidated RST parsing in Airship CMS
2. Confirmed LFI via Gregwar/RST include directive
3. Demonstrated disclosure of /etc/hosts through crafted payload
4. Highlighted need for parser restrictions or alternatives

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]
- [[Collection]]

---

*Last updated: 2023-10-01T00:00:00Z*

---
tags:
  - xss
  - stored-xss
  - ruby
  - rdoc
  - javascript
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Malicious-File-for-XSS-Injection]]'
  - '[[procedures/Verify-Malicious-File-Creation]]'
  - '[[procedures/Generate-RDoc-HTML-with-Embedded-Payload]]'
  - '[[procedures/Trigger-XSS-in-Generated-Documentation]]'
  - '[[procedures/Exploit-Persistent-XSS-in-Search-Results]]'
step_count: 5
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:15:53.436Z'
description: >-
  A multi-stage attack exploiting a stored XSS vulnerability in Ruby's RDoc
  documentation generator by injecting malicious JavaScript through file names,
  resulting in code execution when viewing generated HTML documentation.
skill_level: intermediate
impact_level: high
id: 08c1751c-4d06-4640-8806-a9784ff2691a
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Stored XSS in RDoc via Malicious File Names Leading to Arbitrary JavaScript Execution

Multi-stage attack chain demonstrating exploitation of a stored XSS vulnerability in RDoc, Ruby's documentation generator. An attacker creates a file with a malicious name containing JavaScript, generates HTML documentation, and triggers execution in the browser of anyone viewing the docs, potentially leading to data theft or malware deployment. A secondary persistence issue in search results extends the attack even after partial fixes.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Malicious File] --> B[Verify File]
    B --> C[Generate RDoc HTML]
    C --> D[View Docs and Trigger XSS]
    D --> E[Exploit Search Persistence]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses built-in Ruby and shell commands)

### Target Environment

- Linux OS with Ruby and RDoc installed
- Access to a Ruby project directory for documentation generation
- No specific services or ports required; local execution

### Initial Access Requirements

- Local or remote shell access to a system with Ruby/RDoc
- No credentials needed beyond file system write access
- Prior knowledge of the target project's documentation workflow

## Detailed Attack Procedures

### Step 1: Create Malicious File
procedure: [[procedures/Create-Malicious-File-for-XSS-Injection]]

**Objective**: Inject an XSS payload into a file name to be processed by RDoc.

**Instructions**: Use [[commands/touch-malicious-filename]] to create the file:

```bash
touch ""><object src=1 onerror=\"javascript:alert(1);\">Controlling what is documented here"
```

**Expected Output**: No output; file created with the malicious name.

**Success Indicators**:
- File exists with the exact payload in its name
- Payload includes unescaped HTML and JavaScript

### Step 2: Verify Malicious File Creation
procedure: [[procedures/Verify-Malicious-File-Creation]]

**Objective**: Confirm the malicious file is present before generation.

**Instructions**: Run [[commands/ls-list-files]] to list directory contents:

```bash
ls
```

**Expected Output**: Displays the file name: ""><object src=1 onerror="javascript:alert(1);">Controlling what is documented here

**Success Indicators**:
- Malicious file name visible in listing
- No errors in file creation

### Step 3: Generate RDoc HTML with Embedded Payload
procedure: [[procedures/Generate-RDoc-HTML-with-Embedded-Payload]]

**Objective**: Process the project to embed the unescaped payload into HTML output.

**Instructions**: Execute [[commands/rdoc-generate-docs]] to build documentation:

```bash
rdoc --all
```

**Expected Output**: HTML files generated in doc/ directory, with index.html containing the injected payload as a list item.

**Success Indicators**:
- doc/index.html created
- Payload visible in source as unescaped HTML/JS

### Step 4: Trigger XSS in Generated Documentation
procedure: [[procedures/Trigger-XSS-in-Generated-Documentation]]

**Objective**: Execute the JavaScript by viewing the docs in a browser.

**Instructions**: Open the generated index.html in a web browser. No command needed; the payload triggers on load.

**Expected Output**: Alert box pops up with "1" due to the onerror JavaScript.

**Success Indicators**:
- JavaScript alert executes
- Injected code renders as: '<li><a href="./"><object src=1 onerror="javascript:alert(1);">Controlling what is documented here.html">&quot;&gt;&lt;object src=1 onerror=&quot;javascript:alert(1);&quot;&gt;Controlling what is documented here</a>'

### Step 5: Exploit Persistent XSS in Search Results
procedure: [[procedures/Exploit-Persistent-XSS-in-Search-Results]]

**Objective**: Demonstrate ongoing XSS via search even after filename fixes.

**Instructions**: After generation, interact with the search box on the documentation page by typing 'a'. The darkfish.js search renders unescaped snippets.

**Expected Output**: XSS payload executes in search results, triggering alert.

**Success Indicators**:
- Search interaction executes JS from file name/title
- Persistence confirmed in hookSearch() function

## Attack Chain Summary

### Key Achievements

1. Successful injection of XSS via file name into RDoc output
2. Arbitrary JS execution in victim browsers viewing docs
3. Persistent exploitation through search functionality post-patch

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---

*Last updated: 2023-10-01T00:00:00Z*

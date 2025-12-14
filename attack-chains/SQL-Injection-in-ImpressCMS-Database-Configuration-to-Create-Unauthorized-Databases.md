---
id: ac-uuid-1234
tags:
  - sqli
  - impresscms
  - php
  - mysql
  - installation
type: attack_chain
tools:
  - '[[tools/git]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - PHP
  - MySQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Clone-ImpressCMS-Repository]]'
  - '[[procedures/Initiate-ImpressCMS-Installation]]'
  - '[[procedures/Inject-SQL-Payload-in-Database-Name]]'
  - '[[procedures/Submit-Database-Configuration-Form]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:15.025Z'
description: >-
  Multi-stage attack exploiting SQL injection in the ImpressCMS installation
  process to execute arbitrary SQL commands and create unauthorized databases.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# SQL Injection in ImpressCMS Database Configuration to Create Unauthorized Databases

Multi-stage attack chain demonstrating a complete attack workflow exploiting a SQL injection vulnerability during the ImpressCMS installation process. The vulnerability arises from improper escaping of backticks in the 'Database name' field using PHP's addslashes function, allowing attackers to inject and execute arbitrary SQL commands, such as creating unauthorized databases.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Clone Repository] --> B[Initiate Installation]
    B --> C[Inject SQL Payload]
    C --> D[Submit Form and Execute]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/git]]

### Target Environment

- Web platform with PHP and MySQL services
- Local development environment for testing ImpressCMS installation
- Access to GitHub for cloning the repository

### Initial Access Requirements

- No prior credentials needed; exploits during open installation process
- Local network access to run the setup script
- MySQL server instance available for configuration

## Detailed Attack Procedures

### Step 1: Clone Repository
procedure: [[procedures/Clone-ImpressCMS-Repository]]

**Objective**: Obtain the ImpressCMS source code to set up and test the installation process.

**Instructions**: Use [[commands/git-clone-impresscms]] to download the repository:

```bash
git clone https://github.com/ImpressCMS/impresscms.git
```

**Expected Output**: The repository is cloned into a local directory named 'impresscms'.

**Success Indicators**:
- Directory 'impresscms' created with source files
- No cloning errors in terminal output

### Step 2: Initiate Installation
procedure: [[procedures/Initiate-ImpressCMS-Installation]]

**Objective**: Start the ImpressCMS setup process and navigate to the database configuration step.

**Instructions**: Navigate to the cloned directory and run the setup script, then proceed through the installation wizard until the Database configuration form.

```bash
cd impresscms
php setup.php  # Or access via web server if configured
```

**Expected Output**: Installation wizard loads, reaching the Database configuration menu.

**Success Indicators**:
- Setup form visible in browser or terminal
- Database configuration fields displayed

### Step 3: Inject SQL Payload
procedure: [[procedures/Inject-SQL-Payload-in-Database-Name]]

**Objective**: Introduce a malicious SQL payload into the 'Database name' field to close the original query and append an arbitrary command.

**Instructions**: In the Database name field, enter the payload that exploits the lack of backtick escaping:

Enter: `impresscms`; create database `vuln`

**Expected Output**: Payload accepted without validation errors.

**Success Indicators**:
- Form accepts the input with backticks and semicolon
- No immediate error on payload entry

### Step 4: Submit Form
procedure: [[procedures/Submit-Database-Configuration-Form]]

**Objective**: Submit the form to execute the injected SQL, creating an unauthorized database.

**Instructions**: Complete other required fields (e.g., host, user, password) and submit the database configuration form.

**Expected Output**: Original 'impresscms' database created, plus unauthorized 'vuln' database.

**Success Indicators**:
- Installation completes successfully
- Query MySQL to confirm 'vuln' database exists: `SHOW DATABASES;`
- Arbitrary SQL execution verified

## Attack Chain Summary

### Key Achievements

1. Cloned ImpressCMS source for local testing
2. Navigated to vulnerable database configuration step
3. Injected SQL payload exploiting addslashes limitation on backticks
4. Executed arbitrary SQL to create unauthorized database during installation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*

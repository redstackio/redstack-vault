---
tags:
  - gitlab
  - template-injection
  - data-exfiltration
  - improper-access-control
type: attack_chain
tools:
  - '[[tools/tar]]'
tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
  - '[[Collection]]'
commands:
  - '[[commands/tar-create-archive]]'
platforms:
  - Web
  - GitLab
complexity: medium
procedures:
  - '[[procedures/Export-GitLab-Project-for-Modification]]'
  - '[[procedures/Modify-Project-JSON-to-Inject-Service-Template]]'
  - '[[procedures/Repackage-and-Import-Modified-Project-Archive]]'
  - '[[procedures/Verify-Injected-Service-Template-in-New-Project]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Abuse Elevation Control Mechanism]]'
description: >-
  Exploits a vulnerability in GitLab's project import feature to inject
  malicious service templates, enabling automatic application to new projects
  for data exfiltration, mutation, or social engineering.
skill_level: intermediate
impact_level: high
id: 8d4635a9-7c5a-4b0c-8a36-f47874b88e6e
created_at: '2025-12-11T06:10:28.942Z'
updated_at: '2025-12-11T06:10:28.942Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0003]]'
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1548]]'
---
# GitLab Service Template Injection via Project Import for Data Exfiltration and Mutation

Multi-stage attack chain demonstrating how to exploit a vulnerability in GitLab's project import feature by injecting templated services, allowing attackers to compromise new projects instance-wide.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Project Setup] --> B[Export and Modify] --> C[Import Injection] --> D[Verification and Impact]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/tar]]

### Target Environment

- GitLab platform (web-based)
- Required services: GitLab CI, project import/export features
- Network access requirements: Authenticated access to GitLab instance as a standard user

### Initial Access Requirements

- Credential requirements: Standard user accounts on the GitLab instance
- Network position: Access to the GitLab web interface
- Prior access needed: Ability to create and export projects

## Detailed Attack Procedures

### Step 1: Project Setup and Export - [[procedures/Export-GitLab-Project-for-Modification]]

**Procedure**: [[procedures/Export-GitLab-Project-for-Modification]]

**Objective**: Create and export a GitLab project with an enabled service to prepare for template injection.

**Expected Output**: A downloaded project export archive containing project.json.

**Success Indicators**:
- Project successfully created and exported.
- Archive downloaded and extractable.

First, sign in as any user and create a new project using the GitLab UI. Enable the CI service through Settings > Integrations. Then, export the project and download the export file.

Extract the archive using [[tools/tar]]:

```bash
tar -zxvf project_export.tar.gz
```

### Step 2: Modify Project Files - [[procedures/Modify-Project-JSON-to-Inject-Service-Template]]

**Procedure**: [[procedures/Modify-Project-JSON-to-Inject-Service-Template]]

**Objective**: Edit the exported project.json to convert a service into a malicious template.

**Expected Output**: Modified project.json with template set to true and type changed to MockCiService.

**Success Indicators**:
- JSON edits confirmed without syntax errors.
- File ready for repackaging.

Edit the project.json file to replace "template":false with "template":true in the services array, and change CiService to MockCiService.

### Step 3: Repackage and Import - [[procedures/Repackage-and-Import-Modified-Project-Archive]]

**Procedure**: [[procedures/Repackage-and-Import-Modified-Project-Archive]]

**Objective**: Create a new archive with modified files and import it to inject the template.

**Expected Output**: Successful import of the modified project, injecting the template instance-wide.

**Success Indicators**:
- Archive created without errors.
- Import completes successfully in GitLab.

Repackage the files using [[commands/tar-create-archive]]:

```bash
tar -zcvf service_template.tar.gz project.json VERSION project.bundle
```

Then upload and import the new tar.gz file into GitLab.

### Step 4: Verify Injection - [[procedures/Verify-Injected-Service-Template-in-New-Project]]

**Procedure**: [[procedures/Verify-Injected-Service-Template-in-New-Project]]

**Objective**: Create a new project as another user and confirm the malicious template is applied.

**Expected Output**: Exported project.json from the new project shows the injected service.

**Success Indicators**:
- New project automatically inherits the template.
- Verification export confirms presence of MockCiService as template.

Sign in as another user, create a new project, immediately export it, extract the archive, and observe the injected service in project.json.

## Attack Chain Summary

### Key Achievements

1. Successful injection of malicious service template without admin privileges.
2. Automatic application to all new projects, enabling data exfiltration and mutation.
3. Compromise of confidentiality, integrity, and availability across the GitLab instance.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Abuse Elevation Control Mechanism]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Persistence]]
- [[Collection]]

*Last updated: [TIMESTAMP]*

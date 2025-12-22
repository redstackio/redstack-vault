---
tags:
  - xss
  - gitlab
  - ci-cd
  - dompurify
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Malicious-GitLab-CI-YAML]]'
  - '[[procedures/Run-CI-Jobs-in-GitLab]]'
  - '[[procedures/Erase-Job-Logs-to-Prepare-Trigger]]'
  - '[[procedures/Retry-Job-to-Generate-Error]]'
  - '[[procedures/Trigger-XSS-via-Error-Message-Interaction]]'
step_count: 5
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:39.303Z'
description: >-
  Multi-stage XSS attack exploiting GitLab's v-safe-html directive failure to
  sanitize data-disable-with attributes in CI job error messages, allowing
  arbitrary JavaScript execution when victims interact with the UI.
skill_level: intermediate
impact_level: high
id: 50ba8e7e-7334-4c3c-9f18-74fb4c1781fc
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# GitLab XSS via Unsanitized CI Job Names in Error Messages

Multi-stage attack chain demonstrating exploitation of an XSS vulnerability in GitLab's CI/CD interface. The attack leverages unsanitized user-controlled job names in error messages, bypassing Dompurify sanitization in the v-safe-html directive by injecting payloads into the data-disable-with attribute. This allows arbitrary JavaScript execution or form submissions when administrators or users interact with job interfaces, potentially leading to privilege escalation via API requests.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Malicious YAML] --> B[Run CI Jobs]
    B --> C[Erase Logs]
    C --> D[Retry Job]
    D --> E[Trigger XSS in Error]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- GitLab project access (developer or higher permissions)
- Text editor for YAML creation

### Target Environment

- GitLab instance (self-hosted or SaaS)
- CI/CD pipeline enabled
- Web browser for UI interaction

### Initial Access Requirements

- Valid GitLab account with project creation rights
- No special privileges needed initially; escalates via XSS

## Detailed Attack Procedures

### Step 1: Create Malicious YAML
procedure: [[procedures/Create-Malicious-GitLab-CI-YAML]]

**Objective**: Inject XSS payloads into CI job names to prepare for unsanitized display in error messages.

**Instructions**: Create a .gitlab-ci.yml file with job names containing payloads that exploit the data-disable-with attribute. Commit and push to the repository.

**Expected Output**: YAML file committed, jobs defined with malicious names.

**Success Indicators**:
- YAML validates without syntax errors
- Jobs appear in CI/CD pipeline

### Step 2: Run CI Jobs
procedure: [[procedures/Run-CI-Jobs-in-GitLab]]

**Objective**: Execute the pipeline to process the malicious job names.

**Instructions**: Trigger the pipeline via GitLab UI or push. Wait for jobs to complete.

**Expected Output**: Jobs run successfully, logs generated.

**Success Indicators**:
- Pipeline status shows passed
- Job details viewable in UI

### Step 3: Erase Job Logs
procedure: [[procedures/Erase-Job-Logs-to-Prepare-Trigger]]

**Objective**: Remove artifacts from a specific job to set up dependency failure for error trigger.

**Instructions**: Navigate to the vulnerable job's details and click the trash icon to erase logs and artifacts.

**Expected Output**: Confirmation of deletion, artifacts removed.

**Success Indicators**:
- Job logs cleared
- Artifacts no longer available

### Step 4: Retry Dependent Job
procedure: [[procedures/Retry-Job-to-Generate-Error]]

**Objective**: Attempt to rerun a job dependent on the erased one to force an error message containing the malicious job name.

**Instructions**: Go to the dependent job list, select the job, and click Retry.

**Expected Output**: Error dialog appears referencing the missing artifact job.

**Success Indicators**:
- Retry fails with artifact retrieval error
- Malicious job name displayed in error text

### Step 5: Interact to Trigger XSS
procedure: [[procedures/Trigger-XSS-via-Error-Message-Interaction]]

**Objective**: Cause the victim (e.g., admin) to trigger the payload by clicking in the error interface.

**Instructions**: In the error message, any click (e.g., on the overlay link) executes the injected JavaScript via data-disable-with.

**Expected Output**: Alert pops or form submits (e.g., alert(document.domain)).

**Success Indicators**:
- JavaScript executes (alert fires)
- Potential privilege escalation if form payload used

## Attack Chain Summary

### Key Achievements

1. Bypassed Dompurify sanitization using data-disable-with attribute
2. Achieved arbitrary JS execution in GitLab UI without CSP bypass
3. Demonstrated potential for admin privilege escalation via API form submission

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Execution]]

---

*Last updated: 2023-10-01T00:00:00Z*

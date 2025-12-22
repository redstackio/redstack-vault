---
tags:
  - xss
  - stored-xss
  - gitlab
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-GitLab-Project-and-Branch]]'
  - '[[procedures/Inject-XSS-in-GitLab-Merge-Request]]'
step_count: 16
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T00:11:09.126Z'
description: >-
  A multi-stage attack exploiting a Stored XSS vulnerability in GitLab's merge
  request creation by injecting malicious JavaScript through the source_branch
  parameter, leading to arbitrary code execution on viewing users' browsers.
skill_level: intermediate
impact_level: high
id: eed9e323-500f-4a75-ad5d-4d6b162ea806
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Stored XSS Injection via GitLab Merge Request Source Branch Parameter

Multi-stage attack chain demonstrating exploitation of a Stored XSS vulnerability in GitLab's merge request creation process.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 16 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access: Authenticate and Setup Project] --> B[Preparation: Create Branch]
    B --> C[Execution: Create Merge Request and Intercept]
    C --> D[Exploitation: Inject XSS Payload]
    D --> E[Impact: Arbitrary JS Execution on Viewers]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#e67e22
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- GitLab instance (Ruby on Rails-based)
- Web browser for navigation
- Valid user credentials for GitLab

### Initial Access Requirements

- Authenticated access to GitLab dashboard
- Network access to the GitLab host
- No prior project access needed, but developer/maintainer role assumed for merge requests

## Detailed Attack Procedures

### Step 1: Authenticate to GitLab
procedure: [[procedures/Create-GitLab-Project-and-Branch]]

**Objective**: Gain access to the GitLab instance to begin project setup.

**Instructions**: Sign in using valid credentials via the GitLab login page.

**Expected Output**: Redirect to the dashboard upon successful authentication.

**Success Indicators**:
- User session established
- Access to project creation menu visible

### Step 2: Access Project Creation
procedure: [[procedures/Create-GitLab-Project-and-Branch]]

**Objective**: Navigate to initiate a new project for the attack setup.

**Instructions**: Click the '[+]' icon on the dashboard to open the project creation menu, then select 'New Project'.

**Expected Output**: Project creation form loads.

**Success Indicators**:
- Form fields for project name and visibility appear

### Step 3: Initiate Project Creation
procedure: [[procedures/Create-GitLab-Project-and-Branch]]

**Objective**: Start the project setup process.

**Instructions**: Proceed with filling the project details.

**Expected Output**: Form ready for input.

**Success Indicators**:
- 'Create project' button enabled

### Step 4: Enter Project Name
procedure: [[procedures/Create-GitLab-Project-and-Branch]]

**Objective**: Specify the project identifier.

**Instructions**: Input 'test-project' in the 'Project name' field.

**Expected Output**: Project name validated.

**Success Indicators**:
- No validation errors

### Step 5: Set Project Visibility
procedure: [[procedures/Create-GitLab-Project-and-Branch]]

**Objective**: Configure project access level.

**Instructions**: Select the 'Public' radio button.

**Expected Output**: Visibility option confirmed.

**Success Indicators**:
- Public option highlighted

### Step 6: Initialize Repository
procedure: [[procedures/Create-GitLab-Project-and-Branch]]

**Objective**: Prepare the repository with initial content.

**Instructions**: Check the 'Initialize repository with a README' checkbox.

**Expected Output**: Initialization option enabled.

**Success Indicators**:
- Checkbox ticked

### Step 7: Submit Project Creation
procedure: [[procedures/Create-GitLab-Project-and-Branch]]

**Objective**: Create the project in GitLab.

**Instructions**: Click the 'Create project' button to submit the form.

**Expected Output**: New project dashboard loads.

**Success Indicators**:
- Project 'test-project' appears in the namespace

### Step 8: Navigate to Branch Creation
procedure: [[procedures/Create-GitLab-Project-and-Branch]]

**Objective**: Set up the source branch for the merge request.

**Instructions**: Go to the URL `http(s)://{GitLab host}/{user id}/test-project/branches/new`.

**Expected Output**: New branch form loads.

**Success Indicators**:
- Branch name and source fields visible

### Step 9: Configure Branch Details
procedure: [[procedures/Create-GitLab-Project-and-Branch]]

**Objective**: Define the new branch parameters.

**Instructions**: Enter 'test-branch' as the branch name and select 'master' as 'Create from'.

**Expected Output**: Form fields populated.

**Success Indicators**:
- No input errors

### Step 10: Create the Branch
procedure: [[procedures/Create-GitLab-Project-and-Branch]]

**Objective**: Generate the branch from the master.

**Instructions**: Click the 'Create branch' button.

**Expected Output**: Branch 'test-branch' listed in the repository.

**Success Indicators**:
- Success message or branch visible in branches list

### Step 11: Access Merge Requests
procedure: [[procedures/Inject-XSS-in-GitLab-Merge-Request]]

**Objective**: Prepare to create the vulnerable merge request.

**Instructions**: Navigate to `http://{GitLab host}/{user id}/test-project/merge_requests`.

**Expected Output**: Merge requests page loads.

**Success Indicators**:
- 'Create merge request' button present

### Step 12: Initiate Merge Request
procedure: [[procedures/Inject-XSS-in-GitLab-Merge-Request]]

**Objective**: Start the merge request workflow.

**Instructions**: Click 'Create merge request'.

**Expected Output**: Merge request form appears.

**Success Indicators**:
- Form for source/target branches visible

### Step 13: Proceed to Submission
procedure: [[procedures/Inject-XSS-in-GitLab-Merge-Request]]

**Objective**: Trigger the HTTP request for interception.

**Instructions**: Click 'Submit merge request' to send the request.

**Expected Output**: Request intercepted if proxy is active.

**Success Indicators**:
- Proxy captures the POST request

### Step 14: Intercept the Request
procedure: [[procedures/Inject-XSS-in-GitLab-Merge-Request]]

**Objective**: Capture the merge request submission for modification.

**Instructions**: Use [[tools/Burp-Suite]] to intercept the outgoing HTTP POST request.

**Expected Output**: Request paused in proxy.

**Success Indicators**:
- Request body visible, including merge_request[source_branch]

### Step 15: Modify Source Branch Parameter
procedure: [[procedures/Inject-XSS-in-GitLab-Merge-Request]]

**Objective**: Inject the XSS payload into the parameter.

**Instructions**: Change the value of 'merge_request[source_branch]' to '<img/src=x onerror=alert(1)>' in the request body.

**Expected Output**: Modified parameter saved in proxy.

**Success Indicators**:
- Payload reflected in the intercepted request

### Step 16: Forward Modified Request
procedure: [[procedures/Inject-XSS-in-GitLab-Merge-Request]]

**Objective**: Submit the tampered request to exploit the vulnerability.

**Instructions**: Send the modified request to the server using the proxy.

**Expected Output**: Merge request created with injected payload; alert(1) triggers when viewed.

**Success Indicators**:
- Merge request page loads with XSS execution (e.g., alert popup)
- Other users viewing the MR execute the JS

## Attack Chain Summary

### Key Achievements

1. Successful project and branch setup in GitLab without detection.
2. Injection of Stored XSS payload via intercepted merge request parameter.
3. Achievement of arbitrary JavaScript execution for potential session hijacking or data theft.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---

*Last updated: 2023-10-01T00:00:00Z*

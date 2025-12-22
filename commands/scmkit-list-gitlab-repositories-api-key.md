---
id: 8c51801f-6ef9-430a-8ee1-b2413c44bc6d
name: scmkit-list-gitlab-repositories-api-key
type: command
executor: bash
data: SCMKit.exe -s gitlab -m listrepo -c $_API_KEY -u $_GITLAB_URL
output: null
created_at: '2023-04-06T03:56:25.111741+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - discovery
  - enumeration
verified: true
validated: true
---

# scmkit-list-gitlab-repositories-api-key

## Command

```bash
SCMKit.exe -s gitlab -m listrepo -c $_API_KEY -u $_GITLAB_URL
```

## Description

This command uses SCMKit to list all accessible repositories in a GitLab instance using an API key for authentication. It is useful for initial discovery of projects and their metadata.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -s gitlab | Specifies the SCM system as GitLab | Yes |
| -m listrepo | Mode to list repositories | Yes |
| -c $_API_KEY | API key for authentication | Yes |
| -u $_GITLAB_URL | URL of the GitLab instance (e.g., https://gitlab.example.com) | Yes |

## Examples

### Basic Usage

```bash
SCMKit.exe -s gitlab -m listrepo -c glpat-abc123 -u https://gitlab.example.com
```

### Advanced Usage

Not applicable; this is a basic enumeration command.

## Expected Output

JSON array of repositories:
```
{
  "projects": [
    {
      "id": 1,
      "name": "project1",
      "path_with_namespace": "group/project1"
    }
  ]
}
```

## Related

- [[procedures/GitLab-Repository-Enumeration-and-Search]]
- [[commands/scmkit-list-gitlab-repositories-username-password]]

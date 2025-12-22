---
data: /move <full path of any other project>
tags:
  - gitlab
  - quick-action
type: command
executor: gitlab
platforms:
  - Web
  - GitLab
id: 7313a76c-cdab-4e8b-86b9-b5d1b94f1af8
created_at: '2025-12-06T06:57:46.337Z'
updated_at: '2025-12-06T06:57:46.337Z'
verified: false
validated: true
submitted: true
---
# gitlab-move-quick-action

## Command

```bash
/move <full path of any other project>
```

## Description

This GitLab Quick Action command attempts to move an issue to another project, but due to the vulnerability, it triggers serialization of the target project's model, exposing sensitive data in the response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `<full path of any other project>` | The namespace and path of the target project (e.g., namespace/project) | Yes |

## Examples

### Basic Usage

```bash
/move group/target-project
```

### Advanced Usage

Use in combination with monitoring tools to capture the response.

## Expected Output

JSON response with serialized project data, including errors if the move is invalid, but exposing attributes like runners_token.

## Related

- [[Execute GitLab Move Quick Action]]

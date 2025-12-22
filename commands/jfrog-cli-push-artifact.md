---
data: jfrog rt upload test-file.txt repo-name/
tags:
  - artifactory
  - upload
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: b80e9f9b-a22f-4ccd-ad29-c3aa30e32444
created_at: '2025-12-11T03:47:56.518Z'
updated_at: '2025-12-11T03:47:56.518Z'
verified: false
validated: true
submitted: true
---
# jfrog-cli-push-artifact

## Command

```bash
jfrog rt upload test-file.txt repo-name/
```

## Description

Uploads a file to a JFrog Artifactory repository, demonstrating write access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `test-file.txt` | File to upload | Yes |
| `repo-name/` | Target repository path | Yes |

## Examples

### Basic Usage

```bash
jfrog rt upload test-file.txt repo-name/
```

### Advanced Usage

```bash
jfrog rt upload --recursive dir/ repo-name/
```

## Expected Output

Upload summary with status, e.g., 'Uploaded 1 artifacts.'

## Related

- [[commands/jfrog-cli-login]]
- [[procedures/Access-and-Manipulate-JFrog-Artifactory-Instance]]

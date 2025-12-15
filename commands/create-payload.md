---
id: cmd-uuid-003
data: 'echo ''{"body": "Updated comment exploiting PAT scope flaw."}'' > update.json'
tags:
  - json
  - payload
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-12-01T00:00:00Z'
updated_at: '2025-12-14T17:29:44.687Z'
verified: false
validated: true
submitted: true
---
# create-payload

## Command

```bash
echo '{"body": "Updated comment exploiting PAT scope flaw."}' > update.json
```

## Description

This command generates a JSON payload file for use in GitHub API requests, specifically for updating issue comment bodies.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `echo '{"body": "..."}'` | JSON string with new body | Yes |
| `> update.json` | Redirects output to file | Yes |

## Examples

### Basic Usage

```bash
echo '{"body": "Test update"}' > payload.json
```

### Advanced Usage

```bash
cat > payload.json << EOF
{"body": "Multi-line\nupdated content"}
EOF
```

## Expected Output

Creates a file update.json with the JSON content. Verify with cat update.json.

## Related

- [[commands/github-api-update-comment]]
- [[procedures/Exploit-GitHub-PAT-for-Issue-Comment-Modification]]

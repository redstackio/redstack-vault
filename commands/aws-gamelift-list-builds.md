---
type: command
executor: bash
data: aws gamelift list-builds
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - aws
  - gamelift
  - discovery
verified: true
validated: true
---

# aws-gamelift-list-builds

## Command

```bash
aws gamelift list-builds
```

## Description

Lists all game server builds in AWS GameLift. This command tests read permissions for GameLift resources, useful for verifying if credentials can access gaming infrastructure during cloud enumeration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | No parameters; paginates automatically if needed | No |

## Examples

### Basic Usage

```bash
aws gamelift list-builds
```

### With Max Results

```bash
aws gamelift list-builds --max-results 10
```

## Expected Output

JSON like {"Builds": [{"BuildId": "build-abc123", "Name": "GameServerBuild", "Status": "INITIALIZED"}]}. Empty array if no builds; error if denied.

## Related

- [[procedures/AWS-IAM-Permissions-Enumeration]]

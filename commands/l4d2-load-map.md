---
data: map c1m1_hotel
tags:
  - gaming
  - exploit
type: command
executor: bash
platforms:
  - Windows
  - MacOS
  - Linux
id: 960aa971-deb7-460f-9b21-6f937d97eff1
created_at: '2025-12-11T03:46:01.592Z'
updated_at: '2025-12-11T03:46:01.592Z'
verified: false
validated: true
submitted: true
---
# l4d2-load-map

## Command

```bash
map c1m1_hotel
```

## Description

Loads the specified map in Left 4 Dead 2 via the developer console, triggering the loading and parsing of the associated NAV file, which can exploit a buffer overflow if the file is malformed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `c1m1_hotel` | The name of the map to load, including the malformed NAV file | Yes |

## Examples

### Basic Usage

```bash
map c1m1_hotel
```

### Advanced Usage

```bash
map c1m1_hotel nav
```

## Expected Output

The game attempts to load the map, resulting in a buffer overflow where EIP becomes 0x41414102 if exploiting the vulnerability.

## Related

- [[procedures/Exploit-Buffer-Overflow-in-Left-4-Dead-2-NAV-Parsing]]
- [[tools/Developer-Console]]

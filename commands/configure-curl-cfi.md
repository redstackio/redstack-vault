---
data: >-
  ./configure CC=clang CXX=clang++ LD=clang CFLAGS="-fsanitize=cfi
  -fvisibility=hidden -fuse-ld=gold -flto" CXXFLAGS="-fsanitize=cfi
  -fvisibility=hidden -fuse-ld=gold -flto" LDFLAGS="-fsanitize=cfi
  -fvisibility=hidden -fuse-ld=gold -flto" --disable-shared
tags:
  - configure
  - cfi
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:31.006Z'
id: 5456006c-c9c9-4b6e-8fe7-d584fcfdc8af
verified: false
validated: true
submitted: true
---
# Configure Curl CFI

## Command

```bash
./configure CC=clang CXX=clang++ LD=clang CFLAGS="-fsanitize=cfi -fvisibility=hidden -fuse-ld=gold -flto" CXXFLAGS="-fsanitize=cfi -fvisibility=hidden -fuse-ld=gold -flto" LDFLAGS="-fsanitize=cfi -fvisibility=hidden -fuse-ld=gold -flto" --disable-shared
```

## Description

Configures curl build with Clang CFI flags.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| CC=clang | C compiler | Yes |
| CFLAGS=... | CFI flags | Yes |
| --disable-shared | Static build | Yes |

## Examples

### Basic Usage

```bash
./configure CC=clang ... --disable-shared
```

## Expected Output

Configuration summary for CFI.

## Related

- [[commands/make-curl]]

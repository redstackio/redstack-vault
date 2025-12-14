---
id: cmd-clang-libcurl-001
data: >-
  git clone https://github.com/curl/curl.git && cd curl && ./configure
  --enable-debug --with-nghttp2 && make clean && make
tags:
  - compilation
  - libcurl
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:18.495Z'
verified: false
validated: true
submitted: true
---
# clang-compile-libcurl-asan

## Command

```bash
git clone https://github.com/curl/curl.git && cd curl && ./configure --enable-debug --with-nghttp2 && make clean && make
```

## Description

Clones, configures, and compiles libcurl from source with debug and HTTP/2 support, preparing for ASAN integration in subsequent builds.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--enable-debug` | Enables debug symbols | Yes |
| `--with-nghttp2` | Enables HTTP/2 | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/curl/curl.git && cd curl && ./configure --enable-debug --with-nghttp2 && make clean && make
```

### Advanced Usage

Add CFLAGS for ASAN in configure if needed: `./configure CFLAGS='-fsanitize=address' ...`

## Expected Output

Build logs ending with "libcurl built successfully", producing libcurl.so or .a in src/ directory.

## Related

- [[commands/clang-compile-curl-cpp-asan]]

---
data: >-
  make clean && CC=clang CFLAGS="-fsanitize=address -g"
  LDFLAGS="-fsanitize=address" ./configure --enable-debug --disable-all && make
  -j$(nproc)
tags:
  - compilation
  - sanitizer
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:13.032Z'
id: 545aa800-7ad3-467f-9b03-b78e417a2a6a
verified: false
validated: true
submitted: true
---
# compile-php-asan

## Command

```bash
make clean && CC=clang CFLAGS="-fsanitize=address -g" LDFLAGS="-fsanitize=address" ./configure --enable-debug --disable-all && make -j$(nproc)
```

## Description

This command sequence cleans the PHP build directory, configures the source with AddressSanitizer for memory error detection, and compiles the PHP binary on Linux. Use it when auditing PHP internals for vulnerabilities like buffer overflows.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `CC=clang` | Sets compiler to Clang (supports ASan) | Yes |
| `CFLAGS="-fsanitize=address -g"` | Enables ASan and debug symbols | Yes |
| `LDFLAGS="-fsanitize=address"` | Links ASan runtime | Yes |
| `--enable-debug` | Includes debug features | Yes |
| `--disable-all` | Builds minimal PHP to speed up | No |
| `-j$(nproc)` | Uses all CPU cores for parallel build | No |

## Examples

### Basic Usage

```bash
make clean && CC=clang CFLAGS="-fsanitize=address" ./configure && make
```

### Advanced Usage

```bash
export CC=clang && make clean && CFLAGS="-fsanitize=address -g -O0" LDFLAGS="-fsanitize=address" ./configure --enable-cli && make -j4
```

## Expected Output

Configuration logs followed by build progress; ends with "Build complete."

## Related

- [[Related Procedure|procedures/Compile-PHP-with-AddressSanitizer]]

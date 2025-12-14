---
id: d4e5f6g7-h8i9-0123-defg-456789012345
data: |
  |
    gcc -fsanitize=address -g -o mrb mrbgems/mruby-build/build/lib/libmruby.a vm.c
tags:
  - build
  - asan
  - mrbuby
type: command
output: 'Compilation successful, binary mrb built with ASAN instrumentation.'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:36.945Z'
verified: false
validated: true
submitted: true
---
# build-mruby-with-asan

## Command

```bash
gcc -fsanitize=address -g -o mrb mrbgems/mruby-build/build/lib/libmruby.a vm.c
```

## Description

Compiles the MRuby engine with AddressSanitizer (ASAN) enabled using GCC on Linux x64 to detect memory errors such as null pointer dereferences during runtime testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -fsanitize=address | Enables ASAN for memory error detection | Yes |
| -g | Includes debug symbols for backtraces | Yes |
| vm.c | Source file containing the vulnerable mrb_obj_instance_eval | Yes |

## Examples

### Basic Usage

```bash
gcc -fsanitize=address -g -o mrb mrbgems/mruby-build/build/lib/libmruby.a vm.c
```

### Advanced Usage

```bash
gcc -fsanitize=address,undefined -g -O0 -o mrb mrbgems/mruby-build/build/lib/libmruby.a vm.c
```

## Expected Output

Successful compilation output, producing an executable 'mrb' instrumented for ASAN. No errors if dependencies are met.

## Related

- [[Related Procedure|procedures/Trigger-MRuby-Segmentation-Fault-with-PoC-Script]]

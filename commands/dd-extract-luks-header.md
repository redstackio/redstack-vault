---
type: command
executor: bash
data: dd if=$_INPUT_FILE of=$_OUTPUT_FILE bs=512 count=$_BLOCK_COUNT
output: |-
  root@kali:~# dd if=backup.img of=luks_header.bin bs=512 count=4097
  4097+0 records in
  4097+0 records out
  2097664 bytes (2.1 MB, 2.0 MiB) copied, 0.0162948 s, 129 MB/s
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - cryptography
  - luks
  - extraction
verified: true
validated: true
---

# dd-extract-luks-header

## Command

```bash
dd if=$_INPUT_FILE of=$_OUTPUT_FILE bs=512 count=$_BLOCK_COUNT
```

## Description

This command uses the `dd` utility to extract the LUKS header (including key material and slots) from the start of an encrypted disk image or device. It reads up to the payload offset plus one block, producing a file suitable for offline analysis or cracking with tools like Hashcat. This is useful in forensics or red team scenarios to recover encryption metadata without mounting the volume.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_INPUT_FILE | Path to the input LUKS-encrypted image or device (e.g., /dev/sda1 or backup.img) | Yes |
| $_OUTPUT_FILE | Path for the output header file (e.g., luks_header.bin) | Yes |
| $_BLOCK_COUNT | Number of 512-byte blocks to read (typically the payload offset + 1, e.g., 4097 for standard LUKS1) | Yes |
| bs=512 | Block size in bytes (standard for LUKS headers) | Built-in |
| count=$_BLOCK_COUNT | Limits the read to the specified number of blocks | Built-in |

## Examples

### Basic Usage

```bash
dd if=backup.img of=luks_header.bin bs=512 count=4097
```

Extracts the header from a disk image named backup.img.

### Advanced Usage

```bash
dd if=/dev/sda1 of=luks_header.bin bs=512 count=4097 status=progress
```

Extracts from a live device with progress indication; requires root privileges.

## Expected Output

```
root@kali:~# dd if=backup.img of=luks_header.bin bs=512 count=4097
4097+0 records in
4097+0 records out
2097664 bytes (2.1 MB, 2.0 MiB) copied, 0.0162948 s, 129 MB/s
```

No errors indicate successful extraction. Verify the output file size matches expected bytes (e.g., 4097 * 512 = ~2MB) and inspect with `hexdump` or `file` for LUKS signature (LUKS±±).

## Related

- [[tools/cryptsetup]]

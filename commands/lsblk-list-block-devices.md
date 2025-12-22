---
type: command
executor: bash
data: lsblk
tags:
  - linux
  - storage
platforms:
  - Linux
verified: true
validated: true
---

# lsblk-list-block-devices

## Command

```bash
lsblk
```

## Description

Lists information about block devices, including partitions and mount points, to identify newly attached volumes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Displays tree view of devices | N/A |

## Examples

### Basic Usage

```bash
lsblk
```

### Advanced Usage

With output format:

```bash
lsblk -o NAME,SIZE,TYPE,MOUNTPOINT
```

## Expected Output

Tree-like list:

```
NAME    MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
xvda    202:0    0   20G  0 disk 
└─xvda1 202:1    0   20G  0 part /
xvdf    202:80   0  100G  0 disk 
```

## Related

- [[commands/file-identify-filesystem]]
- [[procedures/AWS-Extract-EBS-Backup-to-EC2-Instance]]

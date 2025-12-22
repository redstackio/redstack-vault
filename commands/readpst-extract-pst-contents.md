---
type: command
executor: bash
data: readpst -tea -m $_FILENAME.pst
output: |-
  root@kali:~# readpst -tea -m backup.pst
  Opening PST file and indexes...
  Processing Folder "Deleted Items"
          "backup" - 2 items done, 0 items skipped.
created_at: '2019-12-13T22:39:54.282259+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - extraction
  - pst
verified: true
validated: true
---

# readpst-extract-pst-contents

## Command

```bash
readpst -tea -m $_FILENAME.pst
```

## Description

This command uses the readpst utility to extract emails, attachments, and folder structures from a Microsoft Outlook PST file. It outputs individual text files for each email, saves attachments to a dedicated folder, and generates an mbox file for importing all emails into compatible clients. This is ideal for post-exploitation data collection, forensic analysis, or red team operations when processing exfiltrated PST archives on Linux systems to reveal sensitive communications or credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-t` | Output emails as separate text files | Yes |
| `-e` | Create individual files for each email (used with -t) | Yes |
| `-a` | Extract attachments to a dedicated folder | Yes |
| `-m` | Generate an mbox file containing all emails | Yes |
| `$_FILENAME.pst` | Path to the input PST file (e.g., backup.pst) | Yes |
| `-o <dir>` (optional) | Custom output directory; defaults to a folder named after the PST file | No |

## Examples

### Basic Usage

```bash
readpst -tea -m example.pst
```

This processes `example.pst` and creates an `example/` directory with extracted content.

### Advanced Usage

```bash
readpst -tea -m -o /tmp/pst_analysis example.pst
```

Specify a custom output directory with `-o` for better organization in analysis workflows.

## Expected Output

Description of what output to expect when the command runs successfully.

```
root@kali:~# readpst -tea -m backup.pst
Opening PST file and indexes...
Processing Folder "Deleted Items"...
Processing Folder "Inbox"...
        "backup" - 2 items done, 0 items skipped.
Appended 2 messages to mbox file.
```

The command logs progress by processing each folder, ending with a summary of items handled. Verify success by checking the output directory for:
- `backup.mbox`: Bulk email archive.
- Numbered text files (e.g., `000001`): Individual email content.
- `attachments/` folder: Extracted files like PDFs or images.

## Related

- [[procedures/Extract-Emails-and-Attachments-from-PST-Files]]
- [[tools/readpst]]

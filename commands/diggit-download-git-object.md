---
id: 3a25a716-8855-491a-ad5e-d9144019e4eb
name: diggit-download-git-object
type: command
executor: bash
data: >-
  ./diggit.py -u remote_git_repo -t temp_folder -o object_hash [-r=True]

  ./diggit.py -u http://web.site -t /path/to/temp/folder/ -o
  d60fbeed6db32865a1f01bb9e485755f085f51c1


  -u is remote path, where .git folder exists

  -t is path to local folder with dummy Git repository and where blob content
  (files) are saved with their real names (cd /path/to/temp/folder && git init)

  -o is a hash of particular Git object to download
output: null
created_at: '2023-04-06T03:55:59.928908+00:00'
updated_at: '2023-04-10T20:33:56.614609+00:00'
platforms:
  - Linux
tags:
  - git
  - download
  - object
verified: true
validated: true
---

# diggit-download-git-object

## Command

```bash
./diggit.py -u $_REMOTE_REPO -t $_TEMP_FOLDER -o $_OBJECT_HASH [-r]
```

## Description

This command uses diggit.py to download a specific Git object by hash from a remote repository's .git directory, saving blobs to a local dummy Git repo. Useful for targeted extraction of sensitive files without full cloning.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u $_REMOTE_REPO | URL to the remote .git directory (e.g., http://example.com/.git) | Yes |
| -t $_TEMP_FOLDER | Local path for dummy Git repo (run 'git init' there first) | Yes |
| -o $_OBJECT_HASH | SHA-1 hash of the Git object to download | Yes |
| -r | Flag to recover deleted objects | No |

## Examples

### Basic Usage

```bash
./diggit.py -u http://web.site -t /path/to/temp/folder/ -o d60fbeed6db32865a1f01bb9e485755f085f51c1
```

### Advanced Usage (Recover Deleted)

```bash
./diggit.py -u http://web.site -t /path/to/temp/folder/ -o d60fbeed6db32865a1f01bb9e485755f085f51c1 -r
```

## Expected Output

Downloading object d60fbeed6db32865a1f01bb9e485755f085f51c1 from http://web.site/.git
Object type: blob
Saved to /path/to/temp/folder/[filename]

(Files appear in temp folder with original names if blobs; errors if hash invalid or access denied)

## Related

- [[procedures/Download-Git-Repository-Object-Using-Diggit]]
- [[tools/diggit]]

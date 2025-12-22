---
data: >-
  if(stat(filename, &sb) == -1 || !S_ISREG(sb.st_mode)) { /* a non-regular file,
  fallback to direct fopen() */ *fh = fopen(filename, FOPEN_WRITETEXT); ... }
tags:
  - toctou
  - vulnerable-code
type: command
executor: c
platforms:
  - Linux
id: 71000b43-7ddc-47e2-a759-d041ae2efb2d
created_at: '2025-12-14T17:24:22.163Z'
updated_at: '2025-12-14T17:24:22.163Z'
verified: false
validated: true
submitted: true
---
# stat-and-fopen-in-curlfopen

## Command

```c
if(stat(filename, &sb) == -1 || !S_ISREG(sb.st_mode)) { /* a non-regular file, fallback to direct fopen() */ *fh = fopen(filename, FOPEN_WRITETEXT); ... }
```

## Description

Core vulnerable code snippet from libcurl's Curl_fopen function, checking if a file is regular via stat before falling back to fopen for writing, creating a TOCTOU race window exploitable by symlink/directory swaps.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| filename | Path to the file being opened (e.g., 'a') | Yes |
| &sb | Pointer to stat buffer for file info | Yes |
| FOPEN_WRITETEXT | Mode string for text write ('w') | Yes |

## Examples

### Basic Usage

```c
stat("a", &sb); if (!S_ISREG(sb.st_mode)) fopen("a", "w");
```

### Advanced Usage

```c
// In context of cookie-jar
if (stat(cookie_file, &sb) == -1 || !S_ISREG(sb.st_mode)) {
    *fh = fopen(cookie_file, FOPEN_WRITETEXT);
}
```

## Expected Output

If stat fails or file is non-regular (e.g., directory), returns file handle from fopen; vulnerable to type change between calls, resulting in unintended file writes.

## Related

- [[commands/curl-cookie-jar-exploit]]
- [[procedures/Trigger-libcurl-with-Cookie-Jar]]

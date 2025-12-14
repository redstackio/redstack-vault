---
id: cmd-001-curl-listing
data: 'curl -s http://target.example.com/ | grep -E ''<a href="[^/]*?/?">'''
tags:
  - reconnaissance
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:31.532Z'
verified: false
validated: true
submitted: true
---
# curl-directory-listing

## Command

```bash
curl -s http://target.example.com/ | grep -E '<a href="[^/]*?/?">'
```

## Description

This command uses curl to fetch the HTTP response from a target directory URL and pipes it to grep to extract HTML links, revealing directory listings if enabled. It is used during web reconnaissance to enumerate exposed files and subdirectories without authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode: Suppress progress meter and error messages | Yes |
| `http://target.example.com/` | The target URL (e.g., root or subdirectory path) | Yes |
| `grep -E '<a href="[^/]*?/?">'` | Regular expression to match anchor tags for links (directories end with /) | Yes |

## Examples

### Basic Usage

```bash
curl -s http://irc.parrotsec.org/ | grep -E '<a href="[^/]*?/?">'
```

### Advanced Usage

```bash
curl -s -A "Mozilla/5.0" http://irc.parrotsec.org/caine/ | grep -E '<a href="[^/]*?/?">' | awk -F'">' '{print $2}' | sed 's/<\/a>//'
```

This adds a user-agent header to mimic a browser and cleans up output to show just directory names.

## Expected Output

Successful execution returns lines like:

`<a href="caine/">caine/</a> 2023-09-15 12:00`

`<a href="direct/">direct/</a> 2023-08-20 10:30`

`<a href="parrot/">parrot/</a> 2023-07-10 14:45`

Indicating enumerated directories with timestamps. If no listing, output may be empty or show a 403/404 error.

## Related

- [[Related Procedure|procedures/Exploit-Directory-Listing-for-Enumeration]]

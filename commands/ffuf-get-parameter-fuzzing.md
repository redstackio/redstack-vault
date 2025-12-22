---
type: command
executor: bash
data: >
  ffuf -w /path/to/paramnames.txt -u
  https://target.com/script.php?FUZZ=test_value -fs 4242
output: null
tags:
  - fuzzing
  - parameter-discovery
platforms:
  - Linux
  - Web
created_at: '2020-07-24T17:11:28.829249+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
verified: true
validated: true
---

# ffuf-get-parameter-fuzzing

## Command

```bash
ffuf -w /path/to/paramnames.txt -u https://target.com/script.php?FUZZ=test_value -fs 4242
```

## Description

This command fuzzes potential GET parameter names in a URL query string to identify undocumented or injectable parameters on a web endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -w | Path to wordlist of parameter names | Yes |
| -u | Target URL with FUZZ as the parameter placeholder | Yes |
| -fs | Size of responses to filter (e.g., error page size) | No |
| FUZZ | Position in URL for substituting parameter names | Yes |

## Examples

### Basic Usage

```bash
ffuf -w paramnames.txt -u https://example.com/page.php?FUZZ=value
```

### Advanced Usage

```bash
ffuf -w params.txt -u https://target.com/api?FUZZ=1 -fs 4242 -mc 200,302
```

## Expected Output

```
        /'___\/___\
       /\      /\ 
      ... (ffuf banner) ...

id                    [Status: 200, Size: 5678, Words: 123]
file                  [Status: 403, Size: 4242, Words: 10] (filtered)
...
```

Discovered parameters shown with response details; unfiltered or varying sizes indicate potential valid params.

## Related

- [[procedures/Directory-and-Parameter-Fuzzing-with-Ffuf]]
- [[tools/Ffuf]]

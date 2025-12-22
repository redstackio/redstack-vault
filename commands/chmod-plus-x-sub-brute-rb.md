---
id: c7d79ab9-a2ba-47a0-ab4c-db053827b487
name: chmod-plus-x-sub-brute-rb
type: command
executor: bash
data: chmod +x sub_brute.rb
output: null
created_at: '2023-04-06T03:56:25.800792+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - setup
verified: true
validated: true
---

# chmod-plus-x-sub-brute-rb

## Command

```bash
chmod +x sub_brute.rb
```

## Description

This command sets execute permissions on the sub_brute.rb Ruby script, allowing it to be run directly as ./sub_brute.rb. Run this after cloning the Hostile Subdomain Bruteforcer repository and navigating to its directory.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| +x | Adds execute permission for owner | Yes |
| sub_brute.rb | Target script file | Yes |

## Examples

### Basic Usage

```bash
chmod +x sub_brute.rb
```

### For All Users

```bash
chmod a+x sub_brute.rb
```

## Expected Output

(No output; permission change is silent. Verify with `ls -l sub_brute.rb` showing executable bit set.)

## Related

- [[procedures/Subdomain-Enumeration-and-Takeover-using-Hostile-Subdomain-Bruteforcer]]
- [[tools/Hostile-Subdomain-Bruteforcer]]

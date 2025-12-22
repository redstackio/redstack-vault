---
id: 01316d4a-2703-4ac4-a9b0-cf1c9e9977a7
name: install-aquatone-via-gem
type: command
executor: bash
data: gem install aquatone
output: null
created_at: '2023-04-06T03:56:25.578064+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - installation
verified: true
validated: true
---

# install-aquatone-via-gem

## Command

```bash
gem install aquatone
```

## Description

Installs the Aquatone Ruby gem, which includes the subdomain discovery and scanning binaries. Use this on systems with RubyGems to set up the tool for native execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; installs latest version | No |

## Examples

### Basic Usage

```bash
gem install aquatone
```

### With Specific Version (Optional)

```bash
gem install aquatone -v 0.7.7
```

## Expected Output

Successfully installed aquatone-0.7.7
Parsing documentation for aquatone-0.7.7
Done installing documentation for aquatone after 1 seconds
1 gem installed

Verify with: aquatone-discover --help

## Related

- [[procedures/Subdomain-Enumeration-with-Aquatone]]
- [[tools/Aquatone]]

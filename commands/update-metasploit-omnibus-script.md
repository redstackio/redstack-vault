---
id: 92aaf94b-8acc-4490-a9d8-4b1ca8f8d995
name: update-metasploit-omnibus-script
type: command
executor: bash
data: >-
  curl
  https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb
  > msfinstall && chmod 755 msfinstall && ./msfinstall
output: null
created_at: '2023-04-06T03:56:21.178025+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Unix
tags:
  - installation
  - metasploit
verified: true
validated: true
---

# update-metasploit-omnibus-script

## Command

```bash
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall
```

## Description

This command downloads the official Metasploit Omnibus update script, sets it executable, and runs it to update the framework to the latest version. Use it on Unix-like systems to refresh exploits, payloads, and core components.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `> msfinstall` | Redirects the downloaded script to a file named 'msfinstall' | Yes |
| `755` | Sets read/write/execute permissions for owner, read/execute for group and others | Yes |
| `./msfinstall` | Executes the downloaded script to perform the update | Yes |

## Examples

### Basic Usage

```bash
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall
```

### Advanced Usage

Run with sudo if permissions require it:

```bash
sudo bash -c "curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall"
```

## Expected Output

The command outputs download progress (e.g., "% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current"), permission change confirmation, and update logs such as "Downloading Metasploit Framework...", "Installing dependencies...", ending with "Update complete. Restart msfconsole to load new modules."

## Related

- [[procedures/Update-Metasploit-Framework]]

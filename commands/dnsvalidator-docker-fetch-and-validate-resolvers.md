---
type: command
executor: bash
data: >-
  docker run -v $(pwd):$_MOUNT_DIR -t codingo/dnsvalidator -tL $_DNS_LIST_URL
  -threads $_THREADS -o $_MOUNT_DIR/$_OUTPUT_FILE
output: "root@kali ~# docker run -v $(pwd):/output -t codingo/dnsvalidator -tL https://public-dns.info/nameservers.txt -threads 20 -o /output/resolvers.txt\nUnable to find image 'codingo/dnsvalidator:latest' locally\nlatest: Pulling from codingo/dnsvalidator\n...\nStatus: Downloaded newer image for codingo/dnsvalidator:latest\n=======================================================\ndnsvalidator v0.1\tby James McLean (@vortexau) \n                \t& Michael Skelton (@codingo_)\n=======================================================\n[22:10:53] [INFO] [1.1.1.1] resolving baseline\n[22:10:53] [INFO] [8.8.8.8] resolving baseline\n[22:10:54] [INFO] [9.9.9.9] resolving baseline\n... [CUT] ...\n[22:11:20] [INFO] Validated 1500 resolvers, output to /output/resolvers.txt"
platforms:
  - Linux
tags:
  - dns
  - docker
  - validation
  - enumeration
verified: true
validated: true
---

# dnsvalidator-docker-fetch-and-validate-resolvers

## Command

```bash
docker run -v $(pwd):$_MOUNT_DIR -t codingo/dnsvalidator -tL $_DNS_LIST_URL -threads $_THREADS -o $_MOUNT_DIR/$_OUTPUT_FILE
```

## Description

This command runs dnsvalidator inside a Docker container to fetch and validate DNS resolvers without requiring a native Go installation. It mounts a host directory to persist the output file, making it ideal for environments where direct installation is restricted or for reproducible setups. The validation process mirrors the native version, testing against baselines for reliability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -v $(pwd):$_MOUNT_DIR | Mount the current host directory to the container path (e.g., /output) for file persistence | Yes |
| -t | Run the container interactively (detached mode not needed for one-off runs) | Yes |
| -tL $_DNS_LIST_URL | URL or file path (relative to container) to DNS server list | Yes |
| -threads $_THREADS | Number of concurrent threads (20-200) | Yes |
| -o $_MOUNT_DIR/$_OUTPUT_FILE | Output path inside the container (must be under the mounted directory) | Yes |
| --timeout | Optional: DNS query timeout in seconds | No |

## Examples

### Basic Usage

```bash
docker run -v $(pwd):/output -t codingo/dnsvalidator -tL https://public-dns.info/nameservers.txt -threads 20 -o /output/resolvers.txt
```

### Advanced Usage

```bash
docker run -v $(pwd):/data -t codingo/dnsvalidator -tL /data/custom-list.txt -threads 50 -o /data/validated.txt --timeout 5
```

(Note: For file inputs, place the list file in the mounted host directory.)

## Expected Output

Docker will first pull the image if not present, then stream the container logs with validation progress. The validated resolvers file appears in the mounted host directory upon completion.

Example output snippet:

```
Unable to find image 'codingo/dnsvalidator:latest' locally
latest: Pulling from codingo/dnsvalidator
...
Status: Downloaded newer image for codingo/dnsvalidator:latest
=======================================================
dnsvalidator v0.1	by James McLean (@vortexau) 
                	& Michael Skelton (@codingo_)
=======================================================
[22:10:53] [INFO] [1.1.1.1] resolving baseline
[22:10:53] [INFO] [8.8.8.8] resolving baseline
[22:10:54] [INFO] [9.9.9.9] resolving baseline
...
[22:11:20] [INFO] Validated 1500 resolvers out of 5000 tested
[22:11:20] [INFO] Output saved to /output/resolvers.txt
```

The host file (resolvers.txt) will list validated IPs.

## Related

- [[tools/dnsvalidator]]

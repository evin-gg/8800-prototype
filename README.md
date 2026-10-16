# 8800-prototype
This is a prototype of a core feature in the 8800 project
course. It takes a pcap dataset and distinguishes all of
the IP addresses and their connections into a data structure
which is essential for the final product.

## Requirements
this project has only been tested on a linux environment
sudo access is required to read and write files within the directory

Python3

## Installation
This project uses a Python3 virtual environment and the
setup is automated in the Makefile

to install virtual environment and requirements run:
```bash
make
```

## Usage
to run the program run:
```bash
make run
```

running the program should prompt you to enter one of the listed IP addresses
you can enter one of the listed IPs or press enter for the default.

Example:
```bash
-----------------------IP Record List -----------------------
178.127.215.73
246.237.103.87
...
Enter IP (default 114.213.235.250):
```
## Cleanup
to remove virtual environment run:
```bash
make clean
```

## Dataset
The provided dataset is a small capture from my home network that has been sanitized
to omit any sensitive information.
# NetScanner-Pro 🛡️

A fast, lightweight network discovery tool using ARP requests to identify active hosts in a local network segment. 



## Features
- **ARP Discovery**: Rapidly identifies live hosts without traditional heavy port scanning.
- **Low Latency**: Uses Scapy to perform raw packet crafting.
- **Portable**: Simple and efficient, designed for quick network recon.

## Installation
  Clone the repo:
   ```bash
   git clone https://github.com/RisetrokPTT/netscanner-pro.git
   cd netscanner-pro
  ```
## Install Dependencies
  ```
  pip install -r requirements.txt
  ```
## Usage
  Run the script with administrator/root privileges (required for raw packet access):
  ```
  sudo python netscan.py 192.168.1.0/24
  ```
## Disclaimer
  This tool is for educational and authorized security testing only.

# Port Scanner (Educational)

This repository contains a simple Python port scanner built for learning and experimentation.

## Warning

This tool is intended for educational use only.

- Use it only on systems that you own or have explicit permission to scan.
- Unauthorized port scanning can be illegal and may violate terms of service.
- You are responsible for how and where you use this tool.

## What it does

The script attempts to connect to TCP ports on a target host and reports which ports are open.

## Usage

1. Open a terminal in this repository folder.
2. Run the script with Python 3:

```bash
python port_scanner.py
```

3. When prompted:
   - Enter the target IP address or hostname.
   - Enter a port range, for example `1-1024`.

The scanner will display only the open ports it finds.

## Notes

- This scanner is a personal learning project and does not replace tools like `nmap`.
- Be careful when scanning networks and always follow ethical guidelines.
- Currently, the port range is set to (1, 1024). Passing a port larger than 1024 will not return a result. This is subject to change but will stay for now.
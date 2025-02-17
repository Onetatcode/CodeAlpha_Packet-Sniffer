Python Network Sniffer

A simple Python-based network sniffer that captures HTTP requests and extracts potential credentials from unencrypted traffic.

🚀 Features

Captures HTTP requests

Extracts possible usernames and passwords from unencrypted traffic

Works on Linux, macOS, and Windows

📌 Prerequisites

Make sure you have Python installed (Python 3 recommended). You also need to install Scapy and scapy-http:

pip install scapy scapy-http

🔧 Setup

Clone the repository:

git clone https://github.com/yourusername/network-sniffer.git
cd network-sniffer

🛠️ Usage

Run the script with administrator/root privileges:

Linux/macOS:

sudo python3 sniffer.py -i eth0  # Replace 'eth0' with your network interface

Windows:

python sniffer.py -i Ethernet  # Replace 'Ethernet' with your interface name

📡 Finding Your Network Interface

Before running the script, find your active network interface:

Linux/macOS:

ip link show

or

ifconfig

Windows (PowerShell):

Get-NetAdapter

⚠️ Disclaimer

This script should only be used for educational and ethical testing purposes. Unauthorized network sniffing is illegal. Ensure you have proper permissions before running this tool.

📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

Made with ❤️ by [Your Name]

OnetatCipher

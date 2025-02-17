🕵️‍♂️ Python Network Sniffer

A simple yet powerful Python-based network sniffer that captures HTTP requests and extracts potential credentials from unencrypted traffic. 🚀

🎯 Features

✅ Captures HTTP requests in real-time✅ Extracts possible usernames and passwords from unencrypted traffic✅ Works on Linux, macOS, and Windows✅ Beginner-friendly & lightweight 💡

📌 Prerequisites

Make sure you have Python 3+ installed. Then, install the required dependencies:

pip install scapy scapy-http

🔧 Installation & Setup

Clone the repository:

git clone https://github.com/yourusername/network-sniffer.git
cd network-sniffer

🚀 Usage

Run the script with administrator/root privileges:

🔹 Linux/macOS:

sudo python3 sniffer.py -i eth0  # Replace 'eth0' with your network interface

🔹 Windows:

python sniffer.py -i Ethernet  # Replace 'Ethernet' with your interface name

📡 Finding Your Network Interface

Before running the script, identify your active network interface:

🔸 Linux/macOS:

ip link show

or

ifconfig

🔸 Windows (PowerShell):

Get-NetAdapter

⚠️ Disclaimer

🚨 Ethical Use Only! 🚨This tool is designed for educational and cybersecurity research purposes only. Unauthorized network sniffing is illegal. Ensure you have explicit permission before using this tool. ❌

📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

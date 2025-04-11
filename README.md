# DNS Subdomain Takeover Scanner

A lightweight Python script to automate DNS reconnaissance and detect dangling subdomains vulnerable to takeover. Checks CNAMEs, A records, and reverse DNS with `dig`, and runs `subjack` for third-party CNAMEs. Works with any domain, outputs verbose results to the console.

## 🌟 Features
- **Automated DNS Checks**: Queries CNAMEs, A records, and reverse DNS.
- **Takeover Detection**: Identifies dangling subdomains via `subjack`.
- **Flexible Input**: Takes any subdomain list from a user-specified file.
- **Universal**: Supports any domain (e.g., `example.com`, `site.com.gh`).
- **Verbose Output**: Clear console results, no extra files.
- **Open-Source**: Free to use and extend.

## 🚀 Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Charis111/dns-takeover-scanner.git
   cd dns-takeover-scanner
2. **Install Dependencies**:
   
    Python 3 (pre-installed on most systems)
   
    dig (from dnsutils):

   ```bash
   sudo apt-get install dnsutils  # Debian/Ubuntu
   sudo yum install bind-utils   # CentOS/RHEL
   ```
   subjack:
    ```bash
    go install github.com/haccer/subjack@latest
    export PATH=$PATH:~/go/bin
    ```

3. **Verify Tools**:
     ```bash
     python3 --version
     dig -v
     subjack -h
     ```
🛠️ Usage

1: Prepare a Subdomain File: Create a file (e.g., subdomains.txt) with one subdomain per line:
```text
 store.business.example.com.gh
 chatbot-dev.example.com.gh
 app.example.com
 ```
2:Run the Script:
 ```bash
 chmod +x dns-takeover-scanner.py
 ./dns-takeover-scanner.py subdomains.txt
```
![dns2](https://github.com/user-attachments/assets/2f9eafcf-3773-445e-9f0d-6037a33b92e4)

📋 Requirements
    Python 3.6+
    dig (dnsutils)
    subjack (Go-based, install via go install)

🐛 Troubleshooting
     File Not Found:
   ```bash
   ./dns_takeover_scanner.py nonexistent.txt
   ```
Ensure the file exists: *ls subdomains.txt*.

Subjack Errors:  Verify:*which subjack*, Update: *go install github.com/haccer/subjack@latest*.

Dig Errors:  *Install: sudo apt-get install dnsutils*.

Verbose Output: *Check console for CNAME, A record, reverse DNS, and subjack results*.

🤝 Contributing
We welcome contributions! To contribute:
  1. Fork the repo.
  2. Create a branch: git checkout -b feature-name.
  3. Commit changes: git commit -m "Add feature".
  4. Push: git push origin feature-name.
      Open a pull request.


📜 License
 - free to use, modify, and distribute.

🙌 Acknowledgments

   1. dig for DNS queries
   2. subjack for takeover detection.
   3. Community for inspiration!
   Secure your domains and happy scanning! 🚀

Star this repo if you find it useful!



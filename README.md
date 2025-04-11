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

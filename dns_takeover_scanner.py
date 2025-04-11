#!/usr/bin/env python3
import subprocess
import sys
import re
import os
from urllib.parse import urlparse

def run_command(command):
    """Run a shell command and return its output."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.strip()}"

def check_cname(subdomain):
    """Check if a subdomain has a CNAME record using dig."""
    command = f"dig {subdomain} CNAME +short"
    output = run_command(command)
    return output if output and not output.startswith("Error") else None

def check_a_record(subdomain):
    """Check the A record for a subdomain."""
    command = f"dig {subdomain} A +short"
    output = run_command(command)
    return output if output and not output.startswith("Error") else None

def reverse_dns(ip):
    """Perform a reverse DNS lookup for an IP."""
    command = f"dig -x {ip} +short"
    output = run_command(command)
    return output if output and not output.startswith("Error") else None

def get_root_domain(subdomain):
    """Extract the root domain from a subdomain (e.g., mtn.com.gh from store.business.mtn.com.gh)."""
    parts = subdomain.split(".")
    if len(parts) >= 3 and parts[-2] in ["com", "co", "org", "net"]:
        return ".".join(parts[-3:])
    return ".".join(parts[-2:]) if len(parts) >= 2 else subdomain

def is_third_party(cname, root_domain):
    """Check if a CNAME points to a third-party (not the root domain)."""
    if not cname:
        return False
    parsed_cname = urlparse(f"http://{cname}").hostname
    if parsed_cname:
        parts = parsed_cname.split(".")
        cname_root = ".".join(parts[-3:]) if len(parts) >= 3 and parts[-2] in ["com", "co", "org", "net"] else ".".join(parts[-2:])
        return cname_root != root_domain
    return False

def run_subjack(subdomain):
    """Run subjack on a subdomain and return results."""
    command = f"subjack -d {subdomain} -v -a -t 10"
    output = run_command(command)
    return output

def main(subdomain_file):
    """Main function to process subdomains."""
    if not os.path.isfile(subdomain_file):
        print(f"Error: {subdomain_file} not found.")
        return

    try:
        with open(subdomain_file, "r") as f:
            subdomains = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Error reading {subdomain_file}: {e}")
        return

    print(f"Scanning {len(subdomains)} subdomains from {subdomain_file}...\n")

    for subdomain in subdomains:
        print(f"\nChecking {subdomain}...")
        root_domain = get_root_domain(subdomain)
        print(f"  Root domain: {root_domain}")

        cname = check_cname(subdomain)
        if cname:
            print(f"  CNAME: {cname}")
            if is_third_party(cname, root_domain):
                print(f"  Third-party CNAME detected: {cname}")
                print(f"  Running subjack on {subdomain}...")
                subjack_output = run_subjack(subdomain)
                if subjack_output and not subjack_output.startswith("Error"):
                    print(f"  Subjack results: {subjack_output}")
                else:
                    print(f"  Subjack error: {subjack_output}")
            else:
                print(f"  CNAME points to internal domain ({cname}), likely safe.")
        else:
            print("  No CNAME found.")
            a_record = check_a_record(subdomain)
            if a_record:
                print(f"  A Record: {a_record}")
                for ip in a_record.split("\n"):
                    reverse = reverse_dns(ip)
                    if reverse:
                        print(f"  Reverse DNS for {ip}: {reverse}")
                    else:
                        print(f"  No reverse DNS for {ip}.")
            else:
                print("  No A record found.")

    print("\nScan complete.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./dns_takeover_scanner.py <subdomain_file>")
        print("Example: ./dns_takeover_scanner.py subdomains.txt")
        sys.exit(1)

    SUBDOMAIN_FILE = sys.argv[1]
    main(SUBDOMAIN_FILE)

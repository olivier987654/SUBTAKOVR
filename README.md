# SUBTAKOVR
SUBTAKOVR is a powerful and user-friendly tool designed for penetration testers and cybersecurity enthusiasts. It automates the process of scanning subdomains to identify potential vulnerabilities related to subdomain takeovers. SUBTAKOVR is easy to use yet robust, making it an essential tool in the arsenal of anyone looking to secure web domains.

Features
Subdomain Enumeration: Efficiently extracts CNAME records from a list of subdomains, providing insight into potential external service dependencies.
HTTP Status Check: Verifies the HTTP response status of each subdomain to identify misconfigured or inactive domains.
Vulnerability Assessment: Offers a basic assessment of potential subdomain takeover vulnerabilities based on DNS and HTTP response analysis.
Delay Feature: Includes a customizable delay option between requests to avoid rate-limiting and ensure responsible scanning practices.
Color-Coded Output: Utilizes red-colored output for better visibility and distinction of subdomains in the terminal.
Command-Line Interface: User-friendly command-line interface with -h (help) support for easy operation.
Usage
Installation: Clone the repository and install the required Python packages.

bash
Copy code
git clone [repository URL]
cd SUBTAKOVR
pip install -r requirements.txt
Basic Command:

bash
Copy code
python subtakovr.py -f path/to/subdomains.txt
With Delay:

bash
Copy code
python subtakovr.py -f path/to/subdomains.txt -d 1.5
Help:

Copy code
python subtakovr.py -h
Requirements
Python 3.x
Requests library
dnspython library
Contributing
Contributions to SUBTAKOVR are welcome! Whether it involves fixing bugs, improving functionality, or enhancing documentation, your input is valued. Please feel free to fork the repository, make changes, and submit pull requests.

License
[Your chosen license]

Disclaimer
SUBTAKOVR is intended for educational and ethical testing purposes only. The authors take no responsibility for misuse of the tool or any issues arising from its use. Always ensure you have permission to perform security testing on any network or domains.

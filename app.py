import argparse
import requests
import dns.resolver
import time

def display_banner():
    banner = """
   
 (                                            )      )             (     
 )\ )             (     *   )     (        ( /(   ( /(             )\ )  
(()/(      (    ( )\  ` )  /(     )\       )\())  )\())   (   (   (()/(  
 /(_))     )\   )((_)  ( )(_)) ((((_)(   |((_)\  ((_)\    )\  )\   /(_)) 
(_))    _ ((_) ((_)_  (_(_())   )\ _ )\  |_ ((_)   ((_)  ((_)((_) (_))   
/ __|  | | | |  | _ ) |_   _|   (_)_\(_) | |/ /   / _ \  \ \ / /  | _ \  
\__ \  | |_| |  | _ \   | |      / _ \     ' <   | (_) |  \ V /   |   /  
|___/   \___/   |___/   |_|     /_/ \_\   _|\_\   \___/    \_/    |_|_\  
                                                                         

    """
    print(banner)

def read_subdomains_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def get_cname(subdomain):
    try:
        answers = dns.resolver.resolve(subdomain, 'CNAME')
        return str(answers[0].target)
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        return None

def check_subdomain_status(subdomains, delay):
    results = {}
    for subdomain in subdomains:
        cname = get_cname(subdomain)
        try:
            response = requests.get(f"http://{subdomain}", timeout=5)
            status_code = response.status_code
        except requests.RequestException:
            status_code = None

        if cname and status_code in [404, None]:
            vulnerable = True
        else:
            vulnerable = False

        results[subdomain] = {
            'status_code': status_code,
            'cname_record': cname,
            'potential_takeover': vulnerable
        }

        # Delay between each request
        time.sleep(delay)

    return results

def main():
    display_banner()
    parser = argparse.ArgumentParser(description='Subdomain Takeover Scanner')
    parser.add_argument('-f', '--file', required=True, help='Path to the file containing subdomains, one per line')
    parser.add_argument('-d', '--delay', type=float, default=0, help='Delay (in seconds) between each request')

    args = parser.parse_args()

    subdomains = read_subdomains_from_file(args.file)
    result = check_subdomain_status(subdomains, args.delay)
    for subdomain, info in result.items():
        print(f"{subdomain}:")
        for key, value in info.items():
            print(f"  {key}: {value}")
        print()

if __name__ == "__main__":
    main()

            

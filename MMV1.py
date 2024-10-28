#!/usr/bin/env python3
#required Libs
#pip3 install socket requests time random beautifulsoup4
#python3 MMV1.py

import socket, requests, time, random
from bs4 import BeautifulSoup

#starting the code.
class ReverseIPLookup:
    def __init__(self):
        self.user_agents = [
# You can change the below user agents as randomly generated.
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.62',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.71',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.62',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.62',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.71',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.62',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',            
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.62',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'
        ]
        self.referers = ['https://google.com', 'https://bing.com', 'https://duckduckgo.com', 'https://yahoo.com']
        self.headers_collection = [
            {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Accept-Language': 'en-US,en;q=0.5', 'Connection': 'keep-alive'},
            {'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'en-GB,en;q=0.9', 'Connection': 'keep-alive'},
            {'Accept': '*/*', 'Accept-Language': 'en-US,en;q=0.9', 'Connection': 'keep-alive'}
        ]
        self.services = ['YouGetSignal', 'HackerTarget', 'Shodan', 'DNSDumpster', 'Robtex']
#Banner
    def print_banner(self):
        banner = """
        ======================================================================================
        | In the name of God, the most gracious, the most merciful                           |
        |                                                                                    |
        |----- MM Reverse IP Lookup Tool v1.0 ------ > MMV1.py                               |
        | Perform a reverse IP lookup to find all A records associated with an IP address.   |
        |                                                                                    |
        | Pray on Muhammad (ﷺ)                                                               |
        |                                                                                    |
        | Free Palestine                                                                     |
        ======================================================================================
        | Available Services:                                           |
        | 1. YouGetSignal        (-> No API require)                    |
        | 2. HackerTarget        (-> No API require)                    |
        | 3. Shodan              (-> No API require)                    |
        | 4. DNSDumpster         (-> No API require)                    |
        | 5. Robtex              (-> No API require)                    |
        | 6. Threatminer         (-> No API require)                    |
        =================================================================
        """
        print(banner)
#Header
    def _get_random_headers(self) -> dict:
        headers = random.choice(self.headers_collection).copy()
        headers['User-Agent'] = random.choice(self.user_agents)
        headers['Referer'] = random.choice(self.referers)
        headers['X-Forwarded-For'] = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
        return headers
#Request
    def _make_request(self, url: str, method: str = 'GET', data: dict = None, headers: dict = None, delay: float = 1.0) -> requests.Response:
        time.sleep(delay + random.uniform(0.1, 0.5))
        try:
            headers = headers or self._get_random_headers()
            if method.upper() == 'GET':
                response = requests.get(url, headers=headers, timeout=10)
            else:
                response = requests.post(url, headers=headers, data=data, timeout=10)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            raise Exception(f"Request failed: {str(e)}")
#query_yougetsignal
    def query_yougetsignal(self, ip_address: str):
        print(f"Querying YouGetSignal for IP {ip_address}...")
        url = "https://domains.yougetsignal.com/domains.php"
        data = {'remoteAddress': ip_address, '_': str(int(time.time() * 1000))}
        response = self._make_request(url, method='POST', data=data)
        result = response.json()
        domains = {domain[0] for domain in result['domainArray']} if result.get('domainArray') else set()
        print(f"[YouGetSignal] Found {len(domains)} domains:")
        for domain in domains:
            print(f" - {domain}")
        return domains
#query_hackertarget
    def query_hackertarget(self, ip_address: str):
        print(f"Querying HackerTarget for IP {ip_address}...")
        url = f"https://api.hackertarget.com/reverseiplookup/?q={ip_address}"
        response = self._make_request(url)
        domains = {domain.strip() for domain in response.text.split('\n') if domain.strip() and not domain.startswith('error') and '.' in domain}
        print(f"[HackerTarget] Found {len(domains)} domains:")
        for domain in domains:
            print(f" - {domain}")
        return domains
#query_shodan
    def query_shodan(self, ip_address: str):
        print(f"Querying Shodan for IP {ip_address}...")
        url = f"https://www.shodan.io/host/{ip_address}"
        response = self._make_request(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table')
        domains = {row.find_all('td')[0].text.strip() for row in table.find_all('tr')[1:] if '.' in row.find_all('td')[0].text} if table else set()
        print(f"[Shodan] Found {len(domains)} domains:")
        for domain in domains:
            print(f" - {domain}")
        return domains
#query_threatminer
    def query_threatminer(self, ip_address: str):
        print(f"Querying ThreatMiner for IP {ip_address}...")
        url = f"https://api.threatminer.org/v2/host.php?q={ip_address}&rt=5"
        response = self._make_request(url)
        
        # Parse the response to extract domains
        data = response.json()
        domains = {item["domain"] for item in data.get("results", []) if "domain" in item}
        
        if domains:
            print(f"[ThreatMiner] Found {len(domains)} domains:")
            for domain in domains:
                print(f" - {domain}")
        else:
            print("[ThreatMiner] No domains found for this IP.")
        
        return domains
#query_dnsdumpster
    def query_dnsdumpster(self, domain: str):
        print(f"Querying DNSDumpster for domain {domain}...")
        url = "https://dnsdumpster.com/"
        response = self._make_request(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']
        data = {'csrfmiddlewaretoken': csrf_token, 'targetip': domain}
        response = requests.post(url, headers=self._get_random_headers(), data=data, cookies=response.cookies)
        soup = BeautifulSoup(response.text, 'html.parser')
        tables = soup.find_all('table', {'class': 'table'})
        domains = {cols[0].text.strip() for table in tables for row in table.find_all('tr') for cols in row.find_all('td')} if tables else set()
        print(f"[DNSDumpster] Found {len(domains)} domains:")
        for domain in domains:
            print(f" - {domain}")
        return domains
#query_robtex
    def query_robtex(self, ip_address: str):
        print(f"Querying Robtex for IP {ip_address}...")
        url = f"https://freeapi.robtex.com/ipquery/{ip_address}"
        response = self._make_request(url, delay=2.0)
        data = response.json()
        domains = {entry['o'] for entry in data['pas'] if entry.get('o')} if 'pas' in data else set()
        print(f"[Robtex] Found {len(domains)} domains:")
        for domain in domains:
            print(f" - {domain}")
        return domains
# Parse the table to find domain names
        table = soup.find('table', {'border': '1'})
        domains = {row.find_all('td')[0].text.strip() for row in table.find_all('tr')[1:]} if table else set()
        
        print(f"[ViewDNS.info] Found {len(domains)} domains:")
        for domain in domains:
            print(f" - {domain}")
        return domains 
#get_ip_from_domain    
    def get_ip_from_domain(self, domain: str):
        try:
            ip_address = socket.gethostbyname(domain)
            print(f"Resolved {domain} to IP address: {ip_address}")
            return ip_address
        except socket.gaierror:
            print(f"Could not resolve {domain}")
            return None
#save_results
    def save_results(self, domains: set, base_filename: str):
        if not domains:
            print("No domains found to save.")
            return
        save = input("Do you want to save the results? (y/n): ").lower().strip()
        if save != 'y':
            return
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"{base_filename}_{timestamp}.txt"
        try:
            with open(filename, "w", encoding='utf-8') as file:
                file.write('\n'.join(sorted(domains)))
            print(f"Results saved to {filename}")
        except IOError as e:
            print(f"Error saving results: {e}")
#Core
    def run(self, domain: str):
        ip_address = self.get_ip_from_domain(domain)
        if not ip_address:
            return
        all_domains = set()
        # Add query_threatminer to the services list
        services = [self.query_yougetsignal, self.query_hackertarget, self.query_shodan, self.query_dnsdumpster, self.query_robtex, self.query_threatminer]
        for service in services:
            try:
                all_domains.update(service(ip_address))
            except Exception as e:
                print(f"Error with service {service.__name__}: {e}")
        all_domains = sorted(all_domains)  # Sort and remove duplicates
        print(f"Total unique domains found: {len(all_domains)}")
        if all_domains:
            self.save_results(all_domains, f"reverse_ip_{domain}")
#Main
def main():
    tool = ReverseIPLookup()
    tool.print_banner()
    while True:
        domain = input("Enter domain (ex: 'example.com') or 'quit' to exit: ").strip().lower()
        if domain == 'quit': break
        if domain: tool.run(domain)

if __name__ == "__main__":
    main()

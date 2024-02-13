import subprocess

def run_subrute(domain):
    try:
        subrute_process = subprocess.Popen(['subrute', '-w', 'subdomains.txt', domain], stdout=subprocess.PIPE)
        subrute_output, _ = subrute_process.communicate()
        subdomains = subrute_output.decode('utf-8').split('\n')

        return subdomains
    except Exception as e:
        print(f"Error running Subrute: {e}")
        return []

def run_ffuf(domain, subdomains):
    try:
        for subdomain in subdomains:
            if subdomain:
                ffuf_process = subprocess.Popen(['ffuf', '-w', 'wordlist.txt', '-u', f'http://{subdomain}.{domain}'], stdout=subprocess.PIPE)
                ffuf_output, _ = ffuf_process.communicate()
                print(ffuf_output.decode('utf-8'))
    except Exception as e:
        print(f"Error running FFuF: {e}")

def main():
    domain = 'example.com'

    subdomains = run_subrute(domain)
    if subdomains:
        run_ffuf(domain, subdomains)
    else:
        print("Subrute did not find any subdomains.")

if __name__ == "__main__":
    main()

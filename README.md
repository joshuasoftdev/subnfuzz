# subnfuzz
This script will execute Subrute first to generate a list of subdomains, and then use FFuF to perform fuzzing on each subdomain

In this script:

run_subrute function takes a domain as input and runs Subrute to generate a list of subdomains.
run_ffuf function takes the domain and the list of subdomains as input and runs FFuF to perform fuzzing on each subdomain.
main function orchestrates the execution of Subrute and FFuF.
The script assumes you have a subdomains.txt file containing a list of common subdomains and a wordlist.txt file containing a list of common fuzzing payloads.
You'll need to replace 'example.com' with your target domain, and ensure that you have the necessary wordlists and that Subrute and FFuF are properly installed and accessible in your environment. Additionally, customize the wordlists and adjust the script according to your specific use case.

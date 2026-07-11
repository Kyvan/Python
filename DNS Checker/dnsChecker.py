#!/home/ky/python_env/bin/python

import validators
import whois
from pathlib import Path
from colorama import Style,Fore,init

init(autoreset=True)

domain_list = Path("/home/ky/git/Python/DNS Checker/domains.txt")

def registrar_checker(domain_name_confirmed):
    try:
        w = whois.whois(domain_name_confirmed)
        print(f"{Style.BRIGHT}This is the registrar {Fore.MAGENTA}{w.registrar}{Fore.RESET} for {Fore.BLUE}{domain_name_confirmed}")
        print(f"This is the expiration date {Fore.MAGENTA}{w.expiration_date}{Fore.RESET} for {Fore.BLUE}{domain_name_confirmed}")
    except Exception as e:
        print(f"{Style.BRIGHT}{Fore.RED}{domain_name_confirmed} IT AIN'T WORKING {e}")

def domain_validator(domain_name):
    if validators.domain(domain_name):
        registrar_checker(domain_name)
    else:
        print(f"{Style.BRIGHT}{Fore.RED}{domain_name} is not domaining")

with domain_list.open() as d:
    for domain in d:
        domain = domain.strip()
        domain_validator(domain)
        
    
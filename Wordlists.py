import os
import itertools
import time
from datetime import datetime
from colorama import Fore, Style, init
from pyfiglet import Figlet

# Initialize colorama
init(autoreset=True)

def print_banner():
    os.system("clear")  # Clears terminal (use "cls" for Windows)
    custom_fig = Figlet(font='slant')
    print(Fore.RED + custom_fig.renderText("PASSWORD CRACKER"))
    print(Fore.YELLOW + "=" * 50)
    print(Fore.GREEN + "      Automated Wordlist Generator")
    print(Fore.YELLOW + "=" * 50)
    print(Fore.CYAN + " Author: Kali Linux User")
    print(Fore.CYAN + " Use this for ethical hacking & security testing only!")
    print(Fore.YELLOW + "=" * 50)
    time.sleep(2)  # Pause for dramatic effect

def loading_animation():
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", 
                 "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", 
                 "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    
    for i in range(len(animation)):
        time.sleep(0.3)
        print(Fore.MAGENTA + f"\rGenerating wordlist... {animation[i]}", end="")
    print("\n" + Fore.GREEN + "[✔] Wordlist generation complete!\n")

def get_inputs():
    target_info = {}
    target_info['first_name'] = input(Fore.CYAN + "[?] Enter target's first name: ").strip()
    target_info['last_name'] = input(Fore.CYAN + "[?] Enter target's last name: ").strip()
    target_info['dob'] = input(Fore.CYAN + "[?] Enter target's date of birth (DDMMYYYY): ").strip()
    target_info['pet_name'] = input(Fore.CYAN + "[?] Enter target's pet name (or 'no' if not applicable): ").strip()
    target_info['father_name'] = input(Fore.CYAN + "[?] Enter target's father's full name: ").strip()
    target_info['mother_name'] = input(Fore.CYAN + "[?] Enter target's mother's full name: ").strip()
    target_info['spouse_name'] = input(Fore.CYAN + "[?] Enter target's spouse name (or 'no' if not applicable): ").strip()
    target_info['mobile_no'] = input(Fore.CYAN + "[?] Enter target's mobile number: ").strip()
    
    return target_info

def generate_variations(info, min_length=4, max_length=16):
    variations = []
    
    # Base words
    base_words = [
        info['first_name'], info['last_name'], info['dob'],
        info['pet_name'] if info['pet_name'].lower() != 'no' else '',
        info['father_name'], info['mother_name'],
        info['spouse_name'] if info['spouse_name'].lower() != 'no' else '',
        info['mobile_no']
    ]
    base_words = [word for word in base_words if word]  # Remove empty strings

    # Generate combinations
    for i in range(1, len(base_words) + 1):
        for combo in itertools.permutations(base_words, i):
            combined = ''.join(combo)
            if min_length <= len(combined) <= max_length:
                variations.extend([
                    combined, combined.lower(), combined.upper(), combined.capitalize()
                ])

    # Common substitutions
    common_substitutions = {
        'a': '@', 'e': '3', 'i': '1', 'o': '0', 's': '$', 'b': '8', 't': '7', 'l': '1'
    }
    substitution_variations = []
    for word in variations:
        for original, sub in common_substitutions.items():
            substitution_variations.append(word.replace(original, sub))
    variations.extend(substitution_variations)

    # Add common suffixes & prefixes
    common_patterns = ['123', '!', '@', '#', '007', '2024']
    pattern_variations = []
    for variation in variations.copy():
        for pattern in common_patterns:
            pattern_variations.append(variation + pattern)
            pattern_variations.append(pattern + variation)
    variations.extend(pattern_variations)

    return set(variations)  # Remove duplicates

def save_wordlist(wordlist):
    script_dir = os.path.dirname(__file__)  # Get script directory
    filename = os.path.join(script_dir, f"wordlist_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
    
    with open(filename, 'w') as file:
        for word in wordlist:
            file.write(f"{word}\n")
    
    print(Fore.GREEN + f"\n[✔] Wordlist saved as: {filename}")

def print_colored_wordlist(wordlist):
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
    for index, word in enumerate(wordlist):
        print(colors[index % len(colors)] + word)

def main():
    print_banner()
    target_info = get_inputs()
    print("\n" + Fore.YELLOW + "[*] Generating password variations... Please wait!\n")
    loading_animation()
    wordlist = generate_variations(target_info)
    save_wordlist(wordlist)
    print(Fore.CYAN + f"\n[+] Generated {len(wordlist)} password variations.\n")
    print_colored_wordlist(wordlist)

if __name__ == "__main__":
    main()

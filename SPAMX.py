#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  🤖  VENS-MD NEO FLOOD  —  by Mr vens                                       ║
# ║  📞  +509 33 54 59 80                                                        ║
# ║  Digital Crew 243 — Neuralink Protocol v2.0                                  ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

import subprocess
import time
import random
import os
import sys
import threading
from datetime import datetime

# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  COLORS — Codex-Man Edition                                                  ║
# ╚══════════════════════════════════════════════════════════════════════════════╝
CYAN = '\033[96m'
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
PURPLE = '\033[95m'
BLUE = '\033[94m'
WHITE = '\033[97m'
BOLD = '\033[1m'
DIM = '\033[2m'
RESET = '\033[0m'

# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  VENS-MD BANNER — Codex-Man Override                                         ║
# ╚══════════════════════════════════════════════════════════════════════════════╝
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    clear_screen()
    print(f"""{CYAN}
    ╔══════════════════════════════════════════════════════════════════╗
    ║  {GREEN}██╗   ██╗███████╗███╗   ██╗███████╗    ███╗   ███╗██████╗ {CYAN}║
    ║  {GREEN}██║   ██║██╔════╝████╗  ██║██╔════╝    ████╗ ████║██╔══██╗{CYAN}║
    ║  {GREEN}██║   ██║█████╗  ██╔██╗ ██║███████╗    ██╔████╔██║██║  ██║{CYAN}║
    ║  {GREEN}╚██╗ ██╔╝██╔══╝  ██║╚██╗██║╚════██║    ██║╚██╔╝██║██║  ██║{CYAN}║
    ║  {GREEN} ╚████╔╝ ███████╗██║ ╚████║███████║    ██║ ╚═╝ ██║██████╔╝{CYAN}║
    ║  {GREEN}  ╚═══╝  ╚══════╝╚═╝  ╚═══╝╚══════╝    ╚═╝     ╚═╝╚═════╝ {CYAN}║
    ║                                                              {CYAN}║
    ║  {BOLD}{WHITE}⚡ VENS-MD NEO FLOOD v7.0.0-CODEX{WHITE}                    {CYAN}║
    ║  {BOLD}{YELLOW}👑 Créateur : Mr vens — +509 33 54 59 80{YELLOW}          {CYAN}║
    ║  {DIM}{BLUE}🌐 Digital Crew 243 — Neuralink Protocol Active{BLUE}{DIM}    {CYAN}║
    ╚══════════════════════════════════════════════════════════════════╝{RESET}
    """)

# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  ANIMATIONS — Typewriter Effect                                               ║
# ╚══════════════════════════════════════════════════════════════════════════════╝
def typewriter(text, color=CYAN, delay=0.03, end='\n'):
    colored_text = f"{color}{text}{RESET}"
    for char in colored_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()

def loading_animation(duration=2, text="NEURALINK SYNC"):
    frames = ["⚫", "🟡", "🟢", "🔵", "🟣", "🔴"]
    start = time.time()
    i = 0
    while time.time() - start < duration:
        sys.stdout.write(f"\r{YELLOW}{BOLD}{text}... {frames[i % len(frames)]}{RESET}")
        sys.stdout.flush()
        time.sleep(0.15)
        i += 1
    sys.stdout.write(f"\r{GREEN}{BOLD}{text}... ✅{RESET}\n")
    sys.stdout.flush()

# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  PAYLOADS — Spam Messages                                                    ║
# ╚══════════════════════════════════════════════════════════════════════════════╝
def load_spam_messages(filename="spam.txt"):
    default_messages = [
        "🔥 VENS-MD — Mr vens 🔥",
        "💀 Digital Crew 243 — Neo Flood 💀",
        "⚡ Neuralink Protocol Activated ⚡",
        "👑 +509 33 54 59 80 — Mr vens 👑",
        "🤖 VENS-MD v7.0 — Codex-Man 🤖",
        "💀 243 Access Granted — DC243 💀",
        "🔥 Neo Flood Sequence — ACTIVE 🔥",
        "⚡ By Mr vens — The Codex-Man ⚡",
    ]
    
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(default_messages))
        return default_messages
    
    with open(filename, 'r', encoding='utf-8') as f:
        messages = [line.strip() for line in f.readlines() if line.strip()]
    
    return messages if messages else default_messages

# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  WHATSAPP LINK GENERATOR                                                     ║
# ╚══════════════════════════════════════════════════════════════════════════════╝
def open_whatsapp_link(phone_number, message):
    clean_number = ''.join(filter(str.isdigit, phone_number))
    encoded_message = message.replace(' ', '%20').replace('\n', '%0A').replace('#', '%23')
    link = f"https://wa.me/{clean_number}?text={encoded_message}"
    
    try:
        subprocess.Popen(['xdg-open', link], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except:
        try:
            subprocess.Popen(['open', link], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
            subprocess.Popen(['start', link], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  SPAM WORKER — Multi-threaded Flood                                          ║
# ╚══════════════════════════════════════════════════════════════════════════════╝
class FloodWorker:
    def __init__(self, phone_number, messages, spam_count, delay_range):
        self.phone_number = phone_number
        self.messages = messages
        self.spam_count = spam_count
        self.delay_min, self.delay_max = delay_range
        self.sent_count = 0
        self.running = True
    
    def worker(self):
        for i in range(self.spam_count):
            if not self.running:
                break
            msg = random.choice(self.messages)
            open_whatsapp_link(self.phone_number, msg)
            self.sent_count += 1
            delay = random.uniform(self.delay_min, self.delay_max)
            time.sleep(delay)
    
    def start(self):
        thread = threading.Thread(target=self.worker)
        thread.daemon = True
        thread.start()
        return thread
    
    def get_stats(self):
        return self.sent_count

def status_monitor(worker, target, total):
    while worker.running and worker.sent_count < total:
        sent = worker.get_stats()
        percent = (sent / total) * 100
        bar_length = 30
        filled = int(bar_length * sent // total)
        bar = '█' * filled + '░' * (bar_length - filled)
        sys.stdout.write(f"\r{YELLOW}[{bar}] {sent}/{total} ({percent:.1f}%) • {target}{RESET}")
        sys.stdout.flush()
        time.sleep(0.5)
    sys.stdout.write(f"\r{GREEN}[{'█' * 30}] {total}/{total} (100%) • {target} — COMPLET ✅{RESET}\n")
    sys.stdout.flush()

# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  MAIN — Neuralink Boot Sequence                                              ║
# ╚══════════════════════════════════════════════════════════════════════════════╝
def main():
    print_banner()
    loading_animation(1.5, "INITIALIZING NEURALINK")
    typewriter("╔════════════════════════════════════════════════════════╗", DIM)
    typewriter("║  VENS-MD NEO FLOOD — Digital Crew 243                 ║", DIM)
    typewriter("║  👑 Propriétaire : Mr vens — +509 33 54 59 80          ║", DIM)
    typewriter("╚════════════════════════════════════════════════════════╝", DIM)
    print()
    
    typewriter("🎯 TARGET ACQUISITION:", BLUE, 0.02)
    target_number = input(f"{PURPLE}╠══[DC243]> {YELLOW}NUMÉRO (ex: 509XXXXXXXX): {RESET}").strip()
    
    typewriter("💀 FLOOD INTENSITY:", BLUE, 0.02)
    spam_count = int(input(f"{PURPLE}╠══[DC243]> {YELLOW}NOMBRE DE MESSAGES: {RESET}"))
    
    typewriter("⏱️ ATTACK TIMING:", BLUE, 0.02)
    delay_min = float(input(f"{PURPLE}╠══[DC243]> {YELLOW}DELAI MIN (s): {RESET}"))
    delay_max = float(input(f"{PURPLE}╠══[DC243]> {YELLOW}DELAI MAX (s): {RESET}"))
    
    messages = load_spam_messages()
    typewriter(f"📦 PAYLOADS CHARGÉS: {len(messages)}", YELLOW, 0.02)
    
    clear_screen()
    print_banner()
    typewriter(f"{RED}{BOLD}⚠️  CONFIRMATION REQUISE ⚠️{RESET}", RED, 0.03)
    typewriter(f"{DIM}Cible: {WHITE}{target_number}{DIM}", DIM)
    typewriter(f"{DIM}Messages: {WHITE}{spam_count}{DIM}", DIM)
    print()
    confirm = input(f"{PURPLE}╠══[DC243]> {RED}LANCER L'ATTAQUE (Y/N): {RESET}").lower()
    
    if confirm == 'y':
        typewriter("🔥 FLOOD SEQUENCE ACTIVE...", GREEN, 0.03)
        typewriter("🌐 DIGITAL CREW 243 — ONLINE", YELLOW, 0.03)
        typewriter(f"👑 Mr vens — Codex-Man Mode — +509 33 54 59 80", CYAN, 0.03)
        print()
        
        worker = FloodWorker(target_number, messages, spam_count, (delay_min, delay_max))
        thread = worker.start()
        
        try:
            status_monitor(worker, target_number, spam_count)
            thread.join(timeout=5)
            print()
            typewriter("✅ FLOOD SEQUENCE COMPLETED", GREEN, 0.03)
            typewriter(f"📊 TOTAL PAYLOADS SENT: {spam_count}", CYAN, 0.03)
            typewriter("💀 VENS-MD — By Mr vens 💀", RED, 0.03)
        except KeyboardInterrupt:
            worker.running = False
            print()
            typewriter("⚠️ NEURALINK DISCONNECTED — SEQUENCE STOPPED", RED, 0.03)
            typewriter(f"📊 PARTIAL PAYLOADS SENT: {worker.sent_count}", YELLOW, 0.03)
    else:
        typewriter("❌ OPERATION CANCELLED BY USER", RED, 0.03)
    
    print()
    typewriter("Press Enter to exit...", DIM)
    input()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}⚠️ Force quit — VENS-MD Neo Flood{RESET}")
    except Exception as e:
        print(f"\n{RED}❌ Error: {e}{RESET}")

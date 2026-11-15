import argparse
import socket
import concurrent.futures # Libreria standard Python per gestire i thread

def scan_port(ip, port):
    # Uso 'with' così il socket si chiude in automatico alla fine (best practice)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5) 
        risultato = s.connect_ex((ip, port))
        
        if risultato == 0:
            print(f"[+] Porta {port}/TCP APERTA su {ip}")

def main():
    parser = argparse.ArgumentParser(description="Port Scanner Multi-Thread TCP")
    parser.add_argument("-t", "--target", required=True, help="Indirizzo IP target")
    # Aggiungiamo un nuovo parametro per scegliere quante porte scansionare
    parser.add_argument("-p", "--ports", type=int, default=1024, help="Num. porte (default: 1024)")
    args = parser.parse_args()

    print(f"[*] Inizio scansione su {args.target} (Prime {args.ports} porte)...")
    print(f"[*] Uso ThreadPoolExecutor per velocizzare l'esecuzione\n")

    # Refactoring: Usiamo un ThreadPool per lanciare le scansioni in parallelo
    # max_workers=50 significa che controllerà fino a 50 porte contemporaneamente
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        for port in range(1, args.ports + 1):
            executor.submit(scan_port, args.target, port)

    print("\n[*] Scansione completata.")

if __name__ == "__main__":
    main()

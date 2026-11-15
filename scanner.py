import argparse

def scan_port(ip, port):
    # Funzione "fittizia" per ora. 
    # Aggiungeremo la logica dei socket nel prossimo step.
    print(f"[*] Provo a connettermi a {ip} sulla porta {port}...")

def main():
    # Configuriamo argparse per far usare il tool da terminale
    parser = argparse.ArgumentParser(description="Uno scanner di rete semplice.")
    parser.add_argument("-t", "--target", required=True, help="L'indirizzo IP da scansionare")
    args = parser.parse_args()

    print(f"Inizio scansione verso il target: {args.target}")
    
    # Per ora testiamo solo la porta 80 (HTTP) per vedere se lo script gira
    scan_port(args.target, 80)

if __name__ == "__main__":
    main()

import argparse
import socket  # La libreria fondamentale per il networking

def scan_port(ip, port):
    # Creiamo un socket (un "cavo di rete virtuale")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Impostiamo un timeout (0.5 sec) per non aspettare in eterno se il server non risponde
    s.settimeout(0.5) 
    
    # connect_ex prova a connettersi. Se ci riesce restituisce il numero 0
    risultato = s.connect_ex((ip, port))
    
    if risultato == 0:
        print(f"[+] Porta {port} APERTA su {ip}")
    else:
        print(f"[-] Porta {port} CHIUSA su {ip}")
        
    s.close() # Regola d'oro: chiudere sempre il socket dopo averlo usato

def main():
    parser = argparse.ArgumentParser(description="Uno scanner di rete semplice.")
    parser.add_argument("-t", "--target", required=True, help="L'indirizzo IP da scansionare")
    args = parser.parse_args()

    print(f"[*] Inizio scansione verso il target: {args.target}")
    
    # Invece di una porta sola, ora testiamo SSH (22), HTTP (80) e HTTPS (443)
    porte_da_testare = [22, 80, 443]
    for port in porte_da_testare:
        scan_port(args.target, port)

if __name__ == "__main__":
    main()

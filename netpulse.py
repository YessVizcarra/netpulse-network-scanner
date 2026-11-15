import argparse   # para recibir --network desde la terminal
import ipaddress
import platform
import subprocess


def ping(host: str, timeout: int = 1) -> bool:
  
    system = platform.system().lower()

    if system == "windows":
        
        command = ["ping", "-n", "1", "-w", str(timeout * 1000), host]
    elif system in ("linux", "darwin"):
       
        command = ["ping", "-c", "1", "-W", str(timeout), host]
    else:
        raise RuntimeError(f"Sistema operativo no soportado: {system}")

    result = subprocess.run(command, capture_output=True, text=True)
    return result.returncode == 0


def main() -> None:
    parser = argparse.ArgumentParser(description="NetPulse Dia 1: ping sweep")
    parser.add_argument("--network", required=True,
                        help="Rango del laboratorio, ej. 192.168.56.0/24")
    parser.add_argument("--timeout", type=int, default=1,
                        help="Segundos de espera por host (default: 1)")
    args = parser.parse_args()

    network = ipaddress.ip_network(args.network, strict=False)
    alive = []
    print(f"Escaneando {network} ...")
    for host in network.hosts():
        host_str = str(host)
        if ping(host_str, args.timeout):
            alive.append(host_str)
            print(f"[+] vivo: {host_str}")

    print(f"\nHosts vivos: {len(alive)}")
    for host in alive:
        print(f"  - {host}")


if __name__ == "__main__":
    main()

import hmac
import hashlib

def encontrar_palabra_original():
    clave_base = input("🔐 Ingresa la clave del acertijo: ").strip()
    palabra_base = input("💬 Ingresa el mensaje: ").strip()
    hash_objetivo = input("🧪 Ingresa el hash firmado entregado: ").strip()

    for i in range(100, 1000):
        firma = f"{clave_base}-{i}"
        for j in range(100, 1000):
            mensaje = f"{palabra_base}-{j}"
            hash_calculado = hmac.new(
                key=firma.encode(),
                msg=mensaje.encode(),
                digestmod=hashlib.sha256
            ).hexdigest()
            
            if hash_calculado == hash_objetivo:
                print(f"\n✅ ¡Match encontrado!")
                print(f"🔑 Clave correcta: {firma}")
                print(f"📦 Palabra original: {mensaje}")
                return

    print("❌ No se encontró coincidencia. Revisa si los datos son correctos.")

# Ejecutar
if __name__ == "__main__":
    encontrar_palabra_original()
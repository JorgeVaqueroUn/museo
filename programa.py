import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet

CONTRASENA_MAESTRA = "LACASANUESTRA"

def verificar_contrasena():
    clave = entrada_contrasena.get()
    if clave == CONTRASENA_MAESTRA:
        ventana_contrasena.destroy()
        iniciar_programa_llave()
    else:
        messagebox.showerror("Acceso denegado", "❌ Contraseña incorrecta.")
        ventana_contrasena.destroy()

def iniciar_programa_llave():
    def descifrar_imagen():
        clave = entrada_clave.get()
        try:
            fernet = Fernet(clave.encode())

            ruta_archivo = filedialog.askopenfilename(title="Selecciona el archivo cifrado", filetypes=[("Archivo cifrado", "*.enc")])
            if not ruta_archivo:
                return

            with open(ruta_archivo, "rb") as file:
                datos_cifrados = file.read()

            datos_descifrados = fernet.decrypt(datos_cifrados)

            ruta_guardado = filedialog.asksaveasfilename(title="Guardar imagen descifrada", defaultextension=".jpg", filetypes=[("Imagen JPG", "*.jpg")])
            if not ruta_guardado:
                return

            with open(ruta_guardado, "wb") as file:
                file.write(datos_descifrados)

            messagebox.showinfo("Éxito", "🔓 Imagen descifrada correctamente.")
        except Exception:
            messagebox.showerror("Error", "❌ Clave incorrecta o archivo corrupto.")

    ventana = tk.Tk()
    ventana.title("🔐 Llave obtenida ENC")
    ventana.geometry("500x250")
    ventana.configure(bg="white")

    tk.Label(ventana, text="Desbloquea el cuadro robado", font=("Helvetica", 16, "bold"), fg="#333", bg="white").pack(pady=10)
    tk.Label(ventana, text="Introduce la clave secreta (ENC):", font=("Helvetica", 12), fg="#333", bg="white").pack(pady=5)
    entrada_clave = tk.Entry(ventana, show="*", width=40, font=("Helvetica", 12))
    entrada_clave.pack(pady=5)
    tk.Button(ventana, text="🔓 Descifrar imagen", command=descifrar_imagen, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", padx=10, pady=5).pack(pady=20)

    ventana.mainloop()

ventana_contrasena = tk.Tk()
ventana_contrasena.title("Acceso")
ventana_contrasena.geometry("400x150")
ventana_contrasena.configure(bg="white")

tk.Label(ventana_contrasena, text="Introduce la contraseña para acceder:", font=("Helvetica", 12), fg="#333", bg="white").pack(pady=10)
entrada_contrasena = tk.Entry(ventana_contrasena, show="*", width=30, font=("Helvetica", 12))
entrada_contrasena.pack(pady=5)
tk.Button(ventana_contrasena, text="Entrar", command=verificar_contrasena, font=("Helvetica", 12, "bold"), bg="#2196F3", fg="white", padx=10, pady=5).pack(pady=10)

ventana_contrasena.mainloop()

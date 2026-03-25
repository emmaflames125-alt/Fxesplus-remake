import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import base64
import io

class ImageToBase64App:
    def __init__(self, root):
        self.root = root
        self.root.title("Image → Base64 Converter")
        self.root.geometry("500x600")

        self.base64_data = ""

        # Buttons
        tk.Button(root, text="Load Image", command=self.load_image).pack(pady=10)
        tk.Button(root, text="Copy Base64", command=self.copy_base64).pack(pady=5)
        tk.Button(root, text="Save Base64", command=self.save_base64).pack(pady=5)

        # Image preview
        self.image_label = tk.Label(root)
        self.image_label.pack(pady=10)

        # Text output
        self.text = tk.Text(root, wrap="word", height=15)
        self.text.pack(fill="both", expand=True, padx=10, pady=10)

    def load_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")]
        )

        if not file_path:
            return

        try:
            # Read image and convert to base64
            with open(file_path, "rb") as img_file:
                encoded = base64.b64encode(img_file.read()).decode("utf-8")

            self.base64_data = encoded

            # Show base64 in textbox
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, encoded)

            # Preview image
            img = Image.open(file_path)
            img.thumbnail((300, 300))
            self.tk_image = ImageTk.PhotoImage(img)
            self.image_label.config(image=self.tk_image)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def copy_base64(self):
        if not self.base64_data:
            return
        self.root.clipboard_clear()
        self.root.clipboard_append(self.base64_data)
        messagebox.showinfo("Copied", "Base64 copied to clipboard!")

    def save_base64(self):
        if not self.base64_data:
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text File", "*.txt")]
        )

        if not file_path:
            return

        with open(file_path, "w") as f:
            f.write(self.base64_data)

        messagebox.showinfo("Saved", "Base64 saved successfully!")


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageToBase64App(root)
    root.mainloop()
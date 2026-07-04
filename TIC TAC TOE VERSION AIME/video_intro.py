import tkinter as tk
from pathlib import Path
import cv2
from PIL import Image, ImageTk

BASE_DIR = Path(__file__).resolve().parent
VIDEO_PATH = BASE_DIR / "assets" / "videos" / "intro_video.mp4"

class VideoIntro(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Vidéo d'introduction")
        self.geometry("900x600")
        self.configure(bg="black")

        self.label = tk.Label(self, bg="black", fg="white")
        self.label.pack(fill="both", expand=True)

        print("Chemin vidéo :", VIDEO_PATH)
        print("Existe :", VIDEO_PATH.exists())

        if not VIDEO_PATH.exists():
            self.label.config(text=f"Fichier introuvable :\n{VIDEO_PATH}")
            return

        self.cap = cv2.VideoCapture(str(VIDEO_PATH))
        print("isOpened :", self.cap.isOpened())

        self.running = True

        if not self.cap.isOpened():
            self.label.config(text=f"Impossible d'ouvrir la vidéo :\n{VIDEO_PATH}")
            return

        self.protocol("WM_DELETE_WINDOW", self.stop_video)
        self.update_frame()

    def update_frame(self):
        if not self.running or self.cap is None:
            return

        ret, frame = self.cap.read()
        print("ret =", ret)

        if not ret:
            self.label.config(text="Lecture terminée ou frame illisible.")
            return

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(frame)
        image = image.resize((900, 600))
        photo = ImageTk.PhotoImage(image=image)

        self.label.configure(image=photo, text="")
        self.label.image = photo

        fps = self.cap.get(cv2.CAP_PROP_FPS)
        if fps <= 0:
            fps = 30
        delay = int(1000 / fps)

        self.after(delay, self.update_frame)

    def stop_video(self):
        self.running = False
        if self.cap is not None:
            self.cap.release()
            self.cap = None
        self.destroy()

if __name__ == "__main__":
    app = VideoIntro()
    app.mainloop()
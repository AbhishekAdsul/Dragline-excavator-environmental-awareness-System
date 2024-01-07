from tkinter import *
from tkinter import ttk
import cv2
from PIL import Image, ImageTk

class rotation_right:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x450+200+250")  # Adjust the window size as needed
        self.root.title("Koyla Yantrik")

        self.video_frame = ttk.Label(self.root)
        self.video_frame.pack()

        self.play_video()

    def play_video(self):
        video_path = "videos/rotation right.mkv"  # Replace this with your video file path
        cap = cv2.VideoCapture(video_path)

        # Get original video frame dimensions
        frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        # Function to resize frames to fit within the window dimensions
        def resize_frame(frame):
            window_width = 800
            window_height = 450
            scale = min(window_width / frame_width, window_height / frame_height)
            new_width = int(frame_width * scale)
            new_height = int(frame_height * scale)
            resized_frame = cv2.resize(frame, (new_width, new_height))
            return resized_frame

        # Function to update the video frame
        def update_frame():
            ret, frame = cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = resize_frame(frame)
                frame = Image.fromarray(frame)
                frame = ImageTk.PhotoImage(image=frame)
                self.video_frame.configure(image=frame)
                self.video_frame.image = frame
                self.video_frame.after(30, update_frame)  # Update after 30 milliseconds
            else:
                cap.release()

        update_frame()

if __name__ == "__main__":
    root = Tk()
    obj = rotation_right(root)
    root.mainloop()

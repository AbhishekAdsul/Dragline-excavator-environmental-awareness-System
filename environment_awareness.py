import cv2
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class environment_awareness:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600+0+0")
        self.root.title("Intruder Detection")

        self.video_frame = ttk.Label(self.root)
        self.video_frame.pack()

        self.detected_label = Label(self.root, text="Detected near Dragline Operator", font=("Arial", 20), fg="red")
        self.detected_label.pack()  # Initially show label, but hide it when no person detected

        self.detect_intruder()

    def detect_intruder(self):
        cap = cv2.VideoCapture(0)

        # Load Haar Cascade classifier for pedestrian detection
        pedestrian_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        def check_intruder():
            ret, frame = cap.read()
            if ret:
                # Detect pedestrians
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                pedestrians = pedestrian_cascade.detectMultiScale(gray, 1.3, 5)

                # Display or hide label based on detection
                if len(pedestrians) > 0:
                    self.detected_label.pack()  # Show label if a person is detected
                else:
                    self.detected_label.pack_forget()  # Hide label if no person is detected

                # Draw rectangles around detected pedestrians
                for (x, y, w, h) in pedestrians:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.putText(frame, 'Person Detected', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

                # Display the frame in tkinter
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                img = ImageTk.PhotoImage(image=img)
                self.video_frame.configure(image=img)
                self.video_frame.image = img
                self.video_frame.after(30, check_intruder)
            else:
                cap.release()

        check_intruder()

if __name__ == "__main__":
    root = Tk()
    obj = environment_awareness(root)
    root.mainloop()

import face_recognition
import cv2
import numpy as np
import pandas as pd
from datetime import datetime
import os
import time

IMAGE_PATH = "E:\\FR_project\\img"
LOG_FILE = "E:\\FR_project\\face_log.xlsx"


known_face_encodings = []
known_face_names = []

def load_known_faces():
    """
    Load known face encodings from images in IMAGE_PATH.
    The image filename (without extension) is used as the person's name.
    """
    for file in os.listdir(IMAGE_PATH):
        img_path = os.path.join(IMAGE_PATH, file)
        
        image = face_recognition.load_image_file(img_path)
        
        face_encodings = face_recognition.face_encodings(image)
        if face_encodings:
            known_face_encodings.append(face_encodings[0])
            known_face_names.append(file.split('.')[0])
        else:
            print(f"No faces found in image: {file}")


load_known_faces()


video_capture = cv2.VideoCapture(0)

def initialize_excel():
    """Initialize the Excel file if it doesn't exist"""
    if not os.path.exists(LOG_FILE):
        
        df = pd.DataFrame(columns=["Name", "Timestamp"])
        df.to_excel(LOG_FILE, index=False, engine='openpyxl')
        print("Excel file created!")

def save_to_excel(name, timestamp):
    """
    Append a new row with the detected name and timestamp to the Excel log.
    """
    
    try:
        existing_df = pd.read_excel(LOG_FILE, engine='openpyxl')
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        
        initialize_excel()
        existing_df = pd.DataFrame(columns=["Name", "Timestamp"])
    
    
    new_entry = pd.DataFrame({"Name": [name], "Timestamp": [timestamp]})
    updated_df = pd.concat([existing_df, new_entry], ignore_index=True)
    updated_df.to_excel(LOG_FILE, index=False, engine='openpyxl')

def process_frame():
    """
    Process each frame to detect faces, log them, and prevent multiple entries.
    """
    logged_names = []  
    ret, frame = video_capture.read()
    if not ret:
        print("Failed to grab frame")
        return

    
    rgb_frame = frame[:, :, ::-1]
   
    rgb_frame = np.ascontiguousarray(rgb_frame)

    
    face_locations = face_recognition.face_locations(rgb_frame, model="hog")
    print(f"Found face locations: {face_locations}")

    if face_locations:
        try:
            
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        except Exception as e:
            print("Error computing face encodings:", e)
            face_encodings = []

        if face_encodings:
            face_names = []
            for face_encoding in face_encodings:
                
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]
                face_names.append(name)

            
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.putText(frame, name, (left + 6, bottom - 6),
                            cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

                
                if name not in logged_names:
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
                    save_to_excel(name, timestamp)
                    logged_names.append(name)

        else:
            print("No face encodings computed!")
    else:
        print("No faces found in this frame.")

    
    cv2.imshow("Video", frame)

   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        return False
    return True

def main():
    """Main function to run the face detection and logging process."""
    initialize_excel()
    while True:
        if not process_frame():
            break
        
        time.sleep(0.1) 

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

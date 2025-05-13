# Face Recognition and Logging System

This project implements a real-time face recognition system using the `face_recognition` library and OpenCV. It detects faces in a live video feed, identifies known individuals based on pre-loaded images, logs their names and timestamps to an Excel file, and includes a utility to remove duplicate log entries.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

## Features
- Real-time face detection and recognition using a webcam.
- Logs recognized faces with timestamps to an Excel file (`face_log.xlsx`).
- Prevents duplicate logging of the same face within a single frame.
- Utility script to remove duplicate entries from the log based on name and timestamp.
- Displays recognized names on the video feed with bounding boxes around detected faces.

## Prerequisites
- Python 3.7 or higher
- Webcam or camera device
- Required Python libraries:
  - `face_recognition`
  - `opencv-python` (`cv2`)
  - `numpy`
  - `pandas`
  - `openpyxl`
- A directory containing images of known individuals for face recognition.

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Set up a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install face_recognition opencv-python numpy pandas openpyxl
   ```

4. **Prepare the image directory**:
   - Create a folder (e.g., `img`) to store images of known individuals.
   - Place images in the folder, where each image filename (without extension) represents the person's name (e.g., `John.jpg` for a person named John).
   - Update the `IMAGE_PATH` variable in `live_face_detect.py` to point to this folder:
     ```python
     IMAGE_PATH = "path/to/your/img/folder"
     ```

5. **Update the log file path**:
   - Ensure the `LOG_FILE` path in `live_face_detect.py` points to your desired location for `face_log.xlsx`:
     ```python
     LOG_FILE = "path/to/your/face_log.xlsx"
     ```

## Project Structure
```
your-repo-name/
│
├── img/                    # Folder containing images of known faces
├── face_log.xlsx          # Excel file for logging detected faces
├── output.xlsx            # Excel file for cleaned log (after removing duplicates)
├── live_face_detect.py    # Main script for face detection and logging
├── clean.py               # Script to remove duplicate log entries
└── README.md              # Project documentation
```

### File Descriptions
- **`live_face_detect.py`**:
  - Loads known face encodings from images in the `img` folder.
  - Captures video from the webcam, detects faces, and recognizes them using `face_recognition`.
  - Logs recognized names and timestamps to `face_log.xlsx`.
  - Displays the video feed with bounding boxes and names.
- **`clean.py`**:
  - Removes duplicate entries from `face_log.xlsx` based on the "Name" and "Timestamp" columns.
  - Saves the cleaned data to `output.xlsx`.
- **`face_log.xlsx`**:
  - Stores the log of detected faces with columns: `Name` and `Timestamp`.
- **`output.xlsx`**:
  - Stores the cleaned log after running `clean.py`.

## Usage
1. **Run the face detection script**:
   ```bash
   python live_face_detect.py
   ```
   - The webcam will start, and the script will detect and recognize faces.
   - Recognized names and timestamps are logged to `face_log.xlsx`.
   - Press `q` to quit the video feed.

2. **Clean the log file**:
   - After collecting logs, remove duplicates by running:
     ```bash
     python clean.py
     ```
   - This generates `output.xlsx` with duplicate entries removed.

3. **View the logs**:
   - Open `face_log.xlsx` to view raw logs or `output.xlsx` to view cleaned logs using any spreadsheet software (e.g., Microsoft Excel, LibreOffice Calc).

## How It Works
1. **Face Loading**:
   - The `live_face_detect.py` script loads images from the `img` folder and computes face encodings using `face_recognition`.
   - Each image filename (without extension) is used as the person's name.

2. **Real-Time Detection**:
   - The script captures video frames from the webcam.
   - It uses the HOG model for face detection and compares detected faces against known encodings.
   - Recognized faces are labeled, and their names are logged with the current timestamp.

3. **Logging**:
   - Logs are appended to `face_log.xlsx` with columns `Name` and `Timestamp`.
   - The script prevents logging the same name multiple times in a single frame.

4. **Duplicate Removal**:
   - The `clean.py` script reads `face_log.xlsx`, removes duplicate rows based on `Name` and `Timestamp`, and saves the result to `output.xlsx`.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

Please ensure your code follows the existing style and includes appropriate documentation.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
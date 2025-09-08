# Vehicle-Counting-Project-OpenCV-Python-
A computer vision project that counts vehicles in traffic videos using Python and OpenCV.  It uses background subtraction and contour detection to detect moving vehicles and  increments a counter whenever they cross a predefined line.
# 🚗 Vehicle Counting Project (OpenCV + Python)

A computer vision project that **counts vehicles in a video** using Python and OpenCV.  
It detects moving vehicles, draws bounding boxes around them, and increases a counter whenever they cross a predefined line.  

---

## 📸 Demo
![Demo Screenshot](images/demo.png)  
*(Add your own screenshot, GIF, or a YouTube demo link here)*  

---

## ✨ Features
- Counts vehicles crossing a line in the video.  
- Ignores small objects or noise.  
- Shows bounding boxes and counter in real-time.  
- Easy to adjust line position and size filters.  

---

## 🛠️ Tech Used
- **Language:** Python  
- **Libraries:** OpenCV, NumPy  

---

## 📂 Project Files
vehicle-counting-opencv/
├── vehicle_counter.py # Main script
├── requirements.txt # Dependencies
├── images/ # Screenshots / demo GIFs
├── videos/ # Sample video (optional, or link externally)
├── .gitignore
├── LICENSE
└── README.md

## How to Run
Place a road traffic video in the project folder and rename it to video.mp4.
(Or change 'video.mp4' to 0 in the code if you want to use webcam)
Run the program:
python vehicle_counter.py

## Settings You Can Change
Inside vehicle_counter.py you can adjust:
min_width_react → minimum width of a vehicle.
min_height_react → minimum height of a vehicle.
count_line_position → position of the counting line.
offset → margin for line crossing detection.

## 📊 How It Works
Capture frames from video.
Convert to grayscale and blur to remove noise.
Detect moving objects using background subtraction.
Clean up the mask using morphology.
Draw boxes around vehicles.
Count vehicles when they cross the line.

#3 🚀 Future Ideas
Detect vehicle types (car, bike, bus).
Count across multiple lanes.
Save results in a file or database.
Show live count on a web or IoT dashboard.

## 📜 License
This project is licensed under the MIT License.

## 👤 Author
Jatinkumar
GitHub: Jatinkumar-08



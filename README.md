<h1>🧠 AI PCB Defect Detection & Classification</h1>

- An end-to-end PCB defect detection system using Image Processing + YOLOv8 Deep Learning + Streamlit Web Interface.

- This project detects, classifies, and visualizes PCB manufacturing defects such as:

   - Missing Hole<br>
   - Mouse Bite<br>
   - Open Circuit<br>
   - Short<br>
   - Spur<br>
   - Spurious Copper<br>

<hr>

<h2>📁 Project Structure</h2>

   ```
   AI_PCB_Defect_Detection_Classification/
   │
   ├── CNN Model Training/
   │   └── YOLO training scripts & notebooks
   │
   ├── Image Processing/
   │   └── Image preprocessing & defect crop generation code
   │
   ├── Results/
   │   ├── Image_Processing_Results/
   │   │   └── 64x64 cropped defect images
   │   └── Streamlit_Results/
   │       └── Output screenshots
   │
   ├── Streamlit/
   │   ├── Model/
   │   │   └── best_yolov8_pcb_defects.pt
   │   ├── app.py
   │   ├── YOLO_inference.py
   │   └── YOLO_requirements.txt
   │
   ├── LICENSE
   └── README.md
   ```
<hr>

<h2>🔄 Overall Workflow</h2><br>

```
   PCB Images

      ↓

   Image Processing (Defect Cropping)

      ↓

   YOLOv8 Model Training

      ↓

   YOLO Inference

      ↓

   Streamlit Web Application
```
<hr>

<h2>🧪 1. Image Processing Module</h2>
📂 Folder: Image Processing/

🔹 Purpose

- To extract defect regions from PCB images and generate 64×64 cropped defect samples.

🔹 Steps Performed

- Resize PCB images

- Apply Gaussian Blur

- Apply Thresholding on:

- Golden (reference) PCB images

- Defective PCB images

- Subtract golden image from defective image

- Detect contours (defect regions)

- Crop defects into 64×64 images

- Save cropped defect images for training

🔹 Output

📂 Results/Image_Processing_Results/
- Contains 64×64 cropped defect images used for YOLO training.

<hr>

<h2>🤖 2. CNN / YOLO Model Training</h2>

📂 Folder: CNN Model Training/

🔹 Model Used

- YOLOv8 (Ultralytics)

- Trained for multi-class object detection

🔹 Why YOLO?

- Handles small PCB defects efficiently

- Performs detection + classification in one step

- Faster and more accurate than pure CNN classifiers

🔹 Training Includes

- Custom dataset (cropped defect images)

- Bounding box annotations

- Validation metrics:

- Precision

- Recall

- mAP@50

- mAP@50-95

🔹 Output Model

📂 Streamlit/Model/
- best_yolov8_pcb_defects.pt

<hr>

<h2>🖥️ 3. Streamlit Web Application</h2>

📂 Folder: Streamlit/

🔹 Files Explained
| File                               | Description                  |
| ---------------------------------- | ---------------------------- |
| `app.py`                           | Streamlit frontend UI        |
| `YOLO_inference.py`                | Backend YOLO inference logic |
| `Model/best_yolov8_pcb_defects.pt` | Trained YOLO model           |
| `YOLO_requirements.txt`            | Required Python dependencies |

📦 Streamlit Requirements
 - 📄 File: YOLO_requirements.txt<br>
    🔹 Install requirements<br>
   ```
   pip install -r YOLO_requirements.txt
   
   ```

<hr>

<h2>▶️ How to Run the Project (Order Matters!)</h2>

✅ Step 1: Image Processing

- Run image processing scripts to generate cropped defect images.

📂 Output:

- Results/Image_Processing_Results/

✅ Step 2: Train YOLO Model

- Train YOLO using the processed dataset.

📂 Output model:

- Streamlit/Model/best_yolov8_pcb_defects.pt

✅ Step 3: Run Streamlit App
   ```
      
      cd Streamlit
      streamlit run app.py

   ```  

<hr>

<h3>🎯 What Happens</h3>

- Upload a PCB image

- YOLO detects defects

- Bounding boxes drawn around defects

- Labels & confidence scores displayed

- Results shown in browser

<hr>

<h3>📊 Results</h3>

📂 Results/Streamlit_Results/
Contains:

   - Output screenshots

   - Detected defects with bounding boxes

   - Confidence scores

<hr>

<h3>🧠 Key Features</h3>

✔ Automated defect detection<br>
✔ Handles multiple defect types<br>
✔ Small-defect friendly (YOLOv8)<br>
✔ Real-time inference<br>
✔ Web-based visualization<br>

<hr>

<h2>📜 License</h2>

- This project is licensed under the MIT License.
- See the LICENSE file for details

<hr>

<h2>👩‍💻 Author</h2>

- Uma Maheswari Rapolu
- AI PCB Defect Detection & Classification Project

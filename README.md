# OpticalFlow Video Processing 
This project provides an easy-to-use tool for visualizing optical flow in videos, using OpenCV and Streamlit. It calculates the motion between consecutive frames using the Farneback method for dense optical flow and allows users to visualize the motion with grayscale or HSV color-coded representations. The app features an intuitive interface for uploading video files, adjusting optical flow parameters like pyramid scaling, window size, and iteration count, and downloading the processed output. Designed for users interested in motion analysis, the tool simplifies complex video processing tasks without requiring advanced knowledge of computer vision techniques.

## Installation
To run the application locally, follow these steps:
### 1. Clone the repository
```
git clone https://github.com/your-repo/optical-flow-streamlit.git
cd optical-flow-streamlit
```
### 2. Install the required Python packages:
```
pip install streamlit opencv-python numpy
```
### 3. Run the Application 
```
streamlit run app.py

```


To use the CLI version here is the following help

```py
usage: CLIapp.py [-h] [-o OUTPUT] input_video

Optical Flow Processing on a Video

positional arguments:
  input_video           Path to the input video file

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Path to the output video file (default: output.mp4)
```

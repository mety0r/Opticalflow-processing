# OpticalFlow Video Processing 
This application is a video processing tool that calculates the optical flow between consecutive frames of a video file. It uses the Farneback method to compute dense optical flow, and allows users to visualize the motion between frames using grayscale or HSV color-coded representations. The app is built using Streamlit for the user interface, OpenCV for video processing, and NumPy for array operations.

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

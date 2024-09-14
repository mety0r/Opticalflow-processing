import streamlit as st
import cv2 as cv
import numpy as np
import tempfile
import os

def process_frame(frame1, frame2, pyr_scale, levels, winsize, iterations, poly_n, poly_sigma, flags, color_mode='grayscale'):
    prvs = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)
    next = cv.cvtColor(frame2, cv.COLOR_BGR2GRAY)
    flow = cv.calcOpticalFlowFarneback(prvs, next, None, pyr_scale, levels, winsize, iterations, poly_n, poly_sigma, flags)
    mag, ang = cv.cartToPolar(flow[..., 0], flow[..., 1])
    
    if color_mode == 'grayscale':
        # Grayscale representation
        hsv = np.zeros_like(frame1)
        hsv[..., 0] = ang * 180 / np.pi / 2
        hsv[..., 2] = cv.normalize(mag, None, 0, 255, cv.NORM_MINMAX)
        processed_frame = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
    elif color_mode == 'hsv':
        # HSV color-coded representation
        hsv = np.zeros_like(frame1)
        hsv[..., 0] = ang * 180 / np.pi / 2
        hsv[..., 1] = 255
        hsv[..., 2] = cv.normalize(mag, None, 0, 255, cv.NORM_MINMAX)
        processed_frame = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
    else:
        raise ValueError("Invalid color_mode. Use 'grayscale' or 'hsv'.")
    
    return processed_frame

def process_video(uploaded_file, pyr_scale, levels, winsize, iterations, poly_n, poly_sigma, flags, frame_skip, color_mode):
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    tfile.seek(0)
    
    video = cv.VideoCapture(tfile.name)
    
    frame_width = int(video.get(cv.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))
    frame_rate = int(video.get(cv.CAP_PROP_FPS))
    frame_count = int(video.get(cv.CAP_PROP_FRAME_COUNT))
    
    frames = []
    ret, prev_frame = video.read()
    frame_number = 1
    while video.isOpened():
        ret, next_frame = video.read()
        if ret and frame_number % frame_skip == 0:
            processed_frame = process_frame(prev_frame, next_frame, pyr_scale, levels, winsize, iterations, poly_n, poly_sigma, flags, color_mode)
            frames.append(processed_frame)
            prev_frame = next_frame
        frame_number += 1
        if not ret:
            break
    
    video.release()
    
    out_path = os.path.join(tempfile.gettempdir(), 'output.mp4')
    out = cv.VideoWriter(out_path, cv.VideoWriter_fourcc(*'mp4v'), frame_rate // frame_skip, (frame_width, frame_height))
    for frame in frames:
        out.write(frame.astype('uint8'))
    out.release()
    
    return out_path

def main():
    st.title("Optical Flow Video Processing")
    
    uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov", "mkv"])
    
    st.sidebar.title("Optical Flow Parameters")
    pyr_scale = st.sidebar.slider("Pyramid Scale (pyr_scale)", 0.1, 1.0, 0.5)
    levels = st.sidebar.slider("Number of Levels (levels)", 1, 10, 3)
    winsize = st.sidebar.slider("Window Size (winsize)", 5, 25, 15)
    iterations = st.sidebar.slider("Number of Iterations (iterations)", 1, 10, 3)
    poly_n = st.sidebar.slider("Size of Pixel Neighborhood (poly_n)", 5, 7, 5)
    poly_sigma = st.sidebar.slider("Standard Deviation (poly_sigma)", 1.1, 2.0, 1.2)
    flags = 0  # Default value for flags
    frame_skip = st.sidebar.slider("Process every nth frame", 1, 10, 1)
    color_mode = st.sidebar.radio("Color Mode", ["Grayscale", "HSV"], index=0).lower()
    
    if uploaded_file is not None:
        with st.spinner('Processing...'):
            output_path = process_video(uploaded_file, pyr_scale, levels, winsize, iterations, poly_n, poly_sigma, flags, frame_skip, color_mode)
        st.success('Processing complete!')
        
        with open(output_path, "rb") as file:
            btn = st.download_button(
                label="Download Processed Video",
                data=file,
                file_name="output.mp4",
                mime="video/mp4"
            )

if __name__ == "__main__":
    main()

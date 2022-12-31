from flask import Flask, render_template, request
import cv2
import numpy as np
from sklearn.model_selection import train_test_split

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_video():
    # Get the uploaded video file
    video_file = request.files['video']

    # Load the video file
    video_capture = cv2.VideoCapture(video_file)

    # Initialize an empty list to store the frames
    frames = []

    # Extract the frames from the video
    while True:
        # Read the next frame from the video
        success, frame = video_capture.read()

        # If there are no more frames, break the loop
        if not success:
            break

        # Add the frame to the list
        frames.append(frame)

    # Initialize an empty list to store the processed frames
    processed_frames = []

    # Iterate over the frames and preprocess them
    for frame in frames:
        # Resize the frame to a smaller size
        frame = cv2.resize(frame, (64, 64))

        # Convert the frame to grayscale
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Add the processed frame to the list
        processed_frames.append(frame)

    # Convert the processed frames to a NumPy array
    X = np.asarray(processed_frames)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2)

    # Train the model using the training data
    model.fit(X_train, y_train)

    # Initialize an empty list to store the predictions
    predictions = []

    # Iterate over the frames in the video
    for frame in frames:
        # Preprocess the frame
        processed_frame = preprocess_frame(frame)

        # Convert the frame to a NumPy array
        image_data = np.asarray(processed_frame)

        # Use the trained model to make a prediction
        prediction = model.predict(image_data)

        # Add the prediction to the list
        predictions.append(prediction)

    return render_template('prediction.html', predictions=predictions)

if __name__ == '__main__':
    app.run()

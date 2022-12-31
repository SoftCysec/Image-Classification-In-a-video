from flask import Flask, render_template, request
import cv2
import numpy as np
from sklearn.externals import joblib

app = Flask(__name__)

# Load the trained model from a file
model = joblib.load('model.pkl')

@app.route('/', methods=['GET', 'POST'])
def classify_video():
  if request.method == 'POST':
      # Get the uploaded video file
      video_file = request.files['video']

      # Use OpenCV or FFmpeg to extract the frames from the video
      frames = extract_frames_from_video(video_file)

      # Initialize an empty list to store the predictions
      predictions = []

      # Iterate over the frames and classify each one using the trained model
      for frame in frames:
          # Convert the frame to a NumPy array
          image = np.asarray(frame)

          # Use the trained model to make a prediction
          prediction = model.predict(image)

          # Add the prediction to the list
          predictions.append(prediction)

      # Render the prediction results in a template
      return render_template('prediction.html', predictions=predictions)
  else:
      # Render the upload form
      return render_template('upload.html')

if __name__ == '__main__':
  app.run()

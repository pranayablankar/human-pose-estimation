import cv2
import mediapipe as mp

# Initialize Mediapipe Pose
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

# Set up the pose estimator
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Open video capture (0 for webcam, or provide path to a video file)
# cap = cv2.VideoCapture("4584879-uhd_3840_2160_25fps.mp4")  # Replace 0 with the path to a video file if needed
cap = cv2.VideoCapture(0) 
if not cap.isOpened():
    print("Error: Could not open video source.")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Resize the frame for faster processing
    new_width = 640  # Set desired width
    new_height = 480  # Set desired height
    frame = cv2.resize(frame, (new_width, new_height))
    
    # Convert the frame to RGB (Mediapipe expects RGB images)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Perform pose estimation
    results = pose.process(frame_rgb)
    
    # Check if pose landmarks were detected
    if results.pose_landmarks:
        # Get image dimensions
        h, w, c = frame.shape
        
        # Draw landmarks as keypoints
        for idx, landmark in enumerate(results.pose_landmarks.landmark):
            # Convert normalized coordinates to pixel coordinates
            cx, cy = int(landmark.x * w), int(landmark.y * h)
            
            # Draw the keypoints on the image
            cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)  # Green color, filled circle
        
        # Optional: Draw landmarks with connections on a copy of the image
        annotated_frame = frame.copy()
        mp_drawing.draw_landmarks(
            annotated_frame, 
            results.pose_landmarks, 
            mp_pose.POSE_CONNECTIONS
        )
        
        # Display the output images
        cv2.imshow("Pose Landmarks", frame)
        cv2.imshow("Pose Drawing", annotated_frame)
    
    else:
        print("No pose landmarks detected.")
    
    # Wait for a key press and check if 'q' is pressed to break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

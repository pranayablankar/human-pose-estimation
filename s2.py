import cv2
import mediapipe as mp
#Initialize Mediapipe Pose
mp_pose mp.solutions.pose
pose = mp_pose. Pose (static_image_mode=True, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils
# Load an image
image_path = "pose-best-case-image-png-format.png" #Replace
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor (image, cv2.COLOR_BGR2RGB)
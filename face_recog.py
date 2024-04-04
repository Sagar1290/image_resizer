from deepface import DeepFace

def get_facial_coords(img_path):
  face_objs = DeepFace.extract_faces(
      img_path=img_path,
      target_size=(100, 100),  # Can be adjusted if needed
      detector_backend="yunet",
      enforce_detection=False
  )

  if face_objs:
    return face_objs[0]['facial_area']
  else:
    return None


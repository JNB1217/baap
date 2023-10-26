import cv2
import mediapipe as mp
import math

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Inicializa el modelo de detección de manos de Mediapipe
hands = mp_hands.Hands()

# Captura de video desde la cámara (puedes cambiar esto según tu fuente)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    frame = cv2.flip(frame, 1)
    height, width, _ = frame.shape
    color_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detectar las manos en la imagen
    results = hands.process(color_frame)

    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            # Calcular el centroide de la mano
            hand_center_x = sum([landmark.x for landmark in landmarks.landmark]) / len(landmarks.landmark)
            hand_center_y = sum([landmark.y for landmark in landmarks.landmark]) / len(landmarks.landmark)

            # Calcula el ángulo en el plano Z (en radianes)
            angle_z_rad = math.atan2(hand_center_y - frame.shape[0] / 2, hand_center_x - frame.shape[1] / 2)

            # Convierte el ángulo a grados
            angle_z_deg = math.degrees(angle_z_rad)

            # Dibuja líneas para visualizar la rotación
            cv2.line(frame, (int(frame.shape[1] / 2), int(frame.shape[0] / 2)),
                     (int(hand_center_x * frame.shape[1]), int(hand_center_y * frame.shape[0])), (0, 255, 0), 2)
            cv2.putText(frame, f"angulo Z: {angle_z_deg:.2f} grados", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Muestra el video con información de rotación
    cv2.imshow('Hand Rotation Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

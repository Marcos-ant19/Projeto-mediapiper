import cv2
import mediapipe as mp
import subprocess
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

bloco = None
ultimo_comando = 0
tempo_espera = 1.5

while True:
    sucesso, frame = cap.read()

    if not sucesso:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    resultado = hands.process(rgb)

    if resultado.multi_hand_landmarks:
        for hand_landmarks in resultado.multi_hand_landmarks:

            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            pontos = hand_landmarks.landmark

            indicador = pontos[8].y < pontos[6].y
            medio = pontos[12].y < pontos[10].y
            anelar = pontos[16].y < pontos[14].y
            mindinho = pontos[20].y < pontos[18].y

            agora = time.time()

            # Gesto 1: indicador levantado
            if indicador and not medio and not anelar and not mindinho:
                if agora - ultimo_comando > tempo_espera:
                    if bloco is None:
                        bloco = subprocess.Popen("notepad.exe")
                        print("Bloco de notas aberto")
                    ultimo_comando = agora

            # Gesto 2: indicador e médio levantados
            elif indicador and medio and not anelar and not mindinho:
                if agora - ultimo_comando > tempo_espera:
                    if bloco is not None:
                        subprocess.call("taskkill /f /im notepad.exe", shell=True)
                        bloco = None
                        print("Bloco de notas fechado")
                    ultimo_comando = agora

    cv2.imshow("Testando programa", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
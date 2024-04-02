import cv2
import time

def capture_images(interval=0.5, save_path='./data/images'):
    # Inicjalizacja kamery z użyciem backendu AVFoundation dla macOS
    cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION if cv2.__version__.startswith('4') else 0)
    if not cap.isOpened():
        print("Nie można otworzyć kamery.")
        return

    try:
        print("Naciśnij 'q' aby zakończyć.")
        last_time = time.time() - interval  # Zapewnia, że pierwsze zdjęcie zostanie zrobione natychmiast
        while True:
            current_time = time.time()
            if current_time - last_time >= interval:
                # Czytanie obrazu z kamery
                ret, frame = cap.read()
                if not ret:
                    print("Nie udało się odczytać obrazu. Koniec pracy.")
                    break

                # Zapisywanie obrazu do pliku
                filename = f"{save_path}/image_{int(time.time())}.jpg"
                cv2.imwrite(filename, frame)
                print(f"Zapisano zdjęcie: {filename}")
                last_time = current_time

            # Wyświetlenie obrazu
            cv2.imshow('frame', frame)
            
            # Sprawdzenie, czy został naciśnięty klawisz 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        # Zwolnienie kamery i zamknięcie okien
        cap.release()
        cv2.destroyAllWindows()

capture_images()

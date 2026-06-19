import pygame

pygame.mixer.init()

while True:
    print("\n===== Music Player =====")
    print("1. Play Song")
    print("2. Pause Song")
    print("3. Resume Song")
    print("4. Stop Song")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        song = input("Enter MP3 file path: ")

        try:
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()
            print("Playing...")
        except:
            print("Could not load file.")

    elif choice == "2":
        pygame.mixer.music.pause()
        print("Paused.")

    elif choice == "3":
        pygame.mixer.music.unpause()
        print("Resumed.")

    elif choice == "4":
        pygame.mixer.music.stop()
        print("Stopped.")

    elif choice == "5":
        pygame.mixer.music.stop()
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
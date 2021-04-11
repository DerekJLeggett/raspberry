# Write your code here :-)
#!/usr/bin/env python3
import pygame
import pygame.camera
from gtts import gTTS
import os

pygame.init()
pygame.camera.init()
pygame.joystick.init()
size = (640,480)
display = pygame.display.set_mode(size,0)
cam = pygame.camera.Camera("/dev/video0", size)
cam.start()

def say(text):
    tts = gTTS(text=text, lang='en')
    tts.save('speech.mp3')
    os.system("cvlc --play-and-exit speech.mp3")
    os.remove('speech.mp3')
say("All systems nominal")
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    # Get the name from the OS for the controller/joystick.
    print("Joystick name: " + joystick.get_name())
    for x in range(0, joystick.get_numaxes()):
        print("Axis: " + str(x) + " - " + str(joystick.get_axis(x)))
    for x in range(0, joystick.get_numbuttons()):
        print("Button: " + str(x) + " - " + str(joystick.get_button(x)))
    for x in range(0, joystick.get_numhats()):
        print("Hats: " + str(x) + " - " + str(joystick.get_hat(x)))
drum = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_tom_mid_hard.wav")
cymbal = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_cymbal_hard.wav")
snare = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_snare_hard.wav")
cowbell = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_cowbell.wav")
loop = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/loop_amen_full.wav")

done = False
while not done:
    image = cam.get_image()
    display.blit(image, (0,0))
    pygame.display.flip()
    # EVENT PROCESSING STEP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.JOYDEVICEADDED:
            joystick = pygame.joystick.Joystick(0)
            joystick.init()
            say("Joystick added")
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN
        # JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print(event.button)
            if event.button == 0:
                drum.play()
                print("Drum")
            if event.button == 1:
                cymbal.play()
                print("Cymbal")
            if event.button == 2:
                snare.play()
                print("Snare")
            if event.button == 3:
                cowbell.play()
                print("Cowbell")
            if event.button == 4:
                loop.play()
                print("Loop")
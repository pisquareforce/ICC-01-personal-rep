import pygame
import pygame_gui
import sys
import os
import base64
from cryptography.fernet import Fernet


# References: 
# https://pygame-gui.readthedocs.io/en/latest/theme_reference/theme_text_entry_line.html
# https://pypi.org/project/pygame/
# https://github.com/baraltech/Text-Input-PyGame/blob/main/main.py
# https://www.youtube.com/watch?v=G8MYGDf_9ho
# https://pypi.org/project/pygame-gui/
# https://cryptography.io/en/latest/installation/
# https://pypi.org/project/pygame-gui/
# https://www.youtube.com/watch?v=nsPeRkbhpcU&list=PL6gx4Cwl9DGBBnHFDEANbv9q8T4CONGZE&index=2
# https://www.peteronion.org.uk/PyGobjectGtk+3/PyGtk.html




#
# 1. Encript class 
#
class Encript:
    def __init__(self):
        self.key_file = "key.key"
        self.key = self.load_or_generate_key()
        self.cipher = Fernet(self.key)

    def load_or_generate_key(self):
        
        if os.path.exists(self.key_file):
            return open(self.key_file, "rb").read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, "wb") as key_file:
                key_file.write(key)
            return key

    def encrypt_message(self, message):
        
        return self.cipher.encrypt(message.encode()).decode()
    
    
    def decrypt_message(self, encrypted_message, key):
        fernet = Fernet(key)
        decrypted_message = fernet.decrypt(encrypted_message).decode()
        print(f" -- Mensagem desencriptada: {decrypted_message}")
        return decrypted_message



#
# 2. GUI class inherits the proprties coming from Encript class
#


class GUI(Encript):
    def __init__(self, WIDTH=600, HEIGHT=300):
        super().__init__()
        pygame.init()
        
        # Screen Setup
        self.WIDTH, self.HEIGHT = WIDTH, HEIGHT
        self.SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("GUI - Encryption (Task6)")

        # Load Background Image
        self.load_background()


        # UI Manager
        self.manager = pygame_gui.UIManager((WIDTH, HEIGHT))

        # Text Input Field
        self.text_input = pygame_gui.elements.UITextEntryLine(
                                                              relative_rect=pygame.Rect((100, 100), (200, 50)), 
                                                              manager=self.manager, 
                                                              object_id='#main_text_entry')

        # Encrypt Button
        self.button_encr = pygame.Surface((200, 50))
        self.button_encr.fill((255, 0, 0))  # Red Button
        
        self.button_encr1 = pygame.Surface((200, 50))
        self.button_encr1.fill((255, 0, 0))  # Red Button

        # Unencrypt

        # Button Text
        self.font1 = pygame.font.SysFont("Arial", 25)
        self.text1 = self.font1.render("Encrypt", True, (255, 255, 255))
        self.text_rect = self.text1.get_rect(center=(200, 225))
        
        self.font3 = pygame.font.SysFont("Arial", 25)
        self.text3 = self.font3.render("Dencrypt", True, (0, 0, 0))
        self.text_rect3 = self.text3.get_rect(center=(450, 225))

        

        # Info Text
        self.font2 = pygame.font.SysFont("Arial", 15)
        self.text2 = self.font2.render("About: This software encrypts messages, file or files", 
                                        True, 
                                        (255, 255, 255))
                                        
        self.text_rect2 = self.text2.get_rect(center=(300, 285))

        self.clock = pygame.time.Clock()
        self.running = True
        self.user_message = ""

        self.encrypted_msg = ""


        # Rectangle for the ouput - Flag 1
        self.rect_width, self.rect_height = 100, 50
        self.rect_surface = pygame.Surface((self.rect_width, self.rect_height))
        self.rect_surface.fill((0, 0, 0))  
        self.border_color = (255, 255, 255)  
        self.border_thickness = 1
        self.font_m = pygame.font.Font(None, 15)
        self.name:str = ""
        pygame.draw.rect(self.rect_surface, self.border_color, (0, 0, self.rect_width, self.rect_height), self.border_thickness)
        self.name = "Flag 1"     
        self.text_ = self.font1.render(self.name, True, (255, 255, 255))  # White text
        self.text_rect_ = self.text_.get_rect(center=(self.rect_width // 2, self.rect_height // 2)) 

        self.encrypted_message = ""

    def load_background(self):
       self.image = pygame.image.load("Background.png")

    def handle_dencryption(self):
        return self.decrypt_message(self.key)


    def update_screen(self, time_delta):
        """ Updates and draws the screen. """
        self.SCREEN.fill((0, 0, 0))

        if self.image:
            self.SCREEN.blit(self.image, (self.WIDTH - 324, 0))

        self.manager.update(time_delta)
        self.manager.draw_ui(self.SCREEN)
        #self.rect_surface.blit(self.text, self.text_rect)
        self.SCREEN.blit(self.button_encr1, (350, 200))
        self.SCREEN.blit(self.button_encr, (100, 200))
        self.SCREEN.blit(self.text1, self.text_rect)
        self.SCREEN.blit(self.text2, self.text_rect2)
        self.SCREEN.blit(self.text3, self.text_rect3)

        # Rectangle for the output - Flags
        self.SCREEN.blit(self.rect_surface, (100, 20))  # Position (150, 200)
        self.rect_surface.blit(self.text_, self.text_rect_)

        pygame.display.update()
        

    def run(self):

        """ Main GUI loop. """
        while self.running:
            time_delta = self.clock.tick(60) / 500.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                    if event.ui_object_id == '#main_text_entry':
                        self.user_message = event.text

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    #print(f"Mouse clicked at ({x}, {y})")


                    #
                    #  Encrypt Button
                    #
                    if 100 <= x <= 300 and 200 <= y <= 250:             # Correct button area
                        self.user_message = self.text_input.get_text()  # Get latest input

                    

                        # Rectangle for the ouput - Flag 2
                        self.rect_width, self.rect_height = 100, 50
                        self.rect_surface = pygame.Surface((self.rect_width, self.rect_height))
                        self.rect_surface.fill((0, 0, 0))  
                        self.border_color = (255, 255, 255)  
                        self.border_thickness = 1
                        self.font_m = pygame.font.Font(None, 15)
                        pygame.draw.rect(self.rect_surface, self.border_color, (0, 0, self.rect_width, self.rect_height), self.border_thickness)
                        self.name = "Flag 2"     
                        self.text_ = self.font1.render(self.name, True, (255, 255, 255))  # White text
                        self.text_rect_ = self.text_.get_rect(center=(self.rect_width // 2, self.rect_height // 2)) 

                        print(f" -- Mensagem: {self.user_message}")                      # Print original text
                        print(f" -- Mensagem encriptada: {self.handle_encryption()}")    # Print encrypted text
                        

                    #
                    #  Dencrypt Button
                    #
                    elif 352 <= x <= 546 and 200 <= y <= 250:

                        # Rectangle for the ouput - Flag 3
                        self.rect_width, self.rect_height = 100, 50
                        self.rect_surface = pygame.Surface((self.rect_width, self.rect_height))
                        self.rect_surface.fill((0, 0, 0))  
                        self.border_color = (255, 255, 255)  
                        self.border_thickness = 1
                        self.font_m = pygame.font.Font(None, 15)


                        test:str = ""
                        test = self.handle_encryption()
                        if test and test.strip():
                            msg = self.decrypt_message(test.encode(), self.key)
                        else: 
                            print(" -- Não tem informação para desencriptar;")


                        
                    
                        pygame.draw.rect(self.rect_surface, self.border_color, (0, 0, self.rect_width, self.rect_height), self.border_thickness)
                        self.name = "Flag 3"     
                        self.text_ = self.font1.render(self.name, True, (255, 255, 255))  # White text
                        self.text_rect_ = self.text_.get_rect(center=(self.rect_width // 2, self.rect_height // 2)) 

                elif event.type == pygame.MOUSEMOTION:
                    x, y = event.pos

                    if 100 <= x <= 300 and 200 <= y <= 250:
                        self.button_encr.fill((100, 0, 0))                
                    elif 352 <= x <= 546 and 200 <= y <= 250:
                        self.button_encr1.fill((100, 0, 0)) 
                    else:
                        self.button_encr.fill((255, 0, 0))              # Default red
                        self.button_encr1.fill((255, 0, 0))             # Default red
                self.manager.process_events(event)
            self.update_screen(time_delta)

        pygame.quit()
        sys.exit()

    def handle_encryption(self):
        """ Encrypts user input and prints output to the terminal. """
        if self.user_message.strip():  # Ensure input is not empty
            encrypted_msg = self.encrypt_message(self.user_message)      # está apenas definida localmente
            return encrypted_msg
        else:
            print("Warning: No text to encrypt.")


if __name__ == "__main__":
    gui = GUI()
    gui.run()


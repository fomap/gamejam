import pygame
import sys

def main(correct_ans):
    
    pygame.init()
    WIDTH, HEIGHT = 1400, 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    pygame.display.set_caption("Final Screen")   
    
    pygame.mixer.music.load('assets/music/menu.mp3')
    pygame.mixer.music.play(0)



    class Button():
        def __init__(self, x, y, image, scale):
            width = image.get_width()
            height = image.get_height()
            self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False

        def click(self, surface):
            action = False
            #get mouse position
            pos = pygame.mouse.get_pos()

            #check mouseover and clicked conditions
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            #draw button on screen
            surface.blit(self.image, (self.rect.x, self.rect.y))

            return action



    bg1 = pygame.image.load('assets/title/finalbg.png')

    #linear algebruh
    img_1 = pygame.image.load('assets/title/menu.png').convert_alpha()
    button1 = Button(510, 420, img_1, 1)

    img_2 = pygame.image.load('assets/title/info.png').convert_alpha()
    button2 = Button(510, 520, img_2, 1)
    
    img_3 = pygame.image.load('assets/title/quit.png').convert_alpha()
    button3 = Button(510, 620, img_3, 1)


    

    newans = correct_ans



    res = 4 - newans
    font = pygame.font.SysFont("comicsansms",40)
    text = font.render(f"CONGRATULATIONS, YOU HAVE {res} RESTAKE!", True, (255,255,255))
    rect = text.get_rect()
    rect.center = (WIDTH // 2, 40)

    


    done = False


    while not done:
        pygame.time.wait(100)

       

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                
            
    
           
        screen.blit(bg1, (0,0)) 
        
        if button1.click(screen):
            import titlescreen
            titlescreen.main()
            
            
        if button2.click(screen):
            import infoscreen
            infoscreen.main()
            
        if button3.click(screen):
            done = True
        
        if res == 1:
            text = font.render(f"CONGRATULATIONS, YOU HAVE {res} RETAKE!", True, (255,255,255))
        else:
            text = font.render(f"CONGRATULATIONS, YOU HAVE {res} RETAKES!", True, (255,255,255))
     
        screen.blit(text, rect)
        

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

#Pygame dev 1

import pygame

Screen_Title = "Crossy RPG"
Screen_Width = 800
Screen_Height = 800
White_Color = (255, 255, 255)
Black_Color = (0, 0, 0)
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('comicsans', 75)

class Game:

    Tick_Rate = 60
    
    def __init__(self, image_path, title, width, height):
        self.title = title
        self.width = width
        self.height = height
        self.game_screen = pygame.display.set_mode((width, height))
        self.game_screen.fill(White_Color)
        pygame.display.set_caption(title)

        background_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(background_image, (width, height))

    def run_game_loop(self, level_speed):
        is_game_over = False
        did_win = False
        direction = 0

        player_character = PlayerCharacter('player.png', 382, 700, 36, 48)

        enemy_0 = NonPlayerCharacter('enemy.png', 20, 600, 48, 36)
        enemy_0.Speed *= level_speed

        enemy_1 = NonPlayerCharacter('enemy.png', self.width - 50, 400, 48, 36)
        enemy_1.Speed *= level_speed

        enemy_2 = NonPlayerCharacter('enemy.png', self.width - 400, 200, 48, 36)
        enemy_2.Speed *= level_speed

        enemies = [enemy_0]
        
        treasure = GameObject('treasure.png', 374, 50, 52, 36)
        
        while not is_game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction = 1
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
                print(event)

            self.game_screen.fill(White_Color)
            self.game_screen.blit(self.image, (0, 0))

            treasure.draw(self.game_screen)

            player_character.move(direction, self.height)
            player_character.draw(self.game_screen)

            enemy_0.move(self.width)
            enemy_0.draw(self.game_screen)
            
            if level_speed > 2:
                enemies.append(enemy_1)
                enemy_1.move(self.width)
                enemy_1.draw(self.game_screen)
            if level_speed > 4:
                enemies.append(enemy_2)
                enemy_2.move(self.width)
                enemy_2.draw(self.game_screen)

            if player_character.detect_collision(treasure):
                is_game_over = True
                did_win = True
                text = font.render('And there was much rejoicing....', True, Black_Color)
                self.game_screen.blit(text, (5, 150))
                pygame.display.update()
                clock.tick(1)
                break
            
            else:
                for enemy in enemies:
                    if player_character.detect_collision(enemy):
                        is_game_over  = True
                        did_win = False
                        text = font.render('Your Mother was a hampster!', True, Black_Color)
                        self.game_screen.blit(text, (25, 150))
                        pygame.display.update()
                        clock.tick(1)
                        break
            
            pygame.display.update()
            clock.tick(self.Tick_Rate)

        if did_win:
            self.run_game_loop(level_speed + 0.5)
        else:
            return

class GameObject:

    def __init__(self, image_path, x, y, width, height):
        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, (width, height))
        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.height = height

    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))

class PlayerCharacter(GameObject):

    Speed = 5

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, direction, max_height):
        if direction > 0:
            self.y_pos -= self.Speed
        elif direction < 0:
            self.y_pos += self.Speed

        if self.y_pos >= max_height - 50:
            self.y_pos = max_height - 50

    def detect_collision(self, other_body):
        if self.y_pos >= other_body.y_pos + other_body.height:
            return False
        elif self.y_pos <= other_body.y_pos:
            return False

        if self.x_pos >= other_body.x_pos + other_body.width:
            return False
        elif self.x_pos + self.width <= other_body.x_pos:
            return False

        return True

class NonPlayerCharacter(GameObject):

    Speed = 5

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, max_width):
        if self.x_pos <= 20:
           self.Speed = abs(self.Speed)
        elif self.x_pos >= max_width - 70:
            self.Speed = -abs(self.Speed)
        self.x_pos += self.Speed

pygame.init()

new_game = Game('background.png',Screen_Title, Screen_Width, Screen_Height)
new_game.run_game_loop(1)

pygame.quit()
quit()

    ##player_image = pygame.image.load("C:/Users/Owner/Desktop/Pygame Project Files/player.png")
       ##player_image = pygame.transform.scale(player_image, (50, 50))


        #pygame.draw.rect(game_display, Black_Color, [350, 350, 100, 100])
        #pygame.draw.circle(game_display, Black_Color, (400, 300), 50)

        #game_screen.blit(player_image, (375, 375))


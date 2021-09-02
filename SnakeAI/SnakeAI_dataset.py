import sys
import pygame
import random

pygame.init()

f = open('snake2.csv', 'w')

f.write('w0,w1,w2,w3,a0,a1,a2,a3,b0,b1,b2,b3,direction' + '\n')


def add_data():
    w0 = snake.pos[1] - game.wall_offset
    w1 = game.w - game.wall_offset - snake.pos[0]
    w2 = game.h - game.wall_offset - snake.pos[1]
    w3 = snake.pos[0] - game.wall_offset

    if snake.pos[0] == apple.x and snake.pos[1] > apple.y:
        a0 = 1
    else:
        a0 = 0

    if snake.pos[0] < apple.x and snake.pos[1] == apple.y:
        a1 = 1
    else:
        a1 = 0

    if snake.pos[0] == apple.x and snake.pos[1] < apple.y:
        a2 = 1
    else:
        a2 = 0

    if snake.pos[0] > apple.x and snake.pos[1] == apple.y:
        a3 = 1
    else:
        a3 = 0

    for part in snake.body:
        if snake.pos[0] == part[0] and snake.pos[1] > part[1]:
            b0 = 1
            break
    else:
        b0 = 0

    for part in snake.body:
        if snake.pos[0] < part[0] and snake.pos[1] == part[1]:
            b1 = 1
            break
    else:
        b1 = 0

    for part in snake.body:
        if snake.pos[0] == part[0] and snake.pos[1] < part[1]:
            b2 = 1
            break
    else:
        b2 = 0

    for part in snake.body:
        if snake.pos[0] > part[0] and snake.pos[1] == part[1]:
            b3 = 1
            break
    else:
        b3 = 0

    direction = 0

    if snake.y_change == 1:
        direction = 2

    if snake.y_change == -1:
        direction = 0

    if snake.x_change == 1:
        direction = 1

    if snake.x_change == -1:
        direction = 3

    if snake.direction != snake.pre_direction or random.random() < 0.05:

        f.write(",".join([str(w0), str(w1), str(w2), str(w3),
                          str(a0), str(a1), str(a2), str(a3),
                          str(b0), str(b1), str(b2), str(b3),
                          str(direction)]) + '\n')
        return True

    else:
        return False


class Apple:
    def __init__(self):
        self.w = 10
        self.h = 10
        self.x = random.randrange(40, game.w - 40, 10)
        self.y = random.randrange(40, game.h - 40, 10)
        self.color = (138, 43, 226)

    def show(self):
        pygame.draw.rect(game.d, self.color, [self.x, self.y, self.w, self.h])


class Snake:
    def __init__(self):
        self.w = 10
        self.h = 10
        self.x = game.w / 2
        self.y = game.h / 2
        self.pos = [self.x, self.y]
        self.name = "mohammad ali"
        self.color = (0, 127, 0)
        self.speed = 10
        self.score = 0
        self.pre_direction = None
        self.direction = random.randint(0, 3)
        self.x_change = 0
        self.y_change = 0
        self.body = [[self.pos[0] - 20, self.pos[1]], [self.pos[0] - 10, self.pos[1]], [self.pos[0], self.pos[1]]]

    def eat(self):
        if apple.x - apple.w <= self.pos[0] <= apple.x + apple.w and apple.y - apple.h <= self.pos[1] <= apple.y + apple.h:
            self.score += 1
            return True
        else:
            return False

    def show(self):
        pygame.draw.rect(game.d, self.color, [self.pos[0], self.pos[1], self.w, self.h])
        for item in self.body:
            pygame.draw.rect(game.d, self.color, [item[0], item[1], self.w, self.h])

    def move(self):
        if self.direction == 0:
            self.x_change = 0
            self.y_change = -1

        elif self.direction == 1:
            self.x_change = 1
            self.y_change = 0

        elif self.direction == 2:
            self.x_change = 0
            self.y_change = 1

        elif self.direction == 3:
            self.x_change = -1
            self.y_change = 0

        self.body.append(list(self.pos))
        if len(self.body) > self.score:
            del (self.body[0])

        self.pos[0] += self.x_change * self.speed
        self.pos[1] += self.y_change * self.speed

    def Screen(self):
        if self.pos[0] == game.w:
            self.pos[0] = 0
        elif self.pos[0] == 0:
            self.pos[0] = game.w
        if self.pos[1] == game.h:
            self.pos[1] = 0
        elif self.pos[1] == 0:
            self.pos[1] = game.h


def collision_with_body(self, direction):
    for part in snake.body:

        if direction == 0:
            if abs(snake.pos[0] - part[0]) < game.wall_offset and abs(snake.pos[1] - 8 - part[1]) == 0:
                return True
            if abs(snake.pos[0] - part[0]) == 0 and abs(snake.pos[1] - 10 - part[1]) < game.wall_offset:
                return True

        if direction == 1:
            if abs(snake.pos[0] + 10 - part[0]) < game.wall_offset and abs(snake.pos[1] - part[1]) == 0:
                return True
            if abs(snake.pos[0] + 10 - part[0]) == 0 and abs(snake.pos[1] - part[1]) < game.wall_offset:
                return True

        if direction == 2:
            if abs(snake.pos[0] - part[0]) < game.wall_offset and abs(snake.pos[1] + 10 - part[1]) == 0:
                return True
            if abs(snake.pos[0] - part[0]) == 0 and abs(snake.pos[1] + 10 - part[1]) < game.wall_offset:
                return True

        if direction == 3:
            if abs(snake.pos[0] - 10 - part[0]) < game.wall_offset and abs(snake.pos[1] - part[1]) == 0:
                return True
            if abs(snake.pos[0] - 10 - part[0]) == 0 and abs(snake.pos[1] - part[1]) < game.wall_offset:
                return True

    return False


def collision_with_wall(direction):
    if direction == 0:
        if snake.pos[1] - 10 > game.wall_offset:
            return False

    elif direction == 1:
        if snake.pos[0] + 10 < game.w - game.wall_offset:
            return False

    elif direction == 2:
        if snake.pos[1] + 10 < game.h - game.wall_offset:
            return False

    elif direction == 3:
        if snake.pos[0] - 10 > game.wall_offset:
            return False

    return True


def vision():
    if snake.pos[0] == apple.x and snake.pos[1] > apple.y:
        for part in snake.body:
            if snake.pos[0] == part[0] and snake.pos[1] > part[1] > apple.y:
                break
        else:
            return 0

    if snake.pos[0] < apple.x and snake.pos[1] == apple.y:
        for part in snake.body:
            if snake.pos[0] < part[0] < apple.x and snake.pos[1] == part[1]:
                break
        else:
            return 1

    if snake.pos[0] == apple.x and snake.pos[1] < apple.y:
        for part in snake.body:
            if snake.pos[0] == part[0] and snake.pos[1] < part[1] < apple.y:
                break
        else:
            return 2

    if snake.pos[0] > apple.x and snake.pos[1] == apple.y:
        for part in snake.body:
            if snake.pos[0] > part[0] > apple.x and snake.pos[1] == part[1]:
                break
        else:
            return 3

    return -1


rows = 0


class Game:
    def __init__(self):
        self.w = 800
        self.h = 600
        self.wall_offset = 16
        self.d = pygame.display.set_mode((self.w, self.h))

    def play(self):

        global rows
        global snake
        global apple

        pygame.display.set_caption('snake game')
        font = pygame.font.SysFont('comicsansms', 30)
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    f.close()
            else:

                if snake.eat():
                    apple = Apple()

                # collision with body
                for part in snake.body:
                    if snake.pos[0] == part[0] and snake.pos[1] == part[1]:
                        print('collide body')
                        snake = Snake()

                direction = vision()

                snake.pre_direction = snake.direction

                # up
                # if direction == 0 and snake.direction != 2:
                #     snake.direction = 0
                #
                # # right
                # elif direction == 1 and snake.direction != 3:
                #     snake.direction = 1
                #
                # # down
                # elif direction == 2 and snake.direction != 0:
                #     snake.direction = 2
                #
                # # left
                # elif direction == 3 and snake.direction != 1:
                #     snake.direction = 3

                # up
                if direction == 0:
                    if snake.direction != 2:
                        snake.direction = 0

                # right
                elif direction == 1:
                    if snake.direction != 3:
                        snake.direction = 1

                # down
                elif direction == 2:
                    if snake.direction != 0:
                        snake.direction = 2

                # left
                elif direction == 3:
                    if snake.direction != 1:
                        snake.direction = 3

                elif collision_with_wall(snake.direction):
                    direction = (snake.direction + 1) % 4
                    if collision_with_wall(direction):
                        direction = (snake.direction - 1) % 4
                        if collision_with_wall(direction):
                            print('collide wall')
                            snake = Snake()

                    snake.direction = direction

                self.d.fill((0, 0, 0))

                snake.show()
                apple.show()
                snake.move()
                # snake.Screen()

                if add_data():
                    rows += 1
                    if rows % 10 == 0:
                        print(rows)

                score_font = font.render("Score: " + str(snake.score), True, (255, 255, 0))
                font_pos = score_font.get_rect(center=(80, self.h - 50))
                self.d.blit(score_font, font_pos)
                pygame.display.update()
                clock.tick(30)


if __name__ == "__main__":
    game = Game()
    snake = Snake()
    apple = Apple()
    font = pygame.font.SysFont('comicsansms', 40)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                f.close()

            else:
                game.d.fill((0, 0, 0))
                main_menu_message = font.render('Press to start the game', True, (255, 255, 255))
                font_pos = main_menu_message.get_rect(center=(game.w // 2, game.w // 2))
                game.d.blit(main_menu_message, font_pos)
                pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                game.play()


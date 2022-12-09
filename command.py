from map import *
from player import Player
import pygame
import sys
import os

# x2 + 36

def resource_path(relative_path):
    try:
        base_path = sys.MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

black = (0,0,0)
white = (255,255,255)

font_url = resource_path('fonts/VictorMono-Regular.ttf')

pygame_url = resource_path('img/pygame_title.png')
title_url = resource_path('img/TLDT_title.png')
backgrd_url = resource_path('img/the_tower.png')

slash_url = resource_path('sounds/sword_slash.wav')
grenade_url = resource_path('sounds/grenade.wav')
step_url = resource_path('sounds/step.wav')
music_url = resource_path('sounds/bg_music.wav')

player = Player(100)

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
fps = 30
font = pygame.font.Font(font_url, 32)
screen = pygame.display.set_mode([720, 480], pygame.NOFRAME)
# screen = pygame.display.set_mode([720, 480], pygame.FULLSCREEN)

pygame_title_small = pygame.image.load(pygame_url).convert()
pygame_title = pygame.transform.scale(pygame_title_small, (240, 66))
title_start = pygame.image.load(title_url)
tower_large = pygame.image.load(backgrd_url).convert()
tower = pygame.transform.scale(tower_large, (720, 480))

slash = pygame.mixer.Sound(slash_url)
grenade_blast = pygame.mixer.Sound(grenade_url)
step = pygame.mixer.Sound(step_url)
bg_music = pygame.mixer.music.load(music_url)

pygame.display.set_caption('TLDT')

currentRoom = 1

x = 0

def render_string(str, x, y, screen):
    enter = 0
    for line in str:
        screen.blit(font.render(line, True, white), (x, y+enter))
        enter = enter + 32


class Button:
    def __init__(self, x, y, label, item=None):
        self.Button = Button
        self.label = label
        self.x = x
        self.y = y
        self.item = item

    def draw(self):
        _len = 0
        for _ in range(0, len(self.label)):
            _len = _len + 1
        px_len = (_len * 18) + 20     # 9 pixels per character
        button = pygame.draw.rect(screen, white, [self.x-10, self.y-4, px_len, 56])
        screen.blit(font.render(self.label, True, black), (self.x, self.y))
        return button

    def draw_dir(self):
        button = pygame.draw.rect(screen, white, [self.x-10, self.y-4, 56, 56])
        screen.blit(font.render(self.label, True, black), (self.x+4, self.y))
        return button

    def get_label(self):        # use this to get state
        return self.label

    def get_item(self):
        return self.item


def intro():
    render_string(["Developed by", "Aren Laure Lizardo", "", "with"], 132, 108, screen)
    screen.blit(pygame_title, (132, 240))


def title(x):
    screen.blit(tower, (0,0))
    screen.blit(title_start, (44, x))
    start.draw()

def light_torch():
    render_string(["It's too dark to see anything..."], 63,180, screen)
    light.draw()

def main_game():
    render_string(map.get(currentRoom).get_description(), 63, 3, screen)
    look.draw()
    take.draw()
    use.draw()
    inventory.draw()
    examine.draw()
    attack.draw()
    eat.draw()
    n.draw()
    s.draw()
    w.draw()
    e.draw()

def large_window():
    pygame.display.update(pygame.draw.rect(screen, white, [88, 40, 540, 400], 1))

def small_window():
    pygame.display.update(pygame.draw.rect(screen, white, [86, 160, 540, 148], 1))


def look_state():
    large_window()
    if map.get(currentRoom).get_monster() != None:
        if map.get(currentRoom).get_monster().get_tag() == 'enemy':
            render_string(map.get(currentRoom).get_monster().get_description(), 100, 40, screen)
        elif map.get(currentRoom).get_monster().get_tag() == 'dead':
            render_string([f"The {map.get(currentRoom).get_monster().get_name()} lays dead."], 100, 40, screen)
        if map.get(currentRoom).get_item() != None:
            render_string(map.get(currentRoom).get_look(), 100, 192, screen)
    elif map.get(currentRoom).get_item() != None:
        render_string(map.get(currentRoom).get_look(), 100, 40, screen)
    elif map.get(currentRoom).get_look() != None:
        render_string(map.get(currentRoom).get_look(), 100, 40, screen)
    else:
        render_string(["There's nothing to look at."], 100, 40, screen)

    cont.draw()


def blocked():
    pygame.display.update(pygame.draw.rect(screen, white, [86, 160, 540, 148], 1))
    render_string(["You cannot go there."], 100, 168, screen)
    if map.get(currentRoom).get_monster() != None:
        if map.get(currentRoom).get_monster().get_tag() == 'dead':
            render_string(["The monster has been", "defeated!"], 100, 204, screen)
        else:
            render_string(["There's a monster here!"], 100, 204, screen)
    cont.draw()


def take_state():
    pygame.display.update(pygame.draw.rect(screen, white, [86, 196, 540, 100], 1))
    if map.get(currentRoom).get_item() != None:
        render_string([f"You took the {map.get(currentRoom).get_item().get_name()}."], 100, 220, screen)
    else:
        render_string([f"There's nothing to take."], 100, 200, screen)
    cont.draw()


def attack_state():
    pygame.display.update(pygame.draw.rect(screen, white, [86, 120, 540, 220], 1))
    cancel.draw()
    render_string(["Attack with what?"], 100, 128, screen)
    if sword_b.get_item().get_count() == 1:
        sword_b.draw()
    if ironSword_b.get_item().get_count() == 1:
        ironSword_b.draw()
    if grenade_b.get_item().get_count() == 1:
        grenade_b.draw()


def damage_state(damage):
    # Assume user has access to sword on attack state
    large_window()
    if damage == 'damage_sword':
        damage = sword_b.get_item().get_damage()
    elif damage == 'damage_ironSword':
        damage = ironSword_b.get_item().get_damage()
    elif damage == 'damage_grenade':
        damage = grenade_b.get_item().get_damage()
    if map.get(currentRoom).get_monster() != None:
        if map.get(currentRoom).get_monster().get_hp() > 0:
            hp = map.get(currentRoom).get_monster().get_hp() - damage
            if hp <= 0:
                hp = 0
            render_string([
                f"You attacked the {map.get(currentRoom).get_monster().get_name()}!",
                f"Its health is at {hp}!",
                f"Your health is now {player.get_hp() - map.get(currentRoom).get_monster().get_attack()}."
            ], 100, 40, screen)
        if map.get(currentRoom).get_monster().get_tag() == 'dead':
            render_string(["It's already dead..."], 100, 40, screen)
    if map.get(currentRoom).get_monster() == None:
        render_string(["There is nothing to attack."], 100, 40, screen)
    cont.draw()
    return damage


def inv_state():
    large_window()
    render_string(["Inventory"], 100, 40, screen)
    for _ in inv_buttons:
        if _.get_item().get_count() == 1:
            _.draw()
    back.draw()


def examine_state():
    large_window()
    render_string(["Examine what?"], 236, 40, screen)
    for _ in inv_buttons:
        if _.get_item().get_count() == 1:
            _.draw()
    back.draw()


def examine_item(label):
    items = {
        'bronze key': bronzeKey_b,
        'gold key': goldKey_b,
        'skeleton key': skeletonKey_b,
        'jeweled skull': jeweledSkull_b,
        'red gem': redGem_b,
        'blue gem': blueGem_b,
        'green gem': greenGem_b,
        'food': food_b
    }
    if label in items:
        large_window()
        render_string(items.get(label).get_item().get_description(), 100, 40, screen)
    back.draw()


def use_item(label):
    items = {
        'bronze key': [1, 6, 5], # direction, roomID, check if currentRoom is correct
        'gold key': [1, 16, 15],
        'skeleton key': [3, 21, 20],
        'jeweled skull': [3, 11, 10],
        'red gem': [3, 26, 25],
        'blue gem': [0, 27, 26],
        'green gem': [1, 25, 24]
    }
    large_window()
    if label in items and (currentRoom == items.get(label)[2]):
        render_string([f"You used the {label}!"], 100, 40, screen)
        render_string(map.get(currentRoom).get_use(), 100, 76, screen)
        map.get(currentRoom).update(items.get(label)[0], items.get(label)[1])
    else:
        render_string([f"You can't use that here..."], 100, 80, screen)
    back.draw()
    

def use_state():
    large_window()
    render_string(["Use what?"], 276, 40, screen)
    for _ in inv_buttons:
        if _.get_item().get_count() == 1:
            _.draw()
    back.draw()


def eat_state():
    small_window()
    if food_b.get_item().get_count() > 0:
        render_string(["You've eaten some food.", "You gain 20 health."], 100, 184, screen)
    else:
        render_string(["There's nothing to eat..."], 100, 184, screen)
    cont.draw()


def state_manager(state):
    if state == 'title':
        title(x)
    if state == 'light torch':
        light_torch()
    if state == 'intro':
        intro()
    if state == 'main':
        main_game()
    if state == 'look':
        look_state()
    elif state == 'examine':
        examine_state()
    elif state == 'examine_item':
        examine_item(item_desc)
    elif state == 'take':
        take_state()
    elif state == 'inv':
        inv_state()
    elif state == 'use':
        use_state()
    elif state == 'use_item':
        use_item(item_desc)
    elif state == 'attack':
        attack_state()
    elif state == 'blocked':
        blocked()
    elif state == 'damage_sword':
        damage_state('damage_sword')
    elif state == 'damage_ironSword':
        damage_state('damage_ironSword')
    elif state == 'damage_grenade':
        damage_state('damage_grenade')
    elif state == 'eat':
        eat_state()
    return


light = Button(240, 240, 'light torch')

look = Button(264, 400, 'look')
take = Button(372, 400, 'take')
use = Button(480, 400, 'use')
inventory = Button(570, 328, 'inv')
eat = Button(570, 400, 'eat')

bronzeKey_b = Button(124, 88, 'bronze key', bronzeKey)
goldKey_b = Button(124, 150, 'gold key', goldKey)
skeletonKey_b = Button(124, 212, 'skeleton key', skeletonKey)
jeweledSkull_b = Button(124, 274, 'jeweled skull', jeweledSkull)
redGem_b = Button(462, 88, 'red gem', redGem)
blueGem_b = Button(444, 150, 'blue gem', blueGem)
greenGem_b = Button(426, 212, 'green gem', greenGem)
food_b = Button(516, 274, 'food', food)

examine = Button(408, 328, 'examine')
attack = Button(264, 328, 'attack')

cont = Button(292, 328, 'continue')
cancel = Button(436, 400, 'cancel')
back = Button(124, 360, 'back')
start = Button(488, 240, 'start')

# n = Button(52, 164, 'n')
# s = Button(52, 200, 's')
# w = Button(21, 182, 'w')
# e = Button(82, 182, 'e')

n = Button(140, 328, 'n')
s = Button(140, 400, 's')
w = Button(78, 364, 'w')
e = Button(200, 364, 'e')

sword_b = Button(180, 180, 'sword', sword)
ironSword_b = Button(308, 180, 'iron sword', ironSword)
grenade_b = Button(240, 250, 'grenades', grenade)

sword_collide = sword_b.draw()
ironSword_collide = ironSword_b.draw()
grenade_collide = grenade_b.draw()

buttons = [
    n,
    s,
    w,
    e,
    look,
    take,
    use,
    inventory,
    attack,
    examine,
    eat]

inv_buttons = [
    bronzeKey_b,
    goldKey_b,
    skeletonKey_b,
    jeweledSkull_b,
    redGem_b,
    blueGem_b,
    greenGem_b,
    food_b
]

weapons_buttons = [
    sword_b,
    ironSword_b,
    grenade_b
]

run = True

state = 'intro'
item_desc = ''
sign = 1

while run:
    clock.tick(fps)
    screen.fill(black)

    pos = pygame.mouse.get_pos()

    state_manager(state)

    x = x + (1 * sign)
    if x > 18:
        sign = -1
    if x < 0:
        sign = 1



    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((0,0,0))
            if state == 'intro' and pygame.MOUSEBUTTONDOWN:
                state = 'title'
                # pygame.mixer.music.play(-1)
            if state == 'title'and start.draw().collidepoint(pos):
                state = 'light torch'
            if state == 'light torch' and light.draw().collidepoint(pos):
                state = 'main'
            if state == 'main':
                for button in buttons:
                    if button.draw().collidepoint(pos):
                        state = button.get_label()
            if state in ['blocked', 'look']:
                if cont.draw().collidepoint(pos):
                    state = 'main'
            if state == 'n' and n.draw().collidepoint(pos):
                if map.get(currentRoom).direction(0) <= 0:
                    state = 'blocked'
                elif map.get(currentRoom).get_monster() != None:
                    print(map.get(currentRoom).get_monster().get_tag())
                    if map.get(currentRoom).get_monster().get_tag() == 'dead' \
                            and map.get(currentRoom).direction(0) > 0:
                        print(map.get(currentRoom).direction(0))
                        currentRoom = map.get(currentRoom).direction(0)
                        pygame.mixer.Sound.play(step)
                        state = 'main'
                    else:
                        state = 'blocked'
                elif map.get(currentRoom).direction(0) > 0 and map.get(currentRoom).get_monster() == None:
                    print(map.get(currentRoom).direction(0))
                    currentRoom = map.get(currentRoom).direction(0)
                    pygame.mixer.Sound.play(step)
                    state = 'main'
            if state == 's' and s.draw().collidepoint(pos):
                if map.get(currentRoom).direction(1) <= 0:
                    state = 'blocked'
                elif map.get(currentRoom).get_monster() != None:
                    print(map.get(currentRoom).get_monster().get_tag())
                    if map.get(currentRoom).get_monster().get_tag() == 'dead' \
                            and map.get(currentRoom).direction(1) > 0:
                        print(map.get(currentRoom).direction(1))
                        currentRoom = map.get(currentRoom).direction(1)
                        pygame.mixer.Sound.play(step)
                        state = 'main'
                    else:
                        state = 'blocked'
                elif map.get(currentRoom).direction(1) > 0 and map.get(currentRoom).get_monster() == None:
                    print(map.get(currentRoom).direction(1))
                    currentRoom = map.get(currentRoom).direction(1)
                    pygame.mixer.Sound.play(step)
                    state = 'main'
            if state == 'w' and w.draw().collidepoint(pos):
                if map.get(currentRoom).direction(2) <= 0:
                    state = 'blocked'
                elif map.get(currentRoom).get_monster() != None:
                    print(map.get(currentRoom).get_monster().get_tag())
                    if map.get(currentRoom).get_monster().get_tag() == 'dead' \
                            and map.get(currentRoom).direction(2) > 0:
                        print(map.get(currentRoom).direction(2))
                        currentRoom = map.get(currentRoom).direction(2)
                        pygame.mixer.Sound.play(step)
                        state = 'main'
                    else:
                        state = 'blocked'
                elif map.get(currentRoom).direction(2) > 0 and map.get(currentRoom).get_monster() == None:
                    print(map.get(currentRoom).direction(2))
                    currentRoom = map.get(currentRoom).direction(2)
                    pygame.mixer.Sound.play(step)
                    state = 'main'
            if state == 'e' and e.draw().collidepoint(pos):
                if map.get(currentRoom).direction(3) <= 0:
                    state = 'blocked'
                elif map.get(currentRoom).get_monster() != None:
                    print(map.get(currentRoom).get_monster().get_tag())
                    if map.get(currentRoom).get_monster().get_tag() == 'dead' \
                            and map.get(currentRoom).direction(3) > 0:
                        print(map.get(currentRoom).direction(3))
                        currentRoom = map.get(currentRoom).direction(3)
                        pygame.mixer.Sound.play(step)
                        state = 'main'
                    else:
                        state = 'blocked'
                elif map.get(currentRoom).direction(3) > 0 and map.get(currentRoom).get_monster() == None:
                    print(map.get(currentRoom).direction(3))
                    currentRoom = map.get(currentRoom).direction(3)
                    pygame.mixer.Sound.play(step)
                    state = 'main'
            if state == 'take' and cont.draw().collidepoint(pos):
                if map.get(currentRoom).get_item() != None:
                    map.get(currentRoom).get_item().take_count()
                    print(f"{map.get(currentRoom).get_item().get_name()}:", map.get(currentRoom).get_item().get_count())
                    map.get(currentRoom).set_item(None)
                state = 'main'
            if state == 'attack':
                if cancel.draw().collidepoint(pos):
                    state = 'main'
                if sword_collide.collidepoint(pos) and sword_b.get_item().get_count() == 1:
                    pygame.mixer.Sound.play(slash)
                    state = 'damage_sword'
                if ironSword_collide.collidepoint(pos) and ironSword_b.get_item().get_count() == 1:
                    pygame.mixer.Sound.play(slash)
                    state = 'damage_ironSword'
                if grenade_collide.collidepoint(pos) and grenade_b.get_item().get_count() == 1:
                    pygame.mixer.Sound.play(grenade_blast)
                    state = 'damage_grenade'
            if state in ['damage_sword', 'damage_ironSword', 'damage_grenade'] and cont.draw().collidepoint(pos):
                    if map.get(currentRoom).get_monster() != None \
                            and map.get(currentRoom).get_monster().get_tag() == 'enemy':
                        map.get(currentRoom).get_monster().is_hit(damage_state(state))
                        player.is_hit(map.get(currentRoom).get_monster().get_attack())
                    state = 'main'
            if state == 'inv' and back.draw().collidepoint(pos):
                    state = 'main'
            if state == 'use':
                for item in inv_buttons:
                    if item.draw().collidepoint(pos):
                        item_desc = item.get_label()
                        state = 'use_item'
                if back.draw().collidepoint(pos):
                    state = 'main'
            if state == 'use_item':
                if back.draw().collidepoint(pos):
                    print(map.get(currentRoom).direction(0))
                    state = 'main'
            if state == 'examine':
                for item in inv_buttons:
                    if item.draw().collidepoint(pos):
                        item_desc = item.get_label()
                        state = 'examine_item'
                if back.draw().collidepoint(pos):
                    state = 'main'
            if state == 'examine_item' and back.draw().collidepoint(pos):
                state = 'main'
            if state == 'eat':
                if cont.draw().collidepoint(pos):
                    if food_b.get_item().get_count() > 0:
                        player.consume()
                        food_b.get_item().consume()
                    state = 'main'

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
    pygame.display.flip()



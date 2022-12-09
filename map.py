from room import *
import script

bronzeKey = Item("bronze key", script.bronzeKey)
goldKey = Item("gold key", script.goldKey)
skeletonKey = Item("skeleton key", script.skeletonKey)
jeweledSkull = Item("jeweled skull", script.jeweledSkull)
redGem = Item("red gem", script.redGem)
blueGem = Item("blue gem", script.blueGem)
greenGem = Item("green gem", script.greenGem)

skeleton = Monster("skeleton", script.skele, 30, 5, "enemy")
grue = Monster("grue", script.grue, 30, 5, "enemy")
goblin = Monster("goblin", script.goblin, 50, 10, "enemy")
demon = Monster("demon", script.demon, 75, 15, "enemy")
dragon = Monster("dragon", script.dragon, 100, 20, "enemy")

food = Food("food", script.food)

ironSword = Weapon("iron sword", "iron sword desc.", 25)
sword = Weapon("sword", "sword desc.", 15)
grenade = Weapon("grenades", "grenade desc.", 50)

r01 = Room(script.r01, -1, 4, -1, 2, bronzeKey, script.bronzeLook)
r02 = Room(script.r02, -1, 3, 1, -1, sword, script.swordLook, skeleton)
r03 = Room(script.r03, 2, -1, 4, -1, food, script.foodLook)
r04 = Room(script.r04, 1, -1, 5, 3)
r05 = Room(script.r05, -1, -1, -1, 4, None, script.r05Look, None, script.bronzeUse)
r06 = Room(script.r06, 7, 5, -1, 8)
r07 = Room(script.r07, -1, 6, -1, 8, jeweledSkull, script.jeweledLook)
r08 = Room(script.r08, -1, 6, 7, 9, food, script.foodLook)
r09 = Room(script.r09, -1, 10, 8, -1, ironSword, script.ironLook)
r10 = Room(script.r10, 9, -1, -1, -1, None, script.r10Look, None, script.jeweledUse)
r11 = Room(script.r11, -1, 10, -1, 12, food, script.foodLook)
r12 = Room(script.r12, -1, 13, 11, 14, goldKey, script.goldLook)
r13 = Room(script.r13, 12, -1, -1, 14, None, None, grue)
r14 = Room(script.r14, 12, 13, -1, 15)
r15 = Room(script.r15, -1, -1, 14, -1, None, script.r15Look, None, script.goldUse)
r16 = Room(script.r16, 17, 19, 15, -1, grenade, script.grenadeLook)
r17 = Room(script.r17, 18, 19, 16, 20, skeletonKey, script.skeletonLook, goblin)
r18 = Room(script.r18, 17, 20, -1, -1, food, script.foodLook)
r19 = Room(script.r19, 16, 20, -1, 17, food, script.foodLook)
r20 = Room(script.r20, 18, 19, 17, -1, None, script.r20Look, None, script.skeletonUse)
r21 = Room(script.r21, 22, 24, 21, -1)
r22 = Room(script.r22, -1, -1, 21, 23, food, script.foodLook)
r23 = Room(script.r23, 22, 24, -1, -1, redGem, script.redLook)
r24 = Room(script.r24, -1, -1, 21, 23, blueGem, script.r24Look, None, script.greenUse)
r25 = Room(script.r25, 24, -1, -1, -1, food, script.r25Look, demon, script.redUse)
r26 = Room(script.r26, -1, -1, 25, -1, None, script.r26Look, dragon, script.blueUse)
r27 = Room(script.r27, -1, -1, -1, -1)

map = {
    1: r01, 2: r02, 3: r03, 4: r04, 5: r05,
    6: r06, 7: r07, 8: r08, 9: r09, 10: r10,
    11: r11, 12: r12, 13: r13, 14: r14, 15: r15,
    16: r16, 17: r17, 18: r18, 19: r19, 20: r20,
    21: r21, 22: r22, 23: r23, 24: r24, 25: r25, 26: r26, 27: r27 }

inv = [
    food,
    sword,
    ironSword,
    grenade,
    bronzeKey
    # goldKey,
    # skeletonKey,
    # jeweledSkull,
    # redGem,
    # blueGem,
    # greenGem
    ]

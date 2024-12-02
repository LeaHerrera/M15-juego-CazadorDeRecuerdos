@namespace
class SpriteKind:
    Button = SpriteKind.create()
    Arrow = SpriteKind.create()
    Bruja = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    
    def on_start_cutscene():
        global PlayerName, teletransporte
        story.show_player_choices("Hablar con la Bruja", "Salir")
        if story.check_last_answer("Hablar con la Bruja"):
            PlayerName = game.ask_for_string("Como te llamas aventurero?")
            story.print_character_text(" Hola " + PlayerName + ". Eres un androide defectuoso, creado para una tarea que ya has olvidado.",
                "Bruja")
            story.print_character_text("Tu memoria se ha perdido, fragmentada en pedazos, y ahora viajas entre diferentes épocas de la humanidad para reconstruirla.",
                "Bruja")
            story.print_character_text("Cada era que atraviesas está llena de pistas, enigmas y personas que, aunque no lo sepan, tienen fragmentos de tu historia.",
                "Bruja")
            story.print_character_text("Debes aprender a confiar en los demás, incluso cuando las piezas de tu identidad estén dispersas en",
                "Bruja")
            story.print_character_text("el tiempo, y cada decisión puede acercarte o alejarte de la verdad.",
                "Bruja")
            story.print_character_text("Para seguir con la historia vete al transportador", "Bruja")
            teletransporte = True
            story.cancel_all_cutscenes()
        if story.check_last_answer("Salir"):
            story.cancel_all_cutscenes()
    story.start_cutscene(on_start_cutscene)
    
sprites.on_overlap(SpriteKind.player, SpriteKind.Bruja, on_on_overlap)

def wolk():
    if controller.up.is_pressed():
        animation.run_image_animation(Character,
            [img("""
                    . . . . . . f f f f . . . . . . 
                                . . . . f f e e e e f f . . . . 
                                . . . f e e e f f e e e f . . . 
                                . . f f f f f 2 2 f f f f f . . 
                                . . f f e 2 e 2 2 e 2 e f f . . 
                                . . f e 2 f 2 f f 2 f 2 e f . . 
                                . . f f f 2 2 e e 2 2 f f f . . 
                                . f f e f 2 f e e f 2 f e f f . 
                                . f e e f f e e e e f e e e f . 
                                . . f e e e e e e e e e e f . . 
                                . . . f e e e e e e e e f . . . 
                                . . e 4 f f f f f f f f 4 e . . 
                                . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                                . . 4 4 f 4 4 4 4 4 4 f 4 4 . . 
                                . . . . . f f f f f f . . . . . 
                                . . . . . f f . . f f . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . f f f f . . . . . . 
                                . . . . f f e e e e f f . . . . 
                                . . . f e e e f f e e e f . . . 
                                . . . f f f f 2 2 f f f f . . . 
                                . . f f e 2 e 2 2 e 2 e f f . . 
                                . . f e 2 f 2 f f f 2 f e f . . 
                                . . f f f 2 f e e 2 2 f f f . . 
                                . . f e 2 f f e e 2 f e e f . . 
                                . f f e f f e e e f e e e f f . 
                                . f f e e e e e e e e e e f f . 
                                . . . f e e e e e e e e f . . . 
                                . . . e f f f f f f f f 4 e . . 
                                . . . 4 f 2 2 2 2 2 e d d 4 . . 
                                . . . e f f f f f f e e 4 . . . 
                                . . . . f f f . . . . . . . . .
                """),
                img("""
                    . . . . . . f f f f . . . . . . 
                                . . . . f f e e e e f f . . . . 
                                . . . f e e e f f e e e f . . . 
                                . . f f f f f 2 2 f f f f f . . 
                                . . f f e 2 e 2 2 e 2 e f f . . 
                                . . f e 2 f 2 f f 2 f 2 e f . . 
                                . . f f f 2 2 e e 2 2 f f f . . 
                                . f f e f 2 f e e f 2 f e f f . 
                                . f e e f f e e e e f e e e f . 
                                . . f e e e e e e e e e e f . . 
                                . . . f e e e e e e e e f . . . 
                                . . e 4 f f f f f f f f 4 e . . 
                                . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                                . . 4 4 f 4 4 4 4 4 4 f 4 4 . . 
                                . . . . . f f f f f f . . . . . 
                                . . . . . f f . . f f . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . f f f f . . . . . . 
                                . . . . f f e e e e f f . . . . 
                                . . . f e e e f f e e e f . . . 
                                . . . f f f f 2 2 f f f f . . . 
                                . . f f e 2 e 2 2 e 2 e f f . . 
                                . . f e f 2 f f f 2 f 2 e f . . 
                                . . f f f 2 2 e e f 2 f f f . . 
                                . . f e e f 2 e e f f 2 e f . . 
                                . f f e e e f e e e f f e f f . 
                                . f f e e e e e e e e e e f f . 
                                . . . f e e e e e e e e f . . . 
                                . . e 4 f f f f f f f f e . . . 
                                . . 4 d d e 2 2 2 2 2 f 4 . . . 
                                . . . 4 e e f f f f f f e . . . 
                                . . . . . . . . . f f f . . . .
                """)],
            500,
            False)
    if controller.down.is_pressed():
        animation.run_image_animation(Character,
            [img("""
                    . . . . . . f f f f . . . . . . 
                                . . . . f f f 2 2 f f f . . . . 
                                . . . f f f 2 2 2 2 f f f . . . 
                                . . f f f e e e e e e f f f . . 
                                . . f f e 2 2 2 2 2 2 e e f . . 
                                . . f e 2 f f f f f f 2 e f . . 
                                . . f f f f e e e e f f f f . . 
                                . f f e f b f 4 4 f b f e f f . 
                                . f e e 4 1 f d d f 1 4 e e f . 
                                . . f e e d d d d d d e e f . . 
                                . . . f e e 4 4 4 4 e e f . . . 
                                . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                                . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                                . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                                . . . . . f f f f f f . . . . . 
                                . . . . . f f . . f f . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . f f f f . . . . . . 
                                . . . . f f f 2 2 f f f . . . . 
                                . . . f f f 2 2 2 2 f f f . . . 
                                . . f f f e e e e e e f f f . . 
                                . . f f e 2 2 2 2 2 2 e e f . . 
                                . f f e 2 f f f f f f 2 e f f . 
                                . f f f f f e e e e f f f f f . 
                                . . f e f b f 4 4 f b f e f . . 
                                . . f e 4 1 f d d f 1 4 e f . . 
                                . . . f e 4 d d d d 4 e f e . . 
                                . . f e f 2 2 2 2 e d d 4 e . . 
                                . . e 4 f 2 2 2 2 e d d e . . . 
                                . . . . f 4 4 5 5 f e e . . . . 
                                . . . . f f f f f f f . . . . . 
                                . . . . f f f . . . . . . . . .
                """),
                img("""
                    . . . . . . f f f f . . . . . . 
                                . . . . f f f 2 2 f f f . . . . 
                                . . . f f f 2 2 2 2 f f f . . . 
                                . . f f f e e e e e e f f f . . 
                                . . f f e 2 2 2 2 2 2 e e f . . 
                                . . f e 2 f f f f f f 2 e f . . 
                                . . f f f f e e e e f f f f . . 
                                . f f e f b f 4 4 f b f e f f . 
                                . f e e 4 1 f d d f 1 4 e e f . 
                                . . f e e d d d d d d e e f . . 
                                . . . f e e 4 4 4 4 e e f . . . 
                                . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                                . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                                . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                                . . . . . f f f f f f . . . . . 
                                . . . . . f f . . f f . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . f f f f . . . . . . 
                                . . . . f f f 2 2 f f f . . . . 
                                . . . f f f 2 2 2 2 f f f . . . 
                                . . f f f e e e e e e f f f . . 
                                . . f e e 2 2 2 2 2 2 e f f . . 
                                . f f e 2 f f f f f f 2 e f f . 
                                . f f f f f e e e e f f f f f . 
                                . . f e f b f 4 4 f b f e f . . 
                                . . f e 4 1 f d d f 1 4 e f . . 
                                . . e f e 4 d d d d 4 e f . . . 
                                . . e 4 d d e 2 2 2 2 f e f . . 
                                . . . e d d e 2 2 2 2 f 4 e . . 
                                . . . . e e f 5 5 4 4 f . . . . 
                                . . . . . f f f f f f f . . . . 
                                . . . . . . . . . f f f . . . .
                """)],
            500,
            False)
def Level_Controler():
    if Level == 0:
        Menu()
    if Level == 1:
        Level1()
    if Level == 2:
        Help()
    if Level == 3:
        Level2()
def Level2():
    sprites.destroy(PlayButton)
    sprites.destroy(HelpButton)
    sprites.destroy(Arrow2)
    sprites.destroy(Bruja2)
    tiles.set_current_tilemap(tilemap("""
        level11
    """))
def Level1():
    global Character, Bruja2
    wolk()
    sprites.destroy(Arrow2)
    sprites.destroy(HelpButton)
    sprites.destroy(PlayButton)
    tiles.set_current_tilemap(tilemap("""
        level4
    """))
    Character = sprites.create(img("""
            . . . . . . f f f f . . . . . . 
                    . . . . f f f 2 2 f f f . . . . 
                    . . . f f f 2 2 2 2 f f f . . . 
                    . . f f f e e e e e e f f f . . 
                    . . f f e 2 2 2 2 2 2 e e f . . 
                    . . f e 2 f f f f f f 2 e f . . 
                    . . f f f f e e e e f f f f . . 
                    . f f e f b f 4 4 f b f e f f . 
                    . f e e 4 1 f d d f 1 4 e e f . 
                    . . f f f f d d d d d e e f . . 
                    . f d d d d f 4 4 4 e e f . . . 
                    . f b b b b f 2 2 2 2 f 4 e . . 
                    . f b b b b f 2 2 2 2 f d 4 . . 
                    . . f c c f 4 5 5 4 4 f 4 4 . . 
                    . . . f f f f f f f f . . . . . 
                    . . . . . f f . . f f . . . . .
        """),
        SpriteKind.player)
    controller.move_sprite(Character)
    scene.camera_follow_sprite(Character)
    Bruja2 = sprites.create(img("""
            . . . . . . . c c . . . . . . . 
                    . . . . . . c 5 c . . . . . . . 
                    . . . . c c 5 5 5 c c c . . . . 
                    . . c c c c 5 5 5 5 c b c c . . 
                    . c b b 5 b 5 5 5 5 b 5 b b c . 
                    . c b 5 5 b b 5 5 b b 5 5 b c . 
                    . . c 5 5 5 b b b b 5 5 5 f . . 
                    . . . f 5 5 5 5 5 5 5 5 f f . . 
                    . . . . f e e e f b e e f f . . 
                    . . . . f e b b f 1 b f f f . . 
                    . . . . f b b b b b b f f . . . 
                    . . . . . f e e e e f e e . . . 
                    . . . . . f 5 b b e b b e . . . 
                    . . . . f 5 5 5 5 e b b e . . . 
                    . . . . c b 5 5 5 5 e e . . . . 
                    . . . . . f f f f f f . . . . .
        """),
        SpriteKind.Bruja)
    tiles.place_on_tile(Bruja2, tiles.get_tile_location(10, 12))
    if teletransporte == False:
        story.print_character_text("Lo primero que tienes que hacer es hablar con la bruja.")

def on_on_overlap2(sprite3, otherSprite2):
    global Level
    if otherSprite2 == PlayButton and controller.A.is_pressed():
        Level = 1
        Level_Controler()
    if otherSprite2 == HelpButton and controller.A.is_pressed():
        Level = 2
        Level_Controler()
sprites.on_overlap(SpriteKind.Arrow, SpriteKind.Button, on_on_overlap2)

def on_overlap_tile(sprite4, location2):
    global Level
    if teletransporte == True:
        Level = 3
        Level_Controler()
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_insignia,
    on_overlap_tile)

def Help():
    sprites.destroy(Arrow2)
    sprites.destroy(HelpButton)
    sprites.destroy(PlayButton)
def Menu():
    global PlayButton, HelpButton, Arrow2
    scene.set_background_image(img("""
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff99d99bbbbbcfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff99ddbdd66168bcccccc9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff999ddbbbd66888111ccccccb99fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9966ddbbbb6688811818ccccccbbc99fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffdd69dddbbb66618881888818818cccccbe9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffddd96dd6b6dbd68888888888888888cccccc99fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffdbbd9666666dbb668886888888cccccccccccccc9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffdbbb99666966d68866888888cccccccccccccccccc69ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffdbbb999669666666888888888ccccbbbcc8bcccccccccc9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffdbbb999666666666888888888cbbcbe8bbbcbcccccbbcccb9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffff9bbb999666666666688888888bccb888888bbbbb88888bcccccfffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffdbbb999669666666866888868bbbbb8888888ccc888b88bbc8cccffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffdbbb9d99ddd666668868888688bbcb888888888bc888bcc8bc886c9fffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffbbbbbbddd966666888688888888888888b88888888888cc8ccc886c9ffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffdbbbbbbdd6966666666868888888888bbdbbebb8888888888bcc8c86c9fffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffff9bbdbddd6666666666888688868888ddddddddde8888888888bccbbccccfffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffff9dbb9dd666666666668868888888bddddddbdbbddcccccd88b8ebccbbbbc9ffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffdd99999666666666668868888888bdddddbbbbbdbbbccccccb8bbbccc8bbb9fffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffff9dd99996696966666666668888bbbdddddbbbddbbbbbbbbbcccc8bcccbb8bbcfffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffff9d999996666966666668688888bbdddbbbbdbbbbbbbbbbbcccccc8bbccc88bc9ffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffff99999999666996696668868868bbdddddbbbdbbbbbbbbbbbbcbccc88bcccc88c6ffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffff999996696669666966d8868666bddbbbddbbdbbbbbbbbbbbbcccccc88bbccc8869fffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffff9999996699669666666d6688668bddbbdbbbbbbbbbbbbbbbbbccccccc88bcccc866fffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffff9dd999669966666666666688668bdddbbbbbbbbbbbbbbbbbbbccccccc888bbccc669ffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffff999999669d69666666666688868bddbbbdbbbbbbbbbbbbbbbbcccccccc888bbcc869ffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffff99999996ddd69666666688888868ddbddbbbbbbbbbbbbbbbbbbccccccccc888888866ffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffff999999969ddd6669666688688888bbbbbbbbbbbbbbbbbbbbbbbbccbccccc8888888869fffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffff99999966ddddd669666688888888bbbbbbbbbbbbbbbbbbbbbbbcbccccccccc88888869fffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffff999bb99666dddd6666666668886888bbbbbbbbbbbbbbbbbbbbbbcccccccccccc8888889fffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffff99bbbb966696666666666888886888bbbbbbbbbbbbbbbbbbbbbbcbccccccccccc888886fffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffff99bbdbb666969666666668888868888bbbbbbbbbbbbbbbbbbbbccbccccccccccc8888869ffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffff99dbbbbb6696966666666668886868888bbbbeb888bbbbbbbbbcccccccccccccc8888869ffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffff99bbbbbbe6969666666666888888888888888888888bbbbbbbbccccccccccccc88888869ffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffff9bbbbbccbc66966666666688888688888888888d888ebbbbbbbcccccccccccbb88888869ffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffff9bbbbbbbbcc69996666688668886888888dd88dbbd88bbbbbbbccccccccccceb88888869ffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffff9bbbbbbbbccc999966668868888888888ddddbbbbd88cbbbbbbbbccccccccc8888888869ffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffff9ebbbbcccccccc9966666688888888888888ddbbbb888bbbbbbbbccccccccc8888888869ffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffff9bbbbbccccccccc666666888866888888888dddddbdd88bbbbbbccccccccc88888888bb9ffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffbbbbbbcccccccccc6666688888888888888888d8888888bbbbbbccccccccc88888888bb9ffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffff9dbbbbccbbccccccb666688868888888888888888888888bbbbbccccccccc888888888b9ffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffff9dbbbbbbbbcccccbb66666688888888888888888888888bbbbccccccccccc88888888869ffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffff9bbbbbbbcccccccb666666688888888888888888888888bbbbcccccccccc888888888869ffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffff9bbbbbbbccccccbb666666688888888888888888888888bbbbcccccccccc88888888886fffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffff99bbbbbbbbccccb6666668888888888888888888888888bbbbcbcccccccc88888888886fffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffff99dbbbcbbccccb6666668888888888888888888888888bbbbbccccccccc888cc888869fffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffff99dbbbcccccccc6666668688688888888888888888888bbbbccccccccc8888cc888869fffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffff999bbbbbccccbc6666666688688888888888888888888bbbbcccccccc88888dd88886ffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffff969bbbbbbcccc69666666668688868888888888888888bbbbccccccc88888bd888886ffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffff99bbbbcccccc696bb668888888868888888888888888bbbcccccccc8888bbd888869ffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffff9999bbbcccc9666dbbb8888888888888888888888888ccbcccccccc8888bc888886fffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffff699bbbbccc966966bbb8888888888888888888888888bbbbccccc88888bcc88869fffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffff9999bbcccc666666dbbdd88888888688888888888888bbcccccc88888888888669fffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffff9699dbcccc66666666bb6d8888888688888888888888bbcccccc8888888888869ffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffff9696bbbcc66666666dbbd6886868888888888888888bbcbccc8888888888d669ffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffff999ebbccc666666666dbb8868888688888888888888bbbccc8888888889b69fffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffff969ccbcc66996666666bbb868888888888888888888bbbc888888888888b6ffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffff96ccccc966966666666bb8688666888888888888888b8888888888888699ffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffff99ccbc996666666666dbb6888668888888888888888888888888888869fffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffff969ccb9666666666666dbb88866888888888888888888888888888869ffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffff969ccc6696666666666dd8888668888888888888888888888888866fffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffff969cc9669666966d66dd8888868888888888888888888bb8888669fffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffff96ccc66699669dddd888868888888888888888888888be888669ffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffff96c66669966666dd88886666668888888888888888dd888669fffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffff96966669966ddd686886868888888888888888888d888669ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffff969666696666666688686888888888888888888888669ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffff9966966966666666886888888888888886888888669fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9699996666666888888888888888888118888699ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff969996666668888881188888888881888669ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff996999666688881818888888881886669ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9961161186618811188886116699ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff99161111611118111666699fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9999661166669999ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff999999999fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    """))
    PlayButton = sprites.create(img("""
            ff1ffffffffffffffffffffffff1ff
                    f1ff6666666666666666666666ff1f
                    1ff688888888888888888888886ff1
                    ff68666666666666666666666686ff
                    f68666ffffffff6fffffffff66686f
                    f68666f1111f1f6f111f1f1f66686f
                    f66666f1ff1f1f6f1f1f1f1f66666f
                    f66666f1111f1f6f111f111f66666f
                    f66666f1ffff1f6f1f1ff1ff66666f
                    f66666f1f6ff1fff1f1ff1f666666f
                    f96666f1f6ff111f1f1ff1f666669f
                    f61666fff6fffffffffffff666696f
                    ff61666666666666666666666696ff
                    1ff811919999999999999999998ff1
                    f1ff8888888888888888888888ff1f
                    ff1ffffffffffffffffffffffff1ff
        """),
        SpriteKind.Button)
    PlayButton.set_position(80, 90)
    HelpButton = sprites.create(img("""
            ff1ffffffffffffffffffffffff1ff
                    f1ff6666666666666666666666ff1f
                    1ff688888888888888888888886ff1
                    ff68666666666666666666666686ff
                    f6866ffffffffffff66ffffff6686f
                    f6866f1f1f1111f1f66f1111f6686f
                    f6666f1f1f1ffff1f66f1ff1f6666f
                    f6666f111f1111f1f66f1111f6666f
                    f6666f111f1ffff1f66f1ffff6666f
                    f6666f1f1f1111f1ffff1f6666666f
                    f9666f1f1ffffff1111fff6666669f
                    f6166fffff666fffffff666666696f
                    ff61666666666666666666666696ff
                    1ff811919999999999999999998ff1
                    f1ff8888888888888888888888ff1f
                    ff1ffffffffffffffffffffffff1ff
        """),
        SpriteKind.Button)
    HelpButton.set_position(80, 110)
    Arrow2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . f f . . . . . . . 
                    . . . . . . f 8 8 f . . . . . . 
                    . . . . . f 8 6 6 8 f . . . . . 
                    . . . . f 8 6 6 6 6 8 f . . . . 
                    . . . f 8 6 6 6 6 6 6 8 f . . . 
                    . . f 8 6 6 6 6 6 6 6 6 8 f . . 
                    . f f f f f f f f f f f f f f . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.Arrow)
    controller.move_sprite(Arrow2)
    Arrow2.set_bounce_on_wall(True)

def on_overlap_tile2(sprite2, location):
    tiles.set_tile_at(location, sprites.dungeon.floor_dark0)
    for value in tiles.get_tiles_by_type(sprites.dungeon.door_locked_north):
        tiles.set_tile_at(value, sprites.dungeon.floor_mixed)
        tiles.set_wall_at(value, False)
    for value2 in tiles.get_tiles_by_type(sprites.dungeon.door_locked_south):
        tiles.set_tile_at(value2, sprites.dungeon.floor_mixed)
        tiles.set_wall_at(value2, False)
    for value3 in tiles.get_tiles_by_type(sprites.dungeon.floor_dark3):
        tiles.set_tile_at(value3, sprites.dungeon.floor_mixed)
        tiles.set_wall_at(value3, False)
    for value4 in tiles.get_tiles_by_type(sprites.dungeon.floor_light3):
        tiles.set_tile_at(value4, sprites.dungeon.floor_mixed)
        tiles.set_wall_at(value4, False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile
    """),
    on_overlap_tile2)

Bruja2: Sprite = None
Arrow2: Sprite = None
HelpButton: Sprite = None
PlayButton: Sprite = None
Character: Sprite = None
teletransporte = False
PlayerName = ""
Level = 0
game.splash("Cazador De Recuerdos")
Level = 0
Level_Controler()
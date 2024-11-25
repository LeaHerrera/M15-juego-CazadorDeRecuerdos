scene.set_background_color(1)
scene.set_background_image(assets.image("""
    aa
"""))
player1 = sprites.create(assets.image("""
    protagonista2
"""), SpriteKind.player)
controller.move_sprite(player1)
scene.camera_follow_sprite(player1)
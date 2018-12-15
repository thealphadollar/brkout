# Animation Package User Guide
This package provides a simple animation and animating effects system which will help to vastly improve the graphics of your pygame.
Where to use:
- Create visual effects like explosions, hits etc.
- Continuous animations like a clock, shining effect etc.
- GUI animations.

# How to use

### Load animation frames
Load your animation frames / images in a list.
```python
blast_anim1_size = 120
blast_anim1 = []
for i in range(0, 6):
    frame = pygame.image.load(os.path.join(assets_directory, 'animation_sprites/blast1/tile' + str(i).rjust(3, '0') + '.png'))
    frame = pygame.transform.scale(frame, (blast_anim1_size, blast_anim1_size))
    blast_anim1.append(frame)
```
- size param determine the animation's size on screen.
- every frame / image should be of the same size.

### Initialize the animation system
Initialize it once in the game
```python
from game.animation_package import *

animation_manager = Animation_Manager(screen)
```
- screen: pygame surface on which to draw animations

### Create a new animating effect
Create a new animating effect using the animation manager.
```python
animation_manager.create_new_effect(blast_anim2, blast_anim2_size, 0, False, (ball.x, ball.y))
```
- blast_anim2: loaded animation frames
- blast_anim2_size: animation's size on screen
- 0: animation playback speed parameter
- False: loop animation or destory it when the sequence is over
- (ball.x, ball.y): screen position where to show the animation

### Drawing the animations on screen
Call the draw function every frame in your game loop
```python
animation_manager.draw_animations()
```

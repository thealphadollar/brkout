# Powerup System
### Types
- Double Damage: Doubles the damge caused to bricks
- Double Power: Sriker's power is doubled
- Double Score: Score is doubled
- Double Speed: Ball's maximum speed is doubled
- No Friction: Friction is removed temporarily

## How to use
Initialize the system once in your game
```python
powerup_manager = Powerup_Manager(screen, 12, 160, 15, 12)
```
Parameters:
- screen: pygame surface
- 12: time between powerup spawn
- 160: radius of spawn
- 15: expiry time of powerups, if it's not picked
- 12: total active time when powerup is picked

Update and draw it every frame
```python
powerup_manager.update(delta_time_actual, striker.get_collider())
powerup_manager.draw()
```
Parameters:
- delta_time_actual: delta time between frame in seconds
- striker circle collider

Reset the system when game ends or restarts
```python
powerup_manager.reset(run_vars)
```

## Create a new Powerup

### Create a new powerup class

Make a new class deriving from Powerup class. The main functions you want to change are the activate and the deactivate functions
Example powerup class:
```python
from .powerup import Powerup
from game.global_objects.constants import *


class Double_Score_Powerup(Powerup):

    def __init__(self, pos_x, pos_y, radius, expire_duration, effect_duration, powerup_manager):
        super().__init__(pos_x, pos_y, radius, expire_duration,
                         effect_duration, powerup_manager)
        self.name = 'Double Score'
        self.description = 'Get double score'
        self.image = double_score_powerup_img

    def activate(self):
        self.old_value = self.powerup_manager.run_vars.score_multiplier
        self.powerup_manager.run_vars.score_multiplier = self.old_value * 2.0
        self.activated = True

    def deactivate(self):
        self.powerup_manager.run_vars.score_multiplier = self.old_value
        self.powerup_manager.powerup_deactivated(self)
```
Functions:
- activate() is called when the powerup is picked by the player. The powerup effects should happen here. In this example, score_multiplier is doubled
- deactivate() is called when the powerup duration ends. The powerup effects should be reset here.

### Add your new class as a powerup enum
Add a new enum entry to E_Powerup_Enum
```python
class E_Powerup_Type(Enum):
    ''' Enum for powerups. '''
    double_damage = 0
    double_power = 1
    double_speed = 2
    no_friction = 3
    double_score = 4
```

### Add your powerup to the powerup manager
Add your new powerup's spawn code in the powerup_manager.py script. Example:
```python
    def spawn_random_powerup(self):
        rand = random.randint(0, len(E_Powerup_Type) - 1)
        rand_powerup = E_Powerup_Type(rand)
        rand_pos = self.get_random_position()

        if rand_powerup == E_Powerup_Type.double_damage:
            powerup = Double_Damage_Powerup(rand_pos[0],
                                            rand_pos[1],
                                            powerup_collider_radius,
                                            self.powerup_expiry_duration,
                                            self.powerup_effect_duration,
                                            self)

    self.powerups.append(powerup)
```

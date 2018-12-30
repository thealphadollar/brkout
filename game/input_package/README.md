# Input Package User Guide
This package provides a wrapper around the basic pygame input functionality to enable easy to use input system for games.
Main features
- Easy to use
- Multiple keys for same button action (ex. ctrl or F to shoot)
- Axis Input (ex. WASD input for moving)
- Multiple Axis Input schemes
- Easy to create input schemes

# How to use
### Create an input scheme
Create new buttons or axis' in the input_scheme.py file

**Button**
```python
# reload
input_list['reload'] = Button('reload', {pygame.K_r, pygame.K_4})
```
- 'reload' is the name of new action/button.
- {pygame.K_r, pygame.K_4} is the list of buttons that can trigger that action/button
- This will return true if the key was pressed or kept pressed this frame

**Button Up**
```python
# reload
input_list['reload'] = Button_Up('reload', {pygame.K_r, pygame.K_4})
```
- This will return True if the key was released this frame
- Usage is same as Button

**Button Down**
```python
# reload
input_list['reload'] = Button_Down('reload', {pygame.K_r, pygame.K_4})
```
- This will return True if the key was pressed down for the first time this frame
- Usage is same as Button

**Axis**
```python
# horizontal
input_list['horizontal'] = Axis('horizontal', {(pygame.K_a, pygame.K_d), (pygame.K_LEFT, pygame.K_RIGHT)})
```
- 'horizontal' is the name of axis
- {(pygame.K_a, pygame.K_d), (pygame.K_LEFT, pygame.K_RIGHT)} is the list of key pair tuples. Every tuple has the negative key and the positive key.
For example, press key a will move character left, pressing d will move right, same with arrow keys.

### Updating the input
The input state of the game changes every frame. To correctly record the changes, simply update the input_manager every frame before you use the input values from buttons or axis.
```python
// init once in the game
input_manager = Input_Manager() 
...
// every frame
input_manager.update(events)
```
### Using the Input values
**Button, Button_Up or Button_Down**
```python
if input_manager.get_button('reload'):
    do_something()
```
get_button('action_name') will either return True or False
Behaviour of Button, Button_Up and Button_Down is slightly different.
Button_Up returns true only if button was released this frame.
Button_Down returns true only if button was pressed this frame.
Button returns true if either the button was pressed this frame or kept pressed from previous frames.
Use Button for things like movement, shooting etc.
Use Button_Up and Button_Down for UI, pause, menu etc.

**Axis**
```python
movement = input_manager.get_axis('horizontal')
```
get_axis('axis_name') will either return -1, 0, or 1
- When negative key is pressed, it will return -1
- When no keys are pressed, it will return 0
- When positive key is pressed it will return 1

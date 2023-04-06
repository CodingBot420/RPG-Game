# Define the map
map = [
    # Room 0 (Starting Room)
    [
        "You are in a dimly lit room. The air is musty and there is a faint smell of decay.",
        {"north": 1, "east": 2, "south": None, "west": None}
    ],
    
    # Room 1
    [
        "You are in a narrow hallway. The walls are made of rough-hewn stone.",
        {"north": None, "east": None, "south": 0, "west": 3}
    ],
    
    # Room 2
    [
        "You are in a large chamber. The ceiling is high and the walls are adorned with intricate carvings.",
        {"north": 3, "east": None, "south": None, "west": 0}
    ],
    
    # Room 3
    [
        "You are in a small alcove. There is a strange object on a pedestal in the center of the room.",
        {"north": None, "east": 0, "south": 2, "west": 1}
    ]
]

# Define the starting room
current_room = 0

# Loop for continuous gameplay
while True:
    # Print the current room description
    print(map[current_room][0])
    
    # Ask the user for their movement action
    movement = input("Which direction do you want to move? (north, south, east, west) ")
    
    # Check if the movement action is valid
    if movement not in map[current_room][1]:
        print("Invalid action.")
        continue
    
    # Get the index of the room in the specified direction
    next_room = map[current_room][1][movement]
    
    # Check if the next room exists (i.e., not None)
    if next_room is None:
        print("You can't move in that direction.")
        continue
    
    # Update the current room
    current_room = next_room
    
    # Check if the player has won
    if current_room == 3:
        print("Congratulations, you have won!")
        break

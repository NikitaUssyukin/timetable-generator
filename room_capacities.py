ROOM_CAPACITIES = {
    269: 33,
    438: 21,
    270: 25,
    258: 22,
    365: 22,
    2: 25,  
    379: 20,
    164: 21,
    161: 14,
}

def get_available_room(remaining_places: dict):
    """
    Finds the first available room with a free seat.
    Returns the room number, updated remaining places, and a boolean indicating availability.
    """
    available_room = None
    for room_number, seat in remaining_places.items():
        if seat:
            available_room = room_number
            remaining_places[room_number] -= 1
            break
    
    if not available_room:
        return available_room, remaining_places, False

    return available_room, remaining_places, True

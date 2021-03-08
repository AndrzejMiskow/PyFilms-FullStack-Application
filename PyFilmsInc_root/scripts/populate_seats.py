from API.models import Seat, Room


def run():
    room = Room.objects.get(name=1)
    for i in range(1, 6):
        current_row = i
        for j in range(1, 16):
            current_number = j
            s = Seat(row=current_row, number=current_number, room_id=room)
            s.save()

    room = Room.objects.get(name=2)
    for i in range(1, 6):
        current_row = i
        for j in range(1, 31):
            current_number = j
            s = Seat(row=current_row, number=current_number, room_id=room)
            s.save()

    room = Room.objects.get(name=3)
    for i in range(1, 11):
        current_row = i
        for j in range(1, 21):
            current_number = j
            s = Seat(row=current_row, number=current_number, room_id=room)
            s.save()

    room = Room.objects.get(name=4)
    for i in range(1, 7):
        current_row = i
        for j in range(1, 26):
            current_number = j
            s = Seat(row=current_row, number=current_number, room_id=room)
            s.save()

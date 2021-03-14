from API.models import Seat, Room


def run():
    rooms = Room.objects.all()
    for i in range(1, 5):
        room = rooms.filter(name=i).first()
        for j in range(1, 5):
            for k in range(1, 9):
                seat = Seat(row=j, number=k, room_id=room)
                seat.save()

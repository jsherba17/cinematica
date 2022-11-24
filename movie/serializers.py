from rest_framework import serializers

from .models import *


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'


class UserTicket(UserSerializer):
	class Meta(UserSerializer.Meta):
		fields = 'first_name',


class MovieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movie
		fields = 'name','description', 'year'


class MovieTicket(MovieSerializer):
	class Meta(MovieSerializer.Meta):
		fields = 'name',

class SeatCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Seat
		fields = ['row', 'place']


class SessionSerializer(serializers.ModelSerializer):
	movie = MovieTicket()
	class Meta:
		model = Session
		fields = 'movie', 'time'


class SessionTicket(SessionSerializer):
	class Meta(SessionSerializer.Meta):
		fields = 'movie', 'time'

class SessionCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Session
		fields = 'movie', 'time',



class RoomSerializer(serializers.ModelSerializer):
	session = SessionTicket()
	class Meta:
		model = Room
		fields = ['id', 'name', 'cinema', 'session']


class RoomTicket(RoomSerializer):
	class Meta(RoomSerializer.Meta):
		fields = 'name', 'session'


class SeatSerializer(serializers.ModelSerializer):

	class Meta:
		model = Seat
		fields = 'row', 'place'



class TypeTicketSerializer(serializers.ModelSerializer):
	class Meta:
		model = TypeTicket
		fields = 'type_name', 'price'


class TicketSerializer(serializers.ModelSerializer):
	user = UserTicket()
	typeticket = TypeTicketSerializer(many=False)
	seat = SeatSerializer(many=False)
	room = RoomTicket()
	class Meta:
		model = Ticket
		fields = 'id','user', 'room', 'typeticket','seat','book',


class TicketCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ticket
		fields = 'user','seat', 'typeticket', 'book','room'


class BookSerializer(serializers.ModelSerializer):
	ticketbook = TicketSerializer(many=True)
	total_price = serializers.SerializerMethodField()

	class Meta:
		model = Book
		fields = 'ticketbook','total_price'

	def get_total_price(self, obj):
		tickets = Ticket.objects.filter(book=obj)
		total_price = 0
		for ticket in tickets:
			total_price += ticket.typeticket.price
		return total_price


class BookCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = '__all__'


class CinemaSerializer(serializers.ModelSerializer):
	room = serializers.StringRelatedField(many=True)

	class Meta:
		model = Cinema
		fields = ['title', 'description', 'schedule', 'address', 'contacts', 'room']




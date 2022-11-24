from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'cinema', CinemaViewSet, basename='cinema')
router.register(r'room', RoomViewSet, basename='room')
router.register(r'seat', SeatViewSet, basename='seat')
router.register(r'ticket', TicketViewSet, basename='ticket')
router.register(r'typeticket', TypeTicketViewSet, basename='typeticket')
router.register(r'book', BookViewSet, basename='book')
router.register(r'session', SessionViewSet, basename='session')
router.register(r'movie', MovieViewSet, basename='movie')

urlpatterns = router.urls

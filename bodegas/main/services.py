from .models import Noticia
from django.db.models import Count, Case, When, IntegerField
from .models import Noticia, User

def getLikesByUser(user_id):
    return Noticia.objects.annotate(likes=Count('users')).annotate(like_me=Count(Case(When(users__id=user_id, then=1))))

def addLike(user_id, noticia_id):
    noticia = Noticia.objects.get(id=noticia_id)
    noticia.users.add(User.objects.get(id=user_id))
    noticia.save()

def removeLike(user_id, noticia_id):
    noticia = Noticia.objects.get(id=noticia_id)
    noticia.users.remove(User.objects.get(id=user_id))
    noticia.save()
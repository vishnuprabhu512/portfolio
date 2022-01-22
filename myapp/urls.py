from django.urls import path
from .import views 

urlpatterns=[
	path('',views.index,name='index'),
	path('about/',views.about,name='about'),
	path('birthday/',views.birthday,name='birthday'),
	path('blogs/',views.blogs,name='blogs'),
	path('calculator/',views.calculator,name='calculator'),
	path('clock/',views.clock,name='clock'),
	path('contact/',views.contact,name='contact'),
	path('portfolio/',views.portfolio,name='portfolio'),
	path('texteditor/',views.texteditor,name='texteditor'),
	path('tictactoe/',views.tictactoe,name='tictactoe'),
	path('todo/',views.todo,name='todo'),
]
## 데이터베이스 설치

```
$ python manage.py migrate
# 마이그레이션을 DB에 반영
```

```python
Genre.objects.all()
# list 

class Genre(models.Model):
  name = odels.CharField(max_length=30)
  # varchard, testfield
```

```python
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ sqlite3 db.sqlite3
# python3 manage.py shell_plus
sqlite> .tabls
sqlite> .schema db_genre


>>> genre.name = '인디밴드'
>>> genre.name
'인디밴드'
>>> genre
<Genre: Genre object (None)>
>>> genre.save()
>>> genre
<Genre: Genre object (1)>
>>> Genre.objects.all()
# class name.manager.quertyset()
<QuerySet [<Genre: Genre object (1)>]>
# 내가 객체를 조작을 해서 저장을 시킬
# 메소드를 활용해서 파이썬 객체로 활용
# CRUD ORM 클래스 생성 테이블 생성
# 필드 변경(수정 삭제 추가) 클래스 수정

>>> Genre.objects.create(name='트로트')
<Genre: Genre object (2)>
>>> genre = Genre()
>>> genre.name = '락'
>>> genre.save()
>>> Genre.objects.all()
<QuerySet [<Genre: Genre object (1)>, <Genre: Genre object (2)>, <Genre: Genre object (3)>]>
>>> type(Genre.objects.all())
<class 'django.db.models.query.QuerySet'>

>>> genres = Genre.objects.all()
>>> for genre in genres:
...     print(genre.name)
... 
인디밴드
트로트
락
>>> Genre.objects.get(id=1)
<Genre: Genre object (1)>
 >>> Genre.objects.filter(id=1)
<QuerySet [<Genre: Genre object (1)>]>

>>> genre = Genre.objects.get(id=1)
>>> genre.name
'인디밴드'
>>> genre.name = '인디음악'
>>> genre.sacve()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Genre' object has no attribute 'sacve'
>>> genre.save()
>>> a = 1
>>> a
1
>>> a = 5
>>> people = ['홍길동', '김철수']
>>> # 다 출력하려면 반복문 써야죠
>>> person = '홍길동'

>>> # 삭제
>>> genre = Genre.objects.get(id=2)
>>> genre
<Genre: Genre object (2)>
 >>> genre.name
'트로트'
>>> genre.delete()
(1, {'db.Genre': 1})

>>> artist = Artist()
>>> artist.name = "아이브"
>>> import datetime
>>> artist.debut = datetime.date(2021, 12, 1)
>>> artist.save()
>>> artist
<Artist: Artist object (1)>
>>> ive = Artist.objects.get(id=1)
>>> ive.debut
datetime.date(2021, 12, 1)

>>> artist = Artist()
>>> artist.name = '아이유'
>>> artist.debut = '2019-12-26'
>>> artist.save()
>>> iu = Artist.objects.get(id=2)
>>> iu.debut
datetime.date(2019, 12, 26)
```

## 모델 만들기 -모델이란 부가적인 메타데이터를 가진 데이터베이스의 구조

```
hextriplej@sinhyeongangs-MacBook-Air DB-ORM-master % python3 manage.py makemigrations
Migrations for 'db':
  db/migrations/0002_artist.py
    - Create model Artist

hextriplej@sinhyeongangs-MacBook-Air DB-ORM-master % python3 manage.py migrate
Operations to perform:
  Apply all migrations: db
Running migrations:
  Applying db.0002_artist... OK
  
hextriplej@sinhyeongangs-MacBook-Air DB-ORM-master % python3 manage.py shell_plus
```



## 모델의 활성화 -모델(즉, 당신의 데이터베이스 스키마)의 변경사항을 디스크에 저장하는 방법

```python
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

```
$ python manage.py makemigrations polls
# 마이그레이션 파일 생성
```

```
$ python manage.py sqlmigrate polls 0001
```



## API 가지고 놀기

```python
$ python manage.py shell
```

## 개발 서버 시작

## 관리자 사이트에 들어가기

## 뷰 추가하기

```python
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```

```python
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```



## 뷰가 실제로 뭔가를 하도록 만들기

```python
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

# Leave the rest of the views (detail, results, vote) unchanged
```



```html
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```



```python
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```



## 지름길: render()

```python
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
```



## 404 에러 일으키기

```python
from django.http import Http404
from django.shortcuts import render

from .models import Question
# ...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
```

```
{{ question }}
```



## 지름길: get_object_or_404()

```python
from django.shortcuts import get_object_or_404, render

from .models import Question
# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
```



## 템플릿 시스템 사용하기

```html
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```

예제의 `{{ question.question_text }}` 구문을 보면, Django는 먼저 `question` 객체에 대해 사전형으로 탐색합니다. 탐색에 실패하게 되면 속성값으로 탐색합니다. (이 예에서는 속성값에서 탐색이 완료됩니다만) 만약 속성 탐색에도 실패한다면 리스트의 인덱스 탐색을 시도하게 됩니다.

[`{% for %}`](https://docs.djangoproject.com/ko/4.1/ref/templates/builtins/#std-templatetag-for) 반복 구문에서 메소드 호출이 일어납니다. `question.choice_set.all`은 Python에서 `question.choice_set.all()` 코드로 해석되는데, 이때 반환된 `Choice` 객체의 반복자는 [`{% for %}`](https://docs.djangoproject.com/ko/4.1/ref/templates/builtins/#std-templatetag-for)에서 사용하기 적당합니다.

## 템플릿에서 하드코딩된 URL 제거하기

```html
<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
```

```html
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

```python
# the 'name' value as called by the {% url %} template tag
path('<int:question_id>/', views.detail, name='detail'),
```

```python
# added the word 'specifics'
path('specifics/<int:question_id>/', views.detail, name='detail'),
```



## URL의 이름공간 정하기

```python
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

```python
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

```python
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```



## 간단한 폼 쓰기

```html
<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
<fieldset>
    <legend><h1>{{ question.question_text }}</h1></legend>
    {% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}
    {% for choice in question.choice_set.all %}
        <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
        <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
    {% endfor %}
</fieldset>
<input type="submit" value="Vote">
</form>
```

```python
path('<int:question_id>/vote/', views.vote, name='vote'),
```

```python
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question
# ...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```



```python
from django.shortcuts import get_object_or_404, render


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
```

```python
<h1>{{ question.question_text }}</h1>

<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
{% endfor %}
</ul>

<a href="{% url 'polls:detail' question.id %}">Vote again?</a>
```



## 제너릭 뷰 사용하기 적은 코드가 더 좋습니다

## URLconf 수정

```python
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```



## views 수정

```python
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    ... # same as above, no changes needed.
```



## 앱의 모양과 느낌을 원하는 대로 바꿔보세요

```css
li a {
    color: green;
}
```

```html
{% load static %}

<link rel="stylesheet" href="{% static 'polls/style.css' %}">
```

```python
$ python manage.py runserver
```



## 배경 이미지 추가하기

```css
body {
    background: white url("images/background.png") no-repeat;
}
```



# 템플릿

웹 프레임워크인 Django는 HTML을 동적으로 생성할 수 있는 편리한 방법이 필요합니다.가장 일반적인 접근방식은 템플릿에 의존합니다.템플릿에는 원하는 HTML 출력의 정적 부분과 동적 컨텐츠 삽입 방법을 설명하는 몇 가지 특별한 구문이 포함됩니다.템플리트로 HTML 페이지를 작성하는 실제 예는 [자습서](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fintro%2Ftutorial03%2F) [3](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fintro%2Ftutorial03%2F)을 참조하십시오.

Django 프로젝트는 하나 이상의 템플릿 엔진(템플릿을 사용하지 않는 경우에는 0)으로 구성할 수 있습니다.Django는 자체 템플릿 시스템(창의적으로 DTL(Dango Template Language)과 일반적인 대체 [Jinja2용](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fjinja.palletsprojects.com%2F) 내장 백엔드를 제공합니다.다른 템플릿 언어에 대한 백엔드는 서드파티에서 사용할 수 있습니다.사용자 지정 백엔드를 직접 작성할 수도 있습니다. 사용자 [지정 템플릿](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fhowto%2Fcustom-template-backend%2F) 백엔드를 [참조](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fhowto%2Fcustom-template-backend%2F)하십시오.

Django는 백엔드에 관계없이 템플릿을 로드 및 렌더링하기 위한 표준 API를 정의합니다.로딩은 특정 식별자에 대한 템플릿을 찾아 전처리하는 것으로 구성됩니다.일반적으로 이 템플릿을 메모리 내 표현으로 컴파일합니다.렌더링이란 템플릿에 컨텍스트 데이터를 보간하여 그 문자열을 반환하는 것을 의미한다.

[장고 템플릿](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Flanguage%2F) 언어는 장고 고유의 템플릿 시스템입니다.Django 1.8까지는 이 옵션만 내장되어 있었습니다.꽤 독단적이고 약간의 특이점을 가지고 있음에도 불구하고 좋은 템플릿 라이브러리입니다.다른 백엔드를 선택할 긴급한 이유가 없는 경우 DTL을 사용해야 합니다.특히 플러그형 응용 프로그램을 작성하고 템플릿을 배포할 경우에는 더욱 그렇습니다.[django.contrib.admin](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Fcontrib%2Fadmin%2F)과 같은 템플릿을 포함하는 Django의 기여 앱은 DTL을 사용합니다.

과거의 이유로 템플릿엔진에 대한 일반적인 지원과 Django 템플릿 언어 구현은 모두 에 존재합니다.`django.template`네임스페이스.

## 장고 템플릿 언어

Django 템플릿은 텍스트 문서 또는 Django 템플릿 언어를 사용하여 마크업된 Python 문자열입니다.일부 구성 요소는 템플릿엔진에 의해 인식되고 해석됩니다.주요 항목은 변수와 태그입니다.

템플릿은 컨텍스트와 함께 렌더링됩니다.렌더링은 변수를 컨텍스트에서 검색되는 값으로 대체하고 태그를 실행합니다.그 외는 모두 그대로 출력됩니다.

Django 템플릿 언어의 구문에는 4개의 구조가 포함됩니다.

#### 변수

변수는 컨텍스트에서 값을 출력합니다.이것은 dict와 같은 오브젝트 키를 값에 매핑하는 것입니다.

변수는 다음과 같이 둘러싸여 있습니다.`{{`그리고.`}}`다음과 같습니다.

```ㅔ
My first name is {{ first_name }}. My last name is {{ last_name }}. 
```

의 문맥락을사용하여`{'first_name': 'John', 'last_name': 'Doe'}`이 템플릿은 다음 대상으로 렌더링됩니다.

```
My first name is John. My last name is Doe. 
```

딕셔너리 룩업, 속성 룩업 및 리스트인덱스 룩업은 도트 표기로 구현됩니다.

```
{{ my_dict.key }} {{ my_object.attribute }} {{ my_list.0 }} 
```

변수가 콜 가능 상태로 해결되면 템플릿시스템은 인수를 지정하지 않고 해당 변수를 호출하고 콜 가능 대신 결과를 사용합니다.



#### 태그

태그는 렌더링 프로세스에서 임의 로직을 제공합니다.

이 정의는 의도적으로 모호하다.예를 들어 태그는 콘텐츠를 출력하거나 제어 구조(예: "if" 문 또는 "for" 루프)로 기능하거나 데이터베이스에서 콘텐츠를 가져오거나 다른 템플릿 태그에 액세스할 수 있습니다.

태그는 다음과 같이 둘러싸여 있습니다.`{%`그리고.`%}`다음과 같습니다.

```
{% csrf_token %} 
```

대부분의 태그는 인수를 받아들입니다.

```
{% cycle 'odd' 'even' %} 
```

일부 태그에는 시작 태그와 종료 태그가 필요합니다.

```
{% if user.is_authenticated %}Hello, {{ user.username }}.{% endif %} 
```

[내장된 태그](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fbuiltins%2F%23ref-templates-builtins-tags)에 대한 참조와 [사용자 지정](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fhowto%2Fcustom-template-tags%2F%23howto-writing-custom-template-tags) 태그 [작성](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fhowto%2Fcustom-template-tags%2F%23howto-writing-custom-template-tags) 지침을 [사용](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fhowto%2Fcustom-template-tags%2F%23howto-writing-custom-template-tags)할 수 있습니다.



#### 필터

필터는 변수 및 태그 인수 값을 변환합니다.

다음과 같습니다.

```
{{ django title }} 
```

의 문맥락을사용하여`{'django': 'the web framework for perfectionists with deadlines'}`이 템플릿은 다음 대상으로 렌더링됩니다.

```
The Web Framework For Perfectionists With Deadlines 
```

일부 필터는 인수를 사용합니다.



```
{{ my_date date:"Y-m-d" }} 
```

[내장된 필터](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fbuiltins%2F%23ref-templates-builtins-filters)에 대한 [참조](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fbuiltins%2F%23ref-templates-builtins-filters)와 사용자 [정의](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fhowto%2Fcustom-template-tags%2F%23howto-writing-custom-template-filters) 필터를 [작성](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fhowto%2Fcustom-template-tags%2F%23howto-writing-custom-template-filters)하기 위한 [지침](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fhowto%2Fcustom-template-tags%2F%23howto-writing-custom-template-filters)을 [사용](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fbuiltins%2F%23ref-templates-builtins-filters)할 수 있습니다.



#### 코멘트

코멘트는 다음과 같습니다.

```
{# this won't be rendered #} 
```

태그는 여러 줄의 주석을 제공합니다.



## 컴포넌트

#### 엔진

[`django.template.Engine`](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fapi%2F%23django.template.Engine) 에 Django 템플릿시스템의 인스턴스를 캡슐화합니다.를 직접 인스턴스화하는 주된 이유는 Django 프로젝트 외부에서 Django 템플릿 언어를 사용하기 위해서입니다.

[`django.template.backends.django.DjangoTemplates`](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Ftopics%2Ftemplates%2F#django.template.backends.django.DjangoTemplates) 는 Django의 템플릿 백엔드 API에 적합한 얇은 wrapper입니다.



#### 템플릿

[`django.template.Template`](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fapi%2F%23django.template.Template) 는 컴파일된 템플릿을 나타냅니다.템플릿은 또는 를 사용하여 입수할 수 있습니다.

저도 마찬가지예요.`django.template.backends.django.Template`는 일반적인 템플릿 API에 적합한 씬 wrapper입니다.



#### 콘텍스트

[`django.template.Context`](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fapi%2F%23django.template.Context) 는 컨텍스트 데이터 외에 일부 메타데이터를 보유하고 있습니다.템플릿을 렌더링하기 위해 에 전달됩니다.

[`django.template.RequestContext`](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fapi%2F%23django.template.RequestContext) 는 현재를 저장하고 템플릿콘텍스트 프로세서를 실행하는 서브 클래스입니다.

공통 API에는 동등한 개념이 없습니다.컨텍스트 데이터는 플레인에서 전달되며 필요에 따라 전류는 별도로 전달됩니다.



#### 로더

템플릿 로더는 템플릿을 찾고 로드하며 개체를 반환합니다.

Django는 여러 개의 [내장 템플릿로더](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fapi%2F%23template-loaders)를 제공하며 [커스텀템플릿 로더](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fapi%2F%23custom-template-loaders)를 [지원](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fapi%2F%23custom-template-loaders)합니다.



#### 콘텍스트 프로세서

컨텍스트 프로세서는 전류를 인수로 수신하고 렌더링 컨텍스트에 추가할 데이터의 를 반환하는 함수입니다.

주요 용도는 모든 보기에서 코드를 반복하지 않고 모든 템플릿이 공유하는 공통 데이터를 컨텍스트에 추가하는 것입니다.

Django는 많은 [콘텍스트 프로세서](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fapi%2F%23context-processors)를 내장하고 있으며, 독자적인 콘텍스트 프로세서를 실장할 수도 있습니다.



## 템플릿 엔진 지원



### 설정

템플릿 엔진은 이 설정으로 구성됩니다.각 엔진에 하나씩 구성된 목록입니다.기본값은 비어 있습니다.그`settings.py`명령어로 생성되는 값은 보다 유용한 값을 정의합니다.

```python
TEMPLATES = [     {         'BACKEND': 'django.template.backends.django.DjangoTemplates',         'DIRS': [],         'APP_DIRS': True,         'OPTIONS': {              ... some options here ...         },     }, ] 
```

[`BACKEND`](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Fsettings%2F%23std-setting-TEMPLATES-BACKEND) 는 Django의 템플릿백엔드 API를 구현하는 템플릿엔진 클래스의 닷이 있는 Python 경로입니다

The built-in backends are [django.template.backends.django.DjangoTemplates](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Ftopics%2Ftemplates%2F#django.template.backends.django.DjangoTemplates) and [django.template.backends.jinja2.Jinja2](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Ftopics%2Ftemplates%2F#django.template.backends.jinja2.Jinja2) .

대부분의 엔진은 파일에서 템플릿을 로드하므로 각 엔진의 최상위 구성에는 다음 두 가지 일반적인 설정이 있습니다.

- [`DIRS`](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Fsettings%2F%23std-setting-TEMPLATES-DIRS) 는 엔진이 템플릿소스 파일을 검색하는 디렉토리 목록을 검색 순서로 정의합니다.
- [`APP_DIRS`](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Fsettings%2F%23std-setting-TEMPLATES-APP_DIRS) 는 엔진이 설치된 응용 프로그램 내에서 템플릿을 검색해야 하는지 여부를 나타냅니다.각 백엔드는 템플릿이 저장되어야 하는 응용 프로그램 내의 서브디렉토리의 통상적인 이름을 정의합니다.

드물지만 동일한 백엔드의 여러 인스턴스를 다른 옵션으로 구성할 수 있습니다.이 경우 각 엔진에 대해 원하는 것을 정의해야 합니다.

[`OPTIONS`](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Fsettings%2F%23std-setting-TEMPLATES-OPTIONS) 에 백엔드 고유의 설정을 나타냅니다.



## 사용

그`django.template.loader`module은 템플릿을 로드하기 위한 두 가지 기능을 정의합니다.

- `get_template`(*syslog_name*, *사용=없음*)

  이 함수는 지정된 이름으로 템플릿을 로드하여`Template`물건.반환값의 정확한 유형은 템플릿을 로드한 백엔드에 따라 달라집니다.각 백엔드는 독자적인`Template`학급.`get_template()`는 성공할 때까지 각 템플릿엔진을 순서대로 시험합니다.템플릿을 찾을 수 없는 경우 가 발생합니다.템플릿이 발견되었지만 잘못된 구문이 포함되어 있는 경우 가 발생합니다.템플릿 검색 및 로드 방법은 각 엔진의 백엔드 및 구성에 따라 달라집니다.검색을 특정 템플릿엔진으로 제한하려면 엔진에서`using`논쟁.

- `select_template`(*syslog_name_list*, *사용=없음*)

  `select_template()`꼭 같다`get_template()`단, 템플릿 이름 목록을 가져옵니다.각 이름을 순서대로 시도하고 존재하는 첫 번째 템플릿을 반환합니다.

템플릿 로딩에 실패했을 경우 다음 두 가지 예외가 정의됩니다.`django.template`, 를 올릴 수 있습니다.

- *예외.* `TemplateDoesNotExist`(*msg*, tryed*=없음*, *백엔드=없음*, *체인=없음*)

  이 예외는 템플릿을 찾을 수 없을 때 발생합니다.디버깅 페이지에서 [템플릿](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fhowto%2Fcustom-template-backend%2F%23template-postmortem)을 사후에 입력하기 위해 다음 옵션 인수를 받아들입니다.`backend`예외가 발생한 템플릿백엔드 인스턴스`tried`템플릿을 찾을 때 시도된 원본 목록입니다.이 형식은 다음을 포함하는 튜플 목록으로 지정됩니다.`(origin, status)`,어디에`origin`[원본](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fhowto%2Fcustom-template-backend%2F%23template-origin-api)과 같은 객체입니다.`status`템플릿을 찾을 수 없는 이유를 나타내는 문자열입니다.`chain`템플릿을 로드하려고 할 때 발생하는 중간 예외 목록입니다.이는 여러 엔진에서 특정 템플릿을 로드하려고 하는 등의 함수에 의해 사용됩니다.

- *예외.* `TemplateSyntaxError`(*msg*)

  이 예외는 템플릿이 발견되었지만 오류가 있을 때 발생합니다.

`Template`에 의해 반환된 오브젝트`get_template()`그리고.`select_template()`를 제공해야 합니다.`render()`다음 시그니처를 가진 메서드:

- `Template.``render`(*콘텍스트=없음*, *요청=없음*)

  지정된 컨텍스트에서 이 템플릿을 렌더링합니다.한다면`context`를 지정해야 합니다.지정되지 않은 경우 엔진은 템플릿을 빈 컨텍스트로 렌더링합니다.한다면`request`를 지정합니다.그런 다음 CSRF 토큰과 함께 템플릿에서 사용할 수 있도록 해야 합니다.이를 실현하는 방법은 각 백엔드에 달려 있습니다.

다음은 검색 알고리즘의 예입니다.이 예에서 설정은 다음과 같습니다.

```python
TEMPLATES = [     {         'BACKEND': 'django.template.backends.django.DjangoTemplates',         'DIRS': [             '/home/html/example.com',             '/home/html/default',         ],     },     {         'BACKEND': 'django.template.backends.jinja2.Jinja2',         'DIRS': [             '/home/html/jinja2',         ],     }, ] 
```

전화하시면`get_template('story_detail.html')`다음은 장고가 찾는 파일 순서입니다.

- `/home/html/example.com/story_detail.html`(`'django'`엔진)
- `/home/html/default/story_detail.html`(`'django'`엔진)
- `/home/html/jinja2/story_detail.html`(`'jinja2'`엔진)

전화하시면`select_template(['story_253_detail.html', 'story_detail.html'])`장고가 기대하는 것은 다음과 같습니다.

- `/home/html/example.com/story_253_detail.html`(`'django'`엔진)
- `/home/html/default/story_253_detail.html`(`'django'`엔진)
- `/home/html/jinja2/story_253_detail.html`(`'jinja2'`엔진)
- `/home/html/example.com/story_detail.html`(`'django'`엔진)
- `/home/html/default/story_detail.html`(`'django'`엔진)
- `/home/html/jinja2/story_detail.html`(`'jinja2'`엔진)

Django는 존재하는 템플릿을 찾으면 검색을 중지합니다.

템플릿을 포함하는 각 디렉토리 내의 서브디렉토리에 정리할 수도 있습니다.이 규칙은 각 Django 앱의 서브디렉토리를 만들고 필요에 따라 서브디렉토리에 서브디렉토리를 만듭니다.

당신 자신을 위해 이것을 하세요.단일 디렉토리의 루트레벨에 모든 템플릿을 저장하면 복잡해집니다.

서브 디렉토리내에 있는 템플릿을 로드하려면 , 다음과 같이 슬래시를 사용합니다.

```
get_template('news/story_detail.html') 
```

위와 같은 옵션을 사용하여 다음 템플릿을 로드하려고 합니다.

- `/home/html/example.com/news/story_detail.html`(`'django'`엔진)
- `/home/html/default/news/story_detail.html`(`'django'`엔진)
- `/home/html/jinja2/news/story_detail.html`(`'jinja2'`엔진)

또한 템플릿 로드 및 렌더링의 반복성을 줄이기 위해 프로세스를 자동화하는 숏컷 기능을 제공합니다.

- `render_to_string`(*context_name*, *context=None*, *request=None*, *사용=없음*)

  `render_to_string()`같은 템플릿을 로드하여 호출합니다.`render()`즉시 방법을 지정합니다.다음 인수를 사용합니다.`template_name`로드 및 렌더링할 템플릿의 이름.템플릿 이름 목록일 경우, Django는 템플릿을 찾는 대신 을 사용합니다.`context`렌더링용 템플릿의 컨텍스트로 사용되는 A.`요청`템플릿 렌더링 프로세스 중에 사용할 수 있는 옵션입니다.`using`옵션 템플릿엔진템플릿 검색은 해당 엔진으로 제한됩니다.

  사용 예: 

```python
from django.template.loader import render_to_string rendered = render_to_string('my_template.html', {'foo': 'bar'}) 
```



뷰에서 되돌리기에 적합한 결과를 호출하여 제공하는 바로 가기도 참조하십시오.

마지막으로 설정된 엔진을 직접 사용할 수 있습니다.

- `engines`

  템플릿 엔진은 다음 위치에서 사용할 수 있습니다.`django.template.engines`:

```python
from django.template import engines  django_engine = engines['django'] template = django_engine.from_string("Hello {{ name }}!") 
```

검색 키:`'django'`이 예에서는 이 엔진의 입니다.



## 내장 백엔드

- *학급* `DjangoTemplates`

  

로 설정`'django.template.backends.django.DjangoTemplates'`Django 템플릿엔진을 설정합니다.

언제가`True`,`DjangoTemplates`엔진은 에서 템플릿을 검색합니다.`templates`설치되어 있는 애플리케이션의 서브 디렉토리.이 일반 이름은 이전 버전과의 호환성을 위해 유지되었습니다.

`DjangoTemplates`엔진은 다음 사항을 지원합니다.

- `'autoescape'`: HTML 자동 이스케이핑 활성화 여부를 제어하는 부울.

  디폴트로는`True`.

- `'context_processors'`: 템플릿이 요청으로 렌더링될 때 컨텍스트를 채우기 위해 사용되는 콜러블에 대한 도트 포함 Python 경로 목록.이러한 콜러블은 요구 오브젝트를 인수로 하여 컨텍스트에 Marge되는 항목을 반환합니다.

  기본값은 빈 목록입니다.

  상세한 것에 대하여는, 을 참조해 주세요.

- `'debug'`: 템플릿 디버깅모드를 온/오프하는 부울.그렇다면`True`템플릿 렌더링 중에 발생한 예외에 대한 상세 보고서가 fancy error 페이지에 표시됩니다.이 보고서에는 적절한 행이 강조 표시된 템플릿의 관련 스니펫이 포함되어 있습니다.

  기본값은 설정값입니다.

- `'loaders'`: 템플릿로더 클래스에 대한 도트 포함 Python 경로 목록입니다.각각`Loader`class는 특정 소스에서 템플릿을 Import하는 방법을 알고 있습니다.옵션으로 문자열 대신 태플을 사용할 수 있습니다.태플의 첫 번째 항목은`Loader`클래스 이름 및 후속 항목이 에 전달됩니다.`Loader`초기화 중.

  기본값은 및 의 값에 따라 달라집니다.

  자세한 내용은 [로더](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fapi%2F%23template-loaders) 유형을 [참조](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fapi%2F%23template-loaders)하십시오.

- `'string_if_invalid'`: 템플릿 시스템이 잘못된(철자 오류 등) 변수에 사용해야 하는 출력(문자열).

  기본값은 빈 문자열입니다.

  자세한 내용은 [잘못된 변수](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fapi%2F%23invalid-template-variables) 처리 [방법](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fapi%2F%23invalid-template-variables)을 [참조](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fapi%2F%23invalid-template-variables)하십시오.

- `'file_charset'`: 디스크상의 템플릿파일을 읽기 위해서 사용되는 문자 세트.

  디폴트로는`'utf-8'`.

- `'libraries'`: 템플릿엔진에 등록할 템플릿태그 모듈의 라벨 및 닷이 있는 Python 경로 사전.새 라이브러리를 추가하거나 기존 라이브러리에 대한 대체 레이블을 제공하는 데 사용할 수 있습니다.예를 들어 다음과 같습니다.

```python
OPTIONS={     'libraries': {         'myapp_tags': 'path.to.myapp.tags',         'admin.urls': 'django.contrib.admin.templatetags.admin_urls',     }, } 
```



- 라이브러리는 해당 사전 키를 태그에 전달하여 로드할 수 있습니다.
- `'builtins'`: [빌트인](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fbuiltins%2F)에 추가할 템플릿 태그 모듈의 도트 포함 Python 경로 목록입니다.예를 들어 다음과 같습니다.

```
OPTIONS={     'builtins': ['myapp.builtins'], } 
```

- 내장된 라이브러리의 태그 및 필터를 먼저 태그를 호출하지 않고 사용할 수 있습니다.



- *학급* `Jinja2`

  

[Jinja2](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fjinja.palletsprojects.com%2F)를 설치해야 합니다.



```
$ python -m pip install Jinja2 
```



로 설정`'django.template.backends.jinja2.Jinja2'`[Jinja2](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fjinja.palletsprojects.com%2F) 엔진을 설정합니다.

언제가`True`,`Jinja2`엔진은 에서 템플릿을 검색합니다.`jinja2`설치되어 있는 애플리케이션의 서브 디렉토리.

에서 가장 중요한 엔트리는`'environment'`. Jinja2 환경을 반환하는 호출 가능한 Python 경로입니다.디폴트로는`'jinja2.Environment'`. Django는 해당 콜 가능을 호출하고 키워드 인수로 다른 옵션을 전달합니다.또한 Django는 몇 가지 옵션에서 Jinja2와 다른 기본값을 추가합니다.

- `'autoescape'`:`True`
- `'loader'`: 및용으로 구성된 로더
- `'auto_reload'`:`settings.DEBUG`
- `'undefined'`:`DebugUndefined if settings.DEBUG else Undefined`

`Jinja2`엔진에서는 다음 기능도 사용할 수 있습니다.

- `'context_processors'`: 템플릿이 요청으로 렌더링될 때 컨텍스트를 채우기 위해 사용되는 콜러블에 대한 도트 포함 Python 경로 목록.이러한 콜러블은 요구 오브젝트를 인수로 하여 컨텍스트에 Marge되는 항목을 반환합니다.

  기본값은 빈 목록입니다.

디폴트 설정은 의도적으로 최소한으로 유지합니다.템플릿이 요구와 함께 렌더링되는 경우(예를 들어 를 사용하는 경우),`Jinja2`backend는 글로벌을 추가합니다.`request`,`csrf_input`,그리고.`csrf_token`문맥에 맞게.그 외에는 이 백엔드는 장고 풍미의 환경을 만들지 않습니다.장고 필터와 태그는 모릅니다.Django 고유의 API를 사용하려면 해당 API를 환경으로 구성해야 합니다.

예를 들어, 다음과 같이 만들 수 있습니다.`myproject/jinja2.py`다음 내용을 포함합니다.



```python
from django.templatetags.static import static from django.urls import reverse  from jinja2 import Environment   def environment(**options):     env = Environment(**options)     env.globals.update({         'static': static,         'url': reverse,     })     return env 
```

를 설정합니다.`'environment'`할 수 있는 선택권`'myproject.jinja2.environment'`.

그런 다음 Jinja2 템플릿에서 다음 구성을 사용할 수 있습니다.



```
<img src="{{ static('path/to/company-logo.png') }}" alt="Company Logo">  <a href="{{ url('admin:index') }}">Administration</a> 
```

태그와 필터의 개념은 Django 템플릿 언어와 Jinja2 모두에 존재하지만 서로 다르게 사용됩니다.Jinja2는 템플릿 내의 콜러블에 인수를 전달하는 기능을 지원하므로 위의 예시와 같이 Jinja2 템플릿 내의 함수를 호출함으로써 Django 템플릿 내의 템플릿 태그 또는 필터를 필요로 하는 많은 기능을 실현할 수 있습니다.Jinja2의 글로벌 네임스페이스는 템플릿 컨텍스트 프로세서를 필요로 하지 않습니다.장고 템플릿 언어에는 Jinja2 테스트와 동등한 것이 없습니다.



## 장고 템플릿 언어

이 문서에서는 Django 템플릿시스템의 언어 구문에 대해 설명합니다.동작 방법과 확장 방법에 대한 보다 기술적인 관점을 찾고 있다면 [Django 템플릿](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fapi%2F) 언어:[ for](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fapi%2F) Python [프로그래머](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fapi%2F)를 [참조](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fapi%2F)하십시오.

장고의 템플릿 언어는 힘과 용이성 사이에서 균형을 이루도록 설계되었습니다.HTML을 사용하는 데 익숙한 사용자에게 편안함을 느낄 수 있도록 [설계](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fwww.smarty.net%2F)되었습니다. Smarty나 [Jinja2](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fpalletsprojects.com%2Fp%2Fjinja%2F)와 같은 다른 텍스트 기반 템플릿 언어에 노출되어 있다면 Django의 템플릿이 있으면 편안함을 느낄 수 있습니다.



## 템플릿

템플릿은 텍스트 파일입니다.임의의 텍스트 기반 형식(HTML, XML, CSV 등)을 생성할 수 있습니다.

템플릿에는 템플릿이 평가될 때 값으로 대체되는 **변수**와 템플릿의 로직을 제어하는 태그가 **포함**됩니다.

다음은 몇 가지 기본을 보여주는 최소한의 템플릿입니다.각 요소에 대해서는 이 문서의 뒷부분에서 설명합니다.



```html
{% extends "base_generic.html" %}  {% block title %}{{ section.title }}{% endblock %}  {% block content %} <h1>{{ section.title }}</h1>  {% for story in story_list %} <h2>   <a href="{{ story.get_absolute_url }}">     {{ story.headline upper }}   </a> </h2> <p>{{ story.tease truncatewords:"100" }}</p> {% endfor %} {% endblock %} 
```



## 변수

변수는 다음과 같습니다.`{{ variable }}`템플릿 엔진은 변수를 발견하면 해당 변수를 평가하여 결과로 대체합니다.변수명은, 영숫자와 밑줄의 임의의 편성으로 구성됩니다( ).`"_"`)는 밑줄로 시작할 수 없으며 숫자도 사용할 수 없습니다.점(`"."`)도 변수 섹션에 표시됩니다.단, 다음과 같이 특별한 의미가 있습니다.*변수* 이름에는 *공백이나 구두점을 사용*할 수 *없습니다*.

점(을 사용)`.`변수 Atribute에 액세스합니다.



위의 예에서는`{{ section.title }}`로 대체됩니다.`title`의 속성`section`물건.

존재하지 않는 변수를 사용하는 경우 템플릿 시스템은 다음 값을 삽입합니다.`string_if_invalid`option(옵션)으로 설정되어 있다.`''`디폴트로는 (빈 문자열)입니다.

템플릿 표현에서 "bar"는 다음과 같습니다.`{{ foo.bar }}`는 리터럴 문자열로 해석되며 변수 "bar" 값이 템플릿 컨텍스트에 존재하는 경우 사용되지 않습니다.

밑줄로 시작하는 변수 속성은 일반적으로 비공개로 간주되므로 액세스할 수 없습니다.



## 필터

필터를 **사용**하여 표시할 변수를 수정할 수 있습니다.

필터는 다음과 같습니다.`{{ name lower }}`. 이것은 의 값을 표시합니다.`{{ name }}`필터를 통해 필터링된 후 텍스트가 소문자로 변환됩니다.파이프 사용(` `필터를 적용합니다.

필터는 「체인」할 수 있습니다.한 필터의 출력이 다음 필터에 적용됩니다. `{{ text escape linebreaks }}`는 텍스트 내용을 이스케이프하여 줄 바꿈을 로 변환하기 위한 일반적인 관용어입니다.`<p>`태그를 지정합니다.

일부 필터는 인수를 사용합니다.필터 인수는 다음과 같습니다.`{{ bio truncatewords:30 }}`. 그러면 처음 30개의 단어가 표시됩니다.`bio`변수.

공백이 포함된 필터 인수는 따옴표로 묶어야 합니다. 예를 들어 사용할 쉼표와 공백으로 목록에 가입하려면`{{ list join:", " }}`.

Django는 약 60개의 템플릿필터를 내장하고 있습니다.[기본](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fbuiltins%2F%23ref-templates-builtins-filters) 제공 [필터](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fbuiltins%2F%23ref-templates-builtins-filters) 참조에서 이러한 모든 정보를 읽을 수 있습니다.사용 가능한 것을 알기 쉽게 하기 위해 일반적으로 사용되는 템플릿필터를 다음에 나타냅니다.

- [`default`](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fbuiltins%2F%23std-templatefilter-default)

  변수가 false이거나 비어 있는 경우 지정된 기본값을 사용합니다.그렇지 않으면 변수 값을 사용합니다.예를 들어 다음과 같습니다.



```python
{{ value default:"nothing" }} 
```



한다면`value`입력되지 않았거나 비어 있습니다.상기에 "가 표시됩니다.`nothing`”.

[`length`](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fbuiltins%2F%23std-templatefilter-length)

값의 길이를 반환합니다.이것은 문자열과 목록 모두에서 작동합니다.예를 들어 다음과 같습니다.

```
{{ value length }} 
```

한다면`value`이`['a', 'b', 'c', 'd']`출력은 다음과 같습니다.`4`.

[`filesizeformat`](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fbuiltins%2F%23std-templatefilter-filesizeformat)

값의 형식을 "사람이 읽을 수 있는" 파일 크기(예:`'13 KB'`,`'4.1 MB'`,`'102 bytes'`등).예를 들어 다음과 같습니다.

```
{{ value filesizeformat }} 
```



이것은 몇 가지 예에 불과합니다.전체 목록은 내장된 [필터 참조](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fbuiltins%2F%23ref-templates-builtins-filters)를 참조하십시오.

사용자 지정 템플릿 필터를 직접 생성할 수도 있습니다. 사용자 [지정 템플릿 태그](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fhowto%2Fcustom-template-tags%2F) 및 [필터](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fhowto%2Fcustom-template-tags%2F) [생성 방법을 참조](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fhowto%2Fcustom-template-tags%2F)하십시오.



## 태그

태그는 다음과 같습니다.`{% tag %}`태그는 변수보다 복잡합니다.일부는 출력에 텍스트를 작성하고 일부는 루프 또는 로직을 실행하여 플로우를 제어하며 일부는 외부 정보를 템플릿에 로드하여 나중에 변수에 사용합니다.

일부 태그에는 시작 태그와 종료 태그가 필요합니다(예:`{% tag %} ... tag contents ... {% endtag %}`).

Django는 약 24개의 템플릿 태그가 내장된 상태로 출고됩니다.[기본](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fbuiltins%2F%23ref-templates-builtins-tags) 제공 [태그](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fbuiltins%2F%23ref-templates-builtins-tags) 참조에서 이러한 모든 정보를 읽을 수 있습니다.사용 가능한 태그에 대해 알아보기 위해 일반적으로 사용되는 태그는 다음과 같습니다.

- [`for`](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fbuiltins%2F%23std-templatetag-for)

  배열의 각 항목을 루프합니다.예를 들어, 에서 제공되는 선수 목록을 표시하려면`athlete_list`:



```html
<ul> {% for athlete in athlete_list %}     <li>{{ athlete.name }}</li> {% endfor %} </ul> 
```

[`if`](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fbuiltins%2F%23std-templatetag-if),`elif`,그리고.`else`

변수를 평가합니다. 변수가 "참"인 경우 블록의 내용이 표시됩니다.



```html
{% if athlete_list %}     Number of athletes: {{ athlete_list length }} {% elif athlete_in_locker_room_list %}     Athletes should be out of the locker room soon! {% else %}     No athletes. {% endif %} 
```

상기의 경우`athlete_list`선수 수는 공백이 아닙니다.선수 수는 다음 순서로 표시됩니다.`{{ athlete_list length }}`변수.그렇지 않으면`athlete_in_locker_room_list`이 비어있지 않으면 "Athletes be out..." 이라는 메시지가 나타납니다.두 목록이 모두 비어 있으면 "선수 없음"이 표시됩니다.

태그에서는 필터와 다양한 연산자를 사용할 수도 있습니다.



```
{% if athlete_list length > 1 %}    Team: {% for athlete in athlete_list %} ... {% endfor %} {% else %}    Athlete: {{ athlete_list.0.name }} {% endif %} 
```

- [`block`](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fbuiltins%2F%23std-templatetag-block) 그리고

  템플릿 [상속을 설정](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Flanguage%2F#id1)합니다(아래 참조).템플릿의 "보일러 플레이트"를 줄이는 강력한 방법입니다.

위의 내용은 목록 전체의 선택일 뿐입니다.전체 목록은 [내장된 태그](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fbuiltins%2F%23ref-templates-builtins-tags) 참조를 참조하십시오.

사용자 지정 템플릿 태그를 직접 생성할 수도 있습니다. 사용자 [지정 템플릿 태그](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fhowto%2Fcustom-template-tags%2F) 및 [필터](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fhowto%2Fcustom-template-tags%2F) [생성 방법을 참조](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fhowto%2Fcustom-template-tags%2F)하십시오.



## 코멘트

템플릿에서 행의 일부를 주석 아웃하려면 주석 구문을 사용합니다.`{# #}`.

예를 들어 이 템플릿은 다음과 같이 렌더링합니다.`'hello'`:

```
{# greeting #}hello 
```

코멘트에는 무효 여부에 관계없이 임의의 템플릿코드를 포함할 수 있습니다.예를 들어 다음과 같습니다.

```
{# {% if foo %}bar{% else %} #} 
```

이 구문은 한 줄 코멘트에만 사용할 수 있습니다.`{#`그리고.`#}`구분자)를 사용합니다.템플릿의 여러 줄 부분을 코멘트 아웃해야 하는 경우 태그를 참조하십시오.



## 템플릿 상속

Django 템플릿엔진의 가장 강력하고 복잡한 부분은 템플릿 상속입니다.템플릿 상속을 사용하면 사이트의 모든 공통 요소를 포함하는 기본 "skeleton" 템플릿을 작성하고 하위 템플릿이 재정의할 수 있는 블록을 **정의**할 수 있습니다.

예를 들어 템플릿 상속을 살펴보겠습니다.

```html
<!DOCTYPE html> <html lang="en"> <head>     <link rel="stylesheet" href="style.css">     <title>{% block title %}My amazing site{% endblock %}</title> </head>  <body>     <div id="sidebar">         {% block sidebar %}         <ul>             <li><a href="/">Home</a></li>             <li><a href="/blog/">Blog</a></li>         </ul>         {% endblock %}     </div>      <div id="content">         {% block content %}{% endblock %}     </div> </body> </html> 
```

이 템플릿, 이 템플릿은`base.html`는 2열 페이지에 사용할 수 있는HTML 스켈레톤 문서를 정의합니다.빈 블록을 콘텐츠로 채우는 것은 "하위" 템플릿의 작업입니다.

이 예에서 태그는 하위 템플릿이 채울 수 있는 3개의 블록을 정의합니다.태그는 템플릿엔진에 자 템플릿이 템플릿의 이러한 부분을 덮어쓸 수 있음을 통지하는 것뿐입니다.

하위 템플릿은 다음과 같습니다.



```html
{% extends "base.html" %}  {% block title %}My amazing blog{% endblock %}  {% block content %} {% for entry in blog_entries %}     <h2>{{ entry.title }}</h2>     <p>{{ entry.body }}</p> {% endfor %} {% endblock %} 
```

여기 태그가 열쇠입니다.이 템플릿은 템플릿엔진에 이 템플릿이 다른 템플릿을 "확장"하는 것을 통지합니다.템플릿 시스템이 이 템플릿을 평가할 때 먼저 부모(이 경우 "base.html")를 찾습니다.

이 시점에서 템플릿엔진은 의 3개의 태그를 인식합니다.`base.html`이러한 블록을 자 템플릿의 내용으로 바꿉니다.의 가치에 따라`blog_entries`출력은 다음과 같습니다.



```html
<!DOCTYPE html> <html lang="en"> <head>     <link rel="stylesheet" href="style.css">     <title>My amazing blog</title> </head>  <body>     <div id="sidebar">         <ul>             <li><a href="/">Home</a></li>             <li><a href="/blog/">Blog</a></li>         </ul>     </div>      <div id="content">         <h2>Entry one</h2>         <p>This is my first entry.</p>          <h2>Entry two</h2>         <p>This is my second entry.</p>     </div> </body> </html> 
```



자 템플릿이 정의되어 있지 않기 때문에`sidebar`대신 부모 템플릿의 값이 사용됩니다.A 내의 콘텐츠`{% block %}`부모 템플릿의 태그는 항상 폴백으로 사용됩니다.

필요한 만큼 상속 수준을 사용할 수 있습니다.상속을 사용하는 일반적인 방법 중 하나는 다음과 같은 3단계 방법입니다.

- 작성하다`base.html`사이트의 주요 모양과 느낌을 유지하는 템플릿입니다.
- 작성하다`base_SECTIONNAME.html`각 "섹션의 각 섹션의 템플릿을 참조해 주세요.예를들면,`base_news.html`,`base_sports.html`이러한 템플릿은 모두 확장됩니다.`base.html`섹션별 스타일/디자인을 포함합니다.
- 뉴스 기사 또는 블로그 항목과 같은 페이지 유형별로 개별 템플리트를 작성합니다.이러한 템플릿은 적절한 섹션 템플릿을 확장합니다.

이 접근방식은 코드 재사용을 최대화하고 섹션 전체 탐색 등의 공유 콘텐츠 영역에 항목을 추가하는 데 도움이 됩니다.

다음은 상속 작업에 대한 몇 가지 팁입니다.

- 템플릿에서 를 사용하는 경우 해당 템플릿의 첫 번째 템플릿태그여야 합니다.그렇지 않으면 템플릿 상속이 작동하지 않습니다.
- 기본 템플릿에 태그가 많을수록 좋습니다.하위 템플릿은 모든 상위 블록을 정의할 필요는 없으므로 여러 블록에 적절한 기본값을 입력한 후 나중에 필요한 기본값만 정의할 수 있습니다.갈고리가 적은 것보다 더 많은 갈고리가 있는 것이 낫다.
- 여러 템플릿에서 콘텐츠를 복제하는 경우 해당 콘텐츠를 다른 템플릿으로 이동해야 합니다.`{% block %}`부모 템플릿에 있습니다.
- 부모 템플릿에서 블록의 내용을 가져올 필요가 있는 경우`{{ block.super }}`variable이 유효합니다.이것은 부모 블록의 내용을 완전히 재정의하지 않고 추가할 때 유용합니다.다음 방법으로 삽입된 데이터`{{ block.super }}`는 필요에 따라 부모 템플릿에서 이미 이스케이프되었기 때문에 자동으로 이스케이프되지 않습니다([다음](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Flanguage%2F#automatic-html-escaping) 항 참조).
- 상속원과 동일한 템플릿 이름을 사용하여 템플릿을 덮어쓰는 동시에 상속할 수 있습니다.와의 조합`{{ block.super }}`작은 커스터마이징을 할 수 있는 강력한 방법입니다.자세한 예는 *Overriding* templates How-to 의 「[How-to](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fhowto%2Foverriding-templates%2F%23extending-an-overridden-template)」를 참조해 주세요[.](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fhowto%2Foverriding-templates%2F%23extending-an-overridden-template)
- 템플릿 태그를 사용하여 외부에서 작성된 변수`as`블록 내부에서는 구문을 사용할 수 없습니다.예를 들어 이 템플릿은 아무것도 렌더링하지 않습니다.

```html
{% translate "Title" as title %} {% block content %}{{ title }}{% endblock %} 
```

가독성을 높이기 위해 *임의*로 이름을 붙일 수 있습니다.`{% endblock %}`태그. 예:

```
{% block content %} ... {% endblock content %} 
```

- 더 큰 템플릿에서는 이 기술을 사용하여 다음 항목을 확인할 수 있습니다.`{% block %}`태그가 닫힙니다.
- [`{% block %}`](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fbuiltins%2F%23std-templatetag-block) 태그가 먼저 평가됩니다.그렇기 때문에 주변 태그의 진실성에 관계없이 블록의 내용은 항상 덮어쓰게 됩니다.예를 들어, 이 템플릿은 항상 의 내용을 *덮어씁니다*.`title`블록:

```
{% if change_title %}     {% block title %}Hello!{% endblock title %} {% endif %} 
```

마지막으로 동일한 템플릿에 동일한 이름의 태그를 여러 개 정의할 수 없습니다.이 제한은 블록 태그가 "양방향"으로 작동하기 때문에 존재합니다.즉, 블록 태그는 단순히 채울 구멍을 제공할 뿐만 아니라 *부모*의 구멍을 메우는 내용도 정의합니다.템플릿에 비슷한 이름의 태그가 두 개 있는 경우 해당 템플릿의 부모는 어떤 블록의 콘텐츠를 사용할지 알 수 없습니다.



## HTML 자동 이스케이프

템플릿에서 HTML을 생성할 때 변수에 HTML에 영향을 미치는 문자가 포함될 위험이 항상 있습니다. 예를 들어, 다음과 같은 템플릿 조각이 있습니다.

```
Hello, {{ name }} 
```

처음에 이것은 사용자의 이름을 표시하는 무해한 방법이라고 생각되지만, 사용자가 이름을 다음과 같이 입력하면 어떻게 되는지 생각해 보십시오.

```
<script>alert('hello')</script> 
```

이 이름 값을 사용하면 템플릿은 다음과 같이 렌더링됩니다.

```
Hello, <script>alert('hello')</script> 
```



브라우저에 JavaScript 경보 상자가 나타납니다.

마찬가지로, 만약 그 이름에 다음 명령어를 포함한다면?`'<'`기호, 이렇게?

```
<b>username 
```

그러면 다음과 같은 템플릿이 렌더링됩니다.

```
Hello, <b>username 
```

...그 결과, 나머지 웹 페이지는 굵은 글씨로 표시됩니다.

사용자가 제출한 데이터를 맹목적으로 신뢰하고 웹 페이지에 직접 삽입해서는 안 됩니다. 악의적인 사용자가 이러한 종류의 구멍을 사용하여 잠재적으로 나쁜 짓을 할 수 있기 때문입니다.이러한 유형의 보안 부정 이용은 [크로스 사이트](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FCross-site_scripting) 스크립팅(XSS) 공격이라고 불립니다.

이 문제를 회피하려면 다음 두 가지 옵션이 있습니다.

- 첫째, 각 신뢰할 수 없는 변수를 필터(아래 문서)를 통해 실행할 수 있습니다. 필터는 잠재적으로 유해한 HTML 문자를 유해하지 않은 문자로 변환합니다.이것은 처음 몇 년간 Django에서 기본 솔루션이었지만, 문제는 개발자/템플릿 작성자인 당신에게 *모든* 것을 회피할 책임이 있다는 것입니다.데이터 유출을 잊기 쉽습니다.
- 둘째, 장고의 자동 HTML 이스케이프를 이용할 수 있습니다.이 섹션의 나머지 부분에서는 자동 이스케이핑의 구조에 대해 설명합니다.

기본적으로는 Django에서는 모든 템플릿이 모든 변수 태그의 출력을 자동으로 이스케이프합니다.구체적으로는, 다음의 5 문자는 이스케이프 됩니다.

- `<`로 변환됩니다.`<`
- `>`로 변환됩니다.`>`
- `'`(단일 따옴표)는 로 변환됩니다.`'`
- `"`(큰따옴표)는 로 변환됩니다.`"`
- `&`로 변환됩니다.`&`

이 동작은 디폴트로 유효하게 되어 있는 것을 강조합니다.장고의 템플릿 시스템을 사용하는 경우 보호됩니다.





### 끄는 방법

사이트별, 템플릿별 수준 또는 변수별 수준에서 데이터를 자동으로 이스케이프하지 않으려면 여러 가지 방법으로 데이터를 해제할 수 있습니다.

왜 끄려고 해?템플릿 변수에는 *원시* HTML로 렌더링하려는 데이터가 포함될 수 있습니다. 이 경우 템플릿 변수의 내용이 이스케이프되지 않도록 해야 합니다.예를 들어 HTML을 데이터베이스에 저장하고 이를 템플릿에 직접 포함하려고 할 수 있습니다.또는 Django의 템플릿 시스템을 사용하여 HTML이 *아닌* 텍스트(예: 이메일 메시지)를 생성할 수도 있습니다.



#### 개별 변수의 경우

개개의 변수에 대해 자동 이스케이프를 디세블로 하려면 , 다음의 필터를 사용합니다.

```
This will be escaped: {{ data }} This will not be escaped: {{ data safe }} 
```

*safe*는 더 *이상* 도망치지 *않기 위한* 줄임말이라고 생각하거나 *HTML로 해석*할 수 있습니다.이 예에서는,`data`포함하다`'<b>'`출력은 다음과 같습니다.

```
This will be escaped: &lt;b&gt; This will not be escaped: <b> 
```



#### 템플릿 블록의 경우

템플릿의 자동 이스케이프를 제어하려면 다음과 같이 템플릿(또는 템플릿의 특정 섹션)을 태그로 랩합니다.

```
{% autoescape off %}     Hello {{ name }} {% endautoescape %} 
```

태그는 다음 중 하나를 사용합니다.`on`또는`off`그 논거로서경우에 따라서는 자동 이스케이프가 비활성화되어 있는 경우에 자동 이스케이프를 강제적으로 실행할 수 있습니다.템플릿의 예를 다음에 나타냅니다.

```
Auto-escaping is on by default. Hello {{ name }}  {% autoescape off %}     This will not be auto-escaped: {{ data }}.      Nor this: {{ other_data }}     {% autoescape on %}         Auto-escaping applies again: {{ name }}     {% endautoescape %} {% endautoescape %} 
```

자동 이스케이프 태그는 모든 블록 태그와 마찬가지로 현재 태그를 확장하는 템플릿과 태그를 통해 포함된 템플릿에 효과를 전달합니다.예를 들어 다음과 같습니다.

```
base.html
{% autoescape off %} <h1>{% block title %}{% endblock %}</h1> {% block content %} {% endblock %} {% endautoescape %} 
child.html
{% extends "base.html" %} {% block title %}This &amp; that{% endblock %} {% block content %}{{ greeting }}{% endblock %} 
```

기본 템플릿에서는 자동 이스케이핑이 해제되어 있기 때문에 하위 템플릿에서도 해제되므로 다음과 같은 HTML이 렌더링됩니다.`greeting`변수는 문자열을 포함합니다.`<b>Hello!</b>`:

```
<h1>This &amp; that</h1> <b>Hello!</b> 
```

### 비고

일반적으로 템플릿 작성자는 자동 이스케이프에 대해 크게 걱정할 필요가 없습니다.Python 측의 개발자(뷰와 커스텀필터를 쓰는 사람)는 데이터를 이스케이프해서는 안 되는 경우를 생각하고 데이터를 적절히 마크하여 템플릿 내에서 Just Work할 필요가 있습니다.

자동 이스케이핑이 활성화되었는지 확실하지 않은 상황에서 사용할 수 있는 템플릿을 작성하는 경우 이스케이프가 필요한 변수에 필터를 추가합니다.자동 이스케이프가 켜져 있으면 필터가 데이터를 *이중* 이스케이프할 위험이 없습니다. 필터는 자동 이스케이프 변수에 영향을 주지 않습니다.



### 스트링 리터럴 및 자동 이스케이프

앞에서 설명한 바와 같이 필터 인수는 문자열이 될 수 있습니다.

```
{{ data default:"This is a string literal." }} 
```

모든 문자열 리터럴이 템플릿에 자동으로 이스케이프되지 않고 **삽입**됩니다.이러한 문자열 리터럴은 모두 필터를 통과한 것처럼 동작합니다.이 배경에는 템플릿 작성자가 문자열 리터럴에 들어가는 내용을 제어할 수 있기 때문에 템플릿 작성 시 텍스트가 올바르게 이스케이프되도록 할 수 있습니다.

이것은 당신이 글을 쓴다는 것을 의미합니다.

```
{{ data default:"3 &lt; 2" }} 
```

…대신:

```
{{ data default:"3 < 2" }}  {# Bad! Don't do this. #} 
```

이것은 변수 자체에서 발생하는 데이터에 영향을 주지 않습니다.템플릿 작성자가 제어할 수 없으므로 변수의 내용은 필요한 경우 자동으로 이스케이프됩니다.



## 메서드 호출 접근

오브젝트에 연결된 대부분의 메서드콜은 템플릿 내에서 사용할 수도 있습니다.즉, 템플릿은 뷰에서 전달되는 클래스 속성(필드 이름 등) 및 변수에만 액세스할 수 없습니다.예를 들어, Django ORM은 외부 키와 관련된 오브젝트 컬렉션을 검색하기 위한 ["entry_set"](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Ftopics%2Fdb%2Fqueries%2F%23topics-db-queries-related) 구문을 제공합니다.따라서 외부 키 관계가 있는 "comment"라는 모델과 "task"라는 모델을 지정하면 다음과 같이 특정 태스크에 첨부된 모든 코멘트를 루프할 수 있습니다.

```
{% for comment in task.comment_set.all %}     {{ comment }} {% endfor %} 
```

[마찬가지](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Fmodels%2Fquerysets%2F)로 QuerySet에서는`count()`포함된 개체 수를 카운트하는 메서드입니다.따라서 다음과 같이 현재 작업과 관련된 모든 코멘트의 수를 얻을 수 있습니다.

```
{{ task.comment_set.all.count }} 
```

자체 모델에 명시적으로 정의한 메서드에 액세스할 수도 있습니다.

```
models.py
class Task(models.Model):     def foo(self):         return "bar" 
template.html
{{ task.foo }} 
```

Django는 템플릿 언어로 사용할 수 있는 논리 처리량을 의도적으로 제한하기 때문에 템플릿 내에서 접근되는 메서드콜에 인수를 전달할 수 없습니다.데이터는 뷰에서 계산한 다음 표시할 템플릿으로 전달해야 합니다.



## 커스텀 태그 및 필터 라이브러리

특정 응용 프로그램은 사용자 지정 태그 및 필터 라이브러리를 제공합니다.템플릿으로 액세스하려면 응용 프로그램이 에 있는지 확인합니다(추가:`'django.contrib.humanize'`다음 예)를 사용하여 템플릿에서 태그를 사용합니다.

```
{% load humanize %}  {{ 45000 intcomma }} 
```

위의 경우 태그가 로드합니다.`humanize`태그 라이브러리가 있으면,`intcomma`사용할 수 있는 필터입니다.를 유효하게 했을 경우는, 관리자의 메뉴얼 영역을 참조하고, 인스톨의 커스텀 라이브러리의 리스트를 참조할 수 있습니다.

태그에는 공백으로 구분된 여러 라이브러리 이름을 사용할 수 있습니다.예:

```
{% load humanize i18n %} 
```

사용자 지정 템플릿 라이브러리 작성에 대한 자세한 내용은 사용자 [지정 템플릿 태그](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fhowto%2Fcustom-template-tags%2F) 및 [필터](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fhowto%2Fcustom-template-tags%2F)를 [생성하는 방법을 참조](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fhowto%2Fcustom-template-tags%2F)하십시오.



### 사용자 정의 라이브러리 및 템플릿 상속

커스텀 태그 또는 필터 라이브러리를 로드하면 태그/필터는 현재 템플릿에서만 사용할 수 있습니다.템플릿 상속 경로를 따라 부모 또는 자녀 템플릿에서는 사용할 수 없습니다.

예를 들어 템플릿이`foo.html`가지다`{% load humanize %}`, 자 템플릿(예:`{% extends "foo.html" %}`) 에서는, 커스터마이즈 템플릿 태그 및 필터에 액세스 할 수 *없습니다*.하위 템플릿이 자체 책임을 집니다.`{% load humanize %}`.

이는 유지보수성과 건전성을 위한 기능입니다.

## 개요

Python에서 템플릿 시스템을 사용하는 과정은 3단계로 이루어집니다.

1. You configure an [Engine](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fapi%2F#django.template.Engine) .
2. You compile template code into a [Template](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fapi%2F#django.template.Template) .
3. You render the template with a [Context](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fapi%2F#django.template.Context) .

일반적으로 Django 프로젝트는 템플릿 시스템의 하위 API가 아닌 [상위 수준의 백엔드에 의존](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Ftopics%2Ftemplates%2F%23template-engines)하지 않는 API에 의존하지 않는 API는 다음과 같습니다.

1. 설정의 각 백엔드에 대해 Django는 .를 인스턴스화하여 공통 템플릿 백엔드 API에 맞춥니다.
2. 이 모듈에서는 템플릿을 로드하는 등의 기능을 제공합니다.그들은 a를 반환한다.`django.template.backends.django.Template`실제를 감쌉니다.
3. 그`Template`에는 콘텍스트 및 요구를 에 정리하고 렌더링을 에 위임하는 방식이 있습니다.



## 엔진 설정

백엔드를 사용하고 있는 경우는, 이것은 찾고 있는 메뉴얼이 아닐 가능성이 있습니다.의 인스턴스`Engine`다음에 설명하는 클래스는`engine`이 백엔드의 Atribute 및 다음에 나타내는 Atribute Default는 에서 전달된 Atribute에 의해 덮어쓰게 됩니다.

- *학급* `Engine`(*dirs=**None*, *app_dirs=*False, *context_processors=**None*, debug*=**False*, *loaders**=**None*, *string_if_debug*='', *file_charset*='*utf-8',* *라이브러리=없음*, *빌트인=없음*, *자동* 이스케이프*=True*)

  의 인스턴스화 시`Engine`모든 인수는 키워드 인수로 전달해야 합니다.`dirs`는 엔진이 템플릿소스 파일을 검색하는 디렉토리 목록입니다.를 설정하기 위해서 사용합니다.기본값은 빈 목록입니다.`app_dirs`디폴트값에만 영향을 줍니다.`loaders`아래를 참조해 주세요.디폴트로는`False`.`autoescape`는 HTML 자동 이스케이핑이 활성화 되어 있는지 여부를 제어합니다.디폴트로는`True`.경고로만 설정`False`HTML 이외의 템플릿을 렌더링하는 경우!`context_processors`는 템플릿이 요구에 의해 렌더링될 때 컨텍스트에 입력하기 위해 사용되는 콜러블에 대한 도트 포함 Python 경로 목록입니다.이러한 콜러블은 요구 오브젝트를 인수로 하여 컨텍스트에 Marge되는 항목을 반환합니다.기본값은 빈 목록입니다.상세한 것에 대하여는, 을 참조해 주세요.`debug`는 템플릿 디버깅모드를 온/오프하는 부울입니다.그렇다면`True`템플릿 엔진에는 템플릿 렌더링 중에 발생한 예외에 대한 자세한 보고서를 표시하기 위해 사용할 수 있는 추가 디버깅 정보가 저장됩니다.디폴트로는`False`.`loaders`는 템플릿로더 클래스의 목록으로 문자열로 지정됩니다.각각`Loader`class는 특정 소스에서 템플릿을 Import하는 방법을 알고 있습니다.옵션으로 문자열 대신 태플을 사용할 수 있습니다.태플의 첫 번째 항목은`Loader`클래스 이름, 후속 항목이 에 전달됩니다.`Loader`초기화 중.기본적으로 다음 항목이 포함된 목록이 사용됩니다.

  `'django.template.loaders.filesystem.Loader'``'django.template.loaders.app_directories.Loader'`만약이라면`app_dirs`이`True`.그런 다음 로더를 로 감쌉니다.Django 4.1에서 변경:이전 버전에서는 캐시된 템플릿로더는 기본적으로 다음과 같은 경우에만 활성화되었습니다.`DEBUG`이었다`False`.자세한 내용은 [로더](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fapi%2F#template-loaders) 유형을 [참조](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fapi%2F#template-loaders)하십시오.`string_if_invalid`는 템플릿시스템이 비활성(철자 오류 등) 변수에 사용하는 문자열로서의 출력입니다.기본값은 빈 문자열입니다.자세한 내용은 [잘못된 변수](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fapi%2F#invalid-template-variables) 처리 [방법](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fapi%2F#invalid-template-variables)을 [참조](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fapi%2F#invalid-template-variables)하십시오.`file_charset`는 디스크상의 템플릿파일을 읽기 위해서 사용되는 문자 세트입니다.디폴트로는`'utf-8'`.`'libraries'`: 템플릿엔진에 등록할 템플릿태그 모듈의 라벨 및 닷이 있는 Python 경로 사전.새 라이브러리를 추가하거나 기존 라이브러리에 대한 대체 레이블을 제공하는 데 사용됩니다.예를 들어 다음과 같습니다.

  ```
  Engine(     libraries={         'myapp_tags': 'path.to.myapp.tags',         'admin.urls': 'django.contrib.admin.templatetags.admin_urls',     }, ) 
  ```

  라이브러리는 해당 사전 키를 태그에 전달하여 로드할 수 있습니다.`'builtins'`: [빌트인](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fbuiltins%2F)에 추가할 템플릿 태그 모듈의 도트 포함 Python 경로 목록입니다.예를 들어 다음과 같습니다.

  ```
  Engine(     builtins=['myapp.builtins'], ) 
  ```

  내장된 라이브러리의 태그 및 필터를 먼저 태그를 호출하지 않고 사용할 수 있습니다.

- *정적인* `Engine.``get_default`( )

  최초 설정된 엔진에서 기본을 반환합니다.엔진이 설정되어 있지 않은 경우에 상승합니다.글로벌하게 이용 가능한 암묵적으로 구성된 엔진에 의존하는 API를 보존하기 위해 필요합니다.다른 사용은 절대 권장되지 않습니다.

- `Engine.``from_string`(*code_code*)

  지정된 템플릿 코드를 컴파일하여 개체를 반환합니다.

- `Engine.``get_template`(*filename_name*)

  지정된 이름으로 템플릿을 로드하고 컴파일한 후 개체를 반환합니다.

- `Engine.``select_template`(*syslog_name_list*)

  마찬가지로 이름 목록을 가져와서 처음 발견된 템플릿을 반환합니다.



## 템플릿 로드

를 작성하려면 , 및 의 공장 출하시 메서드를 호출하는 것이 좋습니다.

설정이 엔진을 정의하는 Django 프로젝트에서는 를 직접 인스턴스화할 수 있습니다.두 개 이상의 엔진이 정의되어 있는 경우 첫 번째 엔진이 사용됩니다.

- *학급* `Template`

  이 반의 거주지는`django.template.Template`. 컨스트럭터는 raw 템플릿코드라는1개의 인수를 사용합니다.

```
from django.template import Template  template = Template("My name is {{ my_name }}.") 
```

비하인드

시스템은 raw 템플릿 코드를 한 번만 해석합니다. 즉,`Template`물건.이후 성능의 트리 구조로 내부에 저장됩니다.

구문 분석 자체도 상당히 빠릅니다.해석의 대부분은 1개의 콜을 통해1개의 짧은 정규 표현으로 이루어집니다.





## 콘텍스트 렌더링

컴파일된 객체가 있으면 해당 객체를 사용하여 컨텍스트를 렌더링할 수 있습니다.같은 템플릿을 재사용하여 다른 컨텍스트에서 여러 번 렌더링할 수 있습니다.

- *학급* `Context`(*dict_=없음*)

  의 작성자`django.template.Context`는 옵션의 인수(변수 이름을 변수 값에 사전 매핑)를 사용합니다.자세한 내용은 아래 [컨텍스트](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fapi%2F#playing-with-context) [개체 재생을 참조](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fapi%2F#playing-with-context)하십시오.

- `Template.``render`(*표준*)

  오브젝트 호출`render()`를 사용한 메서드를 사용하여 템플릿을 "채웁니다.

   

  ```
  >>> from django.template import Context, Template >>> template = Template("My name is {{ my_name }}.")  >>> context = Context({"my_name": "Adrian"}) >>> template.render(context) "My name is Adrian."  >>> context = Context({"my_name": "Dolores"}) >>> template.render(context) "My name is Dolores." 
  ```



### 변수 및 룩업

변수 이름은 임의의 문자(A-Z), 임의의 숫자(0-9), 밑줄(단, 밑줄로 시작해서는 안 됩니다) 또는 점으로 구성되어야 합니다.

템플릿 렌더링에서 점은 특별한 의미를 가집니다.변수 이름의 점은 **조회**를 나타냅니다.구체적으로는 템플릿시스템이 변수명의 닷을 검출하면 다음 순서로 검색을 시도합니다.

- 사전 검색.예:`foo["bar"]`
- 아트리뷰트 룩업예:`foo.bar`
- 리스트 인덱스 룩업예:`foo[bar]`

템플릿 표현에서 "bar"는 다음과 같습니다.`{{ foo.bar }}`는 리터럴 문자열로 해석되며 변수 "bar" 값이 템플릿 컨텍스트에 존재하는 경우 사용되지 않습니다.

템플릿 시스템은 작동하는 첫 번째 검색 유형을 사용합니다.단락 논리입니다.다음은 몇 가지 예입니다.

```
>>> from django.template import Context, Template >>> t = Template("My name is {{ person.first_name }}.") >>> d = {"person": {"first_name": "Joe", "last_name": "Johnson"}} >>> t.render(Context(d)) "My name is Joe."  >>> class PersonClass: pass >>> p = PersonClass() >>> p.first_name = "Ron" >>> p.last_name = "Nasty" >>> t.render(Context({"person": p})) "My name is Ron."  >>> t = Template("The first stooge in the list is {{ stooges.0 }}.") >>> c = Context({"stooges": ["Larry", "Curly", "Moe"]}) >>> t.render(c) "The first stooge in the list is Larry." 
```

변수의 어떤 부분이 호출 가능한 경우 템플릿시스템은 해당 변수의 호출을 시행합니다.예:

```
>>> class PersonClass2: ...     def name(self): ...         return "Samantha" >>> t = Template("My name is {{ person.name }}.") >>> t.render(Context({"person": PersonClass2})) "My name is Samantha." 
```

호출 가능한 변수는 직선 조회만 필요한 변수보다 약간 더 복잡합니다.다음은 유의해야 할 사항입니다.

- 변수가 호출 시 예외를 발생시키면 예외에 속성이 없는 한 예외가 전파됩니다.`silent_variable_failure`그 가치는`True`*예외*에 다음이 있는 경우`silent_variable_failure`값이 다음과 같은 속성`True`변수는 엔진의 값으로 렌더링됩니다.`string_if_invalid`설정 옵션(디폴트에서는 빈 문자열).예:

  ```
  >>> t = Template("My name is {{ person.first_name }}.") >>> class PersonClass3: ...     def first_name(self): ...         raise AssertionError("foo") >>> p = PersonClass3() >>> t.render(Context({"person": p})) Traceback (most recent call last): ... AssertionError: foo  >>> class SilentAssertionError(Exception): ...     silent_variable_failure = True >>> class PersonClass4: ...     def first_name(self): ...         raise SilentAssertionError >>> p = PersonClass4() >>> t.render(Context({"person": p})) "My name is ." 
  ```

  는 모든 Django 데이터베이스 API의 기본 클래스입니다.`DoesNotExist`예외, 있음`silent_variable_failure = True`장고 모델 오브젝트와 함께 장고 템플릿을 사용하는 경우`DoesNotExist`예외는 자동으로 실패합니다.

- 변수는 필수 인수가 없는 경우에만 호출할 수 있습니다.그렇지 않으면 시스템이 엔진의 값을 반환합니다.`string_if_invalid`선택.

- 일부 변수를 호출할 때 부작용이 발생할 수 있으며 템플릿 시스템이 이러한 변수에 액세스할 수 있도록 하는 것은 어리석거나 보안상의 구멍일 수 있습니다.

  좋은 예는 각 Django 모델 객체에 대한 메서드입니다.템플릿 시스템에서 다음과 같은 작업을 수행할 수 없습니다.

  ```
  I will now delete this valuable data. {{ data.delete }} 
  ```

  이 문제를 방지하려면`alters_data`Atribute를 지정합니다.템플릿 시스템은 변수가 다음과 같은 경우 변수를 호출하지 않습니다.`alters_data=True`set, 대신 변수를 로 바꿉니다.`string_if_invalid`, 무조건.Django 모델 객체의 동적 생성 및 메서드는`alters_data=True`자동으로.예:

  ```
  def sensitive_function(self):     self.database_record.delete() sensitive_function.alters_data = True 
  ```

- 경우에 따라서는 다른 이유로 이 기능을 해제하고 템플릿시스템에 어떤 경우에도 변수를 삭제하지 않도록 지시할 수 있습니다.그러기 위해서는,`do_not_call_in_templates`값을 사용하여 콜 가능한 Attribute on the callable`True`템플릿 시스템은 변수를 호출할 수 없는 것처럼 동작합니다(예를 들어 호출 가능한 속성에 액세스할 수 있습니다).



### 잘못된 변수 처리 방법

일반적으로 변수가 존재하지 않는 경우 템플릿 시스템은 엔진의 값을 삽입합니다.`string_if_invalid`설정 옵션(설정)`''`디폴트로는 (빈 문자열)입니다.

유효하지 않은 변수에 적용되는 필터는 다음 경우에만 적용됩니다.`string_if_invalid`로 설정되어 있다.`''`(빈 문자열).한다면`string_if_invalid`다른 값으로 설정되면 변수 필터는 무시됩니다.

이 동작은 에 따라 약간 다릅니다.`if`,`for`그리고.`regroup`템플릿 태그이러한 템플릿 태그 중 하나에 비활성 변수가 제공된 경우 변수는 다음과 같이 해석됩니다.`None`. 필터는 이러한 템플릿태그 내의 비활성 변수에 항상 적용됩니다.

한다면`string_if_invalid`를 포함합니다.`'%s'`형식 마커는 비활성 변수 이름으로 대체됩니다.

디버깅 전용!

하는 동안에`string_if_invalid`는 유용한 디버깅도구가 될 수 있으므로 '개발 기본값'으로 설정하는 것은 좋지 않습니다.

일부 Django를 포함한 많은 템플릿은 존재하지 않는 변수가 발생했을 때 템플릿시스템의 무음화에 의존합니다.다음 값을 할당하는 경우`''`로.`string_if_invalid`이러한 템플릿 및 사이트에서 렌더링 문제가 발생합니다.

일반적으로.`string_if_invalid`는 특정 템플릿 문제를 디버깅하기 위해서만 유효하게 하고 디버깅이 완료되면 클리어해야 합니다.



### 삽입 변수

모든 컨텍스트는 다음을 포함합니다.`True`,`False`그리고.`None`예상대로 이들 변수는 대응하는 Python 오브젝트로 해결됩니다.



### 문자열 리터럴 제한

Django의 템플릿 언어에는 자체 구문에 사용되는 문자를 피할 방법이 없습니다.예를 들어 태그는 다음과 같은 문자 시퀀스를 출력해야 하는 경우 필요합니다.`{%`그리고.`%}`.

이러한 시퀀스를 템플릿필터 또는 태그 인수에 포함할 경우에도 같은 문제가 발생합니다.예를 들어 블록 태그를 해석할 때 Django의 템플릿 파서는 첫 번째 항목을 찾습니다.`%}`잠시 후에`{%`.이것에 의해, 의 사용이 방지됩니다.`"%}"`문자열 리터럴로 사용합니다.예를 들어,`TemplateSyntaxError`는 다음 표현에 대해 발생합니다.

```
{% include "template.html" tvar="Some string literal with %} in it." %}  {% with tvar="Some string literal with %} in it." %}{% endwith %} 
```

필터 인수에 예약된 시퀀스를 사용하여 동일한 문제를 트리거할 수 있습니다.

```
{{ some.variable default:"}}" }} 
```

이러한 시퀀스와 함께 문자열을 사용해야 하는 경우 템플릿 변수에 저장하거나 사용자 지정 템플릿 태그 또는 필터를 사용하여 제한을 해결하십시오.



## 가지고 놀다`Context`오브젝트

대부분의 경우 완전히 채워진 사전을 전달하여 개체를 인스턴스화합니다.`Context()`단, 아이템을 추가 및 삭제할 수 있습니다.`Context`오브젝트도 표준 사전 구문을 사용하여 인스턴스화되면 다음과 같이 됩니다.

```
>>> from django.template import Context >>> c = Context({"foo": "bar"}) >>> c['foo'] 'bar' >>> del c['foo'] >>> c['foo'] Traceback (most recent call last): ... KeyError: 'foo' >>> c['newvariable'] = 'hello' >>> c['newvariable'] 'hello' 
```

- `Context.``get`(*키*, *그렇지* 않으면*=없음*)

  값을 반환합니다.`key`한다면`key`컨텍스트에 있습니다.그렇지 않으면 반환됩니다.`otherwise`.

- `Context.``setdefault`(*키*, 디폴트*=없음*)

  한다면`key`는 컨텍스트에 있습니다.그 값을 반환합니다.그렇지 않으면 삽입`key`의 가치를 지닌`default`및 반환`default`.

- `Context.``pop`( )

  

- `Context.``push`( )

  

- *예외.* `ContextPopException`

  

A `Context`object는 스택입니다.즉, 할 수 있습니다.`push()`그리고.`pop()`만약 당신이`pop()`너무 많으면 높아진다`django.template.ContextPopException`:

```
>>> c = Context() >>> c['foo'] = 'first level' >>> c.push() {} >>> c['foo'] = 'second level' >>> c['foo'] 'second level' >>> c.pop() {'foo': 'second level'} >>> c['foo'] 'first level' >>> c['foo'] = 'overwritten' >>> c['foo'] 'overwritten' >>> c.pop() Traceback (most recent call last): ... ContextPopException 
```

를 사용할 수도 있습니다.`push()`콘텍스트 매니저로서 일치시키는 것을 보증합니다.`pop()`호출됩니다.

```
>>> c = Context() >>> c['foo'] = 'first level' >>> with c.push(): ...     c['foo'] = 'second level' ...     c['foo'] 'second level' >>> c['foo'] 'first level' 
```

모든 인수가 전달됨`push()`에 전달됩니다.`dict`새 컨텍스트 수준을 구축하는 데 사용되는 생성자.

```
>>> c = Context() >>> c['foo'] = 'first level' >>> with c.push(foo='second level'): ...     c['foo'] 'second level' >>> c['foo'] 'first level' 
```

- `Context.``update`(*기타_기타*)

  

에 더하여`push()`그리고.`pop()`,그`Context`오브젝트도 정의한다.`update()`방법.이건 마치`push()`그러나 사전을 인수로 사용하여 해당 사전을 빈 사전 대신 스택에 푸시합니다.

```
>>> c = Context() >>> c['foo'] = 'first level' >>> c.update({'foo': 'updated'}) {'foo': 'updated'} >>> c['foo'] 'updated' >>> c.pop() {'foo': 'updated'} >>> c['foo'] 'first level' 
```

맘에 들다`push()`, 를 사용할 수 있습니다.`update()`콘텍스트 매니저로서 일치시키는 것을 보증합니다.`pop()`호출됩니다.

```
>>> c = Context() >>> c['foo'] = 'first level' >>> with c.update({'foo': 'second level'}): ...     c['foo'] 'second level' >>> c['foo'] 'first level' 
```

사용방법`Context`[일부 커스텀 템플릿](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fhowto%2Fcustom-template-tags%2F%23howto-writing-custom-template-tags) [태그](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fhowto%2Fcustom-template-tags%2F%23howto-writing-custom-template-tags)에서는 스택이 편리합니다.

- `Context.``flatten`( )

  

사용.`flatten()`통째로 얻을 수 있는 방법`Context`스택을 하나의 사전으로 만듭니다(내장 포함)으로 만듭니다.

```
>>> c = Context() >>> c['foo'] = 'first level' >>> c.update({'bar': 'second level'}) {'bar': 'second level'} >>> c.flatten() {'True': True, 'None': None, 'foo': 'first level', 'False': False, 'bar': 'second level'} 
```

A `flatten()`방법은 내부에서도 사용됩니다.`Context`동등한 오브젝트

```
>>> c1 = Context() >>> c1['foo'] = 'first level' >>> c1['bar'] = 'second level' >>> c2 = Context() >>> c2.update({'bar': 'second level', 'foo': 'first level'}) {'foo': 'first level', 'bar': 'second level'} >>> c1 == c2 True 
```

으로부터 결과가 나온`flatten()`비교하기 위해 단위 테스트에서 유용할 수 있습니다.`Context`그에 반대하여`dict`:

```
class ContextTest(unittest.TestCase):     def test_against_dictionary(self):         c1 = Context()         c1['update'] = 'value'         self.assertEqual(c1.flatten(), {             'True': True,             'None': None,             'False': False,             'update': 'value',         }) 
```



### 사용.`RequestContext`

- *학급* `RequestContext`(*요구*, *dict_=없음*, *프로세서=없음*)

  

장고는 스페셜과 함께 제공됩니다.`Context`학급,`django.template.RequestContext`일반과 약간 다르게 동작하는 경우`django.template.Context`첫 번째 차이점은 첫 번째 인수로 a를 사용한다는 것입니다.예를 들어 다음과 같습니다.

```
c = RequestContext(request, {     'foo': 'bar', }) 
```

두 번째 차이점은 엔진의 성능에 따라 컨텍스트를 몇 가지 변수로 자동으로 채운다는 것입니다.`context_processors`설정 옵션.

그`context_processors`option은 요구 객체를 인수로 사용하여 컨텍스트에 Marge할 항목의 사전을 반환하는 콜러블(**콘텍스트프로세서**) **목록**입니다.기본 생성된 설정 파일에서 기본 템플릿엔진에는 다음 컨텍스트프로세서가 포함되어 있습니다.

```
[     'django.template.context_processors.debug',     'django.template.context_processors.request',     'django.contrib.auth.context_processors.auth',     'django.contrib.messages.context_processors.messages', ] 
```

이러한 것 외에, 는 항상`'django.template.context_processors.csrf'`관리자 및 기타 기여 앱에 필요한 보안 관련 컨텍스트프로세서입니다만, 잘못 설정되었을 경우, 이 프로세서는 의도적으로 하드 코드 되어 있기 때문에, 에서는 끌 수 없습니다.`context_processors`선택.

각 프로세서는 순서대로 적용됩니다.즉, 한 프로세서가 콘텍스트에 변수를 추가하고 두 번째 프로세서가 같은 이름의 변수를 추가하면 두 번째 프로세서가 첫 번째 프로세서를 덮어씁니다.디폴트 프로세서는 다음과 같습니다.

컨텍스트 프로세서가 적용되는 경우

콘텍스트 프로세서는 콘텍스트 데이터 위에 적용됩니다.즉, 콘텍스트프로세서가 또는 에 제공한 변수를 덮어쓸 수 있으므로 콘텍스트프로세서가 지정한 변수 이름과 중복되지 않도록 주의하십시오.

콘텍스트 데이터를 콘텍스트프로세서보다 우선하는 경우는, 다음의 패턴을 사용합니다.

```
from django.template import RequestContext  request_context = RequestContext(request) request_context.push({"my_name": "Adrian"}) 
```

이를 통해 및 등의 API에서 컨텍스트데이터가 컨텍스트프로세서를 덮어쓸 수 있게 됩니다.

또한 옵션의 세 번째 positional 인수를 사용하여 추가 프로세서의 목록을 제공할 수 있습니다.`processors`이 예에서는 인스턴스가`ip_address`변수:

```
from django.http import HttpResponse from django.template import RequestContext, Template  def ip_address_processor(request):     return {'ip_address': request.META['REMOTE_ADDR']}  def client_ip_view(request):     template = Template('{{ title }}: {{ ip_address }}')     context = RequestContext(request, {         'title': 'Your IP Address',     }, [ip_address_processor])     return HttpResponse(template.render(context)) 
```



### 빌트인 템플릿콘텍스트 프로세서

각 빌트인 프로세서의 기능은 다음과 같습니다.



#### `django.contrib.auth.context_processors.auth`

- `auth`(*요구*)

  

이 프로세서가 유효하게 되어 있는 경우,`RequestContext`에는 다음 변수가 포함됩니다.

- `user`– AN`auth.User`현재 로그인한 사용자를 나타내는 인스턴스(또는`AnonymousUser`instance(클라이언트가 로그인하지 않은 경우).
- `perms`– 의 인스턴스`django.contrib.auth.context_processors.PermWrapper`현재 로그인한 사용자가 가지고 있는 권한을 나타냅니다.



#### `django.template.context_processors.debug`

- `debug`(*요구*)

  

이 프로세서가 유효하게 되어 있는 경우,`RequestContext`이 2개의 변수가 포함됩니다.단, 설정이 다음과 같이 설정되어 있는 경우에만`True`및 요청의 IP 주소(`request.META['REMOTE_ADDR']`)은, 다음과 같이 설정되어 있습니다.

- `debug`–`True`. 템플릿에서 이 기능을 사용하여 모드 여부를 테스트할 수 있습니다.
- `sql_queries`– 리스트`{'sql': ..., 'time': ...}`사전 - 요청 중에 지금까지 수행된 모든 SQL 쿼리와 소요 시간을 나타냅니다.목록은 데이터베이스 에일리어스, 쿼리 순으로 정렬됩니다.액세스 시 느릿느릿 생성됩니다.



#### `django.template.context_processors.i18n`

- `i18n`(*요구*)

  

이 프로세서가 유효하게 되어 있는 경우,`RequestContext`에는 다음 변수가 포함됩니다.

- `LANGUAGES`– 설정의 값.
- `LANGUAGE_BIDI`–`True`현재 언어가 오른쪽에서 왼쪽(예: 히브리어, 아랍어) 언어인 경우. `False`왼쪽에서 오른쪽 언어(예: 영어, 프랑스어, 독일어)인 경우
- `LANGUAGE_CODE`–`request.LANGUAGE_CODE`(존재하는 경우).그렇지 않으면 설정 값입니다.

동일한 값을 생성하는 템플릿 태그에 대해서는 [i18n 템플릿](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Ftopics%2Fi18n%2Ftranslation%2F%23i18n-template-tags) 태그를 참조하십시오.



#### `django.template.context_processors.media`

이 프로세서가 유효하게 되어 있는 경우,`RequestContext`변수가 포함됩니다.`MEDIA_URL`설정 값을 제공합니다.



#### `django.template.context_processors.static`

- `static`(*요구*)

  

이 프로세서가 유효하게 되어 있는 경우,`RequestContext`변수가 포함됩니다.`STATIC_URL`설정 값을 제공합니다.



#### `django.template.context_processors.csrf`

[이](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Fcsrf%2F) 프로세서는 사이트 간 [요청 위조](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Fcsrf%2F)로부터 [보호](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Fcsrf%2F)하기 위해 템플릿 태그에 필요한 토큰을 추가합니다.



#### `django.template.context_processors.request`

이 프로세서가 유효하게 되어 있는 경우,`RequestContext`변수가 포함됩니다.`request`(이것은 current 입니다).



#### `django.template.context_processors.tz`

- `tz`(*요구*)

  

이 프로세서가 유효하게 되어 있는 경우,`RequestContext`변수가 포함됩니다.`TIME_ZONE`현재 액티브한 타임존의 이름을 나타냅니다.



#### `django.contrib.messages.context_processors.messages`

이 프로세서가 유효하게 되어 있는 경우,`RequestContext`에는 다음 두 가지 변수가 포함됩니다.

- `messages`– [메시지 프레임워크](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Fcontrib%2Fmessages%2F)를 통해 설정된 메시지 목록(문자열).
- `DEFAULT_MESSAGE_LEVELS`– 메시지레벨명과 [수치](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Fcontrib%2Fmessages%2F%23message-level-constants)와의 [매핑](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Fcontrib%2Fmessages%2F%23message-level-constants)



### 독자적인 콘텍스트프로세서 쓰기

콘텍스트프로세서에는, 다음의 간단한 인터페이스가 있습니다.Python 함수는 하나의 인수, 오브젝트를 사용하여 템플릿 컨텍스트에 추가된 사전을 반환하는 함수입니다.

예를 들어, 모든 콘텍스트에 설정을 추가하려면 , 다음의 순서를 실행합니다.

```
from django.conf import settings  def from_email(request):     return {         "DEFAULT_FROM_EMAIL": settings.DEFAULT_FROM_EMAIL,     } 
```

커스텀 콘텍스트 프로세서는, 코드 베이스내의 어느 장소에서도 사용할 수 있습니다.Django가 신경 쓰는 것은 커스텀콘텍스트 프로세서가`'context_processors'`옵션 - 또는`context_processors`직접 사용하는지에 대한 논쟁입니다.



## 템플릿 로드 중

일반적으로 낮은 수준의 API를 직접 사용하는 대신 파일 시스템의 파일에 템플릿을 저장합니다.**템플릿** 디렉토리로 지정된 디렉토리에 템플릿을 저장합니다.

Django는 템플리트 로드 설정에 따라 여러 위치에서 템플리트 디렉토리를 검색하지만(아래 "로더 유형" 참조), 템플리트 디렉토리를 지정하는 가장 기본적인 방법은 이 옵션을 사용하는 것입니다.



### 옵션

설정 파일의 설정 옵션을 사용하여 템플릿디렉토리의 내용을 Django에게 알립니다.또는`dirs`의 인수이것은 템플릿디렉토리에의 풀 패스를 포함한 문자열의 리스트로 설정할 필요가 있습니다.

```
TEMPLATES = [     {         'BACKEND': 'django.template.backends.django.DjangoTemplates',         'DIRS': [             '/home/html/templates/lawrence.com',             '/home/html/templates/default',         ],     }, ] 
```

디렉토리와 템플리트를 웹 서버에서 읽을 수 있는 경우 템플리트는 원하는 위치로 이동할 수 있습니다.원하는 확장자를 사용할 수 있습니다.`.html`또는`.txt`또는 확장자를 전혀 사용할 수 없습니다.

이러한 경로에서는 Windows 상에서도 Unix 스타일의 정방향 슬래시를 사용해야 합니다.



### 로더 타입

기본적으로는 Django는 파일 시스템 기반 템플릿로더를 사용하지만, Django에는 다른 소스에서 템플릿을 로드하는 방법을 알고 있는 몇 가지 다른 템플릿로더가 포함되어 있습니다.

이러한 다른 로더의 일부는 디폴트로 디세블로 되어 있습니다만, 이 로더를 액티브하게 하려면 ,`'loaders'`선택 사항`DjangoTemplates`백엔드 설정 또는 패스`loaders`에의 인수.`loaders`는 문자열 또는 튜플 목록이어야 합니다.여기서 각각은 템플릿로더 클래스를 나타냅니다.Django와 함께 제공되는 템플릿로더는 다음과 같습니다.

```
django.template.loaders.filesystem.Loader
```

- *학급* `filesystem.``Loader`

  에 따라 파일시스템에서 템플릿을 로드합니다.이 로더는 기본적으로 활성화되어 있습니다.그러나 비어 있지 않은 목록으로 설정할 때까지 템플릿을 찾을 수 없습니다.`TEMPLATES = [{     'BACKEND': 'django.template.backends.django.DjangoTemplates',     'DIRS': [BASE_DIR / 'templates'], }] `덮어쓸 수도 있습니다.`'DIRS'`특정 파일 시스템로더의 특정 디렉토리를 지정합니다.`TEMPLATES = [{     'BACKEND': 'django.template.backends.django.DjangoTemplates',     'OPTIONS': {         'loaders': [             (                 'django.template.loaders.filesystem.Loader',                 [BASE_DIR / 'templates'],             ),         ],     }, }] `

```
django.template.loaders.app_directories.Loader
```

- *학급* `app_directories.``Loader`

  파일 시스템의 Django 앱에서 템플릿을 로드합니다.로더는 의 각 앱에 대해`templates`서브 디렉토리디렉토리가 존재하는 경우, Django는 그 디렉토리에서 템플릿을 찾습니다.즉, 개별 앱과 함께 템플릿을 저장할 수 있습니다.기본 템플릿을 사용하여 Django 앱을 배포할 수도 있습니다.예를 들어, 이 설정의 경우:`INSTALLED_APPS = ['myproject.polls', 'myproject.music'] `…그러면`get_template('foo.html')`찾을 것이다`foo.html`다음 디렉토리에서 다음 순서로 지정합니다.`/path/to/myproject/polls/templates/``/path/to/myproject/music/templates/`먼저 발견한 것을 사용합니다.의 순서는 중요합니다!예를 들어, Django 관리자를 커스터마이즈하는 경우 표준을 재정의하도록 선택할 수 있습니다.`admin/base_site.html`템플릿, 발신기지`django.contrib.admin`, 사용자 자신의`admin/base_site.html`에`myproject.polls`그 후, 그 다음, 다음의 조작을 실시할 필요가 있습니다.`myproject.polls`*보다* 우선하다`django.contrib.admin`그 이외의 경우`django.contrib.admin`가 먼저 로드되고 사용자의 것은 무시됩니다.로더는 처음 실행될 때 최적화를 수행합니다. 로더는 다음 패키지의 목록을 캐시합니다.`templates`서브 디렉토리로더를 유효하게 하려면 , 다음과 같이 설정합니다.`True`:`TEMPLATES = [{     'BACKEND': 'django.template.backends.django.DjangoTemplates',     'APP_DIRS': True, }] `

```
django.template.loaders.cached.Loader
```

- *학급* `cached.``Loader`

  Django 템플릿 시스템은 매우 빠르지만 템플릿이 렌더링될 때마다 템플릿을 읽고 컴파일해야 하는 경우 그에 따른 오버헤드가 가중될 수 있습니다.캐시된 템플릿로더를 랩할 다른 로더 목록과 함께 설정합니다.래핑된 로더는 처음 발견된 알 수 없는 템플릿을 찾는 데 사용됩니다.그런 다음 캐시된 로더는 컴파일된 파일을 저장합니다.`Template`기억 속에.캐시된`Template`동일한 템플릿을 로드하는 후속 요구에 대해 인스턴스가 반환됩니다.이 로더는 지정되지 않은 경우 자동으로 활성화됩니다.다음과 같은 설정을 사용하여 일부 커스텀템플릿 로더를 사용하여 템플릿캐싱을 수동으로 지정할 수 있습니다.`TEMPLATES = [{     'BACKEND': 'django.template.backends.django.DjangoTemplates',     'DIRS': [BASE_DIR / 'templates'],     'OPTIONS': {         'loaders': [             ('django.template.loaders.cached.Loader', [                 'django.template.loaders.filesystem.Loader',                 'django.template.loaders.app_directories.Loader',                 'path.to.custom.Loader',             ]),         ],     }, }] `참고내장된 모든 Django 템플릿 태그는 캐시된 로더와 함께 사용해도 안전하지만, 서드파티 패키지에서 온 커스텀템플릿 태그를 사용하거나 사용자가 직접 작성한 경우,`Node`각 태그의 실장은 스레드 세이프입니다.자세한 내용은 [템플릿태그 스레드](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fhowto%2Fcustom-template-tags%2F%23template-tag-thread-safety)안전에 [관한](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fhowto%2Fcustom-template-tags%2F%23template-tag-thread-safety) 고려사항을 [참조](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fhowto%2Fcustom-template-tags%2F%23template-tag-thread-safety)해 주세요.Django 4.1에서 변경:캐시된 템플릿로더는 항상 활성화되었습니다.`OPTIONS['loaders']`를 지정하지 않았습니다.이전에는, 다음의 경우에 유효하게 되어 있었습니다.`DEBUG`이었다`False`.

```
django.template.loaders.locmem.Loader
```

- *학급* `locmem.``Loader`

  Python 사전에서 템플릿을 로드합니다.이것은 테스트에 도움이 됩니다.이 로더는 템플릿 사전을 첫 번째 인수로 사용합니다.`TEMPLATES = [{     'BACKEND': 'django.template.backends.django.DjangoTemplates',     'OPTIONS': {         'loaders': [             ('django.template.loaders.locmem.Loader', {                 'index.html': 'content here',             }),         ],     }, }] `이 로더는 기본적으로 비활성화되어 있습니다.

Django는 템플릿로더를 에 따라 순서대로 사용합니다.`'loaders'`선택.로더가 일치 항목을 찾을 때까지 각 로더를 사용합니다.



## 커스텀 로더

커스텀 템플릿로더를 사용하여 추가 소스에서 템플릿을 로드할 수 있습니다.관습`Loader`클래스는 에서 상속해야 합니다.`django.template.loaders.base.Loader`정의하다`get_contents()`그리고.`get_template_sources()`방법들.



### 로더 방식

- *학급* `Loader`

  파일 시스템이나 데이터베이스와 같은 지정된 원본에서 템플릿을 로드합니다.`get_template_sources`(*filename_name*)를 필요로 하는 방법`template_name`가능한 소스별로 인스턴스를 생성합니다.예를 들어, 파일 시스템 로더가 수신할 수 있습니다.`'index.html'`로서`template_name`논쟁.이 방법은 전체 경로의 기원을 산출합니다.`index.html`로더가 보는 각 템플릿 디렉토리에 표시됩니다.메서드는 템플릿이 지정된 경로에 존재하는지 확인할 필요는 없지만 경로가 유효한지 확인해야 합니다.예를 들어 파일 시스템 로더는 경로가 유효한 템플릿 디렉토리에 있는지 확인합니다.`get_contents`(*표준*)지정된 인스턴스의 템플릿 내용을 반환합니다.파일 시스템 로더가 파일 시스템에서 내용을 읽거나 데이터베이스 로더가 데이터베이스에서 내용을 읽습니다.일치하는 템플릿이 존재하지 않으면 오류가 발생합니다.`get_template`(*skip_name*, *skip=None*)a를 반환한다.`Template`소정의 목적`template_name`를 호출하여 결과를 루프합니다.그러면 첫 번째 일치하는 템플릿이 반환됩니다.템플릿을 찾을 수 없는 경우 가 발생합니다.옵션`skip`인수는 템플릿을 확장할 때 무시할 원본 목록입니다.이를 통해 템플릿은 동일한 이름의 다른 템플릿을 확장할 수 있습니다.또한 재귀 오류를 방지하기 위해 사용됩니다.일반적으로 커스텀템플릿 로더의 경우 및 을 정의하는 것으로 충분합니다. `get_template()`일반적으로 덮어쓸 필요가 없습니다.

독자적인 구축

예를 들어, [Django의 내장 로더의 소스 코드](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fgithub.com%2Fdjango%2Fdjango%2Fblob%2Fmain%2Fdjango%2Ftemplate%2Floaders)를 읽어 보십시오.



## 템플릿 생성원

템플릿에는`origin`로딩된 소스에 따라 속성이 포함됩니다.

- *학급* `Origin`(*이름*, *template_name=**없음*, 로더*=없음*)

  `name`템플릿 로더에 의해 반환되는 템플릿의 경로.파일 시스템에서 읽는 로더의 경우 템플릿에 대한 전체 경로입니다.템플릿 로더가 아닌 템플릿이 직접 인스턴스화되는 경우, 이것은 다음 문자열 값입니다.`<unknown_source>`.`template_name`템플릿 로더에 전달된 템플릿의 상대 경로.템플릿 로더가 아닌 템플릿이 직접 인스턴스화되는 경우, 이는 다음과 같습니다.`None`.`loader`이를 구성한 템플릿로더 인스턴스`Origin`.템플릿 로더가 아닌 템플릿이 직접 인스턴스화되는 경우, 이는 다음과 같습니다.`None`.[`django.template.loaders.cached.Loader`](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fdocs.djangoproject.com%2Fko%2F4.1%2Fref%2Ftemplates%2Fapi%2F#django.template.loaders.cached.Loader) 이 Atribute를 설정하기 위해서는 랩된 모든 로더가 필요합니다.일반적으로 이 Atribute를 인스턴스화함으로써`Origin`와 함께`loader=self`.





다음 섹션에서 탬플릿과 context 변수에 대해 더 다루도록 하겠습니다. 이제 탬플릿을 생성하여 사용자들에게 실제로 무언가를 표시해 봅시다!

### [탬플릿(Template)](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Home_page#탬플릿template)

탬플릿은 파일(HTML 페이지 같은)의 구조(structure)나 배치(layout)을 정의하는 텍스트 파일입니다. 탬플릿은 실제 내용물(content)를 나타내기 위해 플레이스홀더(placeholder)들을 사용합니다. 장고는 당신의 어플리케이션 안에서 'templates' 라고 이름지어진 경로 안에서 자동적으로 탬플릿들을 찾을 것입니다. 예를 들어서, 우리가 방금 추가한 색인(index) 뷰 안에서, `render()` 함수는 **/locallibrary/catalog/templates/** 경로 안에서** *index.html* ***파일을 찾으려 할 것이고, 파일이 없다면 에러를 표시할 것입니다. 이것은 이전의 변경점들을 저장하고 브라우저에서 `127.0.0.1:8000`으로 접근해서 확인할 수 있습니다 - 이것은 다른 세부 사항들과 함께 상당히 직관적인 오류 메세지를 표시할 것입니다 : "`TemplateDoesNotExist at /catalog/`".*

**참고:** **주의:** 프로젝트의 settings 파일에 기초해서, 장고는 여러 장소에서 탬플릿들을 찾아볼 것입니다. 기본적으로는 설치된 어플리케이션에서 검색합니다. 장고가 어떻게 탬플릿들을 찾는지, 그리고 어떤 탬플릿 양식(format)들을 지원하는지에 관해 여기([Templates](https://docs.djangoproject.com/en/2.0/topics/templates/) (Django docs))에서 찾아볼 수 있습니다.

#### 탬플릿 확장(extend)하기

색인(index) 팀플릿은 head 및 body를 위해 표준 HTML 마크업이 필요할 것입니다. 우리가 아직 생성하지 않은 사이트들의 다른 페이지들을 향한 링크를 걸기 위한 탐색(navigation) 섹션도 필요하고요. 그리고 소개 텍스트 및 책 데이터를 표시하는 섹션 또한 필요합니다. 대부분의 HTML과 탐색 구조는 사이트의 모든 페이지에서 동일할 것입니다. 모든 페이지마다 똑같은 코드를 복사하는 대신, 기본 템플릿을 선언하기 위해 장고 탬플릿 언어(Django templating language)를 사용하고, 탬플릿을 확장하여 각각의 페이지 마다 다른 부분들만을 대체(replace)할 수 있습니다.

아래 코드 조각은 **base_generic.html** 파일의 기본 탬플릿 샘플입니다. 이 샘플은 제목, 사이드바를 위한 섹션과 이름이 지정된 `block` 및 `endblock` 탬플릿 태그(굵게 표시)가 마크된 주요 내용(main contents)들이 포함된 일반적인 HTML을 포함합니다. 블럭(block)들을 비워두거나, 또는 탬플릿에서 파생된 페이지들을 렌더링할 때 사용할 기본 내용을 포함할 수 있습니다.

**참고:** **주의:** 탬플릿 태그들은 목록을 반복하거나, 변수 값을 기반으로 조건부 연산을 수행하거나, 여타 다른 일들을 할 수 있는 함수입니다. 탬플릿 태그 외에도 탬플릿 구문(syntax)을 사용하면 view에서 탬플릿으로 전달된 변수들을 참조할 수 있고, 탬플릿 필터(filters)를 사용해서 변수의 형식을 지정할 수 있습니다(예를 들어, 문자열을 소문자로 변환).

```
<!DOCTYPE html>
<html lang="en">
<head>
  {% block title %}<title>Local Library</title>{% endblock %}
</head>
<body>
  {% block sidebar %}<!-- insert default navigation text for every page -->{% endblock %}
  {% block content %}<!-- default content text (typically empty) -->{% endblock %}
</body>
</html>
```

Copy to Clipboard

특정한 view를 위해 탬플릿을 정의할 땐, 먼저 `extends` 탬플릿 태그를 이용하여 기본 탬플릿을 지정합니다 — 아래 코드 샘플을 참조하세요. 그리고 나서 기본 탬플릿에서와 같이 `block`/`endblock` 섹션들을 이용해서 대체할 탬플릿의 섹션들을 선언합니다(있을 경우).

예를 들어, 아래 코드 조각은 extends 탬플릿 태그의 사용 및 content 블럭(block)을 재정의하는 방법을 보여줍니다. 생성된 HTML은 기본 탬플릿에서 정의된 코드와 구조를 포함할 것입니다(`title` 블럭에서 정의한 기본 내용은 포함하지만, 기본 `contents` 블럭 대신 새로운 `contents` 블럭 포함).

```
{% extends "base_generic.html" %}

{% block content %}
  <h1>Local Library Home</h1>
  <p>Welcome to LocalLibrary, a website developed by <em>Mozilla Developer Network</em>!</p>
{% endblock %}
```

Copy to Clipboard

#### LocalLibrary 기본 탬플릿

우리는 아래 코드 조각을 LocalLibrary 웹사이트의 베이스 탬플릿으로 사용할 것입니다. 보시는 바와 같이, 이것은 HTML 코드를 조금 포함하고 `title`, `sidebar` 그리고 `content` 블럭을 정의합니다. 우리는 기본 제목과 모든 책들 및 저자들에 대한 링크를 갖고 있는 기본 사이드바를 갖고 있습니다. 둘 다 미래에 쉽게 변경하기 위해 블럭들 안에 묶여 있습니다.

**참고:** **주의**: 우리는 또한 두 개의 추가적인 탬플릿 태그를 소개합니다: `url` 과 `load static`. 이 태그들은 아래 섹션들에서 설명될 것입니다.

새로운 파일 **base_generic.html** 을 **/locallibrary/catalog/templates/\*base_generic.html\*** 경로 안에 생성해서 아래 코드를 파일에 복사 붙여넣기 하세요:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  {% block title %}<title>Local Library</title>{% endblock %}
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
  <!-- Add additional CSS in static file -->
  {% load static %}
  <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>
<body>
  <div class="container-fluid">
    <div class="row">
      <div class="col-sm-2">
      {% block sidebar %}
        <ul class="sidebar-nav">
          <li><a href="{% url 'index' %}">Home</a></li>
          <li><a href="">All books</a></li>
          <li><a href="">All authors</a></li>
        </ul>
     {% endblock %}
      </div>
      <div class="col-sm-10 ">{% block content %}{% endblock %}</div>
    </div>
  </div>
</body>
</html>
```

Copy to Clipboard

탬플릿에는 HTML 페이지의 레이아웃과 프리젠테이션을 개선하기 위한 [Bootstrap](http://getbootstrap.com/) 의 CSS가 포함되어 있습니다. 부스트스트랩(또는 다른 클라이언트-사이드 웹 프레임워크)를 사용해서 서로 다른 크기의 화면에서도 잘 표시되는 매력적인 페이지를 빠르게 만들 수 있습니다.

또한 기본 탬플릿은 추가적인 꾸미기(styling)를 제공하는 로컬 css 파일(styles.css)을 참조합니다. **styles.css** 파일을 **/locallibrary/catalog/static/css/** 경로 안에 생성하고 아래 코드를 파일 안에 복사 붙여넣기 하세요:

```
.sidebar-nav {
    margin-top: 20px;
    padding: 0;
    list-style: none;
}
```

Copy to Clipboard

#### 색인(index) 탬플릿

새로운 HTML 파일 **index.html** 을 **/locallibrary/catalog/templates/** 경로 안에 생성해서 아래 코드를 파일 안에 복사 붙여넣기 하세요. 보시는 바와 같이 첫째 행에서 우리의 기본 탬플릿을 확장하고, 탬플릿의 기본 `content` 블럭을 새로운 블럭으로 대체합니다.

```python
{% extends "base_generic.html" %}

{% block content %}
  <h1>Local Library Home</h1>
  <p>Welcome to LocalLibrary, a website developed by <em>Mozilla Developer Network</em>!</p>
  <h2>Dynamic content</h2>
  <p>The library has the following record counts:</p>
  <ul>
    <li><strong>Books:</strong> {{ num_books }}</li>
    <li><strong>Copies:</strong> {{ num_instances }}</li>
    <li><strong>Copies available:</strong> {{ num_instances_available }}</li>
    <li><strong>Authors:</strong> {{ num_authors }}</li>
  </ul>
{% endblock %}
```

Copy to Clipboard

동적 콘텐츠 섹션에서 우리는 우리가 포함하고 싶은 view의 정보를 위한 플레이스홀더(탬플릿 변수)를 선언합니다. 이 변수들은 코드 샘플에서 굵게 표시된 것과 같이 이중 중괄호로(핸들 바)로 묶입니다.

**참고:** **주의:** 탬플릿 변수와 탬플릿 태그(함수)들을 쉽게 알 수 있습니다 - 변수들은 이중 중괄호로 감싸여져 있고(`{{ num_books }}`) , 태그들은 퍼센트 기호와 단일 중괄호로 감싸여 있습니다(`{% extends "base_generic.html" %}`).

여기서 주의해야 할 중요한 것은 변수들의 이름은 열쇠(key)들로 정해진다는 것입니다. 이 열쇠(key)들은 우리의 view의 `render()`함수 안의 `context` 사전(dictionary)로 전달하는 열쇠입니다(아래를 확인하세요). 변수들은 탬플릿이 렌더링 될 때 그것들과 연관된 값들로 대체될 것입니다.

```python
context = {
    'num_books': num_books,
    'num_instances': num_instances,
    'num_instances_available': num_instances_available,
    'num_authors': num_authors,
}

return render(request, 'index.html', context=context)
```

Copy to Clipboard

#### Templates 에 정적 파일 참조하기(referencing)

당신의 프로젝트는 자바스크립트, CSS 그리고 이미지를 포함하는 정적 리소스들을 사용할 가능성이 높습니다. 이 파일들의 위치가 알 수 없기 때문에(또는 바뀔 수 있기 때문에), 장고는 `STATIC_URL` 전역 설정을 기준으로 탬플릿에서의 위치를 특정할 수 있도록 합니다. 기본 뼈대 웹사이트(skeleton website)는 `STATIC_URL`의 값을 '`/static/`'으로 설정하지만, 당신은 이것들을 콘텐츠 전달 네트워크(content delivery network)나 다른 곳에서 호스트할 수도 있습니다.

아래 코드 샘플처럼, 탬플릿 안에서 당신은 먼저 탬플릿 라이브러리를 추가하기 위해 "static"을 지정하는 `load` 탬플릿 태그를 호출합니다. 그러고 나서 `static` 탬플릿 태그를 사용할 수 있고 관련 URL을 요구되는 파일에 지정할 수 있습니다.

```python
<!-- Add additional CSS in static file -->
{% load static %}
<link rel="stylesheet" href="{% static 'css/styles.css' %}">
```

Copy to Clipboard

비슷한 방법으로 이미지를 페이지에 추가할 수 있습니다. 예를 들어:

```python
{% load static %}
<img src="{% static 'catalog/images/local_library_model_uml.png' %}" alt="UML diagram" style="width:555px;height:540px;">
```

Copy to Clipboard

**참고:** **주의**: 위의 샘플은 파일들의 위치를 특정하지만, 장고는 기본적으로 파일을 제공하지 않습니다. 우리는 우리가 웹사이트 뼈대를 생성했을 때([created the website skeleton](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/skeleton_website)) 전역 URL 매퍼(/locallibrary/locallibrary/urls.py)를 수정하여 개발 웹 서버가 파일을 제공하도록 설정했습니다만, 제품화되었을(in production)때도 파일을 제공할 수 있어야 합니다. 이것에 관해 차후에 다루겠습니다.

정적 파일들로 작업하는 것에 대한 더 많은 정보는 장고 문서 안의 [Managing static files](https://docs.djangoproject.com/en/2.0/howto/static-files/) 를 참고하세요.

#### URL 링크하기(Linking to URLs)

위의 기본 탬플릿은 `url` 탬플릿 태그를 소개했습니다.

```
<li><a href="{% url 'index' %}">Home</a></li>
```

Copy to Clipboard

이 태그는 **urls.py**에서 호출된 `path()` 함수의 이름 및 연관된 view가 그 함수에서 수신받을 모든 인자들을 위한 값들을 허용하고, 리소스에 링크하는 데 사용할 수 있는 URL을 반환합니다 .

#### 탬플릿을 찾을 수 있는 곳 설정하기

탬플릿 폴더 안에서 탬플릿을 찾아볼 수 있도록 장고에게 위치를 가르쳐 주어야 합니다. 그것을 하기 위해서, 아래 코드 샘플에 굵게 표시된 것 처럼 **settings.py** 파일을 수정하여 TEMPLATES 객체에 templates 경로(dir)를 추가하세요.

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

## [어떻게 보일까요?](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Home_page#어떻게_보일까요)

이 시점에서 우리는 색인(index) 페이지를 나타내기 위해 필요한 모든 요소들을 생성했습니다. 서버를 실행하고 (`python3 manage.py runserver`) 브라우저에서 http://127.0.0.1:8000/으로 이동하세요. 모든 것이 알맞게 설정되었다면, 당신의 사이트는 아래 스크린샷과 같이 보여야 합니다.

![Index page for LocalLibrary website](https://mdn.mozillademos.org/files/14045/index_page_ok.png)

**참고:** **주의:** All books와 All authors 링크들에 대한 경로, 뷰 그리고 탬플릿들이 정의되지 않았기 때문에 그 링크들은 작동하지 않을 것입니다. 우리는 단지 `base_generic.html` 탬플릿 안에 그 링크들을 위한 플레이스홀더(placeholder)들을 삽입했을 뿐입니다.

## [도전 과제](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Home_page#도전_과제)

모델 쿼리, 뷰 그리고 탬플릿들과의 친밀함을 시험할 수 있는 두 가지 임무가 있습니다.

1. LocalLibrary 기본 탬플릿(

   base template

   )에는

    

   ```
   title
   ```

    

   블록이 정의되어 있습니다. 색인 탬플릿(

   index template

   ) 안에 이 블록을 덮어쓰기하고 페이지를 위한 새로운 제목을 만들어 보세요.

   **참고:** **힌트:** [Extending templates](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Home_page#extending_templates) 섹션은 블럭(block)을 생성하고 다른 탬플릿에서 블럭을 확장(extend)하는 방법을 설명합니다.

2. 대소문자 구분 없이 특정한 단어를 포함하는 장르와 책들의 개수(count)를 생성하도록 [view](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Home_page#view_(function-based)) 를 수정하고, 결과를 `context`에 전달해 보세요. 이것은 `num_books`와 `num_instances_available`을 생성하고 사용하는 것과 비슷한 방법으로 달성할 수 있습니다. 그리고 나서 이 변수들을 포함시키기 위해 [index template](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Home_page#the_index_template) 를 업데이트 하세요.

## [요약](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Home_page#요약)

이제 우리의 사이트를 위한 홈 페이지를 생성했습니다 — 데이터베이스의 여러 레코드들을 표시하고 아직 생성되지 않은 페이지로 링크하는 HTML 페이지 입니다. 그 과정에서 우리는 url 매퍼, view, 모델을 이용한 데이터베이스 쿼리, view에서 탬플릿으로의 정보 전달 그리고 탬플릿의 생성과 확장에 관한 기본적인 정보를 배웠습니다.

다음 글에서는 이 지식들을 토대로 우리 웹사이트의 나머지 네 개의 페이지들을 생성할 것입니다.



------

## 페어프로그래밍 흐름

```
개발환경설정
1번.
1. 깃허브 저장소와 장고 프로젝트를 생성
- 2번 사람을 콜라보레이터로 초대

2. 생성한 저장소에 장고 프로젝트를 push
- .gitignore : 가상환경을 ignore
- pip freeze > requirements.txt : 패키지 목록을 생성

2번.
3. 2번 사람이 clone
4. 2번사람만 가상환경 생성과 requirements.txt 설치
- pip install -r requirements.txt 

5. 2번사람만 앱을 생성
6. add / commit / push
7. 1번 pull
- git pull
--------------------------------

개발 진행
# 드라이버 <-> 네비게이터 전환할 때
드라이버 : add commit push
네비게이터 : pull

항상 두 사람이 같은 코드를 유지해야한다.
```

<aside> 📚 페어프로그래밍 진행 후 **가상환경 폴더를 제외한** 파일 및 폴더를 압축해서 실라버스에 제출해주세요. 가상환경을 포함해서 제출하면 용량 제한을 초과하니 꼭 가상환경 폴더를 제외하고 압축해서 제출해주세요.
</aside>

# 주간 페어 프로그래밍 1 - 영화 리뷰 커뮤니티 CRUD

## 목표

두 사람이 팀을 이뤄서 영화 리뷰 커뮤니티 서비스의 CRUD 기능과 페이지를 구현합니다.

## 요구 사항

### 모델 Model

모델은 아래 조건을 만족해야합니다.

기능 추가를 위한 필드를 추가해도 됩니다.

- 모델 이름 : Review

- 모델 필드

  | 이름       | 역할           | 필드     | 속성              |
  | ---------- | -------------- | -------- | ----------------- |
  | title      | 리뷰 제목      | Char     | max_length=80     |
  | content    | 리뷰 내용      | Text     |                   |
  | created_at | 할 일 생성시간 | DateTime | auto_now_add=True |
  | updated_at | 할 일 수정시간 | DateTime | auto_now = True   |
  |            |                |          |                   |

### 기능 View

#### 아래 작성된 기능을 구현합니다.

- 리뷰 목록 보기
- 리뷰 내용 보기
- 리뷰 작성 하기
- 리뷰 수정하기
- 리뷰 삭제하기

### 화면 Template

아래 작성된 페이지와 컴포넌트를 구현해야 합니다.

- 리뷰 목록 페이지 index

  - 리뷰 ID / 리뷰 제목 / 리뷰 작성 시간

    - 리뷰 제목 클릭 시 해당 리뷰의 detail 페이지로 이동

  - 작성 버튼

    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/50d13081-0ac8-40e1-8471-9b1fbc36eaea/Untitled.png)

    - 버튼 클릭 시 new 페이지로 이동

- 리뷰 보기 페이지 detail

  - 리뷰 제목 / 리뷰 내용 / 리뷰 작성 시간
  - 수정 버튼
    - 버튼 클릭 시 edit 페이지로 이동
  - 삭제 버튼
    - 버튼 클릭 시 리뷰 삭제

  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bac1fe0d-449e-49ec-bf04-38e25911406f/Untitled.png)

- 리뷰 작성 페이지 new

  - 리뷰 제목 / 리뷰 내용
  - 생성 버튼
    - 버튼 클릭 시 새로운 리뷰 생성

  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/314f6be0-c2bf-4034-8a1d-54b2b32c1ba3/Untitled.png)

- 리뷰 수정 페이지 edit

  - 작성 폼에 원본 리뷰의 제목 과 내용이 작성된 상태.
  - 수정 버튼
    - 버튼 클릭 시 해당 리뷰 데이터 수정 update

  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5d13815d-08cf-4f10-b630-ea673c8fb83b/Untitled.png)



# 주간 페어 프로그래밍 2 - 영화 리뷰 커뮤니티 CRUD



## Github 저장소 Mirror

### 1. 깃허브 새로운 저장소 생성

2번 개발자는 새로운 저장소를 생성합니다.

### 2. 1번 개발자 저장소 clone

2번 개발자는 1번 개발자의 저장소를 clone 합니다

```bash
git clone --mirror {1번 개발자 페어 프로그래밍 저장소 주소}
cd {1번개발자의저장소이름}
```

### 3. 복사한 저장소의 원격 저장소 설정

2번 개발자는 새롭게 생성한 원격 저장소를 복사해온 프로젝트의 원격 저장소로 설정합니다.

```bash
git remote set-url --push origin {2번 개발자의 새롭게 생성한 저장소 주소}
```

### 4. push

2번 개발자는 프로젝트를 Push 합니다.



## 목표

페어 프로그래밍을 통한 영화 리뷰 커뮤니티 서비스를 개발합니다. 아래 조건을 만족해야합니다.

- ModelForm 활용 CRUD 구현
- Staticfiles 활용 서비스 로고 표시

## 요구 사항

### 모델 Model

모델은 아래 조건을 만족해야합니다.

적절한 필드와 속성을 부여하세요.

- 모델 이름 : Review

  모델 필드

  | 이름       | 역할          | 필드     | 속성              |
  | ---------- | ------------- | -------- | ----------------- |
  | title      | 리뷰 제목     |          |                   |
  | content    | 리뷰 내용     |          |                   |
  | movie_name | 영화 이름     |          |                   |
  | grade      | 영화 평점     |          |                   |
  | created_at | 리뷰 생성시간 | DateTime | auto_now_add=True |
  | updated_at | 리뷰 수정시간 | DateTime | auto_now = True   |

### 기능 View

아래 작성된 기능을 구현합니다.

생성 및 수정은 ModelForm을 사용하여 구현합니다.

- 데이터 목록 조회

  - `GET` http://127.0.0.1:8000/reviews/

- 데이터 정보 조회

  - `GET` http://127.0.0.1:8000/reviews/[int:pk](int:pk)/

- 데이터 생성

  - `POST` http://127.0.0.1:8000/reviews/create/

  사용자에게 아래 데이터를 입력 받습니다.

  - 리뷰 제목
  - 리뷰 내용
  - 영화 이름
  - 영화 평점

- 데이터 수정

  - `POST` http://127.0.0.1:8000/reviews/[int:pk](int:pk)/update/

- 데이터 삭제

  - `POST` http://127.0.0.1:8000/reviews/[int:pk](int:pk)/delete/

### 화면 Template

아래 작성된 페이지를 구현합니다.

**네비게이션바, Bootstrap <nav>**

- 서비스 로고
  - Django Staticfiles 활용
  - 클릭 시 메인 페이지로 이동
- 리뷰 목록 버튼
  - 클릭 시 목록 페이지로 이동
- 리뷰 작성 버튼
  - 클릭 시 작성 페이지로 이동

**메인 페이지**

- `GET` http://127.0.0.1:8000/reviews/
- 자유 디자인

목록 페이지

- `GET` http://127.0.0.1:8000/reviews/index/
- 리뷰 목록 출력
  - 리뷰 제목
  - 영화 이름
- 제목을 클릭하면 해당 리뷰의 정보 페이지로 이동

**리뷰 정보 페이지**

- `GET` http://127.0.0.1:8000/reviews/[int:pk](int:pk)/
- 해당 리뷰 정보 출력
- 수정 / 삭제 버튼
- 

**리뷰 작성 페이지**

- `GET` http://127.0.0.1:8000/reviews/create/
- 리뷰 작성 폼
- 

**리뷰 수정 페이지**

- `GET` http://127.0.0.1:8000/reviews/[int:pk](int:pk)/update/
- 리뷰 수정 폼



# 주간 페어 프로그래밍 3 - 영화 리뷰 커뮤니티 CRUD

## 페어프로그래밍 가이드

개발 환경 설정을 제외한 모든 토픽 개발은 아래 순서에 따라 진행합니다.

1. [로컬/드라이버] main 브랜치에서 개발 토픽에 해당하는 브랜치 생성 및 브랜치 전환

   ```bash
   # 브랜치 생성 & 전환
   git checkout -b [토픽 브랜치명]
   
   # git checkout [브랜치명] : 브랜치를 전환합니다.
   # git checkout -b [브랜치명] : 브랜치를 생성하고 전환합니다. 동일한 브랜치가 있으면 오류가 발생합니다.
   ```

2. [로컬/드라이버] 토픽 개발

3. [로컬/드라이버] 토픽 개발 후 동일한 이름의 원격 저장소 브랜치에 Commit&Push

   ```bash
   git add .
   
   git commit -m '커밋 메세지'
   
   git push origin [토픽 브랜치명]
   ```

4. [원격/드라이버] 토픽 브랜치 병합

   1. 깃허브 PR 생성(토픽 브랜치 → main 브랜치)

      ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/26e2083c-b2d5-4a8a-b700-ce32105916b3/Untitled.png)

   2. 브랜치 병합(토픽 브랜치 → main 브랜치)

      ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/dcb1d4ef-2f39-4b36-991b-cfd1ffe561c6/Untitled.png)

      ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4c24962f-5b89-4c21-aab7-d055a98caf89/Untitled.png)

   3. 토픽 브랜치 삭제

      ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bd4813a2-ea1a-4e7b-beff-52e6884b07f0/Untitled.png)

5. [로컬/전체] main 브랜치 전환 후 Pull

   ```bash
   # main 브랜치로 전환
   git checkout main
   
   # main 브랜치 Pull
   git pull origin main
   ```

6. [로컬/드라이버] 토픽 브랜치 삭제

   ```bash
   # 토픽 브랜치 삭제
   git branch -d [토픽 브랜치명]
   ```

7. 드라이버 변경 후 1번 부터 시작

## 깃 브랜치 명령어

```bash
# 브랜치 생성 & 전환
git checkout -b [브랜치명]

# 브랜치 전환
git checkout [브랜치명]

# 브랜치 삭제
git branch -d [브랜치명]

# 브랜치 이름 변경
git branch -m [기존 브랜치명] [변경할 브랜치명]
```

## 목표

페어 프로그래밍을 통한 영화 리뷰 커뮤니티 서비스를 개발합니다. 아래 조건을 만족해야합니다.

- **CRUD** 구현

- Staticfiles

   

  활용 정적 파일(이미지, CSS, JS) 다루기

  - Django **Auth** 활용 회원 관리(회원가입 / 회원 조회 / 로그인 / 로그아웃)

## 토픽

### 1. 깃 설정

branch main

- 원격 저장소 생성

- 콜라보레이터 초대

- 로컬 저장소 깃 초기화

  ```bash
  git init
  ```

- 로컬 저장소 .gitignore 생성

  ```bash
  touch .gitigngit ore
  ```

- .gitignore 작성

  - 아래 사이트 입력창에 필요한 언어 & 프레임워크 & 환경 입력 후 생성

  [gitignore.io](https://www.toptal.com/developers/gitignore/)

<aside> ❗ 위 과정 완료 후 [로컬/드라이버] main → [원격/드라이버] main, Commit & Push 수행 [원격/전체] 저장소 Clone 수행 드라이버 변경 [로컬/새 드라이버] setup-django 브랜치에서 다음 토픽 진행

</aside>

------

### 2. 장고 개발환경 설정

branch setup-django

Django 프로젝트 생성

- 가상환경 생성 & 실행

- 필요한 패키지 설치git

  주의

  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d49ddbaf-6c78-4244-973d-0206774246d2/Untitled.png)

- 패키지 목록 저장

  ```bash
  pip freeze > requirements.txt
  ```

- Django 프로젝트 생성

  ```bash
  django-admin startproject config .
  ```

<aside> ❗ 위 과정 완료 후 [로컬/드라이버] setup-django → [원격/드라이버] setup-django, Commit & Push 수행 [원격/드라이버] setup-django → [원격/드라이버] main, PR 생성 & Merge 수행 [원격/드라이버] setup-django 브랜치 삭제 [원격/전체] main → [로컬/전체] main, Pull 수행 [로컬/드라이버] setup-django 브랜치 삭제 드라이버 변경 [로컬/새 드라이버] accounts/signup 브랜치에서 다음 토픽 진행

</aside>

------

### 3. 회원가입

branch accounts/signup

앱 App

앱 이름 : accounts

모델 Model

모델 이름 : User

- Django **AbstractUser** 모델 상속

**폼 Form**

- Django 내장 회원가입 폼 UserCreationForm을 상속 받아서 CustomUserCreationForm 작성

  해당 폼은 아래 필드만 출력합니다.

  - username
  - password1
  - password2

**기능 View**

회원가입

- `POST` http://127.0.0.1:8000/accounts/signup/
- CustomUserCreationForm을 활용해서 회원가입 구현

**화면 Template**

회원가입 페이지

- `GET` http://127.0.0.1:8000/accounts/signup/
- 회원가입 폼

<aside> ❗ 위 과정 완료 후 [로컬/드라이버] accounts/signup → [원격/드라이버] accounts/signup, Commit & Push 수행 [원격/드라이버] accounts/signup → [원격/드라이버] main, PR 생성 & Merge 수행 [원격/드라이버] accounts/signup 브랜치 삭제 [원격/전체] main → [로컬/전체] main, Pull 수행 [로컬/드라이버] accounts/signup 브랜치 삭제 드라이버 변경 [로컬/새 드라이버] accounts/login 브랜치에서 다음 토픽 진행

</aside>

------

### 4. 로그인

branch accounts/login

**폼 Form**

로그인

- Django 내장 로그인 폼 **AuthenticationForm 활용**

**기능 View**

로그인

- `POST` http://127.0.0.1:8000/accounts/login/
- **AuthenticationForm**를 활용해서 로그인 구현

**화면 Template**

로그인 페이지

- `GET` http://127.0.0.1:8000/accounts/login/
- 로그인 폼
- 회원가입 페이지 이동 버튼

<aside> ❗ 위 과정 완료 후 [로컬/드라이버] accounts/login → [원격/드라이버] accounts/login, Commit & Push 수행 [원격/드라이버] accounts/login → [원격/드라이버] main, PR 생성 & Merge 수행 [원격/드라이버] accounts/login 브랜치 삭제 [원격/전체] main → [로컬/전체] main, Pull 수행 [로컬/드라이버] accounts/login 브랜치 삭제 드라이버 변경 [로컬/새 드라이버] accounts/index 브랜치에서 다음 토픽 진행

</aside>

------

### 5. 회원 목록 조회

`branch` accounts/index

**기능 View**

회원 목록 조회

- `GET` http://127.0.0.1:8000/accounts/

**화면 Template**

회원 목록 페이지

- `GET` http://127.0.0.1:8000/accounts/
- 회원 목록 출력
- 회원 아이디를 클릭하면 해당 회원 조회 페이지로 이동

<aside> ❗ 위 과정 완료 후 [로컬/드라이버] accounts/index → [원격/드라이버] accounts/index, Commit & Push 수행 [원격/드라이버] accounts/index → [원격/드라이버] main, PR 생성 & Merge 수행 [원격/드라이버] accounts/index 브랜치 삭제 [원격/전체] main → [로컬/전체] main, Pull 수행 드라이버 변경 [로컬/새 드라이버] accounts/detail 브랜치에서 다음 토픽 진행

</aside>

------

### 6. 회원 정보 조회

`branch` accounts/detail

**기능 View**

회원 정보 조회

- `GET` http://127.0.0.1:8000/accounts/[int:user_pk](int:user_pk)/

**화면 Template**

회원 조회 페이지(프로필 페이지)

- `GET` http://127.0.0.1:8000/accounts/[int:user_pk](int:user_pk)/

<aside> ❗ 위 과정 완료 후 [로컬/드라이버] accounts/detail → [원격/드라이버] accounts/detail, Commit & Push 수행 [원격/드라이버] accounts/detail → [원격/드라이버] main, PR 생성 & Merge 수행 [원격/드라이버] accounts/detail 브랜치 삭제 [원격/전체] main → [로컬/전체] main, Pull 수행 드라이버 변경 [로컬/새 드라이버] accounts/update 브랜치에서 다음 토픽 진행

</aside>

------

### 7. 회원 정보 수정

branch accounts/update

**폼 Form**

회원 정보 수정

- Django 내장 회원 수정 폼 UserChangeForm을 상속 받아서 **CustomUserChangeForm** 작성

  해당 폼은 아래 필드만 출력합니다.

  - first_name
  - last_name
  - email

**기능 View**

회원 정보 수정

- `POST` http://127.0.0.1:8000/accounts/update/

**화면 Template**

회원 정보 수정 페이지

- `GET` http://127.0.0.1:8000/accounts/update/

<aside> ❗ 위 과정 완료 후 [로컬/드라이버] accounts/update → [원격/드라이버] accounts/update, Commit & Push 수행 [원격/드라이버] accounts/update → [원격/드라이버] main, PR 생성 & Merge 수행 [원격/드라이버] accounts/update 브랜치 삭제 [원격/전체] main → [로컬/전체] main, Pull 수행 드라이버 변경 [로컬/새 드라이버] accounts/logout 브랜치에서 다음 토픽 진행

</aside>

------

### 8. 로그아웃

branch accounts/logout

**기능 View**

로그아웃

- `POST` http://127.0.0.1:8000/accounts/logout/

<aside> ❗ 위 과정 완료 후 [로컬/드라이버] accounts/logout → [원격/드라이버] accounts/logout, Commit & Push 수행 [원격/드라이버] accounts/logout → [원격/드라이버] main, PR 생성 & Merge 수행 [원격/드라이버] accounts/logout 브랜치 삭제 [원격/전체] main → [로컬/전체] main, Pull 수행 드라이버 변경 [로컬/새 드라이버] template/navbar 브랜치에서 다음 토픽 진행

</aside>

------

### 9. 네비게이션바

branch template/navbar

**화면 Template**

**네비게이션바**

- 리뷰 목록 페이지 이동 버튼
- 리뷰 작성 페이지 이동 버튼
- 비 로그인 유저는 작성 버튼 출력 X
- 로그인 상태에 따라 다른 화면 출력
  1. 로그인 상태
     - 로그인 한 사용자의 username 출력
       - username을 클릭하면 회원 조회 페이지로 이동
     - 로그아웃 버튼
  2. 비 로그인 상태
     - 로그인 페이지 이동 버튼
     - 회원가입 페이지 이동 버튼

<aside> ❗ 위 과정 완료 후 [로컬/드라이버] template/navbar → [원격/드라이버] template/navbar, Commit & Push 수행 [원격/드라이버] template/navbar → [원격/드라이버] main, PR 생성 & Merge 수행 [원격/드라이버] template/navbar 브랜치 삭제 [원격/전체] main → [로컬/전체] main, Pull 수행 드라이버 변경 [로컬/새 드라이버] reviews/create 브랜치에서 다음 토픽 진행

</aside>

------

### 10. 리뷰 생성

branch reviews/create

**앱 App**

앱 이름 : reviews

모델 Model

모델 이름 : Review

- 모델 필드

  | 이름       | 역할          | 필드     | 속성              |
  | ---------- | ------------- | -------- | ----------------- |
  | title      | 리뷰 제목     |          |                   |
  | content    | 리뷰 내용     |          |                   |
  | movie_name | 영화 이름     |          |                   |
  | grade      | 영화 평점     |          |                   |
  | created_at | 리뷰 생성시간 | DateTime | auto_now_add=True |
  | updated_at | 리뷰 수정시간 | DateTime | auto_now = True   |

**기능 View**

데이터 생성

- `POST` http://127.0.0.1:8000/reviews/create/

**화면 Template**

**리뷰 작성 페이지**

- `GET` http://127.0.0.1:8000/reviews/create/
- 리뷰 작성 폼

<aside> ❗ 위 과정 완료 후 [로컬/드라이버] reviews/create → [원격/드라이버] reviews/create, Commit & Push 수행 [원격/드라이버] reviews/create → [원격/드라이버] main, PR 생성 & Merge 수행 [원격/드라이버] reviews/create 브랜치 삭제 [원격/전체] main → [로컬/전체] main, Pull 수행 드라이버 변경 [로컬/새 드라이버] reviews/index 브랜치에서 다음 토픽 진행

</aside>

------

### 11. 리뷰 목록 조회

branch reviews/index

**기능 View**

데이터 목록 조회

- `POST` http://127.0.0.1:8000/reviews/

**화면 Template**

리뷰 **목록 페이지**

- `GET` http://127.0.0.1:8000/reviews/
- 리뷰 목록 출력
- 제목을 클릭하면 해당 리뷰의 정보 페이지로 이동

<aside> ❗ 위 과정 완료 후 [로컬/드라이버] reviews/index → [원격/드라이버] reviews/index, Commit & Push 수행 [원격/드라이버] reviews/index → [원격/드라이버] main, PR 생성 & Merge 수행 [원격/드라이버] reviews/index 브랜치 삭제 [원격/전체] main → [로컬/전체] main, Pull 수행 드라이버 변경 [로컬/새 드라이버] reviews/detail 브랜치에서 다음 토픽 진행

</aside>

------

### 12. 리뷰 정보 조회

branch reviews/detail

**기능 View**

데이터 정보 조회

- `GET` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/

**화면 Template**

**리뷰 정보 페이지**

- `GET` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/
- 해당 리뷰 정보 출력
- 수정 / 삭제 버튼

<aside> ❗ 위 과정 완료 후 [로컬/드라이버] reviews/detail → [원격/드라이버] reviews/detail, Commit & Push 수행 [원격/드라이버] reviews/detail → [원격/드라이버] main, PR 생성 & Merge 수행 [원격/드라이버] reviews/detail 브랜치 삭제 [원격/전체] main → [로컬/전체] main, Pull 수행 드라이버 변경 [로컬/새 드라이버] reviews/update 브랜치에서 다음 토픽 진행

</aside>

------

### 13. 리뷰 정보 수정

branch reviews/update

**기능 View**

데이터 수정

- `POST` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/update/

**화면 Template**

**리뷰 수정 페이지**

- `GET` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/update/
- 리뷰 수정 폼

<aside> ❗ 위 과정 완료 후 [로컬/드라이버] reviews/update → [원격/드라이버] reviews/update, Commit & Push 수행 [원격/드라이버] reviews/update → [원격/드라이버] main, PR 생성 & Merge 수행 [원격/드라이버] reviews/update 브랜치 삭제 [원격/전체] main → [로컬/전체] main, Pull 수행 드라이버 변경 [로컬/새 드라이버] reviews/delete 브랜치에서 다음 토픽 진행
</aside>

------

### 14. 리뷰 삭제

branch reviews/delete

**기능 View**

데이터 삭제

- `POST` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/delete/

<aside> ❗ 위 과정 완료 후 [로컬/드라이버] reviews/delete → [원격/드라이버] reviews/delete, Commit & Push 수행 [원격/드라이버] reviews/delete → [원격/드라이버] main, PR 생성 & Merge 수행 [원격/드라이버] reviews/delete 브랜치 삭제 [원격/전체] main → [로컬/전체] main, Pull 수행 드라이버 변경
</aside>

------

이후 팀원 간 논의하여 적절한 브랜치 이름을 정하여 개발합니다.



# 주간 페어 프로그래밍 4 - 영화 리뷰 커뮤니티 CRUD





<aside> 📚 실습 진행 후 **가상환경 폴더를 제외한** 파일 폴더를 압축해서 실라버스에 제출해주세요. 가상환경을 포함해서 제출하면 용량 제한을 초과하니 꼭 가상환경 폴더를 제외하고 압축해서 제출해주세요.

DJANGO 개발은 꼭 가상 환경을 실행한 상태로 진행하세요.

</aside>

[Git Branch 명령어](https://www.notion.so/Git-Branch-61d408a0688d4c7197ff16a68227a5ed)

[GitHub Flow 가이드](https://www.notion.so/GitHub-Flow-a8a752167a6e4f22a945d8d701b723ed)

[GitHub 병합 충돌 처리 가이드](https://www.notion.so/GitHub-300e6a53ca9d453092696ea891babc8e)

## 목표

페어 프로그래밍을 통한 영화 리뷰 커뮤니티 서비스를 개발합니다. 아래 조건을 만족해야합니다.

- **CRUD** 구현

- **Staticfiles** 활용 정적 파일(이미지, CSS, JS) 다루기

- Django **Auth** 활용 회원 관리 구현

- Media 활용 동적 파일 다루기

- 모델간

   

  1 : N 관계

   

  매핑 코드 작성 및 활용

  - 유저 - 리뷰
  - 리뷰 - 댓글
  - 유저 - 댓글

## 토픽

### 깃 저장소 생성

branch master

1. 원격 저장소 생성

2. 콜라보레이터 초대

3. 로컬 저장소 깃 초기화

4. 로컬 저장소 .gitignore 생성 & 작성

   [gitignore.io](https://www.toptal.com/developers/gitignore/)

------

### 개발환경 설정

branch setup-env

1. Django 프로젝트 생성

2. 가상환경 생성 & 실행

3. 필요한 패키지 설치

4. 패키지 목록 저장

   ```bash
   pip freeze > requirements.txt
   ```

5. Django 프로젝트 생성

   ```bash
   django-admin startproject config .
   ```

------

### 회원 가입

branch account/signup

앱 App 생성

- 앱 이름 : accounts

모델 Model 작성

- 모델 이름 : User
- Django AbstractUser 모델 상속

폼 Form 작성

- Django 내장폼 UserCreationForm을 상속받은 CustomUserCreationForm 작성

기능 View

- `POST` accounts/signup/
- CustomUserCreationForm 활용

화면 Template

- `GET` accounts/signup/
- 회원가입 폼

------

### 로그인

branch accounts/login

기능 View

- `POST` accounts/signup/
- 내장 폼 AuthenticationForm 활용

화면 Template

- `GET` accounts/signup/
- 로그인 폼
- 회원가입 페이지 이동 버튼

------

### 로그아웃

branch accounts/logout

기능 View

- `POST` account/logout

------

### 리뷰 작성

branch reviews/create

앱 App 생성

앱 이름 : reviews

모델 Model 생성

모델 이름 : Review

- 모델 필드

  | 이름       | 역할          | 필드     | 속성              |
  | ---------- | ------------- | -------- | ----------------- |
  | user       | 리뷰 작성자   |          |                   |
  | title      | 리뷰 제목     |          |                   |
  | content    | 리뷰 내용     |          |                   |
  | movie_name | 영화 이름     |          |                   |
  | grade      | 영화 평점     |          |                   |
  | created_at | 리뷰 생성시간 | DateTime | auto_now_add=True |
  | updated_at | 리뷰 수정시간 | DateTime | auto_now = True   |

기능 View

- `POST` reviews/create/

화면 Template

- `GET` reviews/create/
- 리뷰 작성 폼

------

### 리뷰 목록 조회

branch reviews/index

**기능 View**

- `GET` reviews/

**화면 Template**

- `GET` reviews/

------

### 리뷰 정보 조회

branch reviews/detail

**기능 View**

- `GET` reviews/[int:review_pk](int:review_pk)/

**화면 Template**

- `GET` reviews/[int:review_pk](int:review_pk)/
- 리뷰 수정 / 삭제 버튼
  - 수정 / 삭제 버튼은 해당 리뷰 작성자에게만 출력합니다.
- 댓글 작성 폼
  - 댓글 작성 폼은 로그인 사용자에게만 출력합니다.
- 댓글 목록

------

### 리뷰 정보 수정

branch reviews/update

**기능 View**

- `POST` reviews/[int:review_pk](int:review_pk)/update/
- 데이터를 생성한 사용자만 수정할 수 있습니다.

**화면 Template**

- `GET` reviews/[int:review_pk](int:review_pk)/update/
- 리뷰 수정 폼

------

### 리뷰 삭제

branch reviews/delete

**기능 View**

- `POST` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/delete/
- 데이터를 생성한 사용자만 삭제할 수 있습니다.

------

### 댓글 작성

branch comments/create

reviews 앱에 구현

모델 Model 생성

모델 이름 : Comment

- 모델 필드

  | 이름    | 역할        | 필드 | 속성 |
  | ------- | ----------- | ---- | ---- |
  | review  | 참조 리뷰   |      |      |
  | user    | 댓글 작성자 |      |      |
  | content | 댓글 내용   |      |      |

기능 View

- `POST` reviews/[int:review_pk](int:review_pk)/comments/
- 로그인한 사용자만 댓글을 생성할 수 있습니다.

화면 Template

- `GET` reviews/[int:review_pk](int:review_pk)/
- 리뷰 정보 조회 페이지 하단에 댓글 작성 폼 출력

------

### 댓글 목록 조회

branch comments/index

기능 View

- `GET` reviwes/[int:review_pk](int:review_pk)/

화면 Template

- `GET` reviews/[int:review_pk](int:review_pk)/
- 리뷰 정보 조회 페이지 하단에 댓글 목록 출력

------

### 댓글 삭제

branch comments/delete

기능 View

- `POST` reviews/[int:review_pk](int:review_pk)/comments/[int:comment_pk](int:comment_pk)/delete/
- 데이터를 생성한 사용자만 삭제할 수 있습니다.

화면 Template

- `GET` reviews/[int:review_pk](int:review_pk)/
- 각 댓글에 리뷰 삭제 버튼 추가
  - 삭제 버튼은 해당 댓글 작성자에게만 출력합니다.

# 주간 페어 프로그래밍 5 - 영화 리뷰 커뮤니티 CRUD

<aside> 📚 실습 진행 후 **가상환경 폴더를 제외한** 파일 폴더를 압축해서 실라버스에 제출해주세요. 가상환경을 포함해서 제출하면 용량 제한을 초과하니 꼭 가상환경 폴더를 제외하고 압축해서 제출해주세요.

DJANGO 개발은 꼭 가상 환경을 실행한 상태로 진행하세요.

</aside>

[Git Branch 명령어](https://www.notion.so/Git-Branch-b459282f3322426b9d6709a44047b0a5)

[GitHub Flow 가이드](https://www.notion.so/GitHub-Flow-7215dd91cd4a4580872f69481e1b6199)

[GitHub 병합 충돌 처리 가이드](https://www.notion.so/GitHub-086f97a2d17c4f39bd45a8c15edc4309)

## 헤로쿠 배포 가이드

[가이드](https://www.notion.so/e4afcc5c17b04cec97655310b160cffa)

## 목표

페어 프로그래밍을 통한 영화 리뷰 커뮤니티 서비스를 개발합니다. 아래 조건을 만족해야 합니다.

- **CRUD** 구현(구현 방법 제한 없음)
- **Staticfiles** 활용 정적 파일(이미지, CSS, JS) 다루기
- Django **Auth** 활용 회원 관리(회원 가입 / 회원 조회 / 로그인 / 로그아웃)
- Media 활용 동적 파일 다루기
- 모델간 **1 : N / M : N 관계** 매핑

## 요구 사항

### 모델 Model

- 모델 이름 : User

  Django **AbstractUser** 모델을 상속 받고, 필드를 직접 정의하세요.

- 모델 이름 : Review

  모델의 필드를 직접 정의하세요.

- 모델 이름 : Comment

  모델의 필드를 직접 정의하세요.

### **폼 Form**

회원 가입

- Django 내장 회원 가입 폼 UserCreationForm을 상속 받아서 CustomUserCreationForm 생성
- 출력할 필드를 직접 정의합니다.

로그인

- Django 내장 로그인 폼 AuthenticationForm 활용

### 기능 View

**리뷰 reviews**

데이터 목록 조회

- `GET` http://127.0.0.1:8000/reviews/

데이터 정보 조회

- `GET` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/

데이터 생성

- `POST` http://127.0.0.1:8000/reviews/create/
- 로그인한 유저만 데이터 생성이 가능합니다.

데이터 수정

- `POST` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/update/
- 해당 리뷰 작성자만 수정할 수 있습니다.

데이터 삭제

- `POST` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/delete/
- 해당 리뷰 작성자만 삭제할 수 있습니다.

리뷰 좋아요 / 좋아요 취소

- `POST` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/like/
- 로그인한 유저만 좋아요 기능을 사용할 수 있습니다.

**댓글 comments**

리뷰의 댓글 목록 조회

- `GET` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/
- 해당 게시글의 댓글 목록 조회

댓글 생성

- `POST` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/comments/create/
- 로그인한 유저만 댓글 생성이 가능합니다.

댓글 삭제

- `POST` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/comments/[int:comment_pk](int:comment_pk)/delete/
- 해당 댓글 작성자만 삭제할 수 있습니다.

**회원 관리 accounts**

회원 가입

- `POST` http://127.0.0.1:8000/accounts/signup/

회원 목록 조회

- `GET` http://127.0.0.1:8000/accounts/

회원 정보 조회

- `GET` http://127.0.0.1:8000/accounts/[int:user_pk](int:user_pk)/

로그인

- `POST` http://127.0.0.1:8000/accounts/login/

로그아웃

- `POST` http://127.0.0.1:8000/accounts/logout/

팔로우

- `POST` http://127.0.0.1:8000/accounts/[int:user_pk](int:user_pk)/follow/
- 로그인한 유저만 팔로우 기능을 사용할 수 있습니다.
- 자기 자신은 팔로우 할 수 없습니다.

### 화면 Template

**네비게이션바, Bootstrap <nav>**

- 서비스 로고
- 리뷰 목록 페이지 이동 버튼
- 리뷰 작성 페이지 이동 버튼
- 로그인 상태에 따라 다른 화면을 출력합니다.
  1. 로그인 상태
     - 로그인한 사용자의 username
     - 로그아웃 버튼
  2. 비 로그인 상태
     - 로그인 페이지 이동 버튼
     - 회원 가입 페이지 이동 버튼

**메인 페이지**

- `GET` http://127.0.0.1:8000/
- 자유 디자인

**목록 페이지**

- `GET` http://127.0.0.1:8000/reviews/

**리뷰 정보 페이지**

- `GET` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/
- 해당 리뷰 정보 출력
- 댓글 작성 폼
- 해당 리뷰에 작성된 댓글 목록
  - 각 댓글에는 삭제 버튼이 있습니다. 단, 댓글 작성자만 삭제를 할 수 있습니다.
- 좋아요 버튼
  - 해당 리뷰의 좋아요 개수를 함께 출력합니다.
  - 로그인한 유저는 리뷰에 좋아요를 남길 수 있습니다.

**리뷰 작성 페이지**

- `GET` http://127.0.0.1:8000/reviews/create/
- 리뷰 작성 폼

**리뷰 수정 페이지**

- `GET` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/update/
- 리뷰 수정 폼

회원 가입 페이지

- `GET` http://127.0.0.1:8000/accounts/signup/
- 회원 가입 폼

회원 조회 페이지(프로필 페이지)

- `GET` http://127.0.0.1:8000/accounts/[int:user_pk](int:user_pk)/
- 회원이 작성한 게시글 목록 출력

로그인 페이지

- `GET` http://127.0.0.1:8000/accounts/login/
- 로그인 폼
- 회원 가입 페이지 이동 버튼

팔로우 버튼

- x로그인한 유저는 해당 유저를 팔로우 할 수 있습니다.
- 단, 자기 자신은 팔로우 할 수 없습니다.
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

- 로그인한 유저는 해당 유저를 팔로우 할 수 있습니다.
- 단, 자기 자신은 팔로우 할 수 없습니다.
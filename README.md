

# 매일 배운 내용 정리하기

---

## Git(분산 버전 관리 시스템 DVCS, remote repository)/GitHub(Git을 이용한 플랫폼)

---

### Markdown을 활용한 문서 작성

- [ ] 문서 정리
- [ ] IPAD 타블릿
- [ ] 메모장 에버노트 노션
- [ ] docx google docs hwp

### Git을 활용한 버전 관리

### Github을 활용한 포트폴리오 관리 및 개발 프로젝트 시나리오

- 개인 포트폴리오 관리
  - TIL (Today I Learned)
  - 개인 개발 프로젝트
- 프로젝트(협업) PR
  - GitHub Flow를 활용한 개발프로젝트 가이드라인
    - Shared repository model / Fork & Pull model

---

## 마크다운 개요

---

#### 2004년 존 그루버가 만든 텍스트 기반의 가벼운 마크업 언어 Github Flavored Markdown

---

## 마크다운 특징

---

### 워드프로세서(한글/MS word)는 다양한 서식과 구조를 지원,  최소한의 문법으로 구조화

### 단순 텍스트 문법으로 내용을 작성하며, 다양한 환경에서 변환

---

## 마크다운 활용 예 (README.MD 기술 블로그 메모 노트 필기)

---

## 마크다운 문법 - Heading

---

# h1

## h2

### h3

#### h4

##### h5

###### h6

---

## 마크다운 문법 - List(markdown HTML rendered output)

## 마크다운 문법 - Fenced Code Block

## 마크다운 문법 - Inline Code block

## 마크다운 문법 - Link

My favorite translator engine is [PAPAGO](https://papago.naver.com)

---

## 마크다운 문법 - 이미지

## 마크다운 문법 - Blockquotes

>
>
>KDT 1기 1회차

## 마크다운 문법 - Table (표)

## 마크다운 문법 - text 강조

## 마크다운 문법 - 수평선

---

## 마크다운 관련 자료

- [GitHub Flavored Markdown](https://github.github.com/gfm/)
- [Mastering Markdown](https://guides.github.com/features/mastering-markdown/)
- [Markdown Guide](https://www.markdownguide.org/)

---

## 마크다운 실습 1. 마크다운 문법 정리

## 기본 구문

다음은 John Gruber의 원래 설계 문서에서 개략적으로 설명한 요소입니다.모든 Markdown 응용 프로그램은 이러한 요소를 지원합니다.

| 요소                                                         | 마크다운 구문                               |
| ------------------------------------------------------------ | ------------------------------------------- |
| [표제](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fwww.markdownguide.org%2Fbasic-syntax%2F%23headings) | `# H1 ## H2 ### H3`                         |
| [굵은 글씨](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fwww.markdownguide.org%2Fbasic-syntax%2F%23bold) | `**bold text**`                             |
| [이탤릭체](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fwww.markdownguide.org%2Fbasic-syntax%2F%23italic) | `*italicized text*`                         |
| [블록 따옴표](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fwww.markdownguide.org%2Fbasic-syntax%2F%23blockquotes-1) | `> blockquote`                              |
| [주문 목록](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fwww.markdownguide.org%2Fbasic-syntax%2F%23ordered-lists) | `1. First item 2. Second item3. Third item` |
| [주문되지 않은 목록](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fwww.markdownguide.org%2Fbasic-syntax%2F%23unordered-lists) | `- First item - Second item - Third item`   |
| [코드](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fwww.markdownguide.org%2Fbasic-syntax%2F%23code) | ``code``                                    |
| [가로줄](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fwww.markdownguide.org%2Fbasic-syntax%2F%23horizontal-rules) | `---`                                       |
| [링크](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fwww.markdownguide.org%2Fbasic-syntax%2F%23links) | `[title](https://www.example.com)`          |
| [이미지](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fwww.markdownguide.org%2Fbasic-syntax%2F%23images-1) | `![alt text](image.jpg)`                    |

## 확장 구문

이러한 요소는 기능을 추가하여 기본 구문을 확장합니다.일부 Markdown 응용 프로그램은 이러한 요소를 지원하지 않습니다.

| 요소                                                         | 마크다운 구문                                                |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [테이블](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fwww.markdownguide.org%2Fextended-syntax%2F%23tables) | `Syntax Description ----------- ----------- Header Title Paragraph Text ` |
| [펜스 코드 블록](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fwww.markdownguide.org%2Fextended-syntax%2F%23fenced-code-blocks) | ````{"firstName": "John","lastName": "Smith","age": 25}``` ` |
| [각주](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fwww.markdownguide.org%2Fextended-syntax%2F%23footnotes) | `Here's a sentence with a footnote. [^1][^1]: This is the footnote. ` |
| [표제 아이디](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fwww.markdownguide.org%2Fextended-syntax%2F%23heading-ids) | `### My Great Heading {#custom-id}`                          |
| [정의 리스트](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fwww.markdownguide.org%2Fextended-syntax%2F%23definition-lists) | `term: definition `                                          |
| [스트리커](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fwww.markdownguide.org%2Fextended-syntax%2F%23strikethrough) | `~~The world is flat.~~`                                     |
| [작업 목록](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fwww.markdownguide.org%2Fextended-syntax%2F%23task-lists) | `- [x] Write the press release- [ ] Update the website- [ ] Contact the media ` |
| [이모티콘](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fwww.markdownguide.org%2Fextended-syntax%2F%23emoji) ([이모지 복사](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fwww.markdownguide.org%2Fextended-syntax%2F%23copying-and-pasting-emoji) 및 [붙여넣기 참조](https://papago.naver.net/apis/site/proxy?url=https%3A%2F%2Fwww.markdownguide.org%2Fextended-syntax%2F%23copying-and-pasting-emoji)) | `That is so funny! :joy:`                                    |



---

---



## 작업하면 Working directory > add하여 Staging area에모아 INDEX > commit으로 버전 기록 HEAD

## Modifed 파일이 수정된 상태

## staged 수정한 파일을 곧 커밋할 것이라고 표시한 상태

## committed 커밋이 된 상태

---

# Git 코드 정리

## $ git config --global user.name 'GitHub ID'

## $ git config --global user.email 'GitHub Email'

---

## $ git init

- 특정 폴더를 git 저장소(repository)를 만들어 git으로 관리
- .git 폴더 git bash에 master 표기
- 로컬 저장소 생성

## $ git status

-  Working directory staging area
- Git 저장소에 있는 파일의 상태를 확인하기 위하여 활용

## $ git add .

- 파일의 변경 사항 > 버전으로 기록하기 위한 파일 변경사항의 목록
- untracked 상태의 파일 staged로 변경
- modified 상태의 파일을 staged로 변경
- 특정 파일/폴더의 변경 사항 추가

## $ git commit

- 버전으로 기록하기 위한 파일 변경사항의 목록 > 커밋(버전)들이 기록되는 곳
- 파일이 달라지지 않으면 성능을 위해 파일을 새로 저장하지 않음

## $ git commit -m '마크다운 정리'

- staged 상태의 파일들을 커밋을 통해 버전으로 기록
- 커밋 버전 기록 

## $ git log

- 커밋(버전)

- 현재 저장소에 기록된 커밋을 조회

  - $ git log -1

    $ git log --oneline

    $ git log -2 --oneline

---

## $ git remote -v

- 원격저장소 정보 확인

## $ git remoe add <원격저장소> <url>

- 원격저장소 추가 (일반적으로 origin)

## $ git remote rm <원격저장소>

- 원격 저장소 삭제

## $ git push

- 로컬 저장소의 버전을 원격저장소로 보낸다

## $ git pull <원격저장소이름> <브랜치이름>

- 원격 저장소로부터 변경된 내역을 받아와서 이력을 병합함

## $ git push <원격저장소이름> <브랜치이름>

- 원격 저장소로 로컬 저장소 변경 사항(커밋)을 올림(push)
- 로컬 폴더의 파일/폴더가 아닌 저장소의 버전(커밋)이 올라감

## $ git clone <원격저장소이름>

- 원격 저장소를 복제하여 가져옴

---

---

# GitHub에서 원격 저장소 만들기

## 저장소 설정하기

## 확인하기

## 로컬저장소의 버전을 원격저장소로 보내기

---

## 저장소 이름 변경

- Settings > General > Repository name

## 저장소 Public/Private 전환 및 삭제

- Settings > General > 하단부 Danger Zone

## 저장소 접근 관리

- Settings > Collaborators

---

## Push 실패


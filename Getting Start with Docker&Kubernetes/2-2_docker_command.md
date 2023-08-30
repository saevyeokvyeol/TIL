# 도커 명령어

## 도커 이미지

- `docker pull centos:7`
    - 도커 이미지 다운로드
    - `centos:7`
        - *centos*라는 이름의 *7* 버전 이미지를 기반으로 컨테이너 생성
- `docker images`
    - 도커 엔진에 존재하는 이미지 목록 출력

## 컨테이너

- `docker ps -a -q`
    - `docker ps`
        - 컨테이너 목록 출력
        - 옵션이 없을 경우 정지되지 않은 컨테이너 목록만 출력함
    - `-a`
        - 모든 컨테이너 목록 출력
    - `-q`
        - 컨테이너 ID만 출력
    - 컨테이너 목록 해석
        
        ![스크린샷 2023-08-31 오전 5.25.45.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/53555db2-b349-437b-bdb0-d8e6122421c3/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2023-08-31_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_5.25.45.png)
        
        - CONTAINER ID
            - 컨테이너에게 자동으로 할당되는 고유 아이디
            - `docker ps` 명령어에서는 일부만 출력
            - 전체 ID를 확인하고 싶을 경우 `docker inspect **************container_name************** | grep Id` 명령어 사용
        - IMAGE
            - 컨테이너 생성 시 사용된 이미지 이름
        - COMMAND
            - 컨테이너가 시작될 때 실행될 명령어
            - 대부분의 이미지에 미리 내장되어 있기 때문에 따로 설정할 필요 없음
            - 이미지에 내장된 명령어를 덮어쓰고 싶을 경우 생성 시 `docker run *************image_name COMMAND*************` 명령어 입력
        - CREATED
            - 컨테이너 생성 후 흐른 시간
        - STATUS
            - 컨테이너 상태
            - *UP*은 실행 중, *Exited*는 종료, *Pause*는 일시 중지
        - PORTS
            - 컨테이너가 개방한 포트와 호스트에 연결한 포트 목록
            - 컨테이너 생성 시 외부에 노출하지 않도록 설정해 아무 것도 출력되지 않음
        - NAMES
            - 컨테이너의 고유 이름
            - 아무 것도 설정하지 않으면 임의로 형용사_명사를 무작위로 조합해 이름 설정
            - `docker rename *current_name new_name*` 명령어를 사용하면 컨테이너 이름 변경 가능

## 컨테이너 실행

- `docker run -i -t --name myubuntu ubuntu:14.04`
    - `docker run`
        - 컨테이너 실행
        - 해당 이미지가 없다면 도커 허브에서 이미지 다운로드, 컨테이너가 없다면 컨테이너 생성 후 실행
        - 단순 생성은 `docker create` 사용
        - 단순 실행은 `docker start **************container_name**************` 명령어 사용
    - `-i -t`
        - `-i`
            - *interaction*의 약자
            - 컨테이너와 상호작용하게 해줌
            - 즉, 컨테이너의 표준 입출력을 열어줌
        - `-t`
            - **********pseudo-TTY********** 또는 ********terminal********의 약자
            - 컨테이너에서 가상 터미널 환경을 제공
            - 즉, 컨테이너 내부에서 터미널을 사용하는 것처럼 만들어줌
        - `docker run`에서 `-i -t` 명령어는 `docker attach **************container_name`* 명령어를 쓰는 것과 동일
    - `--name myubuntu`
        - 컨테이너 이름 설정
    - `ubuntu:14.04`
        - 컨테이너를 실행하기 위한 Docker 이미지 지정
        - *ubuntu*라는 이름의 *14.04* 버전 이미지를 기반으로 컨테이너 생성

## 컨테이너 종료 및 기타

- Ctrl + D, `Exit`
    - 컨테이너를 빠져나오며 컨테이너를 정지시킴
- Ctrl + P, Q
    - 컨테이너를 정지시키지 않고 컨테이너 터미널에서만 빠져나옴
- `docker stop *container_name*`
    - 컨테이너 정지

## 컨테이너 삭제

- `docker rm container_name | container_id`
    - 컨테이너 이름이나 컨테이너 아이디를 이용해 컨테이너 삭제
    - 현재 정지 상태인 컨테이너만 삭제 가능
    - 되돌릴 수 없으므로 주의해 사용

## 변수

- `$(docker ps -a -q)`
    - `$()`는 내부 명령어를 변수로 처리해줌
    - `docker ps -a -q` 명령어로 출력된 모든 컨테이너 ID를 다른 명령어에 사용 가능
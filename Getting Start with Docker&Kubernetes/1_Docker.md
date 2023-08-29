# 도커

- 리눅스 컨테이너에 여러 기능을 추가해 애플리케이션을 컨테이너로서 사용할 수 있게 만들어진 오픈소스 프로젝트

## 기초 지식

### 가상화

- 하나의 물리적 자원(ex. 서버)를 여러 개의 독립적인 가상 자원으로 분할하거나 가상 환경을 생성하는 기술
- 목적
    - 자원의 효율적인 활용
    - 관리의 용이성
    - 비용 절감
- 가상화의 종류
    - 서버 가상화
        - 하나의 물리 서버에서 여러 개의 독립적인 가상 서버(가상 머신)을 실행하는 것
        - 각 가상 머신은 자체 운영체제와 애플리케이션을 가지고 있음
        - 즉, 하나의 물리 서버 내에 여러 개의 가상 서버를 설치해 각각의 운영 체제와 프로그램을 사용할 수 있게 하는 것
    - 네트워크 가상화
        - 물리적인 네트워크 자원을 가상화하여 여러 독립적인 가상 네트워크를 제공하는 것
        - 즉, 하나의 물리적 네트워크를 여러 개의 가상 네트워크로 나누어 특정 목적이나 기능에 따라 사용하는 것
    - 스토리지 가상화
        - 물리적인 저장 장치를 가상화하며 하나의 큰 가상 스토리지 풀로 관리하는 것
        - 즉, 물리적 저장 장치 하나를 여러 가상 스토리지로 나누어 데이터를 분류하고 관리하는 것

### 하이퍼바이저

- 가상화 환경에서 가상 머신을 생성하고 관리하는 소프트웨어나 하드웨어 컴포넌트
- 즉, 여러 개의 가상 머신이 하나의 물리적 서버에서 실행될 수 있게 돕는 중간 관리자
- 하이퍼바이저의 유형
    - Type 1 (Bare-metal Hypervisor)
        - 물리 하드웨어 위에서 실행되는 하이퍼바이저
        - OS없이 직접 하드웨어에 설치됨
    - Type 2 (Hosted Hypervisor)
        - 기존 운영체제(OS) 위에서 어플리케이션처럼 실행되는 하이퍼바이저
        - 호스트 OS 위에서 작동하며, 해당 OS의 자원을 활용해 가상 머신을 실행

### 호스트

- 호스트 시스템
    - 물리적인 서버, 혹은 컴퓨터 = 하드웨어
    - 이 호스트 시스템 위에서 하이퍼바이저가 실행되며, 하이퍼바이저 위에 여러 가상 머신이 실행됨
- 호스트 OS
    - 하이퍼바이저가 설치된 기본 운영체제 = 소프트웨어
    - Type 2 호스티드 하이퍼바이저를 사용할 경우 호스트 OS 위에서 하이퍼바이저가 실행되며, 하이퍼바이저 위에 여러 가상 머신이 실행됨

### 커널

- 운영체제의 핵심 부분
- 하드웨어와 응용 프로그램 사이의 중재자 역할
- 하드웨어 자원 관리, 프로세스 관리, 메모리 관리, 입출력 관리 등을 담당

## 도커란?

- 일반적으로 도커 엔진, 혹은 도커와 관련된 모든 프로젝트를 일컫는 말.

### 도커 관련 프로젝트

- 도커 컴포즈
- 레지스트리
- 도커 허브
- Docker for Desktop
- **도커 엔진**

### 도커 엔진

- 컨테이너를 생성하고 관리하는 주체
- 그 자체로 컨테이너를 제어 가능하며 다양한 기능 제공
- 기타 프로젝트는 도커 엔진을 편하게 사용하기 위한 도구!

## 가상 머신과 도커 컨테이너

### 가상 머신

- 특징
    - 기존 가상화 기술은 하이퍼바이저라는 소프트웨어를 실행시키고, 그 위에 여러 가상 머신(VM)을 실행시킴
    - 각 VM은 자체 운영체제(=Guest OS)와 필요한 자원(CPU, 메모리, 스토리지 등)을 가짐
    - 각 VM은 격리된 환경에서 실행되므로 다른 VM의 영향을 받지 않음.
- 단점
    - VM을 구축하는 작업은 반드시 하이퍼바이저를 거쳐야 하기 때문에 일반 호스트에 비해 성능이 손실됨
    - VM은 실행을 위한 자체 OS를 포함하기 때문에 크고 무거우며, 배포 이미지 또한 크기가 큼

### 도커 컨테이너(컨테이너)

- 특징
    - 하이퍼바이저와 가상 OS없이 직접 호스트 OS에서 실행됨
    - 여러 컨테이너가 호스트 OS의 커널을 공유해 동작
        - 자체 자원을 사용하기 위한 자체 OS가 없으므로 가볍고 빠름!
    - 내부에 어플리케이션과 해당 어플리케이션의 실행을 위한 종속성과 라이브러리, 환경 변수를 포함
- 장점
    - 전통적인 VM에 비해 가벼워 한 서버에 수백 개의 컨테이너 실행 가능
    - 빠르게 시작하고 종료할 수 있음
    - 애플리케이션과 종속성이 패키지로 포함되어 있어 한 환경에서 생성된 컨테이너를 다른 환경에서도 동일하게 실행 가능
        - 개발, 테스트, 프로덕션 등 다양한 환경에서 동일한 컨테이너를 사용하면 환경 간 차이 최소화 가능
    - 컨테이너는 서로 격리되어 실행되므로 하나의 컨테이너에 문제가 생겨도 다른 컨테이너에는 영향X

### 도커의 장점

- 컨테이너 생태계에서 사실상 표준으로 사용되고 있음
    - 쿠버네티스, 메소스 등 오픈소스 프로젝트는 도커를 기준으로 개발
    - 많은 회사들이 서비스 개발 및 운영 환경에서 도커 컨테이너 도입
- 독립된 개발 환경 보장 가능
    - 도커 컨테이너는 호스트 OS 위에 실행되는 격리 공간
    - 때문에 컨테이너에 특별한 권한을 주지 않으면 컨테이너 내에서 무슨 짓을 해도 호스트 OS에 영향 X
- 애플리케이션 개발 및 배포가 편함
    - 컨테이너에서 작업을 마친 뒤 운영 환경에 배포하기 위해서 ‘도커 이미지’만 운영 서버에 전달하면 됨
        - 패키지나 의존성 따로 관리할 필요X
    - 이미지가 레이어 단위로 구성되어 있어 중복되는 레이어 재사용 가능
        - 배포 속도가 매우 빨라짐!

## Docker Toolbox와 Docker for Mac의 차이점

- 도커 컨테이너를 생성한 뒤 외부에서 접근하는 방법의 차이!

### 도커 툴박스

- 리눅스 가상 버신을 생성해 그 내부에 도커를 설치
- 리눅스 가상 머신을 생성한 뒤 도커를 설치하므로 가상 네트워크가 2개 생성됨
    - 내부 IP를 가진 가상 머신 안에 NAT IP를 할당받은 도커 컨테이너 생성
    - 외부에서 컨테이너에 접근하기 위해 PC-VM, VM-컨테이너의 2중 포트 포워딩 필요
        - VM-컨테이너 포트 포워딩은 도커에서 설정 할 수 있지만 PC-VM 포트 포워딩은 개별 설정 필요

### 도커 for Mac

- 호스트 자체에 가상화 기술을 적용
- 때문에 도커에서 제공하는 포트 포워딩만으로 외부에서 컨테이너 접근 가능
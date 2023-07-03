# MAC주소, IP주소, Port 번호가 식별하는 것
## Mac
- NIC(Network Interface Card, Lan 카드) 식별자
	- 유선, 무선 Lan카드 두 개를 연결했을 때 MAC 주소는 2개
	- MAC 주소는 하드웨어 주소라고도 하며 변경 가능
## IP
- Host(인터넷에 연결된 컴퓨터)에 대한 식별자
	- 한 컴퓨터에는 n개의 IP 주소 존재 가능
	- 하나의 NIC에는 여러 개의 IP를 바인딩 할 수 있음
## Port번호
- S/W 개발자: Process 식별자?
- 네트워크 개발자: Service 식별자?
- H/W 기술자: 인터페이스 번호?

# Host, Switch, Network의 관계
## Host
- 네트워크에 연결된 컴퓨터
- Host의 두 가지 종류
	- 네트워크 이용 주체인 Host(=End-Point=단말)
		- Peer, Server, Client
	- 네트워크 자체를 이루는 Host(=switch)

## Switch
- Router: 경로 선정 스위치
- F/W, IPS: 보안 스위치
- OSI 7계층 중 무엇으로 스위칭하느냐에 따라 스위치를 부르는 명칭이 다름(중요!)
	- MAC주소로 스위칭 -> L2 스위치
	- IP주소로 스위칭 -> L3 스위치(Ex. Router)
	- Port 번호로 스위칭 -> L4 스위치
	- HTTP 프로토콜로 스위칭 -> L7 스위치
	- 계층이 높아질수록 연산이 복잡해져 가격이 비싸짐

## Network
- 대표적인 네트워크: Internet
- 인터넷을 이루는 가장 중요한 구성 요소
	- Router
	- DNS
	- 인터넷은 Router와 DNS의 집합

# 출처
- https://www.youtube.com/playlist?list=PLXvgR_grOs1BFH-TuqFsfHqbh-gpMbFoy
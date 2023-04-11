## Docker
#도커(Docker)란 리눅스 컨테이너를 기반으로 하여 특정한 서비스를 패키징하고 배포하는데 유용한 오픈소스 프로그램이다


#도커의 명령어

docker images
#현재 내 컴퓨텅 어떤 이미지들 있는지 확인하기 위한 명령어

docker pull nginx:1.23
#pull명령어를 통해 nginx이미지를 다운로드
docker run
#이미지 다운과 컨테이너 생성,실행을 동시에 하는 명렁어
docker ps
#컨테이너 리스트를 출력해주는 명령어(현재 실행중인 컨테이너만  출력)
docker ps -a
#컨테이너 리스트를 출력해주는 명령어(현재 실행중, 실행이 멈춘 컨터이네들을 출력)
docker rm
#컨테이너를 삭제하는 명령어
docker kill
# 컨테이너 강제종료
docker stop [id]
#해당 id 중지

#kill과 stop의 차이 stop은 하고 있는 작업을 마무리하고 꺼지지만 kill은 강제종료

docker pause
#컨테이너 일시정지

docker unpuase
#pause 명령으로 일시정지된 컨테이너를 다시 시작

docker start [id]
#해당 id 시작
docker exec [id]
#컨테이너에 대해서 exec 명령어사용 가능
docker run -d --name my-sql -v test-db:/var/lib/mysql -p 3300:3300 --platform linux/amd64 -e MYSQL_ROOT_PASSWORD=12345 mysql:5.7
#my sql 연동

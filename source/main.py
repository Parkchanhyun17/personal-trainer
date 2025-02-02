import get_video_csv
import compare
import numpy as np

#main
#get_video_csv.get_video("스쿼트","user")#user 스켈레톤 동영상과 csv 얻기
#get_video_csv.get_video("스쿼트","trainer")#trainer 스켈레톤 동영상과 csv 얻기

#csv 경로
trainer_csv_path='./trainer/trainer_output.csv'
user_csv_path='./user/user_output.csv'


#0,0 체크
compare.check(trainer_csv_path)
compare.check(user_csv_path)


#이동한 거리(머리)
#distance_trainer_head=compare.distance(trainer_csv_path,str(0))
#distance_user_head=compare.distance(user_csv_path,str(0))
#print(distance_trainer_head)
#print(distance_user_head)

#각도(왼쪽 무릎)
# trainer_angle=compare.angle(trainer_csv_path,8,9,10)
# print(trainer_angle)

#부위별 좌표 csv 받아와서 방향 csv 생성
#compare.direction(trainer_csv_path,'trainer')
#compare.direction(user_csv_path,'user')

# 3대 운동 부위별 각도 계산
# 1. 벤치프레스
#bench_angle= compare.benchpress_angle(trainer_csv_path)
#print(bench_angle) # 벤치프레스 모든 각도 5분위수 출력 - 왼팔각도, 오른팔각도 순


# 2. 데드리프트
#dead_angle = compare.deadlift_angle(trainer_csv_path)
#print(dead_angle) # 데드리프트 모든 각도 5분위수 출력 -뒷목,무릎,팔,척추 순


# 3. 스쿼트
sq_angle = compare.squat_angle(trainer_csv_path)
print(sq_angle) # 스쿼트 모든 각도 5분위수  출력 - 뒷목, 무릎, 척추 순

import cv2
import random
import shutil
import os
import detect
import pygame
import detect
import warnings

# 경고 메시지 무시
warnings.filterwarnings("ignore", category=UserWarning, message="Failed to load image Python extension")
pygame.init()
if not os.path.exists('test_image'):
    os.makedirs('test_image')

choose_evaluation = int(input("원하는 방식을 선택하세요 1.사진, 2.동영상: "))
weights_path = './best_epoch4all.pt'

if choose_evaluation == 1:
    cap = cv2.VideoCapture(0)
    frame_count = 0
    saved_image_count = 0  # 추가된 변수

    while True:
        ret, frame = cap.read()

        if ret:
            cv2.imshow('Camera', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if frame_count % 30 == 0:
            file_name = f"test_image/frame_{frame_count}.jpg"
            cv2.imwrite(file_name, frame)
            print(f'frame_{frame_count}.jpg 파일이 저장 되었습니다.')
            saved_image_count += 1  # 이미지 저장 시 카운트 증가

        if saved_image_count == 10:  # 이미지 개수가 10개이면 종료
            print(f'데이터 수집 종료 총 {saved_image_count}개의 사진이 들어갔습니다.')
            break
        
        frame_count += 1

    cap.release()
    cv2.destroyAllWindows()

    result = []
    a = detect.run(weights=weights_path, source='./test_image')
    result.append(a)
    # print(f'a의 결과는 {a}입니다.')
    mp3_file = 'wow.mp3'
    out_file = 'uu.mp3'
    num1 = 0
    num3 = 0
    for lists in a:
        for data in lists:
            data = int(data)
            if data == 3:
                num3 += 1
            elif data == 1:
                num1 += 1

    if num1 >= 5 and num3 >=5 :
        print('출근 가능')
        pygame.mixer.music.load(mp3_file)
        pygame.mixer.music.play()

        # 음악이 재생되는 동안 대기
        while pygame.mixer.music.get_busy():
            pass
        

    else:
        print(f'출입 불가능')
        # playsound(out_file)
        pygame.mixer.music.load(out_file)
        pygame.mixer.music.play()

        # 음악이 재생되는 동안 대기
        while pygame.mixer.music.get_busy():
            pass

    pygame.quit()

else:

    # Initialize pygame for audio playback
    pygame.init()

    # Load the detection model
    # weights_path = './output_img1_best.pt'
    # model_source = './test_image'
    # detection_results = detect.run(weights=weights_path, source=model_source)

    # Initialize camera
    cap = cv2.VideoCapture(0)
    frame_count = 0
    saved_image_count = 0
    video_frames = []

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow('Camera', frame)

        video_frames.append(frame)
        frame_count += 1

        if frame_count >= 150: 
            print(f'영상 저장이 완료되었습니다.')
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # Save the video frames as an actual video
    out = cv2.VideoWriter('captured_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (640, 480))
    for frame in video_frames:
        out.write(frame)
    out.release()

    # Perform detection on the captured video frames
    detection_results_video = detect.run(weights=weights_path, source='captured_video.mp4')

    # Analyze detection results and play appropriate audio
    num1 = 0
    num3 = 0
    for lists in detection_results_video:
        for data in lists:
            data = int(data)
            if data == 3:
                num3 += 1
            elif data == 1:
                num1 += 1

    if num1 >= 75 and num3 >= 75:
        print('출근 가능')
        pygame.mixer.music.load('wow.mp3')
        pygame.mixer.music.play()
    else:
        print(f'출입 불가능')
        pygame.mixer.music.load('uu.mp3')
        pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pass

    pygame.quit()
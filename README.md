## 1. SEE(Safety Equipment Enforcement)
<div align="center">
  SEE는 2023.08.16 ~ 2023.08.29까지 개발된 프로젝트 입니다.<br>
  SEE는 안전장비 착용 감지를 위한 인공지능 프로젝트입니다.<br>
  공사현장 등에서 착용하는 안전모와 안전조끼를 인식하는 프로그램입니다.<br>
</div>

## 2. 프로젝트 내용
<div align="center">
  <img width="60%" height="50%" src="https://github.com/JinYeong95/zipsafetyproject/assets/117560090/bc1d09a0-6f90-4257-9be4-d3b4ea9e59bf"/><br>
  <br>
  exe로 프로그램을 실행하여 사진 혹은 동영상으로 해당 사진을 저장합니다<br>
사진의 경우 10장, 동영상의 경우 10초동안 150번의 사진을 촬영합니다.<br>
on_harness, off_harness, on_helmet, off_helmet으로 구성되어 있으며, <br>
on_harness와 on_helmet이 절반 이상 인식될 경우 출입 및 출근을 허가합니다.<br>
</div>


## 3. 활용 데이터 셋
<div align="center">
  <div align="center">
  <img width="80%" height="80%" src="https://github.com/JinYeong95/zipsafetyproject/assets/117560090/97d80f61-387c-45fb-bbeb-68ac8336170e"/>
</div>
  <br>
AI HUB 공사현장 안전장비 인식 이미지을 사용<br>
착용 시 on_harness, on_helmet으로 인식<br>
착용하지 않을시 off_harness, off_helmet으로 인식<br>
images와 labels로 구분<br>
  <br>
</div>

## 4. 사용 모델
<div align="center">
  <img width="50%" height="50%" src="https://github.com/JinYeong95/zipsafetyproject/assets/117560090/73f9bc97-b8c4-4d72-a52d-cc02634f02d8"/>
  <br>
  YOLOv5s 모델을 사용
</div>

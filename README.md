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
  <img width="80%" height="80%" src="https://github.com/JinYeong95/zipsafetyproject/assets/117560090/461402c9-162c-432e-9623-9f31abab76de"/>
  <img width="80%" height="80%" src="https://github.com/JinYeong95/zipsafetyproject/assets/117560090/97d80f61-387c-45fb-bbeb-68ac8336170e"/>
</div>
  <br>
AI HUB 공사현장 안전장비 인식 이미지을 사용<br>
착용 시 on_harness, on_helmet으로 인식<br>
착용하지 않을시 off_harness, off_helmet으로 인식<br>
images와 labels로 구분하였습니다.<br>
  <br>
</div>

## 4. 사용 모델
<div align="center">
  <img width="50%" height="50%" src="https://github.com/JinYeong95/zipsafetyproject/assets/117560090/73f9bc97-b8c4-4d72-a52d-cc02634f02d8"/>
  <br>
  YOLOv5s 모델을 사용하였습니다.
</div>

## 5. Stacks
<div align="center">
  <img src="https://camo.githubusercontent.com/ddf481249395b4841579b3c11c78cccf80e350c371e383bebdf1c28bd4e42e77/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f676f6f676c65636f6c61622d4639414230303f7374796c653d666f722d7468652d6261646765266c6f676f3d676f6f676c65636f6c6162266c6f676f436f6c6f723d7768697465" data-canonical-src="https://img.shields.io/badge/googlecolab-F9AB00?style=for-the-badge&amp;logo=googlecolab&amp;logoColor=white" style="max-width: 100%;">
  <a target="_blank" rel="noopener noreferrer nofollow" href="https://camo.githubusercontent.com/0574332816cea5cfd59ad7a4990a26d1a5bec24829b21c6f1b8a276821d8b1a6/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6a7570797465722d4633373632363f7374796c653d666f722d7468652d6261646765266c6f676f3d6a757079746572266c6f676f436f6c6f723d7768697465"><img src="https://camo.githubusercontent.com/0574332816cea5cfd59ad7a4990a26d1a5bec24829b21c6f1b8a276821d8b1a6/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6a7570797465722d4633373632363f7374796c653d666f722d7468652d6261646765266c6f676f3d6a757079746572266c6f676f436f6c6f723d7768697465" data-canonical-src="https://img.shields.io/badge/jupyter-F37626?style=for-the-badge&amp;logo=jupyter&amp;logoColor=white" style="max-width: 100%;"></a>
  <a target="_blank" rel="noopener noreferrer nofollow" href="https://camo.githubusercontent.com/eda318cefcea9bc55d00c18d309eaadbfb4661d4908eba7407104b908404ac13/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f7079636861726d2d3030303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d7079636861726d266c6f676f436f6c6f723d7768697465"><img src="https://camo.githubusercontent.com/eda318cefcea9bc55d00c18d309eaadbfb4661d4908eba7407104b908404ac13/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f7079636861726d2d3030303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d7079636861726d266c6f676f436f6c6f723d7768697465" data-canonical-src="https://img.shields.io/badge/pycharm-000000?style=for-the-badge&amp;logo=pycharm&amp;logoColor=white" style="max-width: 100%;"></a>
  <a target="_blank" rel="noopener noreferrer nofollow" href="https://camo.githubusercontent.com/a9a95986631c3d4945a63d42d2864e3918a834d672d907e174a29f743a1bc3f1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6769742d4630353033323f7374796c653d666f722d7468652d6261646765266c6f676f3d676974266c6f676f436f6c6f723d7768697465"><img src="https://camo.githubusercontent.com/a9a95986631c3d4945a63d42d2864e3918a834d672d907e174a29f743a1bc3f1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6769742d4630353033323f7374796c653d666f722d7468652d6261646765266c6f676f3d676974266c6f676f436f6c6f723d7768697465" data-canonical-src="https://img.shields.io/badge/git-F05032?style=for-the-badge&amp;logo=git&amp;logoColor=white" style="max-width: 100%;"></a><br>
  <a target="_blank" rel="noopener noreferrer nofollow" href="https://camo.githubusercontent.com/ad176bb5a61237550550e47d7e77dd5d1a846518df44c522d2ba9c0a7da6379c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6769746875622d3138313731373f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465"><img src="https://camo.githubusercontent.com/ad176bb5a61237550550e47d7e77dd5d1a846518df44c522d2ba9c0a7da6379c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6769746875622d3138313731373f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465" data-canonical-src="https://img.shields.io/badge/github-181717?style=for-the-badge&amp;logo=github&amp;logoColor=white" style="max-width: 100%;"></a>
  <a target="_blank" rel="noopener noreferrer nofollow" href="https://camo.githubusercontent.com/c4627942eb21a30a1607bfc823a5fcafb8c9b9e8fb2586705bae4569ca6981b0/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f736c61636b2d3441313534423f7374796c653d666f722d7468652d6261646765266c6f676f3d736c61636b266c6f676f436f6c6f723d7768697465"><img src="https://camo.githubusercontent.com/c4627942eb21a30a1607bfc823a5fcafb8c9b9e8fb2586705bae4569ca6981b0/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f736c61636b2d3441313534423f7374796c653d666f722d7468652d6261646765266c6f676f3d736c61636b266c6f676f436f6c6f723d7768697465" data-canonical-src="https://img.shields.io/badge/slack-4A154B?style=for-the-badge&amp;logo=slack&amp;logoColor=white" style="max-width: 100%;"></a>
  <img src="https://camo.githubusercontent.com/94a96cafcd5f60fd05e5a3aca153240be9743e5d31c5c137798315c2e11902fe/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f594f4c4f2d3030464646463f7374796c653d666f722d7468652d6261646765266c6f676f3d796f6c6f266c6f676f436f6c6f723d7768697465" data-canonical-src="https://img.shields.io/badge/YOLO-00FFFF?style=for-the-badge&amp;logo=yolo&amp;logoColor=white" style="max-width: 100%;">
  
</div>

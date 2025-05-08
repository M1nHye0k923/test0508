import qrcode

# 깃허브 사용자 프로필 주소
github_url = 'https://github.com/M1nHye0k923/test0508'

# QR 코드 생성
img = qrcode.make(github_url)  # 변수명을 img로

# 이미지로 저장
img.save('github_qrcode.png')  # img.save로 저장

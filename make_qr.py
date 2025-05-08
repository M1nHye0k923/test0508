import qrcode

def generate_qr_from_github():
    # GitHub raw 주소 입력
    github_url = input("https://raw.githubusercontent.com/M1nHye0k923/test0508/main/test0508.ipynb")

    # QR 코드 객체 생성
    qr = qrcode.QRCode(
        version=1,  # 자동 크기
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(github_url)
    qr.make(fit=True)

    # QR 코드 이미지 생성
    img = qr.make_image(fill_color="black", back_color="white")

    # 이미지 파일로 저장
    filename = "github_qr.png"
    img.save(filename)
    print(f"✅ QR 코드가 '{filename}'로 저장되었습니다!")

if __name__ == "__main__":
    generate_qr_from_github()

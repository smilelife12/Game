import pygame

pygame.init()

# 스크린 크기 설정
Screen = pygame.display.set_mode((400, 300))
# 스크린 캡션 설정
pygame.display.set_caption('파이게임')
finish = False
colorBlue = True

x = 30
y = 30
# 시간 값 가져오기
clock = pygame.time.Clock()
while not finish:
    for event in pygame.event.get():
        # 게임 종료버튼 클릭
        if event.type == pygame.QUIT:
            finish = True
        # 키보드 입력 이벤트 설정
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            colorBlue = not colorBlue

        # 키보드 입력에 따라 방향 바꾸기
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            y -= 3
        if pressed[pygame.K_DOWN]:
            y += 3
        if pressed[pygame.K_LEFT]:
            x -= 3
        if pressed[pygame.K_RIGHT]:
            x += 3

        if colorBlue:
            color = (0, 128, 255)
        else:
            color = (255, 255, 255)

        # 게임 창에 직사각형 그려주기
        Screen.fill((0,0,0))
        pygame.draw.rect(Screen, color, pygame.Rect(x, y, 60, 60))

        pygame.display.flip()
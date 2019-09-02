import pygame
pygame.init()

display_width = 800
display_height = 600

screen = pygame.display.set_mode((display_width, display_height))
# 이미지 파일 불러오기
img = pygame.image.load('./data/myimage1.jpg')

# 음악 파일 불러오기
pygame.mixer.music.load('./data/punch.mp3')
# 음악 파일 재생 횟수
pygame.mixer.music.play(0)

# 이미지 그려 넣는 함수 생성
def myimg(x, y):
    screen.blit(img, (x, y))


x = (display_width *0.5)
y = (display_height * 0.5)

finished = False
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    screen.fill((255, 255, 255))
    # x, y 값을 기준으로 이미지를 스크린에 그려넣음.
    myimg(x,y)
    pygame.display.flip()

pygame.quit()
quit()


from pygame import *

#создай окно 
window = display.set_mode((700,500))
display.set_caption('Догонялки')
#задай фон сцены

background = transform.scale(image.load("gjjg.png"), (700,500))
#создай 2 спрайта и размести их на сцене
sprite1 = transform.scale(image.load('garick.png'),(200,200))
x1 = 1
y1 = 1
sprite2 = transform.scale(image.load('sprite2.png'),(50,50))
x2 = 100
y2 = 100
speed = 10
#обработай событие «клик по кнопке "Закрыть окно"»
clock = time.Clock()
FPS = 60

game = True
while game:
    window.blit(background,(0,0))
    window.blit(sprite1,(x1, y1))
    window.blit(sprite2,(x2, y2))

    for e in event.get():
        if e.type == QUIT:
            game = False
    keys_pressed = key.get_pressed()
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= speed
    if keys_pressed[K_DOWN] and y1 < 500:
        y1 += speed
    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= speed
    if keys_pressed[K_RIGHT] and x1 < 500:
        x1 += speed
    if keys_pressed[K_s] and y2 < 650:
        y2 += speed
    if keys_pressed[K_w] and y2 > 5:
        y2 -= speed
    if keys_pressed[K_d] and x2 < 650:
        x2 += speed
    if keys_pressed[K_a] and x2 > 5:
        x2 -= speed

    clock.tick(FPS)
    display.update()

    

